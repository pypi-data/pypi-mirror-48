#include "pooling_layer.h"

namespace OpenNN {

    PoolingLayer::PoolingLayer(const Vector<size_t>& input_size)
    {
        input_rows_number = input_size[0];

        input_columns_number = input_size[1];

        set_default();

    }


    PoolingLayer::PoolingLayer(const Vector<size_t>& input_size, const Vector<size_t>& pool_size)
    {

        input_rows_number = input_size[0];

        input_columns_number = input_size[1];

        //

        pool_row_size = pool_size[0];

        pool_column_size = pool_size[1];

        set_default();

    }

    PoolingLayer::~PoolingLayer() {
    }


    Matrix<double> PoolingLayer::calculate_outputs(const Matrix<double>& inputs)const
    {
        switch(pooling_method)
        {
            case NoPooling:
                return calculate_outputs_no_pooling(inputs);

            case MaxPooling:
                return calculate_outputs_max_pooling(inputs);

            case AveragePooling:
                return calculate_outputs_average_pooling(inputs);
        }

        return Matrix<double>();
    }


    Matrix<double> PoolingLayer::calculate_outputs_average_pooling(const Matrix<double> & inputs) const
    {

        const size_t neurons_number = get_neurons_number();

        const size_t samples_number = inputs.get_rows_number();


        Matrix<double> outputs(samples_number, neurons_number);

        for(size_t neuron = 0; neuron < neurons_number; neuron++)
        {
            const Vector<size_t> indices = get_inputs_indices(neuron);

            const Matrix<double> submatrix = inputs.get_submatrix_columns(indices);

            const Vector<double> mean_rows_values = submatrix.calculate_rows_sum() / submatrix.get_columns_number();

            for(size_t sample = 0; sample < samples_number; sample++)
            {
                outputs(sample, neuron) = mean_rows_values[sample];
            }

        }

        return outputs;
    }


    Matrix<double> PoolingLayer::calculate_outputs_no_pooling(const Matrix<double>& inputs) const
    {
        return inputs;
    }


    Matrix<double> PoolingLayer::calculate_outputs_max_pooling(const Matrix<double>& inputs) const
    {

        const size_t neurons_number = get_neurons_number();

        const size_t samples_number = inputs.get_rows_number();


        Matrix<double> outputs(samples_number, neurons_number, 0.0);

        for(size_t sample = 0; sample < samples_number; sample ++)
        {
            for(size_t neuron = 0; neuron < neurons_number; neuron++)
            {
                Vector<size_t> indices = get_inputs_indices(neuron);

                Matrix<double> submatrix = inputs.get_submatrix( { sample }, indices);
                Vector<size_t> max_indices = submatrix.calculate_maximal_indices();

                outputs(sample, neuron) = inputs(sample, indices[max_indices[1]]);
            }
        }

        return outputs;
    }


    Tensor<double> PoolingLayer::calculate_activations_derivatives(const Matrix<double> &inputs) const
    {

        switch(pooling_method)
        {
            case NoPooling:

                return calculate_activations_no_pooling_derivatives(inputs);

            case AveragePooling:

                return calculate_activations_average_pooling_derivatives(inputs);

            case MaxPooling:

                return calculate_activations_max_pooling_derivatives(inputs);
        }

        return Tensor<double>();

    }


    Tensor<double> PoolingLayer::calculate_activations_no_pooling_derivatives(const Matrix<double>& inputs) const
    {
        return Tensor<double>({inputs.get_rows_number(), inputs.get_columns_number()}, 1.0);
    }


    Tensor<double> PoolingLayer::calculate_activations_average_pooling_derivatives(const Matrix<double>& inputs) const
    {
        return Tensor<double>({inputs.get_rows_number(), inputs.get_columns_number()}, ( 1.0 / (pool_row_size * pool_column_size) ));
    }


    Tensor<double> PoolingLayer::calculate_activations_max_pooling_derivatives(const Matrix<double>& inputs) const
    {

        return Tensor<double>({inputs.get_rows_number(), inputs.get_columns_number()}, 1.0);
        /*
        Matrix<double> activation_derivatives(inputs.get_rows_number(),
                                              inputs.get_columns_number(),
                                               0.0);

        const size_t neurons_number = get_neurons_number();

        const size_t samples_number = inputs.get_rows_number();

        for(size_t sample = 0; sample < samples_number; sample ++)
        {
            for(size_t neuron = 0; neuron < neurons_number; neuron++)
            {
                Vector<size_t> indices = get_inputs_indices(neuron);

                Matrix<double> submatrix = inputs.get_submatrix( { sample }, indices);
                Vector<size_t> max_indices = submatrix.calculate_maximal_indices();
                activation_derivatives(sample, indices[max_indices[1]]) = 1.0;
            }
        }
        return activation_derivatives;
        */
    }


    Matrix<double> PoolingLayer::calculate_layer_delta(const Matrix<double>& previous_layer_delta, const Matrix<double>& activations, const Matrix<double>& activations_derivatives) const
    {

        switch (pooling_method) {

            case NoPooling:
                return previous_layer_delta;

            case AveragePooling:

                return calculate_average_pooling_layer_delta(previous_layer_delta,
                                                             activations,
                                                             activations_derivatives);

            case MaxPooling:

                return calculate_max_pooling_layer_delta(previous_layer_delta,
                                                         activations,
                                                         activations_derivatives);

        }

        return Matrix<double>();
    }


