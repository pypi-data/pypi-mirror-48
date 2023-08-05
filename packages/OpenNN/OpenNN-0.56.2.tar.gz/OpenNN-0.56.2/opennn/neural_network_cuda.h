#include "utilities_cuda.h"

#include "vector.h"

using namespace OpenNN;

// CALCULATE ACTIVATION

// Activation kernels

__global__ void logistic_kernel(const double* src, double* dst);

__global__ void hyperbolic_tangent_kernel(const double* src, double* dst);

__global__ void threshold_kernel(const double* src, double* dst);

__global__ void symmetric_threshold_kernel(const double* src, double* dst);

__global__ void linear_kernel(const double* src, double* dst);

__global__ void rectified_linear_kernel(const double* src, double* dst);

__global__ void scaled_exponential_linear_kernel(const double* src, double* dst);

__global__ void soft_plus_kernel(const double* src, double* dst);

__global__ void soft_sign_kernel(const double* src, double* dst);

__global__ void hard_logistic_kernel(const double* src, double* dst);

__global__ void exponential_linear_kernel(const double* src, double* dst);



__global__ void linear_kernel(int, const float* src, float* dst);

__global__ void hyperbolic_tangent_kernel(int, const float* src, float* dst);



void logistic(const size_t&, const float* src, float* dst);

void hyperbolic_tangent(const size_t&, const float* src, float* dst);

void threshold(const size_t&, const float* src, float* dst);

void symmetric_threshold(const size_t&, const float* src, float* dst);

void linear(const size_t&, const float* src, float* dst);

void rectified_linear(const size_t&, const float* src, float* dst);

void scaled_exponential_linear(const size_t&, const float* src, float* dst);

void soft_plus(const size_t&, const float* src, float* dst);

void soft_sign(const size_t&, const float* src, float* dst);

void hard_logistic(const size_t&, const float* src, float* dst);

void exponential_linear(const size_t&, const float* src, float* dst);


void logistic_derivative(const size_t&, const float* src, float* dst);

void hyperbolic_tangent_derivative(const size_t&, const float* src, float* dst);

void threshold_derivative(const size_t&, const float* src, float* dst);

void symmetric_threshold_derivative(const size_t&, const float* src, float* dst);

void linear_derivative(const size_t&, const float* src, float* dst);

void rectified_linear_derivative(const size_t&, const float* src, float* dst);

void scaled_exponential_linear_derivative(const size_t&, const float* src, float* dst);

void soft_plus_derivative(const size_t&, const float* src, float* dst);

void soft_sign_derivative(const size_t&, const float* src, float* dst);

void hard_logistic_derivative(const size_t&, const float* src, float* dst);

void exponential_linear_derivative(const size_t&, const float* src, float* dst);

// Activation function

void calculateActivation(double* src, double* dst, const int rows, const int columns, const string& activation);

// CALCULATE ACTIVATION DERIVATIVES

// Activation derivatives kernels

__global__ void logistic_derivative_kernel(const double* src, double* dst);

__global__ void hyperbolic_tangent_derivative_kernel(const double* src, double* dst);

__global__ void hyperbolic_tangent_derivative_kernel(int, const float* src, float* dst);


__global__ void threshold_derivative_kernel(const double* src, double* dst);

__global__ void symmetric_threshold_derivative_kernel(const double* src, double* dst);

__global__ void linear_derivative_kernel(double* dst);

__global__ void linear_derivative_kernel(int, const float*, float* dst);


__global__ void rectified_linear_derivative_kernel(const double* src, double* dst);

__global__ void scaled_exponential_linear_derivative_kernel(const double* src, double* dst);

__global__ void soft_plus_derivative_kernel(const double* src, double* dst);

__global__ void soft_sign_derivative_kernel(const double* src, double* dst);

__global__ void hard_logistic_derivative_kernel(const double* src, double* dst);

__global__ void exponential_linear_derivative_kernel(const double* src, double* dst);

// Activation derivative function

void calculateActivationDerivative(const double* src, double* dst, const int rows, const int columns, const string& activation);

// CALCULATE OUTPUT DERIVATIVE

// Output derivative kernels

__global__ void mean_squared_error_derivative_kernel(const double* outputs, const double* targets, double* output_gradient);

__global__ void mean_squared_error_derivative_kernel(int, const float* outputs, const float* targets, float* output_gradient);

__global__ void sum_squared_error_derivative_kernel(const double* outputs, const double* targets, double* output_gradient);

__global__ void cross_entropy_error_derivative_kernel(const double* outputs, const double* targets, double* output_gradient);

__global__ void pow_p_error_kernel(const double* outputs, const double* targets, double* dst, const double p);

__global__ void pow_p_kernel(const double* src,  double* dst, const double p);

__global__ void minkowski_error_derivative_kernel(const double* outputs, const double* targets, double* output_gradient, const double p, const double* p_norm);

__global__ void normalized_squared_error_derivative_kernel(const double* outputs, const double* targets, double* output_gradient);

__global__ void weighted_squared_error_derivative_kernel(const double* outputs, const double* targets, double* output_gradient,
                                                          const double positives_weight, const double negatives_weight);


void mean_squared_error_derivative(const int, const float* outputs, const float* targets, float* output_gradient);


// Output derivative function

void calculateOutputDerivative(const double* outputs, const double* targets, double* output_gradient, const int rows, const int columns,
                               const string& loss_method, const Vector<double> loss_parameters);

// CALCULATE LOSS

// Loss kernels

__global__ void cross_entropy_loss_kernel(const double* outputs, const double* targets, double* auxiliar_Vector);

__global__ void pow_p_absolute_error_kernel(const double* outputs, const double* targets, double* dst, const double p);

