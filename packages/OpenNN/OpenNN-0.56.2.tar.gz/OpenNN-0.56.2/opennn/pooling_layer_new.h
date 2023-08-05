#ifndef __POOLING_LAYER_H
#define __POOLING_LAYER_H
// System includes

#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <ctype.h>
#include "layer.h"
// OpenNN includes

#include "vector.h"
#include "matrix.h"

// TinyXml includes

#include "tinyxml2.h"
namespace OpenNN {
    class PoolingLayer : public Layer
    {

    public:

        enum PoolingMethod {NoPooling, MaxPooling, AveragePooling };

        PoolingLayer(const Vector<size_t>&);

        PoolingLayer(const Vector<size_t>&, const Vector<size_t> &);

        // Destructor

        virtual ~PoolingLayer();

        Matrix <double> calculate_outputs(const Matrix<double> &) const;

        Matrix <double> calculate_outputs_no_pooling(const Matrix<double> &) const;

        Matrix <double> calculate_outputs_max_pooling(const Matrix<double> &) const;

        Matrix<double> calculate_outputs_average_pooling(const Matrix<double> &) const;

        Tensor<double> calculate_activations_derivatives(const Matrix<double> &) const;

        Tensor<double> calculate_activations_no_pooling_derivatives(const Matrix<double>&) const;

        Tensor<double> calculate_activations_average_pooling_derivatives(const Matrix<double>&) const;

        Tensor<double> calculate_activations_max_pooling_derivatives(const Matrix<double>&) const;

        Matrix<double> calculate_layer_delta(const Matrix<double>&,const Matrix<double>&, const Matrix<double>&) const;

        Matrix<double> calculate_average_pooling_layer_delta(const Matrix<double>&, const Matrix<double>&, const Matrix<double>&) const;

        Matrix<double> calculate_max_pooling_layer_delta(const Matrix<double>&, const Matrix<double>&, const Matrix<double>&) const;

        Vector<size_t> get_inputs_indices(const size_t&) const;

         size_t get_input_rows_number() const;

         size_t get_input_column_number() const;

        size_t get_neurons_number() const;

         size_t get_output_rows_number() const;

         size_t get_output_columns_number() const;

         size_t get_padding_width() const;

         size_t get_row_stride() const;

         size_t get_column_stride() const;

         size_t get_pool_row_size() const;

         size_t get_pool_column_size() const;

        void set_input_rows_number(const size_t&);

        void set_input_columns_number(const size_t&);

        void set_padding_width(const size_t&);

        void set_row_stride(const size_t&);

        void set_column_stride(const size_t&);

        void set_pool_size(const size_t& pool_rows_number,
                           const size_t& pool_columns_number);

        void set_pooling_method(const PoolingMethod&);

        void set_default();


    protected:

        size_t input_rows_number;

        size_t input_columns_number;

        size_t pool_row_size = 2;

        size_t pool_column_size = 2;

        size_t padding_width = 0;

        size_t row_stride = 1;

        size_t column_stride = 1;

        PoolingMethod pooling_method = MaxPooling;

    };

}

#endif // POOLING_LAYER_H

