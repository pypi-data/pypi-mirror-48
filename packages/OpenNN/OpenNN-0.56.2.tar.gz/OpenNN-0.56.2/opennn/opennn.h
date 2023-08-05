/****************************************************************************************************************/
/*                                                                                                              */
/*   OpenNN: Open Neural Networks Library                                                                       */
/*   www.opennn.net                                                                                             */
/*                                                                                                              */
/*   O P E N   N E U R A L   N E T W O R K S   L I B R A R Y                                                    */
/*                                                                                                              */ 
/*   Artificial Intelligence Techniques SL                                                                      */
/*   artelnics@artelnics.com                                                                                    */
/*                                                                                                              */
/****************************************************************************************************************/

#ifndef __OPENNN_H__
#define __OPENNN_H__



// Data set

#include "data_set.h"
#include "instances.h"
#include "variables.h"
#include "missing_values.h"

// Neural network

#include "bounding_layer.h"
#include "inputs.h"
#include "outputs.h"
#include "perceptron_layer.h"
#include "multilayer_perceptron.h"
#include "probabilistic_layer.h"
#include "scaling_layer.h"
#include "unscaling_layer.h"
#include "inputs_trending_layer.h"
#include "outputs_trending_layer.h"
#include "neural_network.h"

// Training strategy

#include "loss_index.h"

#include "cross_entropy_error.h"
#include "mean_squared_error.h"
#include "minkowski_error.h"
#include "normalized_squared_error.h"
#include "sum_squared_error.h"
#include "weighted_squared_error.h"

#include "conjugate_gradient.h"
#include "gradient_descent.h"
#include "levenberg_marquardt_algorithm.h"
#include "quasi_newton_method.h"
#include "optimization_algorithm.h"
#include "learning_rate_algorithm.h"

// Model selection

#include "model_selection.h"
#include "order_selection_algorithm.h"
#include "incremental_order.h"
#include "golden_section_order.h"
#include "simulated_annealing_order.h"
#include "inputs_selection_algorithm.h"
#include "selective_pruning.h"
#include "growing_inputs.h"
#include "pruning_inputs.h"
#include "genetic_algorithm.h"

// Testing analysis

#include "testing_analysis.h"

// Utilities

#include "file_utilities.h"
#include "math.h"
#include "matrix.h"
#include "tensor.h"
#include "sparse_matrix.h"
#include "numerical_differentiation.h"
#include "numerical_integration.h"
#include "association_rules.h"
#include "text_analytics.h"
#include "vector.h"
#include "tinyxml2.h"
#include "correlation_analysis.h"
#include "functions.h"
#include "products.h"
#include "response_optimization.h"

// Layers

#include "layer.h"
#include "pooling_layer.h"
#include "convolutional_layer.h"
#include "max_pooling_layer.h"
#include "flatten_layer.h"

// Cuda

#ifdef __OPENNN_CUDA__

#include "utilities_cuda.h"

#endif

#endif

// OpenNN: Open Neural Networks Library.
// Copyright(C) 2005-2019 Artificial Intelligence Techniques, SL.
//
// This library is free software; you can redistribute it and/or
// modify it under the s of the GNU Lesser General Public
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
