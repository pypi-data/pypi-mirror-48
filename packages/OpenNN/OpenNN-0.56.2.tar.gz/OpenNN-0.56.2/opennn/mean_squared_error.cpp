/****************************************************************************************************************/
/*                                                                                                              */
/*   OpenNN: Open Neural Networks Library                                                                       */
/*   www.opennn.net                                                                                             */
/*                                                                                                              */
/*   M E A N   S Q U A R E D   E R R O R   C L A S S                                                            */
/*                                                                                                              */
/*   Artificial Intelligence Techniques SL                                                                      */
/*   artelnics@artelnics.com                                                                                    */
/*                                                                                                              */
/****************************************************************************************************************/

// OpenNN includes

#include "mean_squared_error.h"

namespace OpenNN
{
// DEFAULT CONSTRUCTOR

/// Default constructor.
/// It creates a mean squared error term not associated to any
/// neural network and not measured on any data set.
/// It also initializes all the rest of class members to their default values.

MeanSquaredError::MeanSquaredError() : LossIndex()
{
}


// NEURAL NETWORK CONSTRUCTOR

/// Neural network constructor.
/// It creates a mean squared error term object associated to a
/// neural network object but not measured on any data set object.
/// It also initializes all the rest of class members to their default values.
/// @param new_neural_network_pointer Pointer to a neural network object.

MeanSquaredError::MeanSquaredError(NeuralNetwork* new_neural_network_pointer)
: LossIndex(new_neural_network_pointer)
{
}


// DATA SET CONSTRUCTOR

/// Data set constructor.
/// It creates a mean squared error term not associated to any
/// neural network but to be measured on a given data set object.
/// It also initializes all the rest of class members to their default values.
/// @param new_data_set_pointer Pointer to a data set object.

MeanSquaredError::MeanSquaredError(DataSet* new_data_set_pointer)
: LossIndex(new_data_set_pointer)
{
}


// NEURAL NETWORK AND DATA SET CONSTRUCTOR

/// Neural network and data set constructor.
/// It creates a mean squared error term object associated to a
/// neural network and measured on a data set.
/// It also initializes all the rest of class members to their default values.
/// @param new_neural_network_pointer Pointer to a neural network object.
/// @param new_data_set_pointer Pointer to a data set object.

MeanSquaredError::MeanSquaredError(NeuralNetwork* new_neural_network_pointer, DataSet* new_data_set_pointer)
: LossIndex(new_neural_network_pointer, new_data_set_pointer)
{
}


// XML CONSTRUCTOR

/// XML constructor.
/// It creates a mean squared error object with all pointers set to nullptr.
/// The object members are loaded by means of a XML document.
/// Please be careful with the format of that file, which is specified in the OpenNN manual.
/// @param mean_squared_error_document TinyXML document with the mean squared error elements.

MeanSquaredError::MeanSquaredError(const tinyxml2::XMLDocument& mean_squared_error_document)
 : LossIndex(mean_squared_error_document)
{
    from_XML(mean_squared_error_document);
}


// COPY CONSTRUCTOR

/// Copy constructor.
/// It creates a copy of an existing mean squared error object.
/// @param other_mean_squared_error Mean squared error object to be copied.

MeanSquaredError::MeanSquaredError(const MeanSquaredError& other_mean_squared_error)
: LossIndex(other_mean_squared_error)
{
}


// DESTRUCTOR

/// Destructor.

MeanSquaredError::~MeanSquaredError()
{
}


// METHODS

double MeanSquaredError::calculate_training_error() const
{
    if(cuda_enabled)
    {
        return calculate_training_error_cuda();
    }
    else
    {
        return calculate_training_error_cpu();
    }
}


double MeanSquaredError::calculate_training_error_cpu() const
{
#ifdef __OPENNN_DEBUG__

check();

#endif

    // Multilayer perceptron

    const MultilayerPerceptron* multilayer_perceptron_pointer = neural_network_pointer->get_multilayer_perceptron_pointer();

    // Data set

    const size_t training_instances_number = data_set_pointer->get_instances_pointer()->get_training_instances_number();

    const Vector< Vector<size_t> > training_batches = data_set_pointer->get_instances_pointer()->get_training_batches();

    const size_t batches_number = training_batches.size();

    double training_error = 0.0;

    #pragma omp parallel for reduction(+ : training_error)

    for(int i = 0; i < static_cast<int>(batches_number); i++)
    {
        const Matrix<double> inputs = data_set_pointer->get_inputs(training_batches[static_cast<unsigned>(i)]);
        const Matrix<double> targets = data_set_pointer->get_targets(training_batches[static_cast<unsigned>(i)]);

        const Matrix<double> outputs = multilayer_perceptron_pointer->calculate_outputs(inputs);

        const double batch_error = outputs.calculate_sum_squared_error(targets);

        training_error += batch_error;
    }

    return training_error/static_cast<double>(training_instances_number);
}


double MeanSquaredError::calculate_training_error_cuda() const
{
    double training_error = 0.0;

#ifdef __OPENNN_CUDA__

    const Vector<size_t> architecture = neural_network_pointer->get_multilayer_perceptron_pointer()->get_architecture();
    const Vector<string> layer_activations = neural_network_pointer->get_multilayer_perceptron_pointer()->write_layers_activation_function();
    const size_t training_instances_number = data_set_pointer->get_instances_pointer()->get_training_instances_number();

    const size_t layers_number = architecture.size() - 1;

    Vector<double*> weights_pointers(layers_number);
    Vector<double*> biases_pointers(layers_number);

    Vector<size_t> weights_rows_numbers(layers_number);
    Vector<size_t> weights_columns_numbers(layers_number);

    Vector<size_t> bias_rows_numbers(layers_number);

    for(size_t i = 0; i < layers_number; i++)
    {
        weights_rows_numbers[i] = architecture[i];
        weights_columns_numbers[i] = architecture[i+1];

        bias_rows_numbers[i] = architecture[i+1];

        const Vector<double> weights_data = neural_network_pointer->get_multilayer_perceptron_pointer()->get_layer(i).get_synaptic_weights().to_vector();
        const Vector<double> biases_data = neural_network_pointer->get_multilayer_perceptron_pointer()->get_layer(i).get_biases();

        mallocCUDA(&weights_pointers[i], static_cast<int>(weights_rows_numbers[i]*weights_columns_numbers[i]*sizeof(double)));
        mallocCUDA(&biases_pointers[i], static_cast<int>(bias_rows_numbers[i]*sizeof(double)));

        memcpyCUDA(weights_pointers[i], weights_data.data(), static_cast<int>(weights_rows_numbers[i]*weights_columns_numbers[i]*sizeof(double)));
        memcpyCUDA(biases_pointers[i], biases_data.data(), static_cast<int>(bias_rows_numbers[i]*sizeof(double)));
    }

    Vector<double> loss_parameters;

    const string loss_method = "SUM_SQUARED_ERROR";

    const Vector< Vector<size_t> > training_batches = data_set_pointer->get_instances_pointer()->get_training_batches();

    const size_t batches_number = training_batches.size();

    for(size_t i = 0; i < batches_number; i++)
    {
        const Matrix<double> inputs_matrix = data_set_pointer->get_inputs(training_batches[static_cast<unsigned>(i)]);
        const double* input_data = inputs_matrix.data();
        const size_t input_rows = inputs_matrix.get_rows_number();
        const size_t input_columns = inputs_matrix.get_columns_number();

        const Matrix<double> targets = data_set_pointer->get_targets(training_batches[static_cast<unsigned>(i)]);
        const double* target_data = targets.data();
        const size_t target_rows = targets.get_rows_number();
        const size_t target_columns = targets.get_columns_number();

        double* input_data_d;

        mallocCUDA(&input_data_d, static_cast<int>(input_rows*input_columns*sizeof(double)));
        memcpyCUDA(input_data_d, input_data, static_cast<int>(input_rows*input_columns*sizeof(double)));

        double* target_data_d;

        mallocCUDA(&target_data_d, static_cast<int>(target_rows*target_columns*sizeof(double)));
        memcpyCUDA(target_data_d, target_data, static_cast<int>(target_rows*target_columns*sizeof(double)));

        training_error += calculateLossCUDA(weights_pointers, weights_rows_numbers, weights_columns_numbers,
                                            biases_pointers, bias_rows_numbers,
                                            input_data_d, input_rows, input_columns,
                                            target_data_d, target_rows, target_columns,
                                            layer_activations, loss_method,
                                            loss_parameters);

        freeCUDA(input_data_d);
        freeCUDA(target_data_d);
    }

    training_error /= training_instances_number;

    for(size_t i = 0; i < layers_number; i++)
    {
        freeCUDA(weights_pointers[i]);
        freeCUDA(biases_pointers[i]);
    }

#endif

    return training_error;
}


double MeanSquaredError::calculate_selection_error() const
{
    if(cuda_enabled)
    {
        return calculate_selection_error_cuda();
    }
    else
    {
        return calculate_selection_error_cpu();
    }
}


double MeanSquaredError::calculate_selection_error_cpu() const
{
#ifdef __OPENNN_DEBUG__

check();

#endif

    // Multilayer perceptron

    const MultilayerPerceptron* multilayer_perceptron_pointer = neural_network_pointer->get_multilayer_perceptron_pointer();

    // Data set

    const size_t selection_instances_number = data_set_pointer->get_instances_pointer()->get_selection_instances_number();

    const Vector< Vector<size_t> > selection_batches = data_set_pointer->get_instances_pointer()->get_selection_batches();

    const size_t batches_number = selection_batches.size();

    double selection_error = 0.0;

    #pragma omp parallel for reduction(+ : selection_error)

    for(int i = 0; i < static_cast<int>(batches_number); i++)
    {
        const Matrix<double> inputs = data_set_pointer->get_inputs(selection_batches[static_cast<unsigned>(i)]);
        const Matrix<double> targets = data_set_pointer->get_targets(selection_batches[static_cast<unsigned>(i)]);

        const Matrix<double> outputs = multilayer_perceptron_pointer->calculate_outputs(inputs);

        const double batch_error = outputs.calculate_sum_squared_error(targets);

        selection_error += batch_error;
    }

    return selection_error/static_cast<double>(selection_instances_number);
}


double MeanSquaredError::calculate_selection_error_cuda() const
{
    double selection_error = 0.0;

#ifdef __OPENNN_CUDA__

    const Vector<size_t> architecture = neural_network_pointer->get_multilayer_perceptron_pointer()->get_architecture();
    const Vector<string> layer_activations = neural_network_pointer->get_multilayer_perceptron_pointer()->write_layers_activation_function();
    const size_t selection_instances_number = data_set_pointer->get_instances_pointer()->get_selection_instances_number();

    const size_t layers_number = architecture.size() - 1;

    vector<double*> weights_pointers(layers_number);
    vector<double*> biases_pointers(layers_number);

    Vector<size_t> weights_rows_numbers(layers_number);
    Vector<size_t> weights_columns_numbers(layers_number);

    Vector<size_t> bias_rows_numbers(layers_number);

    for(size_t i = 0; i < layers_number; i++)
    {
        weights_rows_numbers[i] = architecture[i];
        weights_columns_numbers[i] = architecture[i+1];

        bias_rows_numbers[i] = architecture[i+1];

        const Vector<double> weights_data = neural_network_pointer->get_multilayer_perceptron_pointer()->get_layer(i).get_synaptic_weights().to_vector();
        const Vector<double> biases_data = neural_network_pointer->get_multilayer_perceptron_pointer()->get_layer(i).get_biases();

        mallocCUDA(&weights_pointers[i], static_cast<int>(weights_rows_numbers[i]*weights_columns_numbers[i]*sizeof(double)));
        mallocCUDA(&biases_pointers[i], static_cast<int>(bias_rows_numbers[i]*sizeof(double)));

        memcpyCUDA(weights_pointers[i], weights_data.data(), static_cast<int>(weights_rows_numbers[i]*weights_columns_numbers[i]*sizeof(double)));
        memcpyCUDA(biases_pointers[i], biases_data.data(), static_cast<int>(bias_rows_numbers[i]*sizeof(double)));
    }

    const Vector<double> loss_parameters;

    const string loss_method = "SUM_SQUARED_ERROR";

    const Vector< Vector<size_t> > selection_batches = data_set_pointer->get_instances_pointer()->get_selection_batches();

    const size_t batches_number = selection_batches.size();

    for(size_t i = 0; i < batches_number; i++)
    {
        const Matrix<double> inputs_matrix = data_set_pointer->get_inputs(selection_batches[static_cast<unsigned>(i)]);
        const double* input_data = inputs_matrix.data();
        const size_t input_rows = inputs_matrix.get_rows_number();
        const size_t input_columns = inputs_matrix.get_columns_number();

        const Matrix<double> targets = data_set_pointer->get_targets(selection_batches[static_cast<unsigned>(i)]);
        const double* target_data = targets.data();
        const size_t target_rows = targets.get_rows_number();
        const size_t target_columns = targets.get_columns_number();

        double* input_data_d;

        mallocCUDA(&input_data_d, static_cast<int>(input_rows*input_columns*sizeof(double)));
        memcpyCUDA(input_data_d, input_data, static_cast<int>(input_rows*input_columns*sizeof(double)));

        double* target_data_d;

        mallocCUDA(&target_data_d, static_cast<int>(target_rows*target_columns*sizeof(double)));
        memcpyCUDA(target_data_d, target_data, static_cast<int>(target_rows*target_columns*sizeof(double)));

        selection_error += calculateLossCUDA(weights_pointers, weights_rows_numbers, weights_columns_numbers,
                                             biases_pointers, bias_rows_numbers,
                                             input_data_d, input_rows, input_columns,
                                             target_data_d, target_rows, target_columns,
                                             layer_activations, loss_method,
                                             loss_parameters);

        freeCUDA(input_data_d);
        freeCUDA(target_data_d);
    }

    selection_error /= selection_instances_number;

    for(size_t i = 0; i < layers_number; i++)
    {
        freeCUDA(weights_pointers[i]);
        freeCUDA(biases_pointers[i]);
    }

#endif

    return selection_error;
}


double MeanSquaredError::calculate_training_error(const Vector<double>& parameters) const
{
    if(cuda_enabled)
    {
        return calculate_training_error_cuda(parameters);
    }
    else
    {
        return calculate_training_error_cpu(parameters);
    }
}


double MeanSquaredError::calculate_training_error_cpu(const Vector<double>& parameters) const
{
#ifdef __OPENNN_DEBUG__

check();

#endif

    // Multilayer perceptron

    const MultilayerPerceptron* multilayer_perceptron_pointer = neural_network_pointer->get_multilayer_perceptron_pointer();

    // Data set

    const size_t training_instances_number = data_set_pointer->get_instances_pointer()->get_training_instances_number();

    const Vector< Vector<size_t> > training_batches = data_set_pointer->get_instances_pointer()->get_training_batches();

    const size_t batches_number = training_batches.size();

    double training_error = 0.0;

    #pragma omp parallel for reduction(+ : training_error)

    for(int i = 0; i < static_cast<int>(batches_number); i++)
    {
        const Matrix<double> inputs = data_set_pointer->get_inputs(training_batches[static_cast<unsigned>(i)]);
        const Matrix<double> targets = data_set_pointer->get_targets(training_batches[static_cast<unsigned>(i)]);

        const Matrix<double> outputs = multilayer_perceptron_pointer->calculate_outputs(inputs, parameters);

        const double batch_error = outputs.calculate_sum_squared_error(targets);

        training_error += batch_error;
    }

    return training_error/static_cast<double>(training_instances_number);
}




double MeanSquaredError::calculate_training_error_cuda(const Vector<double>& parameters) const
{
    double training_error = 0.0;
#ifdef __OPENNN_CUDA__
    const Vector<size_t> architecture = neural_network_pointer->get_multilayer_perceptron_pointer()->get_architecture();
    const Vector<string> layer_activations = neural_network_pointer->get_multilayer_perceptron_pointer()->write_layers_activation_function();
    const size_t training_instances_number = data_set_pointer->get_instances_pointer()->get_training_instances_number();

    const size_t layers_number = architecture.size() - 1;

    Vector<double*> weights_pointers(layers_number);
    Vector<double*> biases_pointers(layers_number);

    Vector<size_t> weights_rows_numbers(layers_number);
    Vector<size_t> weights_columns_numbers(layers_number);

    Vector<size_t> bias_rows_numbers(layers_number);

    size_t index = 0;

    for(size_t i = 0; i < layers_number; i++)
    {
        weights_rows_numbers[i] = architecture[i];
        weights_columns_numbers[i] = architecture[i+1];

        bias_rows_numbers[i] = architecture[i+1];

        const Vector<double> weights_data = parameters.get_subvector(index, index+weights_rows_numbers[i]*weights_columns_numbers[i]-1);
        index += weights_rows_numbers[i]*weights_columns_numbers[i];

        const Vector<double> biases_data = parameters.get_subvector(index, index+bias_rows_numbers[i]-1);
        index += bias_rows_numbers[i];

        mallocCUDA(&weights_pointers[i], static_cast<int>(weights_rows_numbers[i]*weights_columns_numbers[i]*sizeof(double)));
        mallocCUDA(&biases_pointers[i], static_cast<int>(bias_rows_numbers[i]*sizeof(double)));

        memcpyCUDA(weights_pointers[i], weights_data.data(), static_cast<int>(weights_rows_numbers[i]*weights_columns_numbers[i]*sizeof(double)));
        memcpyCUDA(biases_pointers[i], biases_data.data(), static_cast<int>(bias_rows_numbers[i]*sizeof(double)));
    }

    const Vector<double> loss_parameters;

    const string loss_method = "SUM_SQUARED_ERROR";

    const Vector< Vector<size_t> > training_batches = data_set_pointer->get_instances_pointer()->get_training_batches();

    const size_t batches_number = training_batches.size();

    for(size_t i = 0; i < batches_number; i++)
    {
        const Matrix<double> inputs_matrix = data_set_pointer->get_inputs(training_batches[static_cast<unsigned>(i)]);
        const double* input_data = inputs_matrix.data();
        const size_t input_rows = inputs_matrix.get_rows_number();
        const size_t input_columns = inputs_matrix.get_columns_number();

        const Matrix<double> targets = data_set_pointer->get_targets(training_batches[static_cast<unsigned>(i)]);
        const double* target_data = targets.data();
        const size_t target_rows = targets.get_rows_number();
        const size_t target_columns = targets.get_columns_number();

        double* input_data_d;

        mallocCUDA(&input_data_d, static_cast<int>(input_rows*input_columns*sizeof(double)));
        memcpyCUDA(input_data_d, input_data, static_cast<int>(input_rows*input_columns*sizeof(double)));

        double* target_data_d;

        mallocCUDA(&target_data_d, static_cast<int>(target_rows*target_columns*sizeof(double)));
        memcpyCUDA(target_data_d, target_data, static_cast<int>(target_rows*target_columns*sizeof(double)));

        training_error += calculateLossCUDA(weights_pointers, weights_rows_numbers, weights_columns_numbers,
                                            biases_pointers, bias_rows_numbers,
                                            input_data_d, input_rows, input_columns,
                                            target_data_d, target_rows, target_columns,
                                            layer_activations, loss_method,
                                            loss_parameters);

        freeCUDA(input_data_d);
        freeCUDA(target_data_d);
    }

    training_error /= training_instances_number;

    for(size_t i = 0; i < layers_number; i++)
    {
        freeCUDA(weights_pointers[i]);
        freeCUDA(biases_pointers[i]);
    }
#endif
    return training_error;
}




double MeanSquaredError::calculate_batch_error(const Vector<size_t>& batch_indices) const
{
#ifdef __OPENNN_DEBUG__

check();

#endif

    // Data set

    const size_t instances_number = batch_indices.size();

    // Neural network

    const MultilayerPerceptron* multilayer_perceptron_pointer = neural_network_pointer->get_multilayer_perceptron_pointer();

    // Loss index

    const Matrix<double> inputs = data_set_pointer->get_inputs(batch_indices);
    const Matrix<double> targets = data_set_pointer->get_targets(batch_indices);

    const Matrix<double> outputs = multilayer_perceptron_pointer->calculate_outputs(inputs);

    const double batch_error = outputs.calculate_sum_squared_error(targets);

    return (batch_error/instances_number);
}




double MeanSquaredError::calculate_batch_error_cuda(const Vector<size_t>& batch_indices, const MultilayerPerceptron::Pointers& pointers) const
{
    double batch_error = 0.0;
#ifdef __OPENNN_CUDA__
    const size_t layers_number = pointers.architecture.size() - 1;

    const Matrix<double> inputs_matrix = data_set_pointer->get_inputs(batch_indices);
    const double* input_data = inputs_matrix.data();
    const size_t input_rows = inputs_matrix.get_rows_number();
    const size_t input_columns = inputs_matrix.get_columns_number();

    const Matrix<double> targets = data_set_pointer->get_targets(batch_indices);
    const double* target_data = targets.data();
    const size_t target_rows = targets.get_rows_number();
    const size_t target_columns = targets.get_columns_number();

    double* input_data_d;

    mallocCUDA(&input_data_d, static_cast<int>(input_rows*input_columns*sizeof(double)));
    memcpyCUDA(input_data_d, input_data, static_cast<int>(input_rows*input_columns*sizeof(double)));

    double* target_data_d;

    mallocCUDA(&target_data_d, static_cast<int>(target_rows*target_columns*sizeof(double)));

    memcpyCUDA(target_data_d, target_data, static_cast<int>(target_rows*target_columns*sizeof(double)));

    Vector<size_t> weights_rows_numbers(layers_number);
    Vector<size_t> weights_columns_numbers(layers_number);

    Vector<size_t> bias_rows_numbers(layers_number);

    for(size_t i = 0; i < layers_number; i++)
    {
        weights_rows_numbers[i] = pointers.architecture[i];
        weights_columns_numbers[i] = pointers.architecture[i+1];

        bias_rows_numbers[i] = pointers.architecture[i+1];
    }

    Vector<double> loss_parameters;

    const string loss_method = get_error_type();

    batch_error = calculateLossCUDA(pointers.weights_pointers, weights_rows_numbers, weights_columns_numbers,
                                    pointers.biases_pointers, bias_rows_numbers,
                                    input_data_d, input_rows, input_columns,
                                    target_data_d, target_rows, target_columns,
                                    pointers.layer_activations, loss_method,
                                    loss_parameters);

    freeCUDA(input_data_d);
    freeCUDA(target_data_d);
#endif
    return batch_error;
}




Vector<double> MeanSquaredError::calculate_training_error_gradient() const
{
    if(cuda_enabled)
    {
        return calculate_training_error_gradient_cuda();
    }
    else
    {
        return calculate_training_error_gradient_cpu();
    }
}


Vector<double> MeanSquaredError::calculate_training_error_gradient_cpu() const
{
#ifdef __OPENNN_DEBUG__

check();

#endif

    // Neural network

    const MultilayerPerceptron* multilayer_perceptron_pointer = neural_network_pointer->get_multilayer_perceptron_pointer();

    const size_t layers_number = multilayer_perceptron_pointer->get_layers_number();

    const size_t parameters_number = multilayer_perceptron_pointer->get_parameters_number();

    // Data set

    const size_t training_instances_number = data_set_pointer->get_instances().get_training_instances_number();

    const Vector< Vector<size_t> > training_batches = data_set_pointer->get_instances_pointer()->get_training_batches();

    const size_t batches_number = training_batches.size();

    // Loss index

    Vector<double> training_error_gradient(parameters_number, 0.0);

    #pragma omp parallel for

    for(int i = 0; i < static_cast<int>(batches_number); i++)
    {
        const Matrix<double> inputs = data_set_pointer->get_inputs(training_batches[static_cast<unsigned>(i)]);
        const Matrix<double> targets = data_set_pointer->get_targets(training_batches[static_cast<unsigned>(i)]);

        const MultilayerPerceptron::ForwardPropagation forward_propagation
                = multilayer_perceptron_pointer->calculate_forward_propagation(inputs);

        const Matrix<double> output_gradient
                = calculate_output_gradient(forward_propagation.layers_activations[layers_number-1], targets);

        const Vector< Matrix<double> > layers_delta
                = calculate_layers_delta(forward_propagation.layers_activations_derivatives, output_gradient);

        const Vector<double> batch_gradient
                = calculate_error_gradient(inputs, forward_propagation.layers_activations, layers_delta);

        #pragma omp critical

        training_error_gradient += batch_gradient;
    }

    return training_error_gradient/static_cast<double>(training_instances_number);
}


Vector<double> MeanSquaredError::calculate_training_error_gradient_cuda() const
{
    const size_t parameters_number = neural_network_pointer->get_multilayer_perceptron_pointer()->get_parameters_number();

    Vector<double> training_error_gradient(parameters_number, 0.0);

#ifdef __OPENNN_CUDA__

    const Vector<size_t> architecture = neural_network_pointer->get_multilayer_perceptron_pointer()->get_architecture();
    const Vector<string> layer_activations = neural_network_pointer->get_multilayer_perceptron_pointer()->write_layers_activation_function();
    const size_t training_instances_number = data_set_pointer->get_instances().get_training_instances_number();

    const size_t layers_number = architecture.size() - 1;

    Vector<double*> weights_d(layers_number);
    Vector<double*> biases_d(layers_number);

    Vector<size_t> weights_rows_numbers(layers_number);
    Vector<size_t> weights_columns_numbers(layers_number);

    Vector<size_t> bias_rows_numbers(layers_number);

    for(size_t i = 0; i < layers_number; i++)
    {
        weights_rows_numbers[i] = architecture[i];
        weights_columns_numbers[i] = architecture[i+1];

        bias_rows_numbers[i] = architecture[i+1];

        const Vector<double> weights_data = neural_network_pointer->get_multilayer_perceptron_pointer()->get_layer(i).get_synaptic_weights().to_vector();
        const Vector<double> biases_data = neural_network_pointer->get_multilayer_perceptron_pointer()->get_layer(i).get_biases();

        mallocCUDA(&weights_d[i], static_cast<int>(weights_rows_numbers[i]*weights_columns_numbers[i]*sizeof(double)));
        mallocCUDA(&biases_d[i], static_cast<int>(bias_rows_numbers[i]*sizeof(double)));

        memcpyCUDA(weights_d[i], weights_data.data(), static_cast<int>(weights_rows_numbers[i]*weights_columns_numbers[i]*sizeof(double)));
        memcpyCUDA(biases_d[i], biases_data.data(), static_cast<int>(bias_rows_numbers[i]*sizeof(double)));
    }

    Vector<double> loss_parameters;

    string loss_method = "SUM_SQUARED_ERROR";

    const Vector< Vector<size_t> > training_batches = data_set_pointer->get_instances_pointer()->get_training_batches();

    const size_t batches_number = training_batches.size();

    for(size_t i = 0; i < batches_number; i++)
    {
        const Matrix<double> inputs_matrix = data_set_pointer->get_inputs(training_batches[static_cast<unsigned>(i)]);
        const double* input_data = inputs_matrix.data();
        const size_t input_rows = inputs_matrix.get_rows_number();
        const size_t input_columns = inputs_matrix.get_columns_number();

        Matrix<double> targets = data_set_pointer->get_targets(training_batches[static_cast<unsigned>(i)]);
        const double* target_data = targets.data();
        const size_t target_rows = targets.get_rows_number();
        const size_t target_columns = targets.get_columns_number();

        double* input_data_d;
        double* target_data_d;

        mallocCUDA(&input_data_d, static_cast<int>(input_rows*input_columns*sizeof(double)));
        mallocCUDA(&target_data_d, static_cast<int>(target_rows*target_columns*sizeof(double)));

        memcpyCUDA(input_data_d, input_data, static_cast<int>(input_rows*input_columns*sizeof(double)));
        memcpyCUDA(target_data_d, target_data, static_cast<int>(target_rows*target_columns*sizeof(double)));

        double* training_error_gradient_d;

        mallocCUDA(&training_error_gradient_d, static_cast<int>(parameters_number*sizeof(double)));

        calculateGradientCUDA(weights_d, weights_rows_numbers, weights_columns_numbers,
                              biases_d, bias_rows_numbers,
                              input_data_d, input_rows, input_columns,
                              target_data_d, target_rows, target_columns,
                              training_error_gradient_d,
                              layer_activations, loss_method, loss_parameters);

        Vector<double> batch_gradient(parameters_number, 0.0);

        getHostVector(training_error_gradient_d, batch_gradient.data(), static_cast<int>(parameters_number*sizeof(double)));

        training_error_gradient += batch_gradient;

        freeCUDA(input_data_d);
        freeCUDA(target_data_d);
        freeCUDA(training_error_gradient_d);
    }

    training_error_gradient /= training_instances_number;

    for(size_t i = 0; i < layers_number; i++)
    {
        freeCUDA(weights_d[i]);
        freeCUDA(biases_d[i]);
    }

#endif

    return training_error_gradient;
}


LossIndex::FirstOrderLoss MeanSquaredError::calculate_first_order_loss() const
{
#ifdef __OPENNN_DEBUG__

check();

#endif

    // Multilayer perceptron

    const MultilayerPerceptron* multilayer_perceptron_pointer = neural_network_pointer->get_multilayer_perceptron_pointer();

    const size_t layers_number = multilayer_perceptron_pointer->get_layers_number();

    const size_t parameters_number = multilayer_perceptron_pointer->get_parameters_number();

    // Data set

    const size_t training_instances_number = data_set_pointer->get_instances_pointer()->get_training_instances_number();

    const Vector< Vector<size_t> > training_batches = data_set_pointer->get_instances_pointer()->get_training_batches();

    const size_t batches_number = training_batches.size();

    FirstOrderLoss first_order_loss(parameters_number);

    #pragma omp parallel for

    for(int i = 0; i < static_cast<int>(batches_number); i++)
    {
        const Matrix<double> inputs = data_set_pointer->get_inputs(training_batches[static_cast<unsigned>(i)]);
        const Matrix<double> targets = data_set_pointer->get_targets(training_batches[static_cast<unsigned>(i)]);

        const MultilayerPerceptron::ForwardPropagation forward_propagation
                = multilayer_perceptron_pointer->calculate_forward_propagation(inputs);

        const Vector<double> error_terms
                = calculate_error_terms(forward_propagation.layers_activations[layers_number-1], targets);

        Matrix<double> output_gradient = (forward_propagation.layers_activations[layers_number-1] - targets)/*/error_terms*/;
        output_gradient.divide_by_rows(error_terms);

        const Vector< Matrix<double> > layers_delta
                = calculate_layers_delta(forward_propagation.layers_activations_derivatives, output_gradient);

        const Matrix<double> error_terms_Jacobian
                = calculate_error_terms_Jacobian(inputs, forward_propagation.layers_activations, layers_delta);

        const Matrix<double> error_terms_Jacobian_transpose = error_terms_Jacobian.calculate_transpose();

        const double loss = Products::dot(error_terms, error_terms);

        const Vector<double> gradient = Products::dot(error_terms_Jacobian_transpose, error_terms);

        #pragma omp critical
        {
            first_order_loss.loss += loss;
            first_order_loss.gradient += gradient;
         }
    }

    first_order_loss.loss /= static_cast<double>(training_instances_number);
    first_order_loss.gradient *= (2.0/static_cast<double>(training_instances_number));

    return first_order_loss;
}


Vector<double> MeanSquaredError::calculate_batch_error_gradient(const Vector<size_t>& batch_indices) const
{
#ifdef __OPENNN_DEBUG__

check();

#endif

    // Data set

    const size_t instances_number = batch_indices.size();

    // Neural network

    const MultilayerPerceptron* multilayer_perceptron_pointer = neural_network_pointer->get_multilayer_perceptron_pointer();

    const size_t layers_number = multilayer_perceptron_pointer->get_layers_number();

    // Loss index

    const Matrix<double> inputs = data_set_pointer->get_inputs(batch_indices);
    const Matrix<double> targets = data_set_pointer->get_targets(batch_indices);

    const MultilayerPerceptron::ForwardPropagation forward_propagation
            = multilayer_perceptron_pointer->calculate_forward_propagation(inputs);

    const Matrix<double> output_gradient = calculate_output_gradient(forward_propagation.layers_activations[layers_number-1], targets);

    const Vector< Matrix<double> > layers_delta = calculate_layers_delta(forward_propagation.layers_activations_derivatives, output_gradient);

    const Vector<double> batch_error_gradient = calculate_error_gradient(inputs, forward_propagation.layers_activations, layers_delta);

    return batch_error_gradient/static_cast<double>(instances_number);

}


LossIndex::FirstOrderLoss MeanSquaredError::calculate_batch_first_order_loss(const Vector<size_t>& batch_indices) const
{
#ifdef __OPENNN_DEBUG__

check();

#endif

    // Data set

    const size_t instances_number = batch_indices.size();

    // Neural network

    const MultilayerPerceptron* multilayer_perceptron_pointer = neural_network_pointer->get_multilayer_perceptron_pointer();

    const size_t layers_number = multilayer_perceptron_pointer->get_layers_number();

    const size_t parameters_number = multilayer_perceptron_pointer->get_parameters_number();

    // Loss index

    FirstOrderLoss first_order_loss(parameters_number);

    const Matrix<double> inputs = data_set_pointer->get_inputs(batch_indices);

    const Matrix<double> targets = data_set_pointer->get_targets(batch_indices);

    const MultilayerPerceptron::ForwardPropagation forward_propagation=
           multilayer_perceptron_pointer->calculate_forward_propagation(inputs);

    const Matrix<double> output_gradient = calculate_output_gradient(forward_propagation.layers_activations[layers_number-1], targets);

    const Vector< Matrix<double> > layers_delta = calculate_layers_delta(forward_propagation.layers_activations_derivatives, output_gradient);

    const Vector<double> batch_error_gradient = calculate_error_gradient(inputs, forward_propagation.layers_activations, layers_delta);

    const double batch_error = forward_propagation.layers_activations[layers_number-1].calculate_sum_squared_error(targets);

    first_order_loss.loss = batch_error / static_cast<double>(instances_number);
    first_order_loss.gradient = batch_error_gradient/static_cast<double>(instances_number);

    // Regularization

    if(regularization_method != RegularizationMethod::None)
    {
        first_order_loss.loss += calculate_regularization();
        first_order_loss.gradient += calculate_regularization_gradient();
    }

    return first_order_loss;
}


LossIndex::FirstOrderLoss MeanSquaredError::calculate_batch_first_order_loss_cuda(const Vector<size_t>& batch_indices,
                                                                                  const MultilayerPerceptron::Pointers& pointers) const
{    
    FirstOrderLoss first_order_loss;

#ifdef __OPENNN_CUDA__

    const size_t instances_number = batch_indices.size();
    const size_t layers_number = pointers.architecture.size() - 1;

    const size_t inputs_number = data_set_pointer->get_variables().get_inputs_number();
    const size_t targets_number = data_set_pointer->get_variables().get_targets_number();

    Matrix<double> outputs(instances_number, pointers.architecture[layers_number]);
    double* output_data = outputs.data();
    const size_t output_rows = instances_number;
    const size_t output_columns = pointers.architecture[layers_number];

    Vector<double*> data_device = data_set_pointer->host_to_device(batch_indices);

    Vector<size_t> weights_rows_numbers(layers_number);
    Vector<size_t> weights_columns_numbers(layers_number);

    Vector<size_t> bias_rows_numbers(layers_number);

    size_t parameters_number = 0;

    for(size_t i = 0; i < layers_number; i++)
    {
        weights_rows_numbers[i] = pointers.architecture[i];

        weights_columns_numbers[i] = pointers.architecture[i+1];

        bias_rows_numbers[i] = pointers.architecture[i+1];

        parameters_number += pointers.architecture[i]*pointers.architecture[i+1] + pointers.architecture[i+1];
    }

    first_order_loss.set_parameters_number(parameters_number);

    Vector<double> loss_parameters;

    const string loss_method = get_error_type();

    first_order_loss.loss = calculateFirstOrderLossCUDA(pointers.weights_pointers.to_std_vector(), weights_rows_numbers, weights_columns_numbers,
                                                        pointers.biases_pointers.to_std_vector(), bias_rows_numbers,
                                                        data_device[0], instances_number, inputs_number,
                                                        data_device[1], instances_number, targets_number,
                                                        first_order_loss.gradient_device,
                                                        output_data, output_rows, output_columns,
                                                        pointers.layer_activations.to_std_vector(), loss_method, loss_parameters);

    // Regularization

    if(regularization_method != RegularizationMethod::None)
    {
        first_order_loss.loss += calculate_regularization(pointers.get_parameters());
        Vector<double> gradient_regularization = calculate_regularization_gradient(pointers.get_parameters());

        double* gradient_regularization_device;
        double alpha = 1;

        cublasHandle_t handle;

        cublasCreate(&handle);

        mallocCUDA(&gradient_regularization_device, static_cast<int>(parameters_number*sizeof(double)));
        memcpyCUDA(gradient_regularization_device, gradient_regularization.data(), static_cast<int>(parameters_number*sizeof(double)));

        cublasDaxpy(handle, static_cast<int>(parameters_number), &alpha,
                    gradient_regularization_device, 1, first_order_loss.gradient_device, 1);

        cublasDestroy(handle);

        freeCUDA(gradient_regularization_device);
    }

    freeCUDA(data_device[0]);
    freeCUDA(data_device[1]);    

#endif

    return first_order_loss;
}


LossIndex::FirstOrderLoss MeanSquaredError::calculate_batch_first_order_loss_cuda(const Vector<size_t>& batch_indices,
                                                                                  const MultilayerPerceptron::Pointers& pointers, const Vector<double*>& data_device) const
{    
    FirstOrderLoss first_order_loss;

#ifdef __OPENNN_CUDA__
    const size_t instances_number = batch_indices.size();
    const size_t layers_number = pointers.architecture.size() - 1;

    const size_t inputs_number = data_set_pointer->get_variables().get_inputs_number();
    const size_t targets_number = data_set_pointer->get_variables().get_targets_number();

    Matrix<double> outputs(instances_number, pointers.architecture[layers_number]);
    double* output_data = outputs.data();
    const size_t output_rows = instances_number;
    const size_t output_columns = pointers.architecture[layers_number];

    Vector<size_t> weights_rows_numbers(layers_number);
    Vector<size_t> weights_columns_numbers(layers_number);

    Vector<size_t> bias_rows_numbers(layers_number);

    size_t parameters_number = 0;

    for(size_t i = 0; i < layers_number; i++)
    {
        weights_rows_numbers[i] = pointers.architecture[i];
        weights_columns_numbers[i] = pointers.architecture[i+1];

        bias_rows_numbers[i] = pointers.architecture[i+1];

        parameters_number += pointers.architecture[i]*pointers.architecture[i+1] + pointers.architecture[i+1];
    }

    first_order_loss.set_parameters_number(parameters_number);

    Vector<double> loss_parameters;

    const string loss_method = get_error_type();

    first_order_loss.loss = calculateFirstOrderLossCUDA(pointers.weights_pointers.to_std_vector(), weights_rows_numbers, weights_columns_numbers,
                                                        pointers.biases_pointers.to_std_vector(), bias_rows_numbers,
                                                        data_device[0], instances_number, inputs_number,
                                                        data_device[1], instances_number, targets_number,
                                                        first_order_loss.gradient_device,
                                                        output_data, output_rows, output_columns,
                                                        pointers.layer_activations.to_std_vector(), loss_method, loss_parameters);

    // Regularization

    if(regularization_method != RegularizationMethod::None)
    {
        first_order_loss.loss += calculate_regularization(pointers.get_parameters());
        Vector<double> gradient_regularization = calculate_regularization_gradient(pointers.get_parameters());

        double* gradient_regularization_device;
        double alpha = 1;

        cublasHandle_t handle;

        cublasCreate(&handle);

        mallocCUDA(&gradient_regularization_device, parameters_number*sizeof(double));
        memcpyCUDA(gradient_regularization_device, gradient_regularization.data(), parameters_number*sizeof(double));

        cublasDaxpy(handle, static_cast<int>(parameters_number), &alpha,
                    gradient_regularization_device, 1, first_order_loss.gradient_device, 1);

        cublasDestroy(handle);

        freeCUDA(gradient_regularization_device);
    }
#endif
    return first_order_loss;
}




Matrix<double> MeanSquaredError::calculate_output_gradient(const Matrix<double>& outputs, const Matrix<double>& targets) const
{
#ifdef __OPENNN_DEBUG__

check_new();

#endif

    return (outputs-targets)*2.0;
}


Matrix<double> MeanSquaredError::calculate_output_gradient_new(const Matrix<double>& outputs, const Matrix<double>& targets) const
{
#ifdef __OPENNN_DEBUG__

check_new();

#endif

    return (outputs-targets)*2.0;
}


/// Returns loss vector of the error terms function for the mean squared error.
/// It uses the error back-propagation method.

Vector<double> MeanSquaredError::calculate_error_terms(const Matrix<double>& outputs, const Matrix<double>& targets) const
{
   // Control sentence

   #ifdef __OPENNN_DEBUG__

   check();

   #endif

   return outputs.calculate_error_rows(targets);
}


Vector<double> MeanSquaredError::calculate_error_terms(const Vector<double>& parameters) const
{
#ifdef __OPENNN_DEBUG__

check();

#endif

    const MultilayerPerceptron* multilayer_perceptron_pointer = neural_network_pointer->get_multilayer_perceptron_pointer();

    const Matrix<double> inputs = data_set_pointer->get_training_inputs();

    const Matrix<double> targets = data_set_pointer->get_training_targets();

    const Matrix<double> outputs = multilayer_perceptron_pointer->calculate_outputs(inputs, parameters);

    const size_t training_instances_number = inputs.get_rows_number();

    return outputs.calculate_error_rows(targets)/static_cast<double>(training_instances_number);
}


LossIndex::SecondOrderLoss MeanSquaredError::calculate_terms_second_order_loss() const
{
#ifdef __OPENNN_DEBUG__

check();

#endif

    // Multilayer perceptron

    const MultilayerPerceptron* multilayer_perceptron_pointer = neural_network_pointer->get_multilayer_perceptron_pointer();

    const size_t layers_number = multilayer_perceptron_pointer->get_layers_number();

    const size_t parameters_number = multilayer_perceptron_pointer->get_parameters_number();

    // Data set

    const size_t training_instances_number = data_set_pointer->get_instances_pointer()->get_training_instances_number();

    const Vector< Vector<size_t> > training_batches = data_set_pointer->get_instances_pointer()->get_training_batches();

    const size_t batches_number = training_batches.size();

    SecondOrderLoss terms_second_order_loss(parameters_number);

    #pragma omp parallel for

    for(int i = 0; i < static_cast<int>(batches_number); i++)
    {
        const Matrix<double> inputs = data_set_pointer->get_inputs(training_batches[static_cast<unsigned>(i)]);
        const Matrix<double> targets = data_set_pointer->get_targets(training_batches[static_cast<unsigned>(i)]);

        const MultilayerPerceptron::ForwardPropagation forward_propagation
                = multilayer_perceptron_pointer->calculate_forward_propagation(inputs);

        const Vector<double> error_terms
                = calculate_error_terms(forward_propagation.layers_activations[layers_number-1], targets);

        /*const */Matrix<double> output_gradient = (forward_propagation.layers_activations[layers_number-1] - targets)/*/error_terms*/;
        output_gradient.divide_by_rows(error_terms);

        const Vector< Matrix<double> > layers_delta
                = calculate_layers_delta(forward_propagation.layers_activations_derivatives, output_gradient);

        const Matrix<double> error_terms_Jacobian
                = calculate_error_terms_Jacobian(inputs, forward_propagation.layers_activations, layers_delta);

        const Matrix<double> error_terms_Jacobian_transpose = error_terms_Jacobian.calculate_transpose();

        const double loss = Products::dot(error_terms, error_terms);

        const Vector<double> gradient = Products::dot(error_terms_Jacobian_transpose, error_terms);

        Matrix<double> Hessian_approximation;// = error_terms_Jacobian.dot(error_terms_Jacobian);
        Hessian_approximation.dot(error_terms_Jacobian_transpose, error_terms_Jacobian);

        #pragma omp critical
        {
            terms_second_order_loss.loss += loss;
            terms_second_order_loss.gradient += gradient;
            terms_second_order_loss.Hessian_approximation += Hessian_approximation;
         }
    }

    terms_second_order_loss.loss /= static_cast<double>(training_instances_number);
    terms_second_order_loss.gradient *= (2.0/static_cast<double>(training_instances_number));
    terms_second_order_loss.Hessian_approximation *= (2.0/static_cast<double>(training_instances_number));

    if(regularization_method != RegularizationMethod::None)
    {
        terms_second_order_loss.loss += calculate_regularization();
        terms_second_order_loss.gradient += calculate_regularization_gradient();
        terms_second_order_loss.Hessian_approximation += calculate_regularization_Hessian();
    }

    return terms_second_order_loss;
}


/// Returns a string with the name of the mean squared error loss type, "MEAN_SQUARED_ERROR".

string MeanSquaredError::get_error_type() const
{
   return "MEAN_SQUARED_ERROR";
}


string MeanSquaredError::get_error_type_text() const
{
   return "Mean squared error";
}


/// Serializes the mean squared error object into a XML document of the TinyXML library.
/// See the OpenNN manual for more information about the format of this document->

tinyxml2::XMLDocument* MeanSquaredError::to_XML() const
{
   ostringstream buffer;

   tinyxml2::XMLDocument* document = new tinyxml2::XMLDocument;

   // Mean squared error

   tinyxml2::XMLElement* mean_squared_error_element = document->NewElement("MeanSquaredError");

   document->InsertFirstChild(mean_squared_error_element);

   // Display
//   {
//      tinyxml2::XMLElement* element = document->NewElement("Display");
//      mean_squared_error_element->LinkEndChild(element);

//      buffer.str("");
//      buffer << display;

//      tinyxml2::XMLText* text = document->NewText(buffer.str().c_str());
//      element->LinkEndChild(text);
//   }

   return(document);
}


void MeanSquaredError::write_XML(tinyxml2::XMLPrinter& file_stream) const
{
    // Error type

    file_stream.OpenElement("Error");

    file_stream.PushAttribute("Type", "MEAN_SQUARED_ERROR");

    file_stream.CloseElement();

    // Regularization

    write_regularization_XML(file_stream);
}


double MeanSquaredError::calculate_training_error_new() const
{
#ifdef __OPENNN_DEBUG__

check();

#endif

    // Data set

    const size_t training_instances_number = data_set_pointer->get_instances_pointer()->get_training_instances_number();

    const Vector< Vector<size_t> > training_batches = data_set_pointer->get_instances_pointer()->get_training_batches();

    const size_t batches_number = training_batches.size();

    double training_error = 0.0;

    #pragma omp parallel for reduction(+ : training_error)

    for(int i = 0; i < static_cast<int>(batches_number); i++)
    {
        const Matrix<double> inputs = data_set_pointer -> get_inputs(training_batches[static_cast<unsigned>(i)]);
        const Matrix<double> targets = data_set_pointer -> get_targets(training_batches[static_cast<unsigned>(i)]);

        const Matrix<double> outputs = neural_network_pointer -> calculate_outputs_new(inputs);

        const double batch_error = outputs.calculate_sum_squared_error(targets);

        training_error += batch_error;
    }

    return training_error/static_cast<double>(training_instances_number);
}


double MeanSquaredError::calculate_training_error_new(const Vector<double>& parameters) const
{
#ifdef __OPENNN_DEBUG__

check_new();

#endif

    const size_t training_instances_number = data_set_pointer -> get_instances_pointer()->get_training_instances_number();

    const Vector< Vector<size_t> > training_batches = data_set_pointer -> get_instances_pointer()->get_training_batches();

    const size_t batches_number = training_batches.size();

    double training_error = 0.0;

    #pragma omp parallel for reduction(+ : training_error)

    for(int i = 0; i < static_cast<int>(batches_number); i++)
    {
        const Matrix<double> inputs = data_set_pointer -> get_inputs(training_batches[static_cast<unsigned>(i)]);
        const Matrix<double> targets = data_set_pointer -> get_targets(training_batches[static_cast<unsigned>(i)]);

        const Matrix<double> outputs = neural_network_pointer -> calculate_outputs_new(inputs, parameters);

        const double batch_error = outputs.calculate_sum_squared_error(targets);

        training_error += batch_error;
    }

    return training_error/static_cast<double>(training_instances_number);
}


Vector<double> MeanSquaredError::calculate_training_error_gradient_new() const
{

#ifdef __OPENNN_DEBUG__

check_new();

#endif

    // Neural network

    const size_t layers_number = neural_network_pointer -> get_layers_number_new();

    const size_t parameters_number = neural_network_pointer -> get_parameters_number();

    // Data set

    const size_t training_instances_number = data_set_pointer -> get_instances().get_training_instances_number();

    const Vector< Vector<size_t> > training_batches = data_set_pointer -> get_instances_pointer()->get_training_batches();

    const size_t batches_number = training_batches.size();

    // Loss index

    Vector<double> training_error_gradient(parameters_number, 0.0);

    #pragma omp parallel for

    for(int i = 0; i < static_cast<int>(batches_number); i++)
    {
        const Matrix<double> inputs = data_set_pointer->get_inputs(training_batches[static_cast<unsigned>(i)]);
        const Matrix<double> targets = data_set_pointer->get_targets(training_batches[static_cast<unsigned>(i)]);

        const NeuralNetwork::ForwardPropagation forward_propagation
                = neural_network_pointer -> calculate_first_order_forward_propagation_new(inputs); //NEW

        const Matrix<double> output_gradient
                = calculate_output_gradient_new(forward_propagation.layers_activations[layers_number-1], targets);

        const Vector< Matrix<double> > layers_delta
                = calculate_layers_delta_new(forward_propagation.layers_activations, forward_propagation.layers_activations_derivatives, output_gradient);

        const Vector<double> batch_gradient
                = calculate_error_gradient_new(inputs, forward_propagation.layers_activations, layers_delta);

        #pragma omp critical

        training_error_gradient += batch_gradient;
    }

    return training_error_gradient/static_cast<double>(training_instances_number);
}


#ifdef __OPENNN_CUDA__

void MeanSquaredError::cuda_calculate_output_gradient(const DataSet::CudaBatch& cuda_batch,
                                                      const MultilayerPerceptron::CudaForwardPropagation& cuda_forward_propagation,
                                                      LossIndex::CudaFirstOrderLoss& cuda_first_order_loss) const
{
    const size_t batch_size = get_data_set_pointer()->get_instances_pointer()->get_batch_size();

    const size_t layers_number = neural_network_pointer->get_multilayer_perceptron_pointer()->get_layers_number();

    const size_t outputs_number = neural_network_pointer->get_outputs_number();

    mean_squared_error_derivative(static_cast<int>(batch_size*outputs_number),
                                  cuda_forward_propagation.layers_activations[layers_number-1],
                                  cuda_batch.targets,
                                  cuda_first_order_loss.output_gradient);
}


void MeanSquaredError::cuda_calculate_error(const DataSet::CudaBatch& cuda_batch,
                                            const MultilayerPerceptron::CudaForwardPropagation& cuda_forward_propagation,
                                            LossIndex::CudaFirstOrderLoss& cuda_first_order_loss) const
{
    // Data set

    const size_t batch_size = get_data_set_pointer()->get_instances_pointer()->get_batch_size();

    // Neural network

    const size_t layers_number = neural_network_pointer->get_multilayer_perceptron_pointer()->get_layers_number();

    const size_t outputs_number = neural_network_pointer->get_outputs_number();

    // Loss index

    if(cudaMemcpy(cuda_first_order_loss.errors, cuda_forward_propagation.layers_activations[layers_number-1],
                  batch_size*outputs_number*sizeof(float), cudaMemcpyDeviceToDevice) != cudaSuccess)
        cout << "Cuda errors copy error" << endl;

    float alpha = -1.0;

    cublasSaxpy(handle, static_cast<int>(batch_size*outputs_number),
                &alpha, cuda_batch.targets, 1,
                cuda_first_order_loss.errors, 1);

    cuda_first_order_loss.loss = 0.0;

    cublasSdot(handle, batch_size*outputs_number, cuda_first_order_loss.errors, 1, cuda_first_order_loss.errors, 1, &cuda_first_order_loss.loss);

    cuda_first_order_loss.loss /= static_cast<float>(batch_size*outputs_number);
}


void MeanSquaredError::cuda_calculate_error_gradient(const DataSet::CudaBatch& cuda_batch,
                                                     const MultilayerPerceptron::CudaForwardPropagation& cuda_forward_propagation,
                                                     LossIndex::CudaFirstOrderLoss& cuda_first_order_loss) const
{
    // Data set

    const size_t batch_size = data_set_pointer->get_instances_pointer()->get_batch_size();

    // Neural network

    const size_t inputs_number = neural_network_pointer->get_inputs_number();

    MultilayerPerceptron* multilayer_perceptron_pointer = neural_network_pointer->get_multilayer_perceptron_pointer();

    const Vector<size_t> layers_size = multilayer_perceptron_pointer->get_layers_neurons_numbers();
    const Vector<size_t> layers_inputs_number = multilayer_perceptron_pointer->get_layers_inputs_number();

    const size_t layers_number = multilayer_perceptron_pointer->get_layers_number();

    const size_t parameters_number = multilayer_perceptron_pointer->get_parameters_number();

    // Loss index

    cudaMemset(cuda_first_order_loss.gradient, 0, static_cast<size_t>(parameters_number)*sizeof(float));

    size_t index = 0;

    float alpha = 1.0;
    float beta = 1.0;

    cublasSgemm(handle, CUBLAS_OP_T, CUBLAS_OP_N, static_cast<int>(inputs_number), static_cast<int>(layers_size[0]), static_cast<int>(batch_size),
                &alpha, cuda_batch.inputs, static_cast<int>(batch_size), cuda_first_order_loss.layers_delta[0], static_cast<int>(batch_size),
                &beta, cuda_first_order_loss.gradient + index, static_cast<int>(inputs_number));

    index += layers_inputs_number[0]*layers_size[0];

    cublasSgemv(handle, CUBLAS_OP_T, static_cast<int>(batch_size), static_cast<int>(layers_size[0]),
                &alpha, cuda_first_order_loss.layers_delta[0], static_cast<int>(batch_size),
                cuda_first_order_loss.ones, 1, &beta, cuda_first_order_loss.gradient + index, 1);

    index += layers_size[0];

    for(size_t i = 1; i < layers_number; i++)
    {
        cublasSgemm(handle, CUBLAS_OP_T, CUBLAS_OP_N, static_cast<int>(layers_size[i-1]), static_cast<int>(layers_size[i]), static_cast<int>(batch_size),
                    &alpha, cuda_forward_propagation.layers_activations[i-1], static_cast<int>(batch_size), cuda_first_order_loss.layers_delta[i], static_cast<int>(batch_size),
                    &beta, cuda_first_order_loss.gradient + index, static_cast<int>(layers_size[i-1]));

        index += layers_inputs_number[i]*layers_size[i];

        cublasSgemv(handle, CUBLAS_OP_T,
                    static_cast<int>(batch_size), static_cast<int>(layers_size[i]),
                    &alpha, cuda_first_order_loss.layers_delta[i], static_cast<int>(batch_size),
                    cuda_first_order_loss.ones, 1, &beta, cuda_first_order_loss.gradient + index, 1);

        index += layers_size[i];
    }

    alpha = 1.0/static_cast<float>(batch_size);

    cublasSscal(handle, static_cast<int>(parameters_number), &alpha, cuda_first_order_loss.gradient, 1);
}

#endif

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
