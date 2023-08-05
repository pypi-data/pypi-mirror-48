/****************************************************************************************************************/
/*                                                                                                              */
/*   OpenNN: Open Neural Networks Library                                                                       */
/*   www.opennn.net                                                                                             */
/*                                                                                                              */
/*   P E R C E P T R O N   L A Y E R   C L A S S   H E A D E R                                                  */
/*                                                                                                              */
/*   Artificial Intelligence Techniques SL                                                                      */
/*   artelnics@artelnics.com                                                                                    */
/*                                                                                                              */
/****************************************************************************************************************/

#ifndef __PERCEPTRONLAYER_H__
#define __PERCEPTRONLAYER_H__

// System includes

#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>

// OpenNN includes

#include "vector.h"
#include "layer.h"
#include "matrix.h"
#include "tensor.h"
#include "functions.h"

#ifdef __OPENNN_CUDA__

#include <cuda.h>
#include <cuda_runtime.h>
#include <cublas_v2.h>
#include <cublasXt.h>
#include <curand.h>

#include "cuda_runtime_api.h"

#include "neural_network_cuda.h"

#endif

namespace OpenNN
{

/// This class represents a layer of perceptrons.
/// Layers of perceptrons will be used to construct multilayer perceptrons. 

class PerceptronLayer : public Layer
{

public:
    // ENUMERATIONS

    /// Enumeration of available activation functions for the perceptron neuron model.

    enum ActivationFunction{Threshold, SymmetricThreshold, Logistic, HyperbolicTangent, Linear, RectifiedLinear, ExponentialLinear, ScaledExponentialLinear, SoftPlus, SoftSign, HardSigmoid};

   // DEFAULT CONSTRUCTOR

   explicit PerceptronLayer();

   // ARCHITECTURE CONSTRUCTOR 

   explicit PerceptronLayer(const size_t&, const size_t&, const ActivationFunction& = PerceptronLayer::HyperbolicTangent);

   // COPY CONSTRUCTOR

   PerceptronLayer(const PerceptronLayer&);

   // DESTRUCTOR
   
   virtual ~PerceptronLayer();

   // ASSIGNMENT OPERATOR

   PerceptronLayer& operator = (const PerceptronLayer&);

   // EQUAL TO OPERATOR

   bool operator == (const PerceptronLayer&) const;

   // GET METHODS

   bool is_empty() const;

   size_t get_inputs_number() const;
   size_t get_perceptrons_number() const;
   size_t get_neurons_number() const;
//   inline Vector<size_t> get_ouput_shape() const;
//   inline Vector<size_t> get_input_shape() const;

   // Parameters

   Vector<double> get_biases() const;
   Matrix<double> get_synaptic_weights() const;

   Vector<double> get_biases(const Vector<double>&) const;
   Matrix<double> get_synaptic_weights(const Vector<double>&) const;

   size_t get_parameters_number() const;
   Vector<double> get_parameters() const;

   // Activation functions

   const PerceptronLayer::ActivationFunction& get_activation_function() const;

   string write_activation_function() const;

   // Display messages

   const bool& get_display() const;

   // SET METHODS

   void set();
   void set(const size_t&, const size_t&, const PerceptronLayer::ActivationFunction& = PerceptronLayer::HyperbolicTangent);
   void set(const PerceptronLayer&);

   void set_default();

   // Architecture

   void set_inputs_number(const size_t&);
   void set_perceptrons_number(const size_t&);
   void set_input_shape(const Vector<size_t>&);

   // Parameters

   void set_biases(const Vector<double>&);
   void set_synaptic_weights(const Matrix<double>&);

   void set_parameters(const Vector<double>&);

   // Activation functions

   void set_activation_function(const ActivationFunction&);
   void set_activation_function(const string&);

   // Display messages

   void set_display(const bool&);

   // Growing and pruning

   void grow_input();
   void grow_perceptron();
   void grow_perceptrons(const size_t&);

   void prune_input(const size_t&);
   void prune_perceptron(const size_t&);

   // Initialization methods

   void initialize_random();

   // Parameters initialization methods

   void initialize_biases(const double&); 
   void initialize_synaptic_weights(const double&);
   void initialize_synaptic_weights_Glorot(const double&,const double&);

   void initialize_parameters(const double&);

   void randomize_parameters_uniform();
   void randomize_parameters_uniform(const double&, const double&);
   void randomize_parameters_uniform(const Vector<double>&, const Vector<double>&);
   void randomize_parameters_uniform(const Vector< Vector<double> >&);

   void randomize_parameters_normal();
   void randomize_parameters_normal(const double&, const double&);
   void randomize_parameters_normal(const Vector<double>&, const Vector<double>&);
   void randomize_parameters_normal(const Vector< Vector<double> >&);

   // Parameters norm 

   double calculate_parameters_norm() const;

   // Perceptron layer combinations

   Matrix<double> calculate_combinations(const Matrix<double>&) const;

   Matrix<double> calculate_combinations(const Matrix<double>&, const Vector<double>&) const;

   Matrix<double> calculate_combinations(const Matrix<double>&, const Vector<double>&, const Matrix<double>&) const;

   // Perceptron layer activations

   Matrix<double> calculate_activations(const Matrix<double>&) const;
   Tensor<double> calculate_activations_derivatives(const Matrix<double>&) const;
   Matrix<double> calculate_activations_derivatives_matrix(const Matrix<double>&) const;

   // Perceptron layer outputs

   Matrix<double> calculate_outputs(const Matrix<double>&) const;
   Matrix<double> calculate_outputs(const Matrix<double>&, const Vector<double>&, const Matrix<double>&) const;

   Matrix<double> calculate_outputs_combinations(const Matrix<double>&) const;

   // Expression methods

   string write_expression(const Vector<string>&, const Vector<string>&) const;
   string write_activation_function_expression() const;

   string object_to_string() const;


#ifdef __OPENNN_CUDA__

   float* get_biases_device() const;
   float* get_synaptic_weights_device() const;

   void allocate();

   void copy();

   void free();

   void print() const;

  void cuda_calculate_combinations(const size_t&, const float*, const float*, float*) const;
  void cuda_calculate_activations(const size_t&, const float*, float*) const;
  void cuda_calculate_activations_derivatives(const size_t&, const float*, float*) const;

#endif

private:

   // MEMBERS

   Vector<double> biases;

   Matrix<double> synaptic_weights;

   /// Activation function variable.

   ActivationFunction activation_function;

   /// Display messages to screen. 

   bool display;

#ifdef __OPENNN_CUDA__

   cublasHandle_t handle;

   float* biases_device = nullptr;

   float* synaptic_weights_device = nullptr;

#endif

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

