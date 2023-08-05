/****************************************************************************************************************/
/*                                                                                                              */
/*   OpenNN: Open Neural Networks Library                                                                       */
/*   www.opennn.net                                                                                             */
/*                                                                                                              */
/*   F U N C T I O N S   C L A S S   H E A D E R                                                                */
/*                                                                                                              */
/*   Artificial Intelligence Techniques, SL                                                                     */
/*   artelnics@artelnics.com                                                                                    */
/*                                                                                                              */
/****************************************************************************************************************/

#ifndef __FUNCTIONS_H_
#define __FUNCTIONS_H_

#include "vector.h"
#include "matrix.h"
#include "tensor.h"
#include <math.h>
#include "omp.h"

using namespace std;

namespace OpenNN
{

 class Functions
 {
    public:

     // SINE FUNCTIONS

     static Vector<double> sine(const Vector<double>&);

     static Matrix<double> sine(const Matrix<double>&);

     static Vector< Matrix<double> > sine(const Vector<Matrix<double>>&);


     // COSINE FUNCTIONS

     static Vector<double> cosine(const Vector<double>&);

     static Matrix<double> cosine(const Matrix<double>&);

     static Vector< Matrix<double> > cosine(const Vector<Matrix<double>>&);


     // LINEAR

     static Vector<double> linear(const Vector<double>&);

     static Matrix<double> linear(const Matrix<double>&);

     static Vector< Matrix<double> > linear(const Vector<Matrix<double>>&);


     // HYPERBOLIC TANGENT

     static Vector<double> hyperbolic_tangent(const Vector<double>&);

     static Matrix<double> hyperbolic_tangent(const Matrix<double>&);

     static Vector<Matrix<double>> hyperbolic_tangent(const Vector<Matrix<double>>&);


     // LOGISTIC

     static Vector<double> logistic(const Vector<double>&);

     static Matrix<double> logistic(const Matrix<double>&);

     static Vector<Matrix<double>> logistic(const Vector<Matrix<double>>&);


     // THRESHOLD

     static Vector<double> threshold(const Vector<double>&);

     static Matrix<double> threshold(const Matrix<double>&);

     static Vector<Matrix<double>> threshold(const Vector<Matrix<double>>&);


     // SYMMETRIC THRESHOLD

     static Vector<double> symmetric_threshold(const Vector<double>&);

     static Matrix<double> symmetric_threshold(const Matrix<double>&);

     static Vector<Matrix<double>> symmetric_threshold(const Vector<Matrix<double>>&);


     // RECTIFIED LINEAR

     static Vector<double> rectified_linear(const Vector<double>&);

     static Matrix<double> rectified_linear(const Matrix<double>&);

     static Vector<Matrix<double>> rectified_linear(const Vector<Matrix<double>>&);


     // SCALED EXPONENTIAL LINEAR

     static Vector<double> scaled_exponential_linear(const Vector<double>&);

     static Matrix<double> scaled_exponential_linear(const Matrix<double>&);

     static Vector<Matrix<double>> scaled_exponential_linear(const Vector<Matrix<double>>&);


     // SOFT PLUS

     static Vector<double> soft_plus(const Vector<double>&);

     static Matrix<double> soft_plus(const Matrix<double>&);

     static Vector<Matrix<double>> soft_plus(const Vector<Matrix<double>>&);


     // SOFT SIGN

     static Vector<double> soft_sign(const Vector<double>&);

     static Matrix<double> soft_sign(const Matrix<double>&);

     static Vector<Matrix<double>> soft_sign(const Vector<Matrix<double>>&);


     // HARD SIGMOID

     static Vector<double> hard_sigmoid(const Vector<double>&);

     static Matrix<double> hard_sigmoid(const Matrix<double>&);

     static Vector<Matrix<double>> hard_sigmoid(const Vector<Matrix<double>>&);


     // EXPONENTIAL LINEAR

     static Vector<double> exponential_linear(const Vector<double>&);

     static Matrix<double> exponential_linear(const Matrix<double>&);

     static Vector<Matrix<double>> exponential_linear(const Vector<Matrix<double>>&);


     // SOFTMAX

     static Vector<double> softmax(const Vector<double>&);


     // LINEAR DERIVATIVES

     static Vector<double> linear_derivatives(const Vector<double>&);

     static Matrix<double> linear_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> linear_derivatives(const Vector<Matrix<double>>&);

     static Tensor<double> tensor_linear_derivatives(const Matrix<double>&);


     // HYPERBOLIC TANGENT DERIVATIVES

     static Vector<double> hyperbolic_tangent_derivatives(const Vector<double>&);

     static Matrix<double> hyperbolic_tangent_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> hyperbolic_tangent_derivatives(const Vector<Matrix<double>>&);

     static Tensor<double> hyperbolic_tangent_derivatives(const Tensor<double>&);

     static Tensor<double> tensor_hyperbolic_tangent_derivatives(const Matrix<double>&);


     // LOGISTIC DERIVATIVES

     static Vector<double> logistic_derivatives(const Vector<double>&);

     static Matrix<double> logistic_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> logistic_derivatives(const Vector<Matrix<double>>&);

     static Tensor<double> logistic_derivatives(const Tensor<double>&);

     static Tensor<double> tensor_logistic_derivatives(const Matrix<double>&);


     // THRESHOLD DERIVATIVES

     static Vector<double> threshold_derivatives(const Vector<double>&);

     static Matrix<double> threshold_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> threshold_derivatives(const Vector<Matrix<double>>&);

     static Tensor<double> threshold_derivatives(const Tensor<double>&);


     // SYMMETRIC THRESHOLD DERIVATIVES

