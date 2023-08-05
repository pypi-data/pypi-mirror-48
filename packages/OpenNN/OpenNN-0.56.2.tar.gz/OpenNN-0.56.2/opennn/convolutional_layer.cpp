/****************************************************************************************************************/
/*                                                                                                              */
/*   OpenNN: Open Neural Networks Library                                                                       */
/*   www.opennn.net                                                                                             */
/*                                                                                                              */
/*   C O N V O L U T I O N A L   L A Y E R   C L A S S                                                          */
/*                                                                                                              */
/*   Artificial Intelligence Techniques SL                                                                      */
/*   artelnics@artelnics.com                                                                                    */
/*                                                                                                              */
/****************************************************************************************************************/

// OpenNN includes

#include "convolutional_layer.h"

namespace OpenNN
{
    /// DEFAULT CONSTRUCTOR FOR THE FIRST LAYER

    ConvolutionalLayer::ConvolutionalLayer(const size_t& filters_number,
                                           const Vector<size_t>& kernel_shape,
                                           const Vector<size_t>& input_shape) : Layer()
    {

        if (filters_number == 0)
        {
            throw ("EXCEPTION: Filters number must be greater than zero.");
        }

        set_input_shape(input_shape);

        // Derived members

        set_kernel_shape(kernel_shape);

        if(needs_padding(input_rows_number, kernel_rows_number) || needs_padding(input_columns_number, kernel_columns_number))
        {
            throw ("EXCEPTION: Output data will be out of bounds. It is necessary to insert a padding or change the input shape.");
        }


        filters = Vector<filter_t> (filters_number,
                                    filter_t(input_channels_number,
                                    Matrix<double>(kernel_rows_number, kernel_columns_number)));

        for(size_t i = 0; i < filters.size(); i++)
        {
            for(size_t j = 0; j < filters[i].size(); j++)
            {
                filters[i][j].randomize_normal();
            }
        }

        biases = Vector<double>(filters_number);
        biases.randomize_normal();
        trainable = true;
        layer_type = Layer::Convolutional_Layer;
    }

    /// @todo

    ConvolutionalLayer::ConvolutionalLayer(const size_t& filters_number,
                                           const size_t& kernel_rows_number,
                                           const size_t& kernel_columns_number,
                                           const PaddingOption& padding_option) : Layer()
    {
//        instance_of = "ConvolutionalLayer";
        layer_type = Layer::Convolutional_Layer;

        // Not implemented

//        throw exception("EXCEPTION: Not implemented exception.");
        throw ("EXCEPTION: Not implemented exception.");
    }


    bool ConvolutionalLayer::check_input_shape(const Vector< Matrix <double> >&inputs) const
    {
        const size_t inputs_size = inputs.size();

        if (inputs.size() != input_channels_number) return false;

        for(size_t i = 0; i  < inputs_size; i++)
        {
            const size_t rows_number = inputs[i].get_rows_number();
            const size_t columns_number = inputs[i].get_columns_number();

            if(rows_number != input_rows_number || columns_number != input_columns_number) return false;
        }

        return true;
    }


   Matrix<double> ConvolutionalLayer::calculate_activations(const Matrix<double>& convolutions) const
    {
       switch(activation_function)
       {
           case ConvolutionalLayer::Linear:
           {
                return Functions::linear(convolutions);
           }

           case ConvolutionalLayer::Logistic:
           {
                return Functions::logistic(convolutions);
           }

           case ConvolutionalLayer::HyperbolicTangent:
           {
                return Functions::hyperbolic_tangent(convolutions);
           }

           case ConvolutionalLayer::Threshold:
           {
                return Functions::threshold(convolutions);
           }

           case ConvolutionalLayer::SymmetricThreshold:
           {
                return Functions::symmetric_threshold(convolutions);
           }

           case ConvolutionalLayer::RectifiedLinear:
           {
                return Functions::rectified_linear(convolutions);
           }

           case ConvolutionalLayer::ScaledExponentialLinear:
           {
                return Functions::scaled_exponential_linear(convolutions);
           }

           case ConvolutionalLayer::SoftPlus:
           {
                return Functions::soft_plus(convolutions);
           }

           case ConvolutionalLayer::SoftSign:
           {
                return Functions::soft_sign(convolutions);
           }

           case ConvolutionalLayer::HardSigmoid:
           {
                return Functions::hard_sigmoid(convolutions);
           }

           case ConvolutionalLayer::ExponentialLinear:
           {
                return Functions::exponential_linear(convolutions);
           }
       }

        return Matrix<double>();
    }