__global__ void weighted_squared_loss_kernel(const double* outputs, const double* targets, double* auxiliar_Vector,
                                                          const double positives_weight, const double negatives_weight);

// Loss function

double calculateLoss(const double* outputs, const double* targets, const int rows, const int columns,
                     const string loss_method, const Vector<double> loss_parameters);

// Auxiliar functions and kernels

__global__ void elementwise_multiplication_kernel(const double* Vector1, const double* Vector2, double* result);

void elementwiseMultiplication(const double* Vector1, const double* Vector2, double* result, const int rows, const int columns);

__global__ void elementwise_multiplication_kernel(int, const float* Vector1, const float* Vector2, float* result);

void elementwise_multiplication(int, const float* Vector1, const float* Vector2, float* result);

__global__ void elementwise_square_kernel(const double* Vector1, double* result);

void elementwiseSquare(const double* Vector1, double* result, const int rows, const int columns);

__global__ void elementwise_division_kernel(double* numerator, const double* denominator);

void elementwiseDivision(double* numerator, const double* denominator, const int rows, const int columns);

__global__ void square_root_elements_kernel(double* result, const double epsilon);

void squareRootElementsPlusEpsilon(double* result, const double epsilon,const int rows, const int columns);

// CALCULATE LOSS, GRADIENT AND FIRST ORDER LOSS

void calculate_perceptron_layer_combinations_cuda(const int inputs_number, const int perceptrons_number,
                                                  const double* input_data_device, const int samples_number,
                                                  const double* biases_device,
                                                  const double* weights_device,
                                                  double* combinations_device);

void calculateOutputsCUDA(const Vector<double*> weights_d, const Vector<size_t> weights_rows_numbers, const Vector<size_t> weights_columns_numbers,
                          const Vector<double*> biases_d, const Vector<size_t> bias_rows_numbers,
                          const double* input_data_h, const size_t input_rows, const size_t input_columns,
                          double* output_data_h, const size_t output_rows, const size_t output_columns,
                          const Vector<string> layers_activations);


double calculateLossCUDA(const Vector<double*> weights_d, const Vector<size_t> weights_rows_numbers, const Vector<size_t> weights_columns_numbers,
                         const Vector<double*> biases_d, const Vector<size_t> bias_rows_numbers,
                         const double* input_data_d, const size_t input_rows, const size_t input_columns,
                         const double* target_data_d, const size_t target_rows, const size_t target_columns,
                         const Vector<string> layers_activations, const string loss_method,
                         const Vector<double> loss_parameters);

void calculateGradientCUDA(const Vector<double*> weights_d, const Vector<size_t> weights_rows_numbers, const Vector<size_t> weights_columns_numbers,
                           const Vector<double*> biases_d, const Vector<size_t> bias_rows_numbers,
                           const double* input_data_d, const size_t input_rows, const size_t input_columns,
                           const double* target_data_d, const size_t target_rows, const size_t target_columns,
                           double* gradient_vec_d,
                           const Vector<string> layers_activations, const string loss_method,
                           const Vector<double> loss_parameters);
/*
void calculateFirstOrderForwardPropagationCUDA(const Vector<double*> weights_d, const Vector<size_t> weights_rows_numbers, const Vector<size_t> weights_columns_numbers,
                                               const Vector<double*> biases_d, const Vector<size_t> bias_rows_numbers,
                                               const double* input_data_h, const size_t input_rows, const size_t input_columns,
                                               Vector<double*> layers_activations_data, Vector<double*> layers_activation_derivatives_data,
                                               const Vector<size_t> activations_rows_numbers, const Vector<size_t> activations_columns_numbers,
                                               const Vector<string> layers_activations);
*/

double calculateFirstOrderLossCUDA(const Vector<double*> weights_d, const Vector<size_t> weights_rows_numbers, const Vector<size_t> weights_columns_numbers,
                                   const Vector<double*> biases_d, const Vector<size_t> bias_rows_numbers,
                                   const double* input_data_d, const size_t input_rows, const size_t input_columns,
                                   const double* target_data_d, const size_t target_rows, const size_t target_columns,
                                   double* gradient_vec_d,
                                   double* output_data_h, const size_t output_rows, const size_t output_columns,
                                   const Vector<string> layers_activations, const string loss_method,
                                   const Vector<double> loss_parameters);

// UPDATE NEURAL NETWORK PARAMETERS

void updateParametersCUDA(Vector<double*> weights_d, const Vector<size_t> weights_rows_numbers, const Vector<size_t> weights_columns_numbers,
                          Vector<double*> biases_d, const Vector<size_t> bias_rows_numbers,
                          const double* gradient_h, const size_t parameters_number);

void updateParametersSgdCUDA(Vector<double*> weights_d, const Vector<size_t> weights_rows_numbers, const Vector<size_t> weights_columns_numbers,
                             Vector<double*> biases_d, const Vector<size_t> bias_rows_numbers,
                             const double* gradient_d, const size_t parameters_number,
                             const double momentum, const bool& nesterov, const double initial_learning_rate,
                             const double initial_decay, const size_t learning_rate_iteration, double*& last_increment);

void updateParametersAdamCUDA(Vector<double*> weights_d, const Vector<size_t> weights_rows_numbers, const Vector<size_t> weights_columns_numbers,
                              Vector<double*> biases_d, const Vector<size_t> bias_rows_numbers,
                              const double* gradient_d, const size_t parameters_number,
                              const double beta_1, const double beta_2, const double epsilon,
                              const double initial_learning_rate, const double initial_decay, const size_t learning_rate_iteration,
                              double*& last_increment, double*& last_square_increment);
