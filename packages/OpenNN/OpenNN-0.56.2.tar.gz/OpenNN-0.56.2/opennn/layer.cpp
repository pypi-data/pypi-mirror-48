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

#include "layer.h"

namespace OpenNN {

/// Default constructor

Layer::Layer()
{
}


Layer::~Layer()
{
}


// Architecture


Vector<double> Layer::get_parameters() const
{
    return Vector<double>();
}


inline size_t Layer::get_parameters_number() const
{
    return 0;
}


//Matrix<double> Layer::get_synaptic_weights() const
//{
//    return Matrix<double>();
//}


void Layer::set_parameters(const Vector<double>&)
{

}


// Activations

Matrix<double> Layer::calculate_activations(const Matrix<double>&) const
{
    return Matrix<double>();
}

Matrix<double> Layer::calculate_activations(const Vector<Matrix<double>>&) const
{
    return Matrix<double>();
}


Tensor<double> Layer::calculate_activations_derivatives(const Matrix<double>&) const
{
    return Tensor<double>();
}

Matrix<double> Layer::calculate_activations_derivatives_matrix(const Matrix<double>&) const
{
    return Matrix<double>();
}


Matrix<double> Layer::calculate_activations_Jacobian(const Vector<Matrix<double>>&) const
{
    return Matrix<double>();
}


// Combinations

Matrix<double> Layer::calculate_combinations(const Matrix<double>&) const
{
    return Matrix<double>();
}


Matrix<double> Layer::calculate_combinations(const Matrix<double>&, const Vector<double>&) const
{
    return Matrix<double>();
}


Matrix<double> Layer::calculate_combinations(const Matrix<double>&, const Vector<double>&, const Matrix<double>&) const
{
    return Matrix<double>();
}


Vector<double> Layer::parameters_to_biases(const Vector<double>&) const
{
    return Vector<double>();
}


Matrix<double> Layer::parameters_to_synaptic_weights(const Vector<double>&) const
{
    return Matrix<double>();
}

Matrix<double> Layer::calculate_outputs(const Matrix<double>& inputs, const Vector<double>&, const Matrix<double>&) const
{
    return calculate_outputs(inputs);
}


void Layer::set_trainable(const bool& trainable)
{
    this -> trainable = trainable;
}


bool Layer::is_trainable() const
{
    return trainable;
}


void Layer::set_layer_type(const LayerType& new_layer_type)
{
    layer_type = new_layer_type;
}


string Layer::get_layer_type() const
{
    string type_string;

    switch(layer_type)
    {
        case Convolutional_Layer:
        {
            type_string = "Convolutional_layer";
            break;
        }

        case Perceptron_Layer:
        {
            type_string = "Perceptron_layer";
            break;
        }

        case Bounding_Layer:
        {
            type_string = "Bounding_layer";
            break;
        }

        case Pooling_Layer:
        {
            type_string = "Pooling_layer";
            break;
        }

        case Probabilistic_Layer:
        {
            type_string = "Pooling_layer";
            break;
        }

        case Scaling_Layer:
        {
            type_string = "Scaling_layer";
            break;
        }

        case Unscaling_Layer:
        {
            type_string = "Unscaling_layer";
            break;
        }
    }

    return type_string;
}

}
