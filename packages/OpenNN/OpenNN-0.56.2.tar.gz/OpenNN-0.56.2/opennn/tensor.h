/****************************************************************************************************************/
/*                                                                                                              */
/*   OpenNN: Open Neural Networks Library                                                                       */
/*   www.opennn.net                                                                                             */
/*                                                                                                              */
/*   T E N S O R   C O N T A I N E R                                                                            */
/*                                                                                                              */
/*   Artificial Intelligence Techniques, SL                                                                     */
/*   artelnics@artelnics.com                                                                                    */
/*                                                                                                              */
/****************************************************************************************************************/

#pragma once

#ifndef __TENSOR_H__
#define __TENSOR_H__

// System includes

#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdexcept>

// OpenNN includes

#include "vector.h"
//#include "sparse_matrix.h"

using namespace std;

namespace OpenNN
{


/// This template class defines a matrix for general purpose use.
/// This matrix also implements some mathematical methods which can be useful. 

template <typename T>
class Tensor : public vector<T>
{

public:

    // CONSTRUCTORS

    explicit Tensor();

    explicit Tensor(const Vector<size_t>&);
    explicit Tensor(const Vector<size_t>&, const T&);
    explicit Tensor(const size_t&, const size_t&, const size_t&);
    explicit Tensor(const Matrix<T>&);

    // DESTRUCTOR

    virtual ~Tensor();

    // ASSIGNMENT OPERATORS

    inline Tensor<T>& operator = (const Tensor<T>&);

    // REFERENCE OPERATORS

    inline T& operator()(const size_t&);    
    inline T& operator()(const size_t&, const size_t&);    
    inline T& operator()(const size_t&, const size_t&, const size_t&);    
    inline T& operator()(const Vector<size_t>&);
	
    inline const T& operator()(const size_t&, const size_t&) const;
    inline const T& operator()(const size_t&, const size_t&, const size_t&) const;
    inline const T& operator()(const Vector<size_t>&) const;


    // OTHERS OPERATORS
    // inline Tensor<T> operator * (const Matrix<T>&) const;
    inline Matrix<T> operator * (const Matrix<T>&) const;

    Matrix<T> calculate_product(const Matrix<T>&) const;
    Tensor<T> calculate_product(const Tensor<T>&) const;

    Matrix<T> dot(const Matrix<T>&) const;
    Tensor<T> dot(const Tensor<T>&) const;


    // METHODS
    size_t get_order() const;
    void add_matrix(const Matrix<T>&);
    Matrix<T> get_matrix(const size_t&) const;

    void tuck_in(const size_t&, const size_t&, const Matrix<T>&);
    void tuck_in(const size_t&, const size_t&, const Tensor<T>&);

    // GET METHODS
    Vector<size_t> get_dimensions() const;


    // SET METHODS

    void set_dimensions(const Vector<size_t>&);

private:

