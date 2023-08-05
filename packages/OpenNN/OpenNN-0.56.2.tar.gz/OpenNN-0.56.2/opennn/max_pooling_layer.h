#ifndef __MAX_POOLING_LAYER_H
#define __MAX_POOLING_LAYER_H


#include "pooling_layer.h"

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

// TinyXml includes

#include "tinyxml2.h"


namespace OpenNN {

    class MaxPoolingLayer : public PoolingLayer
    {
    public:

        Matrix<double> calculate_outputs(const Matrix<double> &) const;
        Matrix <double> max_pool_operation(const Matrix<double> &) const;

    protected:
        // Members
    };

}


#endif // __MAX_POOLING_LAYER_H
