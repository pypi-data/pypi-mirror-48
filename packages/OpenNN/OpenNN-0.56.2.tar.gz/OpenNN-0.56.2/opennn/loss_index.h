/****************************************************************************************************************/
/*                                                                                                              */
/*   OpenNN: Open Neural Networks Library                                                                       */
/*   www.opennn.net                                                                                             */
/*                                                                                                              */
/*   L O S S   I N D E X   C L A S S   H E A D E R                                                              */
/*                                                                                                              */
/*   Artificial Intelligence Techniques SL                                                                      */
/*   artelnics@artelnics.com                                                                                    */
/*                                                                                                              */
/****************************************************************************************************************/

#ifndef __LOSSINDEX_H__
#define __LOSSINDEX_H__

// System includes

#include <string>
#include <sstream>
#include <iostream>
#include <cmath>

// OpenNN includes

#include "vector.h"
#include "matrix.h"

#include "data_set.h"

#include "neural_network.h"
#include "pooling_layer.h"

// TinyXml includes

#include "tinyxml2.h"

#ifdef __OPENNN_CUDA__

#include "utilities_cuda.h"

#endif

namespace OpenNN
{
/// This class represents the concept of error term. 
/// A error term is a summand in the loss functional expression.

class LossIndex
{

public:

   // DEFAULT CONSTRUCTOR

   explicit LossIndex();

   // NEURAL NETWORK CONSTRUCTOR

   explicit LossIndex(NeuralNetwork*);

   // DATA SET CONSTRUCTOR

   explicit LossIndex(DataSet*);

   // NEURAL NETWORK AND DATA SET CONSTRUCTOR

   explicit LossIndex(NeuralNetwork*, DataSet*);

   // XML CONSTRUCTOR

   explicit LossIndex(const tinyxml2::XMLDocument&);

   // COPY CONSTRUCTOR

   LossIndex(const LossIndex&);

   // DESTRUCTOR

   virtual ~LossIndex();

   // ASSIGNMENT OPERATOR

   LossIndex& operator = (const LossIndex&);

   // EQUAL TO OPERATOR

   bool operator == (const LossIndex&) const;

   enum RegularizationMethod{L1, L2, None};

   struct FirstOrderLoss
   {
       /// Default constructor.

       explicit FirstOrderLoss() {}

       explicit FirstOrderLoss(const size_t& new_parameters_number);

       void set_parameters_number(const size_t& new_parameters_number);

       Vector<double> get_gradient_from_device() const;

       virtual ~FirstOrderLoss();

       double loss;

       Vector<double> gradient;

       double* gradient_device;
   };


   struct SecondOrderLoss
   {
       /// Default constructor.

       SecondOrderLoss() {}

       SecondOrderLoss(const size_t& parameters_number)
       {
           loss = 0.0;
           gradient.set(parameters_number, 0.0);
           Hessian_approximation.set(parameters_number, parameters_number, 0.0);
       }

//       virtual ~SecondOrderLoss()
//       {
//       }

       double loss;
       Vector<double> gradient;
       Matrix<double> Hessian_approximation;
   };


   // METHODS

   // Get methods

   /// Returns a pointer to the neural network object associated to the error term.

   inline NeuralNetwork* get_neural_network_pointer() const 
   {
        #ifdef __OPENNN_DEBUG__

        if(!neural_network_pointer)
        {
             ostringstream buffer;

             buffer << "OpenNN Exception: LossIndex class.\n"
                    << "NeuralNetwork* get_neural_network_pointer() const method.\n"
                    << "Neural network pointer is nullptr.\n";

             throw logic_error(buffer.str());
        }

        #endif

      return(neural_network_pointer);
   }

   /// Returns a pointer to the data set object associated to the error term.

