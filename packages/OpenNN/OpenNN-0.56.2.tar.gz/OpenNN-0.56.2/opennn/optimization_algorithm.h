/****************************************************************************************************************/
/*                                                                                                              */
/*   OpenNN: Open Neural Networks Library                                                                       */
/*   www.opennn.net                                                                                             */
/*                                                                                                              */
/*   O P T I M I Z A T I O N   A L G O R I T H M   C L A S S   H E A D E R                                      */
/*                                                                                                              */
/*   Artificial Intelligence Techniques SL                                                                      */
/*   artelnics@artelnics.com                                                                                    */
/*                                                                                                              */
/****************************************************************************************************************/

#ifndef __OPTIMIZATIONALGORITHM_H__
#define __OPTIMIZATIONALGORITHM_H__

// System includes

#include <iostream>
#include <fstream>
#include <algorithm>
#include <functional>
#include <limits>
#include <cmath>
#include <ctime>

// OpenNN includes

#include "loss_index.h"

// TinyXml includes

#include "tinyxml2.h"


#ifdef __OPENNN_CUDA__

#include "utilities_cuda.h"

#endif

namespace OpenNN
{

/// This abstract class represents the concept of optimization algorithm for a neural network. 
/// Any derived class must implement the perform_training() method.

class OptimizationAlgorithm
{

public:

   // DEFAULT CONSTRUCTOR

   explicit OptimizationAlgorithm();

   // GENERAL CONSTRUCTOR

   explicit OptimizationAlgorithm(LossIndex*);

   // XML CONSTRUCTOR

   explicit OptimizationAlgorithm(const tinyxml2::XMLDocument&);

   // DESTRUCTOR

   virtual ~OptimizationAlgorithm();

    // ASSIGNMENT OPERATOR

    virtual OptimizationAlgorithm& operator = (const OptimizationAlgorithm&);

    // EQUAL TO OPERATOR

    virtual bool operator == (const OptimizationAlgorithm&) const;

    // ENUMERATIONS

    /// Enumeration of all possibles condition of stop for the algorithms.

    enum StoppingCondition{MinimumParametersIncrementNorm, MinimumLossDecrease, LossGoal, GradientNormGoal,
                           MaximumSelectionErrorIncreases, MaximumIterationsNumber, MaximumTime};

   // STRUCTURES

   ///
   /// This structure contains the optimization algorithm results. 
   ///

   struct Results
   {
       explicit Results()
       {

       }

       virtual ~Results()
       {

       }

       string write_stopping_condition() const;

       /// Stopping condition of the algorithm.

       StoppingCondition stopping_condition;

      /// Returns a string representation of the results structure. 

      string object_to_string() const;

       /// Returns a default(empty) string matrix with the final results from training.

       Matrix<string> write_final_results(const size_t&) const;

       /// Resizes training history variables.

       void resize_training_history(const size_t&);

       /// Writes final results of the training.

       Matrix<string> write_final_results(const int& precision = 3) const;

       // Training history

       /// History of the loss function loss over the training iterations.

       Vector<double> training_error_history;

       /// History of the selection error over the training iterations.

       Vector<double> selection_error_history;

       // Final values

       /// Final neural network parameters vector.

       Vector<double> final_parameters;

       /// Final neural network parameters norm.

       double final_parameters_norm;

       /// Final loss function evaluation.

       double final_training_error;

       /// Final selection error.

       double final_selection_error;

       /// Final gradient norm.

       double final_gradient_norm;

       /// Elapsed time of the training process.

       double elapsed_time;

       /// Maximum number of training iterations.

       size_t epochs_number;

       /// Stopping criterion

       string stopping_criterion;
   };


   // METHODS

   // Get methods

   LossIndex* get_loss_index_pointer() const;

   bool has_loss_index() const;

   // Utilities

   const bool& get_display() const;

   const size_t& get_display_period() const;

   const size_t& get_save_period() const;

   const string& get_neural_network_file_name() const;

   // Set methods

   void set();
   void set(LossIndex*);

//   void set_epochs_number(const size_t&);

   virtual void set_default();

   virtual void set_loss_index_pointer(LossIndex*);

   virtual void set_display(const bool&);

   void set_display_period(const size_t&);

   void set_save_period(const size_t&);
   void set_neural_network_file_name(const string&);

   // Training methods

   virtual void check() const;

   /// Trains a neural network which has a loss index associated. 

   virtual Results perform_training() = 0;

   virtual string write_optimization_algorithm_type() const {return string();}

   // Serialization methods

   virtual string object_to_string() const;
   void print() const;

   virtual Matrix<string> to_string_matrix() const;

   virtual tinyxml2::XMLDocument* to_XML() const;
   virtual void from_XML(const tinyxml2::XMLDocument&);

   virtual void write_XML(tinyxml2::XMLPrinter&) const;
   //virtual void read_XML(   );

   void save(const string&) const;
   void load(const string&);

   virtual void initialize_random();

   bool check_cuda() const;

protected:

   // FIELDS

   /// Pointer to a loss index for a multilayer perceptron object.

   LossIndex* loss_index_pointer;

   size_t epochs_number = 10000;

   // UTILITIES

   /// Number of iterations between the training showing progress.

   size_t display_period;

   /// Number of iterations between the training saving progress.

   size_t save_period;

   /// Path where the neural network is saved.

   string neural_network_file_name;

   /// Display messages to screen.

   bool display;

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