   Matrix<double> ConvolutionalLayer::calculate_combinations(const Matrix<double>& input) const
   {
       const size_t samples_number = input.get_rows_number();
       const size_t output_columns_number = get_output_columns_number() * get_output_rows_number() * filters.size();
       Matrix<double> outputs(samples_number, output_columns_number, 0.0);

       for(size_t i = 0; i < samples_number; i++)
       {
           const Vector<double> sample = input.get_row(i);
           const Vector < Matrix <double> > channels_matrix = sample.to_vector_matrix(input_rows_number, input_columns_number, input_channels_number);
           const Vector < Matrix < double > > matrix_with_padding = prepare_input(channels_matrix);
           const Vector < Matrix < double > > convolution_output = calculate_convolutions(matrix_with_padding);
           outputs.set_row(i, to_vector(convolution_output));
      }
       return outputs;
   }


    Matrix<double> ConvolutionalLayer::calculate_combinations(const Matrix<double>&input, const Vector<double>& new_biases, const Matrix<double>& new_synaptic_weights) const
    {
        const size_t samples_number = input.get_rows_number();
        const size_t output_columns_number = get_output_columns_number() * get_output_rows_number() * filters.size();
        Matrix<double> outputs(samples_number, output_columns_number, 0.0);

        for(size_t i = 0; i < samples_number; i++)
        {
            const Vector<double> sample = input.get_row(i);
            const Vector < Matrix <double> > channels_matrix = sample.to_vector_matrix(input_rows_number, input_columns_number, input_channels_number);
            const Vector < Matrix < double > > matrix_with_padding = prepare_input(channels_matrix);
            const Vector < Matrix < double > > convolution_output = calculate_convolutions(matrix_with_padding, new_biases, new_synaptic_weights);
            outputs.set_row(i, to_vector(convolution_output));
       }
        return outputs;

    }

   Matrix<double> ConvolutionalLayer::calculate_combinations(const Matrix<double>& input, const Vector<double>& parameters) const
   {

       const size_t samples_number = input.get_rows_number();
       const size_t output_columns_number = get_output_columns_number() * get_output_rows_number() * filters.size();
       Matrix<double> outputs(samples_number, output_columns_number, 0.0);

       const Vector<double> new_biases = parameters_to_biases(parameters);
       const Matrix<double> new_synaptic_weights = parameters_to_synaptic_weights(parameters);

       for(size_t i = 0; i < samples_number; i++)
       {
           const Vector<double> sample = input.get_row(i);
           const Vector < Matrix <double> > channels_matrix = sample.to_vector_matrix(input_rows_number, input_columns_number, input_channels_number);
           const Vector < Matrix < double > > matrix_with_padding = prepare_input(channels_matrix);
           const Vector < Matrix < double > > convolution_output = calculate_convolutions(matrix_with_padding, new_biases, new_synaptic_weights);
           outputs.set_row(i, to_vector(convolution_output));
      }
       return outputs;
   }