    Matrix<double> PoolingLayer::calculate_average_pooling_layer_delta(const Matrix<double>& previous_layer_delta, const Matrix<double>& activations, const Matrix<double>& activations_derivatives) const
    {
        Matrix<double> layer_delta(activations_derivatives.get_rows_number(),
                                   activations_derivatives.get_columns_number(),
                                   0.0);

        const size_t neurons_number = get_neurons_number();

        for(size_t sample = 0; sample < activations_derivatives.get_rows_number(); sample++)
        {
            for(size_t neuron = 0; neuron < neurons_number; neuron ++)
            {
                const Vector<size_t> indices = get_inputs_indices(neuron);

                for(size_t index = 0; index < indices.size(); index ++)
                {
                    layer_delta(sample, indices[index]) += previous_layer_delta(sample, neuron);
                }
            }
        }
       return layer_delta * activations_derivatives;

    }


    Matrix<double> PoolingLayer::calculate_max_pooling_layer_delta(const Matrix<double>& previous_layer_delta, const Matrix<double>& activations, const Matrix<double>& activations_derivatives) const
    {
        Matrix<double> layer_delta(activations.get_rows_number(),
                                   activations.get_columns_number(),
                                   0.0);
        const size_t neurons_number = get_neurons_number();
        const size_t samples_number = activations.get_rows_number();
        for(size_t sample = 0; sample < samples_number; sample++)
        {
            for(size_t neuron = 0; neuron < neurons_number; neuron ++)
            {
                const Vector<size_t> indices = get_inputs_indices(neuron);
                const Matrix<double> submatrix = activations.get_submatrix({sample} , indices);
                const Vector<size_t> max_indices = submatrix.calculate_maximal_indices();

                layer_delta(sample, indices[max_indices[1]]) += previous_layer_delta(sample, neuron);
            }
        }

        return layer_delta * activations_derivatives;
    }


    size_t PoolingLayer::get_neurons_number() const
    {
        return(get_output_rows_number() * get_output_columns_number());
    }

    Vector<size_t> PoolingLayer::get_inputs_indices(const size_t& neuron) const
    {
        if(neuron > get_neurons_number() - 1)
        {
            return Vector<size_t>();
        }
        const size_t row_index = (neuron / get_output_columns_number());
        const size_t column_index = (neuron % get_output_columns_number());

        //cout << "("<< row_index << " ," << column_index << " )" << endl;
        Vector<size_t> indices;

        // With stride = 1
        for(size_t i = row_index; i < (row_index + pool_row_size); i++)
        {
            for(size_t j = column_index; j < (column_index + pool_column_size); j++)
            {
                indices.push_back(i*input_columns_number + j );
            }
        }
        return indices;
    }


     size_t PoolingLayer::get_input_rows_number() const
    {
        return input_rows_number;
    }


     size_t PoolingLayer::get_input_column_number() const
    {
        return input_columns_number;
    }


     size_t PoolingLayer::get_output_rows_number() const
    {
        return ((input_rows_number - pool_row_size) / row_stride) + 1;
    }


     size_t PoolingLayer::get_output_columns_number() const
    {
        return ((input_columns_number - pool_column_size) / column_stride ) + 1;;
    }


     size_t PoolingLayer::get_padding_width() const
    {
        return padding_width;
    }


     size_t PoolingLayer::get_row_stride() const
    {
        return row_stride;
    }


     size_t PoolingLayer::get_column_stride() const
    {
        return column_stride;
    }


     size_t PoolingLayer::get_pool_row_size() const
    {
        return pool_row_size;
    }


     size_t PoolingLayer::get_pool_column_size() const
    {
        return pool_column_size;
    }


    void PoolingLayer::set_input_rows_number(const size_t& new_input_rows_number)
    {
        input_rows_number = new_input_rows_number;
    }


    void PoolingLayer::set_input_columns_number(const size_t& new_input_columns_number)
    {
        input_columns_number = new_input_columns_number;
    }


    void PoolingLayer::set_padding_width(const size_t& new_padding_width)
    {
        padding_width = new_padding_width;
    }


    void PoolingLayer::set_row_stride(const size_t& new_row_stride)
    {
        row_stride = new_row_stride;
    }


    void PoolingLayer::set_column_stride(const size_t& new_column_stride)
    {
        column_stride = new_column_stride;
    }

    void PoolingLayer::set_pool_size(const size_t& new_pool_rows_number,
                       const size_t& new_pool_columns_number)
    {

        pool_row_size = new_pool_rows_number;
        pool_column_size = new_pool_columns_number;

    }

    void PoolingLayer::set_pooling_method(const PoolingMethod& new_pooling_method)
    {
        pooling_method = new_pooling_method;
    }

    void PoolingLayer::set_default()
    {
        instance_of = "PoolingLayer";

        trainable = false;
    }


}

