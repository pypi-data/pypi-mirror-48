#include "utilities_cuda.h"

// Inverse approximation functions

void dfpInverseHessian(
        double* old_parameters, double* parameters,
        double* old_gradient, double* gradient,
        double* old_inverse_Hessian, double* auxiliar_matrix,
        double* inverse_Hessian_host, int n);

void bfgsInverseHessian(
        double* old_parameters, double* parameters,
        double* old_gradient, double* gradient,
        double* old_inverse_Hessian, double* auxiliar_matrix,
        double* inverse_Hessian_host, int n);