   Tensor<double> ConvolutionalLayer::calculate_activations_derivatives(const Matrix<double>& combinations) const
   {
      if(combinations.empty())
      {
        ostringstream buffer;

        buffer << "OpenNN Exception: Convolutional Layer class.\n"
               << "Tensor<double> calculate_activations_derivatives(const Matrix<double>&) const method.\n"
               << "There is not any combinations values.\n";

        throw logic_error(buffer.str());
      }

       switch(activation_function)
       {
           case ConvolutionalLayer::Linear:
           {
                return Functions::tensor_linear_derivatives(combinations);
           }
/*
           case ConvolutionalLayer::Logistic:
           {
                return logistic_derivatives(combinations);
           }

           case ConvolutionalLayer::HyperbolicTangent:
           {
                return hyperbolic_tangent_derivatives(combinations);
           }

           case ConvolutionalLayer::Threshold:
           {
                return threshold_derivatives(combinations);
           }

           case ConvolutionalLayer::SymmetricThreshold:
           {
                return symmetric_threshold_derivatives(combinations);
           }
*/
           case ConvolutionalLayer::RectifiedLinear:
           {
                return Functions::tensor_rectified_linear_derivatives(combinations);
           }
/*
           case ConvolutionalLayer::ScaledExponentialLinear:
           {
                return scaled_exponential_linear_derivate(combinations);
           }

           case ConvolutionalLayer::SoftPlus:
           {
                return soft_plus_derivatives(combinations);
           }

           case ConvolutionalLayer::SoftSign:
           {
                return soft_sign_derivatives(combinations);
           }

           case ConvolutionalLayer::HardSigmoid:
           {
                return hard_sigmoid_derivatives(combinations);
           }

           case ConvolutionalLayer::ExponentialLinear:
           {
                return exponential_linear_derivatives(combinations);
           }
           */
       default:
           ostringstream buffer;

           buffer << "OpenNN Exception: Convolutional Layer class.\n"
                  << "Tensor<double> calculate_activations_derivatives(const Matrix<double>&) const method.\n"
                  << "The activation function is not defined.\n";

           throw logic_error(buffer.str());
       }
       return Tensor<double>();
   }

    Vector< Matrix<double> > ConvolutionalLayer::calculate_convolutions(const Vector< Matrix<double> >& inputs) const
    {

        const size_t filters_number = filters.size();

        Vector<Matrix <double> > outputs(filters_number);

        for(size_t i = 0; i < filters_number; i++)
        {
            outputs[i] = calculate_convolution_in_filter(filters[i], inputs) + biases[i];
        }

        return outputs;
    }

    Vector < Matrix <double> > ConvolutionalLayer::calculate_convolutions(const Vector<Matrix <double> > &inputs, const Vector<double>& new_biases, const Matrix<double>& new_synaptic_weights) const
    {
        const Vector<filter_t> new_filters = synaptic_weights_to_filters(new_synaptic_weights);

        const size_t new_filters_size = new_filters.size();

        Vector<Matrix <double> > outputs(new_filters_size);

        for(size_t i = 0; i < new_filters_size; i++)
        {
            outputs[i] = calculate_convolution_in_filter(new_filters[i], inputs) + new_biases[i];
        }

        return outputs;
    }

    Matrix<double> ConvolutionalLayer::calculate_convolution_in_filter(const filter_t& filter, const Vector< Matrix<double> >& inputs) const
    {
        const size_t channels_number = inputs.size();

        const size_t output_rows_number = get_output_rows_number();

        const size_t output_columns_number = get_output_columns_number();

        Matrix<double> output(output_rows_number, output_columns_number, 0.0);

        for(size_t i = 0; i < channels_number; i++)
        {
            output += convolution(inputs[i], filter[i]);
        }

        return output;
    }


    Matrix<double> ConvolutionalLayer::calculate_outputs(const Matrix<double>& inputs) const
    {
        return calculate_activations(calculate_combinations(inputs));
    }


    Matrix<double> ConvolutionalLayer::calculate_outputs(const Matrix<double>&inputs, const Vector<double>& new_biases, const Matrix<double>& new_synaptic_weights) const
    {
        return calculate_activations(calculate_combinations(inputs, new_biases, new_synaptic_weights));
    }