   inline DataSet* get_data_set_pointer() const 
   {
        #ifdef __OPENNN_DEBUG__

        if(!data_set_pointer)
        {
             ostringstream buffer;

             buffer << "OpenNN Exception: LossIndex class.\n"
                    << "DataSet* get_data_set_pointer() const method.\n"
                    << "DataSet pointer is nullptr.\n";

             throw logic_error(buffer.str());
        }

        #endif

      return(data_set_pointer);
   }

   const double& get_regularization_weight() const;
   const bool& get_display() const;
   const bool& get_cuda_enabled() const;

   bool has_neural_network() const;
   bool has_data_set() const;

   // Set methods

   void set();
   void set(NeuralNetwork*);
   void set(DataSet*);
   void set(NeuralNetwork*, DataSet*);

   void set(const LossIndex&);

   void set_neural_network_pointer(NeuralNetwork*);

   void set_data_set_pointer(DataSet*);

   void set_default();

   void set_regularization_method(const RegularizationMethod&);
   void set_regularization_method(const string&);
   void set_regularization_weight(const double&);

   void set_display(const bool&);

   bool has_selection() const;

   // Loss methods

   double calculate_training_loss() const;
   double calculate_training_loss(const Vector<double>&) const;
   double calculate_training_loss(const Vector<double>&, const double&) const;

   // Loss gradient methods

   Vector<double> calculate_training_loss_gradient() const;

   // ERROR METHODS

   virtual double calculate_training_error() const = 0;
   virtual double calculate_selection_error() const = 0;
   virtual double calculate_training_error(const Vector<double>&) const = 0;
   virtual double calculate_batch_error(const Vector<size_t>&) const = 0;

   virtual double calculate_training_error_cpu() const = 0;
   virtual double calculate_selection_error_cpu() const = 0;
   virtual double calculate_training_error_cpu(const Vector<double>&) const = 0;

   virtual double calculate_training_error_cuda() const = 0;
   virtual double calculate_selection_error_cuda() const = 0;
   virtual double calculate_training_error_cuda(const Vector<double>&) const = 0;

   virtual double calculate_batch_error_cuda(const Vector<size_t>&, const MultilayerPerceptron::Pointers&) const {return 0.0;}

   // GRADIENT METHODS

   virtual Vector<double> calculate_training_error_gradient() const = 0;

   virtual Vector<double> calculate_training_error_gradient_cpu() const = 0;
   virtual Vector<double> calculate_training_error_gradient_cuda() const = 0;

   virtual Vector<double> calculate_batch_error_gradient(const Vector<size_t>&) const {return Vector<double>();}

   // ERROR TERMS METHODS

   virtual Vector<double> calculate_batch_error_terms(const Vector<size_t>&) const  {return Vector<double>();}
   virtual Matrix<double> calculate_batch_error_terms_Jacobian(const Vector<size_t>&) const  {return Matrix<double>();}

   virtual FirstOrderLoss calculate_batch_first_order_loss(const Vector<size_t>&) const {return FirstOrderLoss();}

   virtual FirstOrderLoss calculate_batch_first_order_loss_cuda(const Vector<size_t>&, const MultilayerPerceptron::Pointers&) const
   {return FirstOrderLoss();}

   virtual FirstOrderLoss calculate_batch_first_order_loss_cuda(const Vector<size_t>&, const MultilayerPerceptron::Pointers&, const Vector<double*>&) const
   {return FirstOrderLoss();}

   virtual FirstOrderLoss calculate_first_order_loss() const {return FirstOrderLoss();}
   virtual SecondOrderLoss calculate_terms_second_order_loss() const {return SecondOrderLoss();}

   // Regularization methods

   double calculate_regularization() const;
   Vector<double> calculate_regularization_gradient() const;
   Matrix<double> calculate_regularization_Hessian() const;

   double calculate_regularization(const Vector<double>&) const;
   Vector<double> calculate_regularization_gradient(const Vector<double>&) const;
   Matrix<double> calculate_regularization_Hessian(const Vector<double>&) const;

   // Serialization methods

   string object_to_string() const;

