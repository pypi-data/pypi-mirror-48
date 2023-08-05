/****************************************************************************************************************/
/*                                                                                                              */
/*   OpenNN: Open Neural Networks Library                                                                       */
/*   www.opennn.net                                                                                             */
/*                                                                                                              */
/*   L A Y E R                                                                                                  */
/*                                                                                                              */
/*   Artificial Intelligence Techniques SL                                                                      */
/*   artelnics@artelnics.com                                                                                    */
/*                                                                                                              */
/****************************************************************************************************************/

#ifndef __LAYER_H_
#define __LAYER_H_

// System includes

#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <ctype.h>

// OpenNN includes

#include "vector.h"
#include "matrix.h"
#include "tensor.h"

// TinyXml includes

#include "tinyxml2.h"

namespace OpenNN {

class Layer
{

public:

        // ENUMERATIONS

        enum LayerType{Convolutional_Layer, Perceptron_Layer, Bounding_Layer, Pooling_Layer, Probabilistic_Layer, Scaling_Layer, Unscaling_Layer};

        explicit Layer();

        virtual ~Layer();

        // Parameters initialization methods

        virtual void initialize_parameters(const double&) {}

        virtual void randomize_parameters_uniform() const {}
        virtual void randomize_parameters_uniform() {}
        virtual void randomize_parameters_uniform(const double&, const double&) {}
        virtual void randomize_parameters_uniform(const Vector<double>&, const Vector<double>&) {}
        virtual void randomize_parameters_uniform(const Vector< Vector<double> >&) {}

        virtual void randomize_parameters_normal() {}
        virtual void randomize_parameters_normal(const double&, const double&) {}
        virtual void randomize_parameters_normal(const Vector<double>&, const Vector<double>&) {}
        virtual void randomize_parameters_normal(const Vector< Vector<double> >&) {}

        // Architecture

        virtual Vector<double> get_parameters() const;
        virtual inline size_t get_parameters_number() const;

        virtual Matrix<double> get_synaptic_weights() const {return Matrix<double>();}
        virtual Matrix<double> get_synaptic_weights(const Vector<double>&) const {return Matrix<double>();}


        virtual Vector<double> get_biases(const Vector<double>&) const {return Vector<double>();}
        virtual Vector<double> get_biases() const {return Vector<double>();}

        virtual void set_parameters(const Vector<double>&);

        void set_trainable(const bool&);

        bool is_trainable() const;

        // Combinations

        virtual Matrix<double> calculate_combinations(const Matrix<double>&) const;

        virtual Matrix<double> calculate_combinations(const Matrix<double>&, const Vector<double>&) const;

        virtual Matrix<double> calculate_combinations(const Matrix<double>&, const Vector<double>&, const Matrix<double>&) const;

        // Activations

        virtual Matrix<double> calculate_activations(const Matrix<double>&) const;

        virtual Matrix<double> calculate_activations(const Vector<Matrix<double>>&) const;

        virtual Tensor<double> calculate_activations_derivatives(const Matrix<double>&) const;

        virtual Matrix<double> calculate_activations_derivatives_matrix(const Matrix<double>&) const;

        virtual Matrix<double> calculate_activations_Jacobian(const Vector<Matrix<double>>&) const;

        // Calculate Outputs

        virtual Matrix<double> calculate_outputs(const Matrix<double>&) const = 0;

        virtual Matrix<double> calculate_outputs(const Matrix<double>&, const Vector<double>&, const Matrix<double>&) const;

        virtual Vector<double> parameters_to_biases(const Vector<double>&) const;
        virtual Matrix<double> parameters_to_synaptic_weights(const Vector<double>&) const;

        // Get neurons number

        virtual size_t get_neurons_number() const = 0;

        //Layer Tag

        string get_layer_type() const;
        void set_layer_type(const LayerType&);

    protected:

        bool trainable = true;

        LayerType layer_type = Perceptron_Layer;
    };
}


#endif // __LAYER_H_