    Matrix<double> ConvolutionalLayer::convolution(const Matrix<double>& input, const Matrix<double>& kernel) const
    {
        const size_t output_rows_number = get_output_rows_number();

        const size_t output_columns_number = get_output_columns_number();

        Matrix<double> output(output_rows_number, output_columns_number);

        size_t initial_row_index = 0, initial_column_index = 0;

        for(size_t i = 0; i < output_rows_number; i++)
        {
            initial_column_index = 0;

            const Vector<size_t> submatrix_rows_indexes(initial_row_index, 1.0, initial_row_index + kernel_rows_number - 1);

            for(size_t j = 0; j < output_columns_number; j++)
            {

                const Vector<size_t> submatrix_column_indexes(initial_column_index, 1.0, initial_column_index + kernel_columns_number - 1);

                const Matrix<double> submatrix = input.get_submatrix(submatrix_rows_indexes, submatrix_column_indexes);

                const Matrix<double> product = submatrix * kernel;

                output(i,j) = product.calculate_sum();

                initial_column_index += column_stride;
            }

            initial_row_index += row_stride;
        }

        return output;
    }


    Vector<double> ConvolutionalLayer::parameters_to_biases(const Vector<double>& parameters) const
    {
        return parameters.get_last(biases.size());
    }


    Matrix<double> ConvolutionalLayer::parameters_to_synaptic_weights(const Vector<double>& parameters) const
    {
        const size_t filters_size = filters.size();
        const size_t output_rows_number = filters_size * kernel_rows_number * input_channels_number;
        const size_t output_columns_number = kernel_columns_number;

        return parameters.get_first(filters.size() * kernel_rows_number * kernel_columns_number * input_channels_number)
                .to_matrix(output_rows_number, output_columns_number);
    }


    Vector<filter_t> ConvolutionalLayer::parameters_to_filters(const Vector<double>& parameters) const
    {

        return synaptic_weights_to_filters(parameters_to_synaptic_weights(parameters));
    }

    Vector<filter_t> ConvolutionalLayer::synaptic_weights_to_filters(const Matrix<double>& synaptic_weights) const
    {
        const size_t filters_size = filters.size();

        Vector<filter_t> new_filters(filters_size,
                                     Vector<Matrix < double> >(input_channels_number,
                                                               Matrix<double>(kernel_rows_number, kernel_columns_number, 0.0)));

        Vector < Matrix <double> > filters_matrix = synaptic_weights.to_vector_matrix(filters_size, kernel_rows_number * input_channels_number,
                                                                                      kernel_columns_number);

        for(size_t i = 0; i < filters_size; i++)
        {
            new_filters[i] = filters_matrix[i].to_vector_matrix(input_channels_number,
                                                                kernel_rows_number, kernel_columns_number);
        }

        return new_filters;
    }

    inline ConvolutionalLayer::ActivationFunction ConvolutionalLayer::get_activation_function() const
    {
        return activation_function;
    }


    inline Vector<size_t> ConvolutionalLayer::get_input_shape() const
    {
        Vector<size_t> input_size(3);

        input_size[0] = input_channels_number;
        input_size[1] = input_rows_number;
        input_size[2] = input_columns_number;

        return input_size;
    }


    inline size_t ConvolutionalLayer::get_input_columns_number() const
    {
        return input_columns_number;
    }


    inline size_t ConvolutionalLayer::get_input_rows_number() const
    {
        return input_rows_number;
    }


    size_t ConvolutionalLayer::get_output_rows_number() const
    {
        return ((input_rows_number - kernel_rows_number + 2*padding_width) / row_stride ) + 1;
    }


    size_t ConvolutionalLayer::get_output_columns_number() const
    {
        return ((input_columns_number - kernel_columns_number + 2*padding_height) / column_stride ) + 1;
    }

    inline Vector<size_t> ConvolutionalLayer::get_ouput_shape() const
    {
        Vector<size_t> output_size(3);

        output_size[0] = get_filters_number();
        output_size[1] = get_output_rows_number();
        output_size[2] = get_output_columns_number();

        return output_size;
    }

    inline ConvolutionalLayer::PaddingOption ConvolutionalLayer::get_padding_option() const {
        return padding_option;
    }