     static Vector<double> symmetric_threshold_derivatives(const Vector<double>&);

     static Matrix<double> symmetric_threshold_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> symmetric_threshold_derivatives(const Vector<Matrix<double>>&);

     static Tensor<double> symmetric_threshold_derivatives(const Tensor<double>&);


     // RECTIFIED LINEAR DERIVATIVES

     static Vector<double> rectified_linear_derivatives(const Vector<double>&);

     static Matrix<double> rectified_linear_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> rectified_linear_derivatives(const Vector<Matrix<double>>&);

     static Tensor<double> rectified_linear_derivatives(const Tensor<double>&);

     static Tensor<double> tensor_rectified_linear_derivatives(const Matrix<double>&);


     // SCALED EXPONENTIAL LINEAR DERIVATIVES

     static Vector<double> scaled_exponential_linear_derivatives(const Vector<double>&);

     static Matrix<double> scaled_exponential_linear_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> scaled_exponential_linear_derivatives(const Vector<Matrix<double>>&);

     static Tensor<double> scaled_exponential_linear_derivatives(const Tensor<double>&);


     //SOFT PLUS DERIVATIVES

     static Vector<double> soft_plus_derivatives(const Vector<double>&);

     static Matrix<double> soft_plus_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> soft_plus_derivatives(const Vector<Matrix<double>>&);

     static Tensor<double> soft_plus_derivatives(const Tensor<double>&);


     // SOFT SIGN DERIVATIVES

     static Vector<double> soft_sign_derivatives(const Vector<double>&);

     static Matrix<double> soft_sign_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> soft_sign_derivatives(const Vector<Matrix<double>>&);

     static Tensor<double> soft_sign_derivatives(const Tensor<double>&);


     // HARD SIGMOID DERIVATIVES

     static Vector<double> hard_sigmoid_derivatives(const Vector<double>&);

     static Matrix<double> hard_sigmoid_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> hard_sigmoid_derivatives(const Vector<Matrix<double>>&);

     static Tensor<double> hard_sigmoid_derivatives(const Tensor<double>&);


     // EXPONENTIAL LINEAR DERIVATIVES

     static Vector<double> exponential_linear_derivatives(const Vector<double>&);

     static Matrix<double> exponential_linear_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> exponential_linear_derivatives(const Vector<Matrix<double>>&);

     static Tensor<double> exponential_linear_derivatives(const Tensor<double>&);


     // SOFTMAX DERIVATIVES

     static Tensor<double> softmax_derivatives(const Matrix<double>&);


    // LINEAR SECOND DERIVATIVES

     static Vector<double> linear_second_derivatives(const Vector<double>&);

     static Matrix<double> linear_second_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> linear_second_derivatives(const Vector<Matrix<double>>&);


    // HYPERBOLIC TANGENT SECOND DERIVATIVES

     static Vector<double> hyperbolic_tangent_second_derivatives(const Vector<double>&);

     static Matrix<double> hyperbolic_tangent_second_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> hyperbolic_tangent_second_derivatives(const Vector<Matrix<double>>&);


    // LOGISTIC SECOND DERIVATIVES

     static Vector<double> logistic_second_derivatives(const Vector<double>&);

     static Matrix<double> logistic_second_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> logistic_second_derivatives(const Vector<Matrix<double>>&);


    // THRESHOLD SECOND DERIVATIVES

     static Vector<double> threshold_second_derivatives(const Vector<double>&);

     static Matrix<double> threshold_second_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> threshold_second_derivatives(const Vector<Matrix<double>>&);


    // SYMMETRIC THRESHOLD SECOND DERIVATIVES

     static Vector<double> symmetric_threshold_second_derivatives(const Vector<double>&);

     static Matrix<double> symmetric_threshold_second_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> symmetric_threshold_second_derivatives(const Vector<Matrix<double>>&);


    // RECTIFIED LINEAR SECOND DERIVATIVES

     static Vector<double> rectified_linear_second_derivatives(const Vector<double>&);

     static Matrix<double> rectified_linear_second_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> rectified_linear_second_derivatives(const Vector<Matrix<double>>&);


    // SCALED EXPONENTIAL LINEAR SECOND DERIVATIVES

     static Vector<double> scaled_exponential_linear_second_derivatives(const Vector<double>&);

     static Matrix<double> scaled_exponential_linear_second_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> scaled_exponential_linear_second_derivatives(const Vector<Matrix<double>>&);


    // SOFT PLUS SECOND DERIVATIVES

     static Vector<double> soft_plus_second_derivatives(const Vector<double>&);

     static Matrix<double> soft_plus_second_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> soft_plus_second_derivatives(const Vector<Matrix<double>>&);


    // SOFT SIGN SECOND DERIVATIVES

     static Vector<double> soft_sign_second_derivatives(const Vector<double>&);

     static Matrix<double> soft_sign_second_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> soft_sign_second_derivatives(const Vector<Matrix<double>>&);


    // HARD SIGMOID SECOND DERIVATIVES

     static Vector<double> hard_sigmoid_second_derivatives(const Vector<double>&);

     static Matrix<double> hard_sigmoid_second_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> hard_sigmoid_second_derivatives(const Vector<Matrix<double>>&);


    // EXPONENTIAL LINEAR SECOND DERIVATIVES

     static Vector<double> exponential_linear_second_derivatives(const Vector<double>&);

     static Matrix<double> exponential_linear_second_derivatives(const Matrix<double>&);

     static Vector<Matrix<double>> exponential_linear_second_derivatives(const Vector<Matrix<double>>&);

 };

}

#endif // __FUNCTIONS_H_
