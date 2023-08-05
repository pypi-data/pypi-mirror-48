/****************************************************************************************************************/
/*                                                                                                              */
/*   OpenNN: Open Neural Networks Library                                                                       */
/*   www.opennn.net                                                                                             */
/*                                                                                                              */
/*   P R O D U C T S   C L A S S   H E A D E R                                                                  */
/*                                                                                                              */
/*   Artificial Intelligence Techniques, SL                                                                     */
/*   artelnics@artelnics.com                                                                                    */
/*                                                                                                              */
/****************************************************************************************************************/

#ifndef __PRODUCTS_H_
#define __PRODUCTS_H_

#include "vector.h"
#include "matrix.h"
#include "tensor.h"
#include <math.h>
#include "omp.h"

#include "../eigen/Eigen"


using namespace std;

namespace OpenNN
{

 class Products
 {
    public:

     // SINE FUNCTIONS

     static double dot(const Vector<double>&, const Vector<double>&);

     static Vector<double> dot(const Vector<double>&, const Matrix<double>&);

     static Vector<double> dot(const Matrix<double>&, const Vector<double>&);

     static Matrix<double> dot(const Matrix<double>&, const Matrix<double>&);

     static Matrix<double> dot(const Matrix<double>&, const Tensor<double>&);

 };

}

#endif // __FUNCTIONS_H_