   tinyxml2::XMLDocument* to_XML() const;
   void from_XML(const tinyxml2::XMLDocument&);

   virtual void write_XML(tinyxml2::XMLPrinter&) const;

   void regularization_from_XML(const tinyxml2::XMLDocument&);
   void write_regularization_XML(tinyxml2::XMLPrinter&) const;

   string get_error_type() const;
   virtual string get_error_type_text() const;

   string write_information() const;

   string write_regularization_method() const;

   // Checking methods

   void check() const;
   void check_new() const;

   // METHODS

   Vector< Matrix<double> > calculate_layers_delta(const Vector< Matrix<double> >&, const Matrix<double>&) const;

   Vector< Matrix<double> > calculate_layers_delta_new(const Vector< Tensor<double> >&, const Matrix<double>&) const;
   Vector< Matrix<double> > calculate_layers_delta_new(const Vector<Matrix<double>>&, const Vector< Tensor<double> >&, const Matrix<double>&) const;

   Vector<double> calculate_layer_error_gradient(const Matrix<double>&, const Matrix<double>&) const;

   Vector<double> calculate_error_gradient(const Matrix<double>&, const Vector< Matrix<double> >&, const Vector< Matrix<double> >&) const;
   Vector<double> calculate_error_gradient_new(const Matrix<double>&, const Vector< Matrix<double> >&, const Vector< Matrix<double> >&) const;

   Matrix<double> calculate_layer_error_terms_Jacobian(const Matrix<double>&, const Matrix<double>&) const;
   Matrix<double> calculate_error_terms_Jacobian(const Matrix<double>&, const Vector< Matrix<double> >&, const Vector< Matrix<double> >&) const;

   bool check_cuda();

#ifdef __OPENNN_CUDA__

  struct CudaFirstOrderLoss
  {
      /// Default constructor.

      CudaFirstOrderLoss(LossIndex* new_loss_index_pointer)
      {
          loss_index_pointer = new_loss_index_pointer;

          allocate();
      }

      virtual ~CudaFirstOrderLoss()
      {
          free();
      }

      // Members

      LossIndex* loss_index_pointer;

      float loss = 0.0;

      float* gradient = nullptr;

      float* output_gradient = nullptr;

      Vector<float*> layers_delta;
      Vector<float*> auxiliar_matrices;

      float* errors = nullptr;

      float* ones = nullptr;

      // Methods

      void allocate();

      void print() const;

      void free();
  };


  void cuda_calculate_first_order_loss(const DataSet::CudaBatch&, const MultilayerPerceptron::CudaForwardPropagation&, LossIndex::CudaFirstOrderLoss&) const;

  void cuda_calculate_layers_delta(const MultilayerPerceptron::CudaForwardPropagation&, LossIndex::CudaFirstOrderLoss&) const;

  virtual void cuda_calculate_output_gradient(const DataSet::CudaBatch&, const MultilayerPerceptron::CudaForwardPropagation&, LossIndex::CudaFirstOrderLoss&) const {}

  virtual void cuda_calculate_error(const DataSet::CudaBatch&, const MultilayerPerceptron::CudaForwardPropagation&, LossIndex::CudaFirstOrderLoss&) const {}

  virtual void cuda_calculate_error_gradient(const DataSet::CudaBatch&, const MultilayerPerceptron::CudaForwardPropagation&, LossIndex::CudaFirstOrderLoss&) const {}


#endif

protected:

   // MEMBERS

   /// Pointer to a multilayer perceptron object.

   NeuralNetwork* neural_network_pointer;

   /// Pointer to a data set object.

   DataSet* data_set_pointer;

   RegularizationMethod regularization_method;

   double regularization_weight = 0.0;

   /// Use CUDA or CPU mode.

   bool cuda_enabled = false;

   /// Display messages to screen. 

   bool display;  

#ifdef __OPENNN_CUDA__

   cublasHandle_t handle;

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