    inline size_t ConvolutionalLayer::get_padding_width() const
    {
        return padding_width;
    }


    inline size_t ConvolutionalLayer::get_filters_number() const {

        return filters.size();
    }


    inline size_t  ConvolutionalLayer::get_kernel_rows_number() const
    {
        return kernel_rows_number;
    }


    inline size_t ConvolutionalLayer::get_kernel_columns_number() const
    {
        return kernel_columns_number;
    }

    Vector<double> ConvolutionalLayer::get_parameters() const
    {
        Vector<double> output;

        for(size_t i = 0; i < filters.size(); i++)
        {
            for(size_t j = 0; j < filters[i].size(); j++)
            {
                output = output.assemble(filters[i][j].to_vector());
            }
        }

        output = output.assemble(biases);
        return output;
    }


    size_t ConvolutionalLayer::get_parameters_number() const
    {
        return (filters.size() * input_channels_number * kernel_rows_number * kernel_columns_number) + biases.size();
    }


    void ConvolutionalLayer::initialize_biases(const double& bias_value)
    {
        const size_t biases_size = biases.size();

        for(size_t i = 0; i < biases_size; i++)
        {
            biases[i] = bias_value;
        }
    }


    void ConvolutionalLayer::initialize_synaptic_weights(const double& synaptic_weights_value)
    {
        const size_t filters_size = filters.size();

        for(size_t i = 0; i < filters_size; i++)
        {
            filters[i] = Vector<Matrix <double> >(input_channels_number, Matrix<double>(kernel_rows_number,
                                                                                        kernel_columns_number,
                                                                                        synaptic_weights_value));
        }

    }


    void ConvolutionalLayer::initialize_parameters(const double& value)
    {
        initialize_biases(value);
        initialize_synaptic_weights(value);
    }


    bool ConvolutionalLayer::needs_padding(const size_t& input_size, const size_t& weight_size) const
    {
        double _output_shape =  (( static_cast<double>(input_size - weight_size + 2*padding_width) / row_stride) + 1);

        if(_output_shape != static_cast<int>(_output_shape))
        {

            return true;
        } else
        {

            return false;
        }
    }



    Vector< Matrix <double> > ConvolutionalLayer::prepare_input(const Vector< Matrix <double> >& inputs) const
    {

        if(!check_input_shape(inputs))
//            throw exception("EXCEPTION: The input shape is not right.");
            throw ("EXCEPTION: The input shape is not right.");

        const size_t inputs_size = inputs.size();

        Vector< Matrix <double> > prepared_input(inputs_size);

        for(size_t i = 0; i < inputs_size; i++)
        {
            prepared_input[i] = inputs[i].insert_padding(padding_width, padding_height);
        }

        return prepared_input;
    }


    void ConvolutionalLayer::set_activation_function(const ConvolutionalLayer::ActivationFunction& new_activation_function)
    {
        activation_function = new_activation_function;
    }


    void ConvolutionalLayer::set_biases(const Vector<double>& new_biases)
    {
        biases = new_biases;
    }

    void ConvolutionalLayer::set_filters(const Vector<filter_t>& new_filters)
    {
        if(new_filters.size() == 0)
        {
//            throw exception("EXECPTION: The filters size must be greater than zero.");
            throw ("EXECPTION: The filters size must be greater than zero.");
        }
        filters = new_filters;
    }

    void set_filters(const Matrix<double>& new_filters)
    {
//        throw exception("EXCEPTION: Not implemented Method.\n");
        throw ("EXCEPTION: Not implemented Method.\n");
    }


    void ConvolutionalLayer::set_input_shape(const Vector<size_t>& inputs_size)
    {
        if(inputs_size.size() != 3)
        {
//            throw exception("EXCEPTION: The input shape of this layer must be [channels_number, rows_number, columns_number]");
            throw ("EXCEPTION: The input shape of this layer must be [channels_number, rows_number, columns_number]");
        } else
        {

            const size_t channels_number = inputs_size[0];
            const size_t rows_number = inputs_size[1];
            const size_t columns_number = inputs_size[2];

            set_input_channels_number(channels_number);
            set_input_rows_number(rows_number);
            set_input_columns_number(columns_number);
        }
    }


