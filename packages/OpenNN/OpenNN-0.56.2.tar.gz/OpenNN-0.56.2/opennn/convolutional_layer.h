                      /****************************************************************************************************************/
/*                                                                                                              */
/*   OpenNN: Open Neural Networks Library                                                                       */
/*   www.opennn.net                                                                                             */
/*                                                                                                              */
/*   B O U N D I N G   L A Y E R   C L A S S   H E A D E R                                                      */
/*                                                                                                              */
/*   Artificial Intelligence Techniques SL                                                                      */
/*   artelnics@artelnics.com                                                                                    */
/*                                                                                                              */
/****************************************************************************************************************/

#ifndef __CONVOLUTIONALLAYER_H__
#define __CONVOLUTIONALLAYER_H__

// System includes

#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <ctype.h>
#include <stdexcept>

// OpenNN includes

#include "vector.h"
#include "matrix.h"
#include "layer.h"
#include "functions.h"

// TinyXml includes

#include "tinyxml2.h"

namespace OpenNN
{

    /// This class represents a layer of bounding neurons.
    /// A bounding layer is used to ensure that variables will never fall below or above given values.

    typedef  Vector< Matrix < double> > filter_t;

    class ConvolutionalLayer : public Layer
    {

    public:

        /// Enumeration of available activation functions for the perceptron layer.

        enum ActivationFunction {Threshold, SymmetricThreshold, Logistic, HyperbolicTangent, Linear, RectifiedLinear, ExponentialLinear, ScaledExponentialLinear, SoftPlus, SoftSign, HardSigmoid};

        enum PaddingOption {NoPadding, Same};


        /// @brief Default Constructor
        /// @param filters_number sets the number of filters for this convolutional layer.
        /// @param kernel_shape sets the rows and the columns number of each kernel.
        /// @param input_shape set the input channels number, the input rows number and the input columns number.

        explicit ConvolutionalLayer(const size_t&, const Vector<size_t>&, const Vector<size_t>&);

        /// @param filters_number sets the number of filters for this convolutional layer.
        /// @param kernel_rows_number sets the rows number of the kernel for all filter in the layer.
        /// @param kernel_columns_number sets the columns number of the kernel for all filter in the layer.
        /// @param padding_option sets a Zero-Padding over the input.

       explicit ConvolutionalLayer(const size_t&, const size_t&, const size_t&, const PaddingOption& = NoPadding);

       Matrix<double> calculate_combinations(const Matrix<double>&) const;

       Matrix<double> calculate_combinations(const Matrix<double>&, const Vector<double>&) const;

       Matrix<double> calculate_combinations(const Matrix<double>&, const Vector<double>&, const Matrix<double>&) const;

       Matrix<double> calculate_activations(const Matrix<double>& ) const;

       Tensor<double> calculate_activations_derivatives(const Matrix<double>&) const;

       Vector< Matrix<double> > calculate_convolutions(const Vector< Matrix<double> >&) const;

       Vector< Matrix<double> > calculate_convolutions(const Vector< Matrix<double> >&, const Vector<double>&, const Matrix<double>&) const;

       Matrix<double> calculate_convolution_in_filter(const filter_t&, const Vector< Matrix<double> >&) const;

       Matrix<double> calculate_outputs(const Matrix<double>&) const;

       Matrix<double> calculate_outputs(const Matrix<double>&, const Vector<double>&, const Matrix<double>&) const;

       Matrix<double> convolution(const Matrix<double>&, const Matrix<double>&) const;

       bool check_input_shape(const Vector< Matrix <double> >&) const;

       Vector<double> parameters_to_biases(const Vector<double>&) const;

       Matrix<double> parameters_to_synaptic_weights(const Vector<double>&) const;

       Vector<filter_t> parameters_to_filters(const Vector<double>&) const;

       Vector<filter_t> synaptic_weights_to_filters(const Matrix<double>&) const;

       Vector<double> get_biases() const;

       inline ActivationFunction get_activation_function() const;

       inline Vector<size_t> get_input_shape() const;

       inline size_t get_input_rows_number() const;

       inline size_t get_input_columns_number() const;

       size_t get_output_rows_number() const;

       size_t get_output_columns_number() const;

       Vector<size_t> get_ouput_shape() const;

       inline PaddingOption get_padding_option() const;

       inline size_t get_padding_width() const;

       inline size_t get_column_stride() const;

       inline size_t get_row_stride() const;

       inline size_t get_filters_number() const;

       inline Vector<size_t> get_kernel_shape() const;

       inline size_t get_kernel_rows_number() const;

       inline size_t get_kernel_columns_number() const;

       size_t get_neurons_number() const;

       Vector<double> get_parameters() const;

       Matrix<double> get_synaptic_weights() const;

       Vector<size_t> get_synaptic_weights_indeces_of_input(const size_t&) const;

       Vector<size_t> get_inputs_indices(const size_t&) const;

       inline size_t get_synaptic_weights_number() const;

       inline size_t get_bias_number() const;

       Vector<double> get_synaptic_weights_of_input(const size_t&) const;

       size_t get_parameters_number() const;

       void initialize_biases(const double&);

       void initialize_synaptic_weights(const double&);

       void initialize_parameters(const double&);

       bool needs_padding(const size_t&, const size_t&) const;

       void set_activation_function(const ActivationFunction&);

       void set_biases(const Vector<double>&);

       void set_filters(const Vector<filter_t>&);

       void set_filters(const Matrix<double>&);

       void set_input_shape(const Vector<size_t>&);

       void set_input_rows_number(const size_t&);

       void set_input_columns_number(const size_t&);

       void set_input_channels_number(const size_t&);

       void set_kernel_shape(const Vector<size_t>&);

       void set_kernel_rows_number(const size_t&);

       void set_kernel_columns_number(const size_t&);

       void set_padding_option(const PaddingOption&);

       void set_padding_width(const size_t&);

       void set_padding_height(const size_t&);

       void set_parameters(const Vector<double>&);

       void set_row_stride(const size_t&);

       void set_column_stride(const size_t&);

       Vector< Matrix <double> > prepare_input(const Vector< Matrix <double> >&) const;

    protected:

       // New members

       Matrix<double> synaptic_weights;
       //
       Vector < filter_t > filters;

       Vector<double> biases;

       size_t row_stride = 1;

       size_t column_stride = 1;

       size_t padding_width = 0;

       size_t padding_height = 0;

       size_t input_rows_number;

       size_t input_columns_number;

       size_t input_channels_number;

       ActivationFunction activation_function = RectifiedLinear;

       PaddingOption padding_option = NoPadding;

       // Derived members

       size_t kernel_rows_number;

       size_t kernel_columns_number;

    };
}

#endif


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

