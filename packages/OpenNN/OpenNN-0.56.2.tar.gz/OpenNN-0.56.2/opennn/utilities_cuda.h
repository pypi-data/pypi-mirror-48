// Cuda includes

#include <cuda.h>
#include <cuda_runtime.h>
#include <cublas_v2.h>
#include <cublasXt.h>
#include <curand.h>

// System includes

#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <time.h>

// OpenNN includes

#include "vector.h"
#include "matrix.h"
#include "tensor.h"

// Forward declarations

using namespace std;
using namespace OpenNN;

// Utilities functions


void randomizeVector(double* A_d, const int& n);

void createHandle(cublasHandle_t* handle);

void destroyHandle(cublasHandle_t* handle);

void initCUDA();

int mallocCUDA(double** A_d, int nBytes);

int memcpyCUDA(double* A_d, const double* A_h, int nBytes);

int getHostVector(const double* A_d, double* A_h, int nBytes);

void freeCUDA(double* A_d);

Vector<double> vector_to_host(const double*, const size_t&);
Matrix<double> matrix_to_host(const double*, const size_t&, const size_t&);

double* vector_to_device(const Vector<double>&);
double* matrix_to_device(const Matrix<double>&);

