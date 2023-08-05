#include "max_pooling_layer.h"

namespace OpenNN {

    Matrix<double> MaxPoolingLayer::calculate_outputs(const Matrix<double>& inputs) const
    {
        const size_t samples_number = inputs.get_rows_number();
        const size_t neurons_number = get_neurons_number();

        Matrix<double> outputs(samples_number, get_output_rows_number() * get_output_columns_number(), 0.0);

        for(size_t neuron = 0; neuron < neurons_number; neuron ++)
        {
            const Vector<size_t> indices = get_inputs_indices(neuron);

        }

        return outputs;
    }

    Matrix<double> MaxPoolingLayer::max_pool_operation(const Matrix<double>& input) const
    {
        const size_t output_columns_number = get_output_columns_number();

        const size_t output_rows_number = get_output_rows_number();

        Matrix<double> output(output_rows_number, output_columns_number, 0.0);

        for(size_t i = 0; i < output_rows_number; i++)
        {
            for(size_t j = 0; j < output_columns_number; j++)
            {
                const Vector<size_t> submatrix_rows_indexes(i, 1.0, j + pool_row_size - 1);

                const Vector<size_t> submatrix_column_indexes(j, 1.0, j + pool_column_size - 1);

                const Matrix<double> submatrix = input.get_submatrix(submatrix_rows_indexes, submatrix_column_indexes);

                output(i,j) = submatrix.calculate_maximum();
            }
        }

        return output;
    }
}

