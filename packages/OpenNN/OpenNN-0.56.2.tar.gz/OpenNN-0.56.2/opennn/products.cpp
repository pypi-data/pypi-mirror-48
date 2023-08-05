/****************************************************************************************************************/
/*                                                                                                              */
/*   OpenNN: Open Neural Networks Library                                                                       */
/*   www.opennn.net                                                                                             */
/*                                                                                                              */
/*   P R O D U C T S   C L A S S                                                                                */
/*                                                                                                              */
/*   Artificial Intelligence Techniques, SL                                                                     */
/*   artelnics@artelnics.com                                                                                    */
/*                                                                                                              */
/****************************************************************************************************************/

#include "products.h"

namespace OpenNN
{

double Products::dot(const Vector<double>& a, const Vector<double>& b)
{
    const size_t a_size = a.size();

  // Control sentence(if debug)

  #ifdef __OPENNN_DEBUG__

    const size_t b_size = b.size();

    if(a_size != b_size)
    {
      ostringstream buffer;

      buffer << "OpenNN Exception: Vector Template.\n"
             << "Type dot(const Vector<T>&) const method.\n"
             << "Both vector sizes must be the same.\n";

      throw logic_error(buffer.str());
    }

  #endif

    double dot_product = 0.0;

    for(size_t i = 0; i < a_size; i++)
    {
      dot_product += a[i] * b[i];
    }

    return(dot_product);

}



Vector<double> Products::dot(const Vector<double>& vector, const Matrix<double>& matrix)
{
    const size_t rows_number = matrix.get_rows_number();
    const size_t columns_number = matrix.get_columns_number();

    const size_t vector_size = vector.size();

  // Control sentence(if debug)

  #ifdef __OPENNN_DEBUG__

    if(rows_number != vector_size)
    {
      ostringstream buffer;

      buffer << "OpenNN Exception: Vector Template.\n"
             << "Vector<T> dot(const Matrix<T>&) const method.\n"
             << "Matrix number of rows (" << rows_number << ") must be equal to vector size (" << vector_size << ").\n";

      throw logic_error(buffer.str());
    }

  #endif

    Vector<double> product(columns_number, 0.0);

     for(size_t j = 0; j < columns_number; j++)
     {
        for(size_t i = 0; i < rows_number; i++)
        {
           product[j] += vector[i]*matrix(i,j);
        }
     }

    return product;
}


Vector<double> Products::dot(const Matrix<double>& matrix, const Vector<double>& vector)
{
    const size_t rows_number = matrix.get_rows_number();
    const size_t columns_number = matrix.get_columns_number();

    Vector<double> product(rows_number);

    const Eigen::Map<Eigen::MatrixXd> matrix_eigen((double*)matrix.data(), rows_number, columns_number);
    const Eigen::Map<Eigen::VectorXd> vector_eigen((double*)vector.data(), columns_number);
    Eigen::Map<Eigen::VectorXd> product_eigen(product.data(), rows_number);

    product_eigen = matrix_eigen*vector_eigen;

    return  product;
}


Matrix<double> Products::dot(const Matrix<double>& matrix, const Matrix<double>& other_matrix)
{
    const size_t rows_number = matrix.get_rows_number();
    const size_t columns_number = matrix.get_columns_number();

    const size_t other_rows_number = other_matrix.get_rows_number();
    const size_t other_columns_number = other_matrix.get_columns_number();

    Matrix<double> product(rows_number, other_columns_number);

    const Eigen::Map<Eigen::MatrixXd> this_eigen((double*)matrix.data(), rows_number, columns_number);
    const Eigen::Map<Eigen::MatrixXd> other_eigen((double*)other_matrix.data(), other_rows_number, other_columns_number);
    Eigen::Map<Eigen::MatrixXd> product_eigen(product.data(), rows_number, other_columns_number);

    product_eigen = this_eigen*other_eigen;

    return(product);
}


Matrix<double> Products::dot(const Matrix<double>& matrix, const Tensor<double>& tensor)
{
    const size_t order = tensor.get_order();

    if(order == 2)
    {
        return dot(matrix, tensor.get_matrix(0));
    }
    else if (order > 2)
    {
        const size_t n = tensor.get_dimensions()[2];

        Matrix<double> outputs(n, matrix.get_columns_number());

        for(size_t i = 0; i < n; i ++)
        {
            const Matrix<double> i_matrix = tensor.get_matrix(i);

            const Matrix<double> i_row = matrix.get_submatrix_rows( {i} );

            Matrix<double> dot_product = dot(i_row, i_matrix);

            outputs.set_row( i, dot_product.to_vector() );
        }

        return outputs;
    }

    return Matrix<double>();
}



}