    void ConvolutionalLayer::set_input_channels_number(const size_t& new_channels_number)
    {
        if(new_channels_number == 0)
//            throw exception("EXCEPTION: The new input channels number must be greater than zero.");
            throw ("EXCEPTION: The new input channels number must be greater than zero.");

        input_channels_number = new_channels_number;
    }


    void ConvolutionalLayer::set_input_columns_number(const size_t& new_input_columns)
    {
        if(new_input_columns == 0)
        {
//            throw exception("EXCEPTION: The new input columns number must be greater than zero.");
            throw ("EXCEPTION: The new input columns number must be greater than zero.");
        }

        input_columns_number = new_input_columns;
    }


    void ConvolutionalLayer::set_input_rows_number(const size_t& new_input_rows)
    {
        if(new_input_rows == 0)
        {
//            throw exception("EXCEPTION: The new input rows number must be greater than zero.");
            throw ("EXCEPTION: The new input rows number must be greater than zero.");
        }
        input_rows_number = new_input_rows;
    }


    void ConvolutionalLayer::set_kernel_shape(const Vector<size_t>& new_kernel_shape)
    {
        if(new_kernel_shape.size() != 2)
        {
//            throw exception("EXCEPTION: It was expected a kernel shape of two dimensions: [kernel_rows_number, kernel_columns_number]");
            throw ("EXCEPTION: It was expected a kernel shape of two dimensions: [kernel_rows_number, kernel_columns_number]");
        }

        const size_t new_kernel_rows_number = new_kernel_shape[0];
        const size_t new_kernel_columns_number = new_kernel_shape[1];

        set_kernel_rows_number(new_kernel_rows_number);
        set_kernel_columns_number(new_kernel_columns_number);
    }


    void ConvolutionalLayer::set_kernel_columns_number(const size_t& new_kernel_columns_number)
    {
        if(new_kernel_columns_number == 0)
//            throw exception("EXCEPTION: The kernel columns number must be greater than zero.");
            throw ("EXCEPTION: The kernel columns number must be greater than zero.");

        kernel_columns_number = new_kernel_columns_number;
    }


    void ConvolutionalLayer::set_kernel_rows_number(const size_t& new_kernel_rows_number)
    {
        if(new_kernel_rows_number == 0)
//            throw exception("EXCEPTION: The kernel rows number must be greater than zero.");
            throw ("EXCEPTION: The kernel rows number must be greater than zero.");
        kernel_rows_number = new_kernel_rows_number;
    }


    void ConvolutionalLayer::set_padding_option(const  ConvolutionalLayer::PaddingOption& new_padding_option)
    {

        padding_option = new_padding_option;

        const size_t new_padding_width = (row_stride * (input_rows_number - 1) - input_rows_number + kernel_rows_number) / 2;

        const size_t new_padding_height = (column_stride * (input_columns_number - 1) - input_columns_number + kernel_columns_number) / 2;

        set_padding_width(new_padding_width);

        set_padding_height(new_padding_height);
    }


    void ConvolutionalLayer::set_padding_height(const size_t& new_padding_height)
    {
       padding_height = new_padding_height;
    }


    void ConvolutionalLayer::set_padding_width(const size_t& new_padding_width)
    {
        padding_width = new_padding_width;
    }


    void ConvolutionalLayer::set_row_stride(const size_t& new_stride_row)
    {

        if(new_stride_row == 0)
        {
//            throw exception("EXCEPTION: new_stride_row must be a positive number");
            throw ("EXCEPTION: new_stride_row must be a positive number");
        }

        row_stride = new_stride_row;
    }