    Vector<size_t> dimensions;

};



// CONSTRUCTORS

/// Default constructor. It creates a matrix with zero rows and zero columns.

template <class T>
Tensor<T>::Tensor() : vector<T>()
{
//    set();
}


template <class T>
Tensor<T>::Tensor(const Vector<size_t>& order_vector) : vector<T> (order_vector.calculate_product())
{
    dimensions = order_vector;
}


template <class T>
Tensor<T>::Tensor(const Vector<size_t>& order_vector, const T& value) : vector<T> (order_vector.calculate_product(), value)
{
    dimensions = order_vector;
}


template <class T>
Tensor<T>::Tensor(const size_t& rank_1, const size_t& rank_2, const size_t& rank_3) : vector<T>(rank_1*rank_2*rank_3)
{
    dimensions = Vector<size_t>({rank_1, rank_2, rank_3});
}


template <class T>
Tensor<T>::Tensor(const Matrix<T>& matrix) : vector<T> (matrix)
{
    dimensions = Vector<size_t>({ matrix.get_rows_number(), matrix.get_columns_number() });
}



template <class T>
Tensor<T>::~Tensor() {

}

template<class T>
ostream& operator << (ostream& os, const Tensor<T>& t)
{
    const size_t order = t.get_order();

    if(order == 1)
    {
        const size_t n = t.get_dimensions()[0];

        for(size_t i = 0; i < n; i ++)
        {
            os << t[i] << " ";
        }
        os << "\n";
    } else if(order == 2)
    {
        const size_t rows_number = t.get_dimensions()[0];
        const size_t columns_number = t.get_dimensions()[1];

        for(size_t i = 0; i < rows_number; i ++)
        {
            for(size_t j = 0; j < columns_number; j++)
            {
                os << t(i,j) << " ";
            }

            os << endl;
        }
    } else if(order > 2)
    {
        const size_t rows_number = t.get_dimensions()[0];
        const size_t columns_number = t.get_dimensions()[1];
        const size_t rank = t.get_dimensions()[2];

        for(size_t k = 0; k < rank; k ++)
        {
            os << "submatrix_" << k << "\n";
            for(size_t i = 0; i < rows_number; i ++)
            {
                for(size_t j = 0; j < columns_number; j++)
                {
                    os << t(i, j, k) << "\t";
                }

                os << "\n";
            }
        }
    }

   return(os);
}


template <class T>
Tensor<T>& Tensor<T>::operator=(const Tensor<T>& b)
{
    set_dimensions( b.get_dimensions() );

    const size_t n = b.size();

    for(size_t i = 0; i < n; i++)
        (*this)[i] = b[i];

    return *this;
}



template <class T>
inline const T& Tensor<T>::operator()(const size_t& index_0 , const size_t& index_1, const size_t& index_2) const
{
    return ((*this)[index_2 * (dimensions[0] * dimensions[1]) + index_0 * dimensions[1] + index_1]);
}


template <class T>
T& Tensor<T>::operator()(const size_t& index_0 , const size_t& index_1, const size_t& index_2)
{
    return ((*this)[index_2 * (dimensions[0] * dimensions[1]) + index_0 * dimensions[1] + index_1]);
}


template<class T>
inline const T&  Tensor<T>::operator()(const size_t& index_0, const size_t& index_1) const
{
    return ((*this)[dimensions[1]*index_0 + index_1]);
}


template <class T>
Matrix<T> Tensor<T>::operator * (const Matrix<T>& matrix) const
{
    const size_t rows_number = matrix.get_rows_number();
    const size_t columns_number = matrix.get_columns_number();

    Matrix<T> output(rows_number, columns_number, 0 );

    if(get_order() == 2 && dimensions[0] == rows_number &&
            dimensions[1] == columns_number)
    {
        Matrix<T> tensor_matrix = get_matrix(0);

        output = tensor_matrix * matrix;

        return output;

    } else {

        ostringstream buffer;

        buffer << "OpenNN Exception: The matrix and the tensor have not got the same size." << endl;

        throw logic_error(buffer.str());
    }

    return output;
}


template <class T>
Matrix<T> Tensor<T>::calculate_product(const Matrix<T>&  matrix) const
{
    const size_t rows_number = matrix.get_rows_number();
    const size_t columns_number = matrix.get_columns_number();

    const size_t matrix_size = matrix.size();

    Matrix<T> result(rows_number, columns_number, 0.0);

    if(get_order() == 2)
    {
//        if(size() == matrix.size()) // Original
        if(this->size() == matrix.size())
        {
            for(size_t i = 0; i < matrix_size; i ++ )
                result[i] = (*this)[i] * matrix[i];
        }
    }
    return result;
}


template <class T>
Matrix<T> Tensor<T>::dot(const Matrix<T>& a_matrix) const
{
    if(get_order() == 2)
    {
        Matrix<T> tensor_matrix = get_matrix(0);

        return tensor_matrix.dot(a_matrix);

    } else {

        return Matrix<T>();
    }
}


template <class T>
size_t Tensor<T>::get_order() const
{
    return dimensions.size();
}


template <class T>
Matrix<T> Tensor<T>::get_matrix(const size_t& matrix_index) const
{
    size_t order = get_order();

    if(order == 2)
    {

        const size_t rows_number = dimensions[0];
        const size_t columns_number = dimensions[1];
        const size_t elements_number = rows_number * columns_number;

        Matrix<T> matrix(rows_number, columns_number);

        for(size_t i = 0; i < elements_number; i++)
        {
            matrix[i] = (*this)[i];
        }

        return matrix;

    }
    else if(order > 2)
    {

        if(matrix_index > dimensions[2])
        {

//            throw exception("Matrix out of bounds");
        }

        const size_t rows_number = dimensions[0];
        const size_t columns_number = dimensions[1];

        const size_t elements_number = rows_number * columns_number;

        Matrix<T> matrix(rows_number, columns_number);

        for(size_t i = 0; i < elements_number; i ++)
            matrix[i] = (*this)[matrix_index * elements_number + i];
        return matrix;
    }
    else
    {
        return Matrix<T>();
    }

}


template <class T>
void Tensor<T>::add_matrix(const Matrix<T>& a_matrix)
{
    const size_t order = get_order();

    if(order < 2)
    {
//        throw exception("OpenNN Exception: Tensor<T> template\n\
//        Cannot add a new matrix to this tensor.");

    } else if(order == 2)
    {

        this -> insert(this -> end(), a_matrix.begin(), a_matrix.end());

        dimensions = Vector<size_t>({ dimensions[0], dimensions[1], 2} );

    } else if (order == 3)
    {

        // set_dimensions({ dimensions[0], dimensions[1], dimensions[2] });

        this -> insert(this -> end(), a_matrix.begin(), a_matrix.end());
        dimensions[2] += 1;
        cout << *this << endl;

    }
    else
    {
        //
    }
}



/// This method re-writes the output operator << for the Matrix template.
/// @param os Output stream.
/// @param m Output matrix.



template<class T>
Vector<size_t> Tensor<T>::get_dimensions() const
{
    return dimensions;
}

template <class T>
void Tensor<T>::set_dimensions(const Vector<size_t>& new_dimensions)
{
    dimensions = new_dimensions;

//    resize(new_dimensions.calculate_product()); // Original
    this->resize(new_dimensions.calculate_product());
}

/// Tuck in another matrix starting from a given position.
/// @param row_position Insertion row position.
/// @param column_position Insertion row position.
/// @param other_matrix Matrix to be inserted.

template <class T>
void Tensor<T>::tuck_in(const size_t& row_position, const size_t& column_position, const Matrix<T>& other_matrix)
{
   const size_t other_rows_number = other_matrix.get_rows_number();
   const size_t other_columns_number = other_matrix.get_columns_number();

   // Control sentence(if debug)

   #ifdef __OPENNN_DEBUG__

   if(row_position + other_rows_number > rows_number)
   {
      ostringstream buffer;

      buffer << "OpenNN Exception: Matrix Template.\n"
             << "void insert(const size_t&, const size_t&, const Matrix<T>&) const method.\n"
             << "Cannot tuck in matrix.\n";

      throw logic_error(buffer.str());
   }

   if(column_position + other_columns_number > columns_number)
   {
      ostringstream buffer;

      buffer << "OpenNN Exception: Matrix Template.\n"
             << "void insert(const size_t&, const size_t&, const Matrix<T>&) const method.\n"
             << "Cannot tuck in matrix.\n";

      throw logic_error(buffer.str());
   }

   #endif

   for(size_t i = 0; i < other_rows_number; i++)
   {
      for(size_t j = 0; j < other_columns_number; j++)
      {
        (*this)(row_position+i,column_position+j) = other_matrix(i,j);
      }
   }
}


/// Tuck in another matrix starting from a given position.
/// @param row_position Insertion row position.
/// @param column_position Insertion row position.
/// @param other_tensor Tensor to be inserted.

template <class T>
void Tensor<T>::tuck_in(const size_t& row_position, const size_t& column_position, const Tensor<T>& other_tensor)
{
   const size_t other_rows_number = other_tensor.get_rows_number();
   const size_t other_columns_number = other_tensor.get_columns_number();

   // Control sentence(if debug)

   #ifdef __OPENNN_DEBUG__

   if(row_position + other_rows_number > rows_number)
   {
      ostringstream buffer;

      buffer << "OpenNN Exception: Matrix Template.\n"
             << "void insert(const size_t&, const size_t&, const Matrix<T>&) const method.\n"
             << "Cannot tuck in matrix.\n";

      throw logic_error(buffer.str());
   }

   if(column_position + other_columns_number > columns_number)
   {
      ostringstream buffer;

      buffer << "OpenNN Exception: Matrix Template.\n"
             << "void insert(const size_t&, const size_t&, const Matrix<T>&) const method.\n"
             << "Cannot tuck in matrix.\n";

      throw logic_error(buffer.str());
   }

   #endif

   for(size_t i = 0; i < other_rows_number; i++)
   {
      for(size_t j = 0; j < other_columns_number; j++)
      {
        (*this)(row_position+i,column_position+j) = other_tensor(i,j);
      }
   }
}

}
// end namespace

#endif

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