    void ConvolutionalLayer::set_column_stride(const size_t& new_stride_column)
    {

        if(new_stride_column == 0)
        {
//            throw exception("EXCEPTION: new_stride_column must be a positive number");
            throw ("EXCEPTION: new_stride_column must be a positive number");
        }

        column_stride = new_stride_column;
    }


    void ConvolutionalLayer::set_parameters(const Vector<double>& new_parameters)
    {
        set_filters( parameters_to_filters(new_parameters) );
        set_biases( parameters_to_biases(new_parameters) );
    }

    Vector<double> ConvolutionalLayer::get_biases() const
    {
        return biases;
    }

    Vector<double> ConvolutionalLayer::get_synaptic_weights_of_input(const size_t& input) const
    {
        // Convolutional Layer with Stride (1,1)

        const size_t row_index = (input / input_columns_number);
        const size_t column_index = (input % input_columns_number);

        const size_t filters_size = filters.size();

        Vector<double> synaptic_weights;


        for(size_t filter = 0; filter < filters_size; filter++)
        {
            for(size_t channel = 0; channel < filters[filter].size(); channel++)
            {
                synaptic_weights.push_back(1.0);
            }
        }

        return synaptic_weights;
    }


    Vector<size_t> ConvolutionalLayer::get_inputs_indices(const size_t& neuron) const
    {
        if(neuron > get_neurons_number() - 1 )
        {
//            throw exception("EXCEPTION: The neuron is greater than the neurons number of this layer.");
            throw ("EXCEPTION: The neuron is greater than the neurons number of this layer.");
        }

        const size_t row_index = (neuron / get_output_columns_number());
        const size_t column_index = (neuron % get_output_columns_number());

        Vector<size_t> indices;

        for(size_t i = row_index; i < (row_index + kernel_rows_number); i++)
        {
            for(size_t j = column_index; j < (column_index + kernel_columns_number); j++)
            {
                indices.push_back(i*input_columns_number + j);
            }
        }

        return indices;
    }


    Vector<size_t> ConvolutionalLayer::get_synaptic_weights_indeces_of_input(const size_t& input) const
    {
        const size_t row_index = (input / input_columns_number);
        const size_t column_index = (input % input_columns_number);

        const size_t filters_size = filters.size();

        const size_t first_input_column_index = 0;
        const size_t last_input_column_index = input_columns_number - 1;
        const size_t first_input_row_index = 0;
        const size_t last_input_row_index = input_rows_number - 1;

        if(row_index == first_input_row_index && column_index == first_input_column_index)
        {
            return Vector<size_t>(1, 0);

        } else if(row_index == first_input_row_index && column_index == last_input_column_index)
        {
            return Vector<size_t>(1, kernel_columns_number - 1);

        } else if(row_index == last_input_row_index && column_index == first_input_column_index)
        {
            return Vector<size_t>(1, (kernel_rows_number - 1) * kernel_columns_number);

        } else if (row_index == last_input_row_index && column_index == last_input_column_index)
        {
            return Vector<size_t>(1, (kernel_rows_number - 1) * kernel_columns_number + (kernel_columns_number - 1));

        } else
        {
            //Change !!
            return Vector<size_t>(1, 0);
        }

        Vector<size_t> indices;

        for(size_t i = 0; i < filters_size; i++)
        {     
            for(size_t j = 0; j < filters[i].size(); j++)
            {

            }
        }


        return indices;
    }

    Matrix<double> ConvolutionalLayer::get_synaptic_weights() const
    {
       Matrix<double> synaptic_weights;

       const size_t filters_size = filters.size();

       for(size_t i = 0; i < filters_size; i++)
       {
           for(size_t j = 0; j < filters[i].size(); j++)
           {
               synaptic_weights.append_column(filters[i][j].to_vector());
           }
       }

       return synaptic_weights;
    }


    size_t ConvolutionalLayer::get_neurons_number() const
    {
        return get_output_rows_number() * get_output_columns_number();
    }


}

// OpenNN: Open Neural Networks Library.
// Copyright(C) 2005-2019 Artificial Intelligence Techniques, SL.
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Lesser General Public License for more details.

// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
