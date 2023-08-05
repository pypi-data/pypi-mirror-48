#include "functions.h"


namespace OpenNN {

Vector<double> Functions::sine(const Vector<double>& x)
{
const size_t n = x.size();

Vector<double> y(n);

for(size_t i = 0; i < n; i ++)
   y[i] = sin(x[i]);

return y;
}


Matrix<double> Functions::sine(const Matrix<double>& x)
{
const size_t rows_number = x.get_rows_number();
const size_t columns_number = x.get_columns_number();
const size_t n = rows_number * columns_number;

Matrix<double> y(rows_number, columns_number, 0.0);

for(size_t i = 0; i < n; i++)
{
   y[i] = sin(x[i]);
}

return y;
}


Vector<Matrix<double>> Functions::sine(const Vector<Matrix<double>>& x)
{

const size_t n = x.size();
Vector<Matrix<double>> y(n);

for(size_t i = 0; i < n; i ++)
{
   y[i] = sine(x[i]);
}

return y;
}


Vector<double> Functions::cosine(const Vector<double>& x)
{
const size_t n = x.size();

Vector<double> y(n);

for(size_t i = 0; i < n; i ++)
    y[i] = cos(x[i]);

return y;
}


Matrix<double> Functions::cosine(const Matrix<double>& x)
{
const size_t rows_number = x.get_rows_number();
const size_t columns_number = x.get_columns_number();
const size_t n = rows_number * columns_number;

Matrix<double> y(rows_number, columns_number, 0.0);

for(size_t i = 0; i < n; i++)
{
   y[i] = cos(x[i]);
}

return y;
}


Vector<Matrix<double>> Functions::cosine(const Vector<Matrix<double>>& x)
{
const size_t n = x.size();
Vector<Matrix<double>> y(n);

for(size_t i = 0; i < n; i ++)
{
   y[i] = cosine(x[i]);
}

return y;
}


Vector<double> Functions::linear(const Vector<double>& x)
{
return x;
}


Matrix<double> Functions::linear(const Matrix<double>& x)
{
return x;
}


Vector< Matrix<double> > linear(const Vector<Matrix<double>>& x)
{
return x;
}


Vector<double> Functions::hyperbolic_tangent(const Vector<double>& x)
{
const size_t n = x.size();

Vector<double> y(n, 0.0);

for(size_t i = 0; i < n; i ++)
   y[i] = tanh(x[i]);

return  y;
}


Matrix<double> Functions::hyperbolic_tangent(const Matrix<double>& x)
{
const size_t rows_number = x.get_rows_number();
const size_t columns_number = x.get_columns_number();

const size_t n = x.size();

Matrix<double> y(rows_number, columns_number);

for(size_t i = 0; i < n; i ++)
   y[i] = tanh(x[i]);

return  y;
}


Vector< Matrix<double> > Functions::hyperbolic_tangent(const Vector<Matrix<double>>& x)
{
const size_t n = x.size();

Vector<Matrix<double>> y(n);

for(size_t i = 0; i < n; i ++)
   y[i] = Functions::hyperbolic_tangent(x[i]);

return  y;
}


Vector<double> Functions::logistic(const Vector<double>& x)
{
const size_t n = x.size();

Vector<double> y(n);

for(size_t i = 0; i < n; i++)
{
    y[i] = 1.0 / (1.0 + exp(-x[i]));
}

return y;
}


Matrix<double> Functions::logistic(const Matrix<double>& x)
{
Matrix<double> y(x.get_rows_number(), x.get_columns_number());

for(size_t i = 0; i < x.size(); i++)
{
    y[i] = 1.0/(1.0 + exp(-x[i]));
}

return y;
}


Vector<Matrix<double>> Functions::logistic(const Vector<Matrix<double>>& x)
{
const size_t n = x.size();

Vector<Matrix <double>> y(n);

for(size_t i = 0; i < n; i ++)
{
   y[i] = Functions::logistic(x[i]);
}

return y;
}


Vector<double> Functions::threshold(const Vector<double>& x)
{
 const size_t n = x.size();

 Vector<double> y(n);

  for(size_t i = 0; i < n; i++)
      y[i] = x[i] < 0.0 ? 0.0 : 1.0;

  return y;
}


Matrix<double> Functions::threshold(const Matrix<double>& x)
{
 Matrix<double> y(x.get_rows_number(), x.get_columns_number());

  for(size_t i = 0; i < x.size(); i++)

      y[i] = x[i] < 0 ? 0.0 : 1.0;

  return y;
}


Vector<Matrix<double>> Functions::threshold(const Vector<Matrix<double>>& x)
{
 const size_t n = x.size();

 Vector<Matrix<double>> y(n);

 for(size_t i = 0; i < n; i++)
     y[i] = Functions::threshold(x[i]);

 return y;
}


Vector<double> Functions::symmetric_threshold(const Vector<double>& x)
{
 const size_t n = x.size();

 Vector<double> y(n);

 for(size_t i = 0; i < n; i++)
     y[i] = x[i] < 0 ? -1.0 : 1.0;

 return y;
}


Matrix<double> Functions::symmetric_threshold(const Matrix<double>& x)
{
 const size_t n = x.size();

 Matrix<double> y(x.get_rows_number(), x.get_columns_number());

  for(size_t i = 0; i < n; i++)
      y[i] = x[i] < 0 ? -1.0 : 1.0;

 return y;
}


Vector<Matrix<double>> Functions::symmetric_threshold(const Vector<Matrix<double>>& x)
{
const size_t n = x.size();

Vector<Matrix<double>> y(n);

for(size_t i = 0; i < n; i ++)

   Functions::symmetric_threshold(x[i]);

return y;
}


// RECTIFIED LINEAR

Vector<double> Functions::rectified_linear(const Vector<double>& x)
{
 const size_t n = x.size();

 Vector<double> y(n);

 for(size_t i = 0; i < n; i++)
     y[i] = x[i] < 0.0 ? 0.0 : x[i];

 return y;
}

Matrix<double> Functions::rectified_linear(const Matrix<double>& x)
{
 const size_t n = x.size();

 Matrix<double> y(x.get_rows_number(), x.get_columns_number());

 for(size_t i = 0; i < n; i++)
 {
     y[i] = x[i] < 0.0 ? 0.0 : x[i];
 }

 return y;

}

Vector<Matrix<double>> rectified_linear(const Vector<Matrix<double>>& x)
{
 const size_t n = x.size();

 Vector<Matrix<double>> y(n);

 for(size_t i = 0; i < n; i ++)
   y[i] = Functions::rectified_linear(x[i]);

 return y;

}



// SCALED EXPONENTIAL LINEAR

Vector<double> Functions::scaled_exponential_linear(const Vector<double>& x)
{
 const size_t n = x.size();

 const double lambda = 1.0507;
 const double alpha = 1.67326;

 Vector<double> y(n);

 for(size_t i = 0; i < n; i++)
 {
     x[i] < 0.0 ? y[i] = lambda * alpha * (exp(x[i]) - 1) : y[i] = lambda * x[i];
 }

 return y;
}


Matrix<double> Functions::scaled_exponential_linear(const Matrix<double>& x)
{
 const size_t n = x.size();

 double lambda =1.0507;
 double alpha =1.67326;


 Matrix<double> y(x.get_rows_number(), x.get_columns_number());


 for(size_t i = 0; i < n; i++)
 {
     x[i] < 0.0 ? y[i] = lambda * alpha * (exp(x[i]) - 1) : y[i] = lambda * x[i];
 }

 return y;
}


Vector<Matrix<double>> Functions::scaled_exponential_linear(const Vector<Matrix<double>>& x)
{
 const size_t n = x.size();

 Vector<Matrix<double>> y(n);

 for(size_t i = 0; i < n; i ++)
     y[i] = Functions::scaled_exponential_linear(x[i]);

 return y;
}


// SOFT PLUS

Vector<double> Functions::soft_plus(const Vector<double>& x)
{
const size_t n = x.size();

Vector<double> y(n);

for(size_t i = 0; i < n; i++)
{
    y[i] = log(1 + exp(x[i]));
}

return y;
}

Matrix<double> Functions::soft_plus(const Matrix<double>& x)
{
 const size_t n = x.size();

 Matrix<double> y(x.get_rows_number(), x.get_columns_number());

 for(size_t i = 0; i < n; i++)
 {
     y[i] = log(1 + exp(x[i]));
 }

 return y;
}


Vector<Matrix<double>> Functions::soft_plus(const Vector<Matrix<double>>& x)
{
const size_t n = x.size();

Vector<Matrix<double>> y(n);

for(size_t i = 0; i < n; i ++)
   y[i] = Functions::soft_plus(x[i]);

return y;
}


// SOFT SIGN

Vector<double> Functions::soft_sign(const Vector<double>& x)
{
 const size_t n = x.size();

 Vector<double> y(n);

 for(size_t i = 0; i < n; i++)
 {
    x[i] < 0.0 ? y[i] = x[i] / (1 - x[i]) : y[i] = x[i] / (1 + x[i]);
 }

 return y;
}


Matrix<double> Functions::soft_sign(const Matrix<double>& x)
{
 const size_t n = x.size();

 Matrix<double> y(x.get_rows_number(), x.get_columns_number());

 for(size_t i = 0; i < n; i++)
 {
    x[i] < 0.0 ? y[i] = x[i] / (1 - x[i]) : y[i] = x[i] / (1 + x[i]);
 }

 return y;
}


Vector<Matrix<double>> Functions::soft_sign(const Vector<Matrix<double>>& x)
{
const size_t n = x.size();

Vector<Matrix<double>> y(n);

for(size_t i = 0; i < n ; i ++)
    y[i] = Functions::soft_sign(x[i]);

return y;
}


// HARD SIGMOID

Vector<double> Functions::hard_sigmoid(const Vector<double>& x)
{
 const size_t n = x.size();

 Vector<double> y(n);

 for(size_t i = 0; i < n; i++)
 {
     if(x[i] < -2.5)
     {
        y[n] = 0;
     }
     else if(x[i] > 2.5)
     {
         y[n] = 1;
     }
     else
     {
         y[n] = 0.2 * x[i] + 0.5;
     }
 }

 return y;
}


Matrix<double> Functions::hard_sigmoid(const Matrix<double>& x)
{
 const size_t n = x.size();

 Matrix<double> y(x.get_rows_number(), x.get_columns_number());

 for(size_t i = 0; i < n; i++)
 {
     if(x[i] < -2.5)
     {
        y[i] = 0;
     }
     else if(x[i] > 2.5)
     {
         y[i] = 1;
     }
     else
     {
         y[i] = 0.2 * x[i] + 0.5;
     }
 }

 return y;
}


Vector< Matrix<double> > Functions::hard_sigmoid(const Vector<Matrix<double>>& x)
{
const size_t n = x.size();

Vector<Matrix<double>> y(n);

for(size_t i = 0; i < n; i ++)
   y[i] = Functions::hard_sigmoid(x[i]);

return y;

}


// EXPONENTIAL LINEAR

Vector<double> Functions::exponential_linear(const Vector<double>& x)
{
 const size_t n = x.size();

 Vector<double> y(n);

 const double alpha = 1.0;

 for(size_t i = 0; i < n; i++)
 {
     x[i] < 0.0 ? y[i] = alpha * (exp(x[i])- 1) : y[i] = x[i];
 }

 return y;

}


Matrix<double> Functions::exponential_linear(const Matrix<double>& x)
{

 const size_t n = x.size();

 Matrix<double> y(x.get_rows_number(), x.get_columns_number(), 0.0);

 const double alpha = 1.0;

 for(size_t i = 0; i < n; i++)
 {
     x[i] < 0.0 ? y[i] = alpha * (exp(x[i])- 1) : y[i] = x[i];
 }

 return y;
}


Vector<Matrix<double>> Functions::exponential_linear(const Vector<Matrix<double>>& x)
{
const size_t n = x.size();

Vector<Matrix<double>> y(n);

for(size_t i = 0; i < n; i ++)
   y[i] = Functions::exponential_linear(x[i]);

return y;
}

// LINEAR DERIVATIVES


Vector<double> Functions::linear_derivatives(const Vector<double>& x)
{
return Vector<double>(x.size(), 1.0);
}


Matrix<double> Functions::linear_derivatives(const Matrix<double>& x)
{
 return Matrix<double>(x.get_rows_number(), x.get_columns_number(), 1.0);
}


Vector<Matrix<double>> Functions::linear_derivatives(const Vector<Matrix<double>>& x)
{
 const size_t n = x.size();

 Vector<Matrix<double>> y(n);

 for(size_t i = 0; i < n; i ++)
 {
     y[i] = Functions::linear_derivatives(x[i]);
 }

 return y;
}

/*
Tensor<double> Math::linear_derivatives(const Tensor<double>& x)
{
return Tensor<double>(x.get_dimensions(), 1.0);
}
*/


Tensor<double> Functions::tensor_linear_derivatives(const Matrix<double>& x)
{
 const size_t n = x.get_rows_number();

 const size_t columns_number = x.get_columns_number();

 Vector<size_t> constructor = {columns_number, columns_number, n};

 Tensor<double> y (constructor);

 for (size_t i = 0; i < n; i++)
 {
     const Vector<double> linear_values = Functions::linear(x.get_row(i));

     for(size_t j = 0; j < columns_number; j++)
     {
         for(size_t k = 0; k < columns_number; k ++)
         {
             y(j, k, i) = 1.0;
         }
     }
 }

 return y;
}


// HYPERBOLIC TANGENT DERIVATIVES


Vector<double> Functions::hyperbolic_tangent_derivatives(const Vector<double>& x)
{
 const size_t n = x.size();

 Vector<double> y(n);

 for(size_t i = 0; i < n; i++)
 {
     const double hyperbolic_tangent = tanh(x[i]);

     y[i] = 1.0 - hyperbolic_tangent*hyperbolic_tangent;
 }

 return y;
}


Matrix<double> Functions::hyperbolic_tangent_derivatives(const Matrix<double>& x)
{
 Matrix<double> y(x.get_rows_number(), x.get_columns_number());

 for(size_t i = 0; i < x.size(); i++)
 {
     const double hyperbolic_tangent = tanh(x[i]);

     y[i] = 1.0 - hyperbolic_tangent*hyperbolic_tangent;
 }

 return y;
}


Vector<Matrix<double>> Functions::hyperbolic_tangent_derivatives(const Vector<Matrix<double>>& x)
{
 const size_t n = x.size();

 Vector<Matrix<double>> y(n);

 for(size_t i = 0; i < n; i ++)
 {
    y[i] = Functions::hyperbolic_tangent_derivatives(x[i]);
 }

 return y;
}


Tensor<double> Functions::tensor_hyperbolic_tangent_derivatives(const Matrix<double>& x)
{
const size_t n = x.size();

//    Tensor<double> y( { x.get_rows_number(), x.get_columns_number() } );  // Original

Tensor<double> y(Vector<size_t>( {x.get_rows_number(), x.get_columns_number()} ));

for(size_t i = 0; i < n; i++)
{
    const double hyperbolic_tangent = tanh(x[i]);

    y[i] = 1.0 - hyperbolic_tangent*hyperbolic_tangent;
}

return y;
}


Tensor<double> Functions::hyperbolic_tangent_derivatives(const Tensor<double>& x)
{
const size_t n = x.size();

Tensor<double> y(x.get_dimensions());

for(size_t i = 0; i < n; i++)
{
    const double hyperbolic_tangent = tanh(x[i]);

    y[i] = 1.0 - hyperbolic_tangent*hyperbolic_tangent;
}

return y;

}



// LOGISTIC DERIVATIVES

Vector<double> Functions::logistic_derivatives(const Vector<double>& x)
{
 const size_t n = x.size();

 Vector<double> y(n);

 for(size_t i = 0; i < n; i++)
 {
     const double exponential = exp(-x[i]);

     y[i] = exponential / ((1.0 + exponential)*(1.0 + exponential));
 }

 return y;
}


Matrix<double> Functions::logistic_derivatives(const Matrix<double>& x)
{
 Matrix<double> y(x.get_rows_number(), x.get_columns_number());

 for(size_t i = 0; i < x.size(); i++)
 {
     const double exponential = exp(-x[i]);

     y[i] = exponential/((1.0 + exponential)*(1.0 + exponential));
 }

 return y;
}

Vector<Matrix<double>> Functions::logistic_derivatives(const Vector<Matrix<double>>& x)
{
const size_t n = x.size();

Vector<Matrix<double>> y(n);

for(size_t i = 0; i < n; i ++)
{
    y[i] = Functions::logistic_derivatives(x[i]);
}

return y;
}



Tensor<double> Functions::logistic_derivatives(const Tensor<double>& x)
{
 const size_t n = x.size();

 Tensor<double> y (x.get_dimensions());

 for(size_t i = 0; i < x.size(); i++)
 {
     const double exponential = exp(-x[i]);

     y[i] = exponential/((1.0 + exponential)*(1.0 + exponential));
 }

 return y;

}


Tensor<double> Functions::tensor_logistic_derivatives(const Matrix<double>& x)
{
Tensor<double> y(Vector<size_t>{x.get_rows_number(), x.get_columns_number(), 1});

for(size_t i = 0; i < x.size(); i++)
{
    const double exponential = exp(x[i]);

    y[i] = exponential/((1.0 + exponential)*(1.0 + exponential));
}

return y;
}

// THRESHOLD DERIVATIVES

Vector<double> Functions::threshold_derivatives(const Vector<double>& x)
{
 const size_t n = x.size();

 Vector<double> y(n);

  for(size_t i = 0; i < n; i++)
  {
      if(x[i] < 0 || x[i] > 0)
      {
          y[i] = 0.0;
      }
      else
      {
          ostringstream buffer;

          buffer << "OpenNN Exception: OpenNN Math Template.\n"
                 << "Vector<double> threshold_derivatives(const Vector<double>&).\n"
                 << "Derivate does not exist for x equal to 0.\n";

          throw logic_error(buffer.str());
      }
  }

  return y;
}


Matrix<double> Functions::threshold_derivatives(const Matrix<double>& x)
{
 Matrix<double> y(x.get_rows_number(), x.get_columns_number());

  for(size_t i = 0; i < x.size(); i++)
  {
      if(x[i] < 0 || x[i] > 0)
      {
          y[i] = 0.0;
      }
      else
      {
          ostringstream buffer;

          buffer << "OpenNN Exception: OpenNN Math Template.\n"
                 << "Matrix<double> threshold_derivatives(const Matrix<double>&).\n"
                 << "Derivate does not exist for x equal to 0.\n";

          throw logic_error(buffer.str());
      }
  }

  return y;
}


Vector<Matrix<double>> Functions::threshold_derivatives(const Vector<Matrix<double>>& x)
{

 const size_t n = x.size();

 Vector<Matrix<double>> y(n);

 for(size_t i = 0; i < n; i ++)
    y[i] = Functions::threshold_derivatives(x[i]);

 return y;
}



Tensor<double> Functions::threshold_derivatives(const Tensor<double>& x)
{
const size_t n = x.size();

Tensor<double> y(x.get_dimensions());

for(size_t i = 0; i < x.size(); i++)
{
    if(x[i] < 0 || x[i] > 0)
    {
        y[i] = 0.0;
    }
    else
    {
        ostringstream buffer;

        buffer << "OpenNN Exception: OpenNN Math Template.\n"
               << "Matrix<double> threshold_derivatives(const Matrix<double>&).\n"
               << "Derivate does not exist for x equal to 0.\n";

        throw logic_error(buffer.str());
    }
}

return y;

}

// SYMMETRIC THRESHOLD DERIVATIVES

Vector<double> Functions::symmetric_threshold_derivatives(const Vector<double>& x)
{
 const size_t n = x.size();

 Vector<double> y(n);

 for(size_t i = 0; i < n; i++)
 {
     if(x[i] < 0 || x[i] > 0)
     {

         y[i] = 0.0;

     }
     else
     {
         ostringstream buffer;

         buffer << "OpenNN Exception: OpenNN Math Template.\n"
                << "Vector<double> symmetric_threshold_derivatives(const Vector<double>&).\n"
                << "Derivate does not exist for x equal to 0.\n";

         throw logic_error(buffer.str());
     }
 }

 return y;
}


Matrix<double> Functions::symmetric_threshold_derivatives(const Matrix<double>& x)
{
 Matrix<double> y(x.get_rows_number(), x.get_columns_number());

 for(size_t i = 0; i < x.size(); i++)
 {
     if(x[i] < 0 || x[i] > 0)
     {

         y[i] = 0.0;

     }
     else
     {
         ostringstream buffer;

         buffer << "OpenNN Exception: OpenNN Math Template.\n"
                << "Matrix<double> symmetric_threshold_derivatives(const Matrix<double>&).\n"
                << "Derivate does not exist for x equal to 0.\n";

         throw logic_error(buffer.str());
     }
 }

 return y;
}


Vector<Matrix<double>> Functions::symmetric_threshold_derivatives(const Vector<Matrix<double>>& x)
{
const size_t n = x.size();

Vector<Matrix<double>> y(n);

for(size_t i  = 0; i < n; i ++)
    y[i] = Functions::symmetric_threshold_derivatives(x[i]);

return y;
}


Tensor<double> Functions::symmetric_threshold_derivatives(const Tensor<double>& x)
{
const size_t n = x.size();

Tensor<double> y(x.get_dimensions());

for(size_t i = 0; i < x.size(); i++)
{
    if(x[i] < 0 || x[i] > 0)
    {

        y[i] = 0.0;

    }
    else
    {
        ostringstream buffer;

        buffer << "OpenNN Exception: OpenNN Math Template.\n"
               << "Matrix<double> symmetric_threshold_derivatives(const Matrix<double>&).\n"
               << "Derivate does not exist for x equal to 0.\n";

        throw logic_error(buffer.str());
    }
}

return y;
}



// RECTIFIED LINEAR DERIVATIVES

Vector<double> Functions::rectified_linear_derivatives(const Vector<double>& x)
{
 const size_t n = x.size();

 Vector<double> derivatives(n);

 for(size_t i = 0; i < n; i++)
 {
     x[i] <= 0.0 ? derivatives[i] = 0.0 : derivatives[i] = 1.0;
 }

 return derivatives;
}


Matrix<double> Functions::rectified_linear_derivatives(const Matrix<double>& x)
{
 const size_t n = x.size();

 Matrix<double> derivatives(x.get_rows_number(), x.get_columns_number());

 for(size_t i = 0; i < n; i++)
 {
     x[i] < 0.0 ? derivatives[i] = 0.0 : derivatives[i] = 1.0;
 }

 return derivatives;
}


Vector<Matrix<double>> Functions::rectified_linear_derivatives(const Vector<Matrix<double>>& x)
{
 const size_t n = x.size();

 Vector<Matrix<double>> derivatives(n);
 for(size_t i = 0; i < n; i++)
 {
     derivatives[i] = Functions::rectified_linear_derivatives(x[i]);
 }

 return derivatives;
}


Tensor<double> Functions::tensor_rectified_linear_derivatives(const Matrix<double>& x)
{
 const Tensor<double> result = Tensor<double>(Functions::rectified_linear_derivatives(x));
 return result;
}


Tensor<double> Functions::rectified_linear_derivatives(const Tensor<double>& x)
{
const size_t n = x.size();

Tensor<double> y(x.get_dimensions());

for(size_t i = 0; i < n; i++)
{
    x[i] < 0.0 ? y[i] = 0.0 : y[i] = 1.0;
}

return y;

}


// SCALED EXPONENTIAL LINEAR DERIVATIVES

Vector<double> Functions::scaled_exponential_linear_derivatives(const Vector<double>&x )
{
 const size_t n = x.size();

 const double lambda =1.0507;
 const double alpha =1.67326;

 Vector<double> derivatives(n);

 for(size_t i = 0; i < n; i++)
 {
     x[i] < 0.0 ? derivatives[i] = lambda * alpha * exp(x[i]) : derivatives[i] = lambda;
 }

 return derivatives;
}


Matrix<double> Functions::scaled_exponential_linear_derivatives(const Matrix<double>& x)
{
 const size_t n = x.size();

 double lambda =1.0507;
 double alpha =1.67326;


 Matrix<double> derivatives(x.get_rows_number(), x.get_columns_number());


 for(size_t i = 0; i < n; i++)
 {
     x[i] < 0.0 ? derivatives[i] = lambda * alpha * exp(x[i]) : derivatives[i] = lambda;
 }

 return derivatives;
}


Vector<Matrix<double>> Functions::scaled_exponential_linear_derivatives(const Vector<Matrix<double>>& x)
{
const size_t n = x.size();

Vector<Matrix<double>> derivatives(n);

for(size_t i = 0; i < n; i ++)
    derivatives[i] = Functions::scaled_exponential_linear_derivatives(x[i]);

return derivatives;
}


Tensor<double> Functions::scaled_exponential_linear_derivatives(const Tensor<double>& x)
{
const size_t n = x.size();

double lambda =1.0507;
double alpha = 1.67326;

Tensor<double> y(x.get_dimensions());

for(size_t i = 0; i < n; i++)
{
    x[i] < 0.0 ? y[i] = lambda * alpha * exp(x[i]) : y[i] = lambda;
}

return y;
}


//SOFT PLUS DERIVATIVES

Vector<double> Functions::soft_plus_derivatives(const Vector<double>& x)
{
 const size_t n = x.size();

 Vector<double> derivatives(n);

 for(size_t i = 0; i < n; i++)
 {
     derivatives[i] = 1/(1 + exp(-x[i]));
 }

 return derivatives;
}


Matrix<double> Functions::soft_plus_derivatives(const Matrix<double>& x)
{
 const size_t n = x.size();

 Matrix<double> derivatives(x.get_rows_number(), x.get_columns_number());

 for(size_t i = 0; i < n; i++)
 {
     derivatives[i] = 1/(1 + exp(-x[i]));
 }

 return derivatives;
}


Vector<Matrix<double>> Functions::soft_plus_derivatives(const Vector<Matrix<double>>& x)
{
const size_t n = x.size();
Vector<Matrix<double>> derivatives(n);

for(size_t i = 0; i < n; i ++)
    derivatives[i] = Functions::soft_plus_derivatives(x[i]);

return derivatives;

}


Tensor<double> Functions::soft_plus_derivatives(const Tensor<double>& x)
{
const size_t n = x.size();

Tensor<double> y(x.get_dimensions());

return y;

}

// SOFT SIGN DERIVATIVES


Vector<double> Functions::soft_sign_derivatives(const Vector<double>&x)
{
 const size_t n = x.size();

 Vector<double> derivatives(n);

 for(size_t i = 0; i < n; i++)
 {
    x[i] < 0.0 ? derivatives[i] = 1 / pow((1 - x[i]), 2) : derivatives[i] = 1 / pow((1 + x[i]), 2);

 }

 return derivatives;
}


Matrix<double> Functions::soft_sign_derivatives(const Matrix<double>& x)
{
 const size_t n = x.size();

 Matrix<double> derivatives(x.get_rows_number(), x.get_columns_number());

 for(size_t i = 0; i < n; i++)
 {
    x[i] < 0.0 ? derivatives[i] = 1 / pow((1 - x[i]), 2) : derivatives[i] = 1 / pow((1 + x[i]), 2);

 }

 return derivatives;
}


Vector<Matrix<double>> Functions::soft_sign_derivatives(const Vector<Matrix<double>>& x)
{
const size_t n = x.size();

Vector<Matrix<double>> derivatives(n);

for(size_t i = 0; i < n; i ++)
{
    derivatives[i] = Functions::soft_plus_derivatives(x[i]);
}

return derivatives;
}


// HARD SIGMOID DERIVATIVES

Vector<double> Functions::hard_sigmoid_derivatives(const Vector<double>& x)
{
 const size_t n = x.size();

 Vector<double> derivatives(n);

 for(size_t i = 0; i < n; i++)
 {
     x[i] < -2.5 || x[i] > 2.5 ? derivatives[i] = 0.0 : derivatives[i] = 0.2;
 }

 return derivatives;
}


Matrix<double> Functions::hard_sigmoid_derivatives(const Matrix<double>& x)
{
const size_t n = x.size();

Matrix<double> derivatives(x.get_rows_number(), x.get_columns_number());

 for(size_t i = 0; i < n; i++)
 {
     x[i] < -2.5 || x[i] > 2.5 ? derivatives[i] = 0.0 : derivatives[i] = 0.2;
 }

 return derivatives;
}


Vector<Matrix<double>> Functions::hard_sigmoid_derivatives(const Vector<Matrix<double>>& x)
{
 const size_t n = x.size();

 Vector<Matrix<double>> derivatives(n);

 for(size_t i = 0; i < n; i ++)
 {
     derivatives[i] = Functions::hard_sigmoid_derivatives(x[i]);
 }

 return derivatives;
}


// EXPONENTIAL LINEAR DERIVATIVES

Vector<double> Functions::exponential_linear_derivatives(const Vector<double>& x)
{
 const size_t n = x.size();

 Vector<double> derivatives(n);

 const double alpha = 1.0;

 for(size_t i = 0; i < n; i++)
 {
     x[i] < 0.0 ? derivatives[i] = alpha * exp(x[i]) : derivatives[i] = 1.0;
 }

 return derivatives;
}


Matrix<double> Functions::exponential_linear_derivatives(const Matrix<double>& x)
{
 const size_t n = x.size();

 Matrix<double> derivatives(x.get_rows_number(), x.get_columns_number(), 0.0);

 const double alpha = 1.0;

 for(size_t i = 0; i < n; i++)
 {
     x[i] < 0.0 ? derivatives[i] = alpha * exp(x[i]) : derivatives[i] = 1.0;
 }

 return derivatives;
}


Vector<Matrix<double>> Functions::exponential_linear_derivatives(const Vector<Matrix<double>>& x)
{
 const size_t n = x.size();

 Vector<Matrix<double>> derivatives(n);

 for(size_t i = 0; i < n; i ++)
 {
     derivatives[i] = Functions::exponential_linear_derivatives(x[i]);
 }

 return derivatives;
}


Vector<double> Functions::softmax(const Vector<double>& x) {
const size_t this_size = x.size();

Vector<double> softmax(this_size);

double sum = 0;

for(size_t i = 0; i < this_size; i++) {
sum += exp(x[i]);
}

for(size_t i = 0; i < this_size; i++) {
softmax[i] = exp(x[i]) / sum;
}

return(softmax);
}


Tensor<double> Functions::softmax_derivatives(const Matrix<double>& x)
{
 const size_t n = x.get_rows_number();

 const size_t columns_number = x.get_columns_number();

 Vector<size_t> constructor = {columns_number, columns_number, n};

 Tensor<double> y (constructor);


 for(size_t i = 0; i < n; i ++)
 {
     const Vector<double> softmax_values = Functions::softmax(x.get_row(i));

     for(size_t j = 0; j < columns_number; j++)
     {

         for(size_t k = 0; k < columns_number; k ++)
         {
             if(j == k)
             {
                 y(j,k,i) = softmax_values[j]*(1.0 - softmax_values[k]);
             }
             else
             {
                 y(j,k,i) = -softmax_values[j] * softmax_values[k];
             }
         }
     }
 }

 return y;
}


// LINEAR SECOND DERIVATIVES

Vector<double> Functions::linear_second_derivatives(const Vector<double>& x)
{
   return Vector<double>(x.size(), 0.0);
}


Matrix<double> Functions::linear_second_derivatives(const Matrix<double>& x)
{
return Matrix<double>(x.get_rows_number(), x.get_columns_number(), 0.0);
}


Vector<Matrix<double>> Functions::linear_second_derivatives(const Vector<Matrix<double>>& x)
{

const size_t n = x.size();

Vector<Matrix<double>> second_derivatives(n);

for(size_t i = 0; i < n; i ++)
    second_derivatives[i] = Functions::linear_second_derivatives(x[i]);

return second_derivatives;

}


// HYPERBOLIC TANGENT SECOND DERIVATIVES

Vector<double> Functions::hyperbolic_tangent_second_derivatives(const Vector<double>& x)
{
  const size_t n = x.size();

  Vector<double> y(n);

  for(size_t i = 0; i < n; i++)
  {
      const double hyperbolic_tangent = tanh(x[i]);

      y[i] = -2*hyperbolic_tangent*(1 - hyperbolic_tangent * hyperbolic_tangent);
  }

  return y;
}


Matrix<double> Functions::hyperbolic_tangent_second_derivatives(const Matrix<double>& x)
{
  Matrix<double> y(x.get_rows_number(), x.get_columns_number());

  for(size_t i = 0; i < x.size(); i++)
  {
      const double hyperbolic_tangent = tanh(x[i]);

      y[i] = -2*hyperbolic_tangent*(1 - hyperbolic_tangent*hyperbolic_tangent);
  }

  return y;
}


Vector<Matrix<double>> Functions::hyperbolic_tangent_second_derivatives(const Vector<Matrix<double>>& x)
{

  const size_t n = x.size();

  Vector<Matrix<double>> second_derivatives(n);

  for(size_t i = 0; i < n; i ++)
      second_derivatives[i] = Functions::hyperbolic_tangent_second_derivatives(x[i]);

  return second_derivatives;

}


// LOGISTIC SECOND DERIVATIVES

Vector<double> Functions::logistic_second_derivatives(const Vector<double>& x)
{
  const size_t n = x.size();

  Vector<double> y(n);

  for(size_t i = 0; i < n; i++)
  {
      const double exponential = exp(-x[i]);

      y[i] = (exponential*exponential - exponential) / ((1.0 + exponential)*(1.0 + exponential)*(1.0 + exponential));
  }

  return y;
}


Matrix<double> Functions::logistic_second_derivatives(const Matrix<double>& x)
{
 Matrix<double> y(x.get_rows_number(), x.get_columns_number());

 for(size_t i = 0; i < x.size(); i++)
  {
      const double exponential = exp(-x[i]);

      y[i] = (exponential*exponential - exponential)/((1.0 + exponential)*(1.0 + exponential)*(1.0 + exponential));
  }

  return y;
}


Vector<Matrix<double>> Functions::logistic_second_derivatives(const Vector<Matrix<double>>& x)
{
  const size_t n = x.size();

  Vector<Matrix<double>> second_derivatives(n);

  for(size_t i = 0; i < n; i ++)
      second_derivatives[i] = Functions::logistic_second_derivatives(x[i]);

  return second_derivatives;
}


// THRESHOLD SECOND DERIVATIVES

Vector<double> Functions::threshold_second_derivatives(const Vector<double>& x)
{
  const size_t n = x.size();

  Vector<double> y(n);

   for(size_t i = 0; i < n; i++)
   {
       if(x[i] < 0 || x[i] > 0)
       {
           y[i] = 0.0;
       }
       else
       {
           ostringstream buffer;

           buffer << "OpenNN Exception: OpenNN Math Template.\n"
                  << "Vector<double> threshold_second_derivatives(const Vector<double>&).\n"
                  << "Derivate does not exist for x equal to 0.\n";

           throw logic_error(buffer.str());
       }
   }

   return y;
}


Matrix<double> Functions::threshold_second_derivatives(const Matrix<double>& x)
{
  Matrix<double> y(x.get_rows_number(), x.get_columns_number());

   for(size_t i = 0; i < x.size(); i++)
   {
       if(x[i] < 0 || x[i] > 0)
       {
           y[i] = 0.0;
       }
       else
       {
           ostringstream buffer;

           buffer << "OpenNN Exception: OpenNN Math Template.\n"
                  << "Matrix<double> threshold_second_derivatives(const Matrix<double>&).\n"
                  << "Derivate does not exist for x equal to 0.\n";

           throw logic_error(buffer.str());
       }
   }

   return y;
}


Vector<Matrix<double>> Functions::threshold_second_derivatives(const Vector<Matrix<double>>& x)
{
  const size_t n = x.size();

  Vector<Matrix<double>> second_derivatives(n);

  for(size_t i = 0; i < n; i ++)
      second_derivatives[i] = Functions::threshold_second_derivatives(x[i]);

  return second_derivatives;
}


// SYMMETRIC THRESHOLD SECOND DERIVATIVES

Vector<double> Functions::symmetric_threshold_second_derivatives(const Vector<double>& x)
{
  const size_t n = x.size();

  Vector<double> y(n);

  for(size_t i = 0; i < n; i++)
  {
      if(x[i] < 0.0 || x[i] > 0.0)
      {
          y[i] = 0.0;
      }
      else
      {
          ostringstream buffer;

          buffer << "OpenNN Exception: OpenNN Math Template.\n"
                 << "Vector<double> symmetric_threshold_second_derivatives(const Vector<double>&).\n"
                 << "Derivate does not exist for x equal to 0.\n";

          throw logic_error(buffer.str());
      }
  }

  return y;
}


Matrix<double> Functions::symmetric_threshold_second_derivatives(const Matrix<double>& x)
{
    const size_t n = x.size();

  Matrix<double> y(x.get_rows_number(), x.get_columns_number());

  for(size_t i = 0; i < n; i++)
  {
      if(x[i] < 0.0 || x[i] > 0.0)
      {
          y[i] = 0.0;
      }
      else
      {
          ostringstream buffer;

          buffer << "OpenNN Exception: OpenNN Math Template.\n"
                 << "Matrix<double> symmetric_threshold_second_derivatives(const Matrix<double>&).\n"
                 << "Derivate does not exist for x equal to 0.\n";

          throw logic_error(buffer.str());
      }
  }

  return y;
}


Vector<Matrix<double>> Functions::symmetric_threshold_second_derivatives(const Vector<Matrix<double>>& x)
{
  const size_t n = x.size();

  Vector<Matrix<double>> second_derivatives(n);

  for(size_t i = 0; i < n; i ++)
      second_derivatives[i] = Functions::symmetric_threshold_second_derivatives(x[i]);

  return second_derivatives;

}


// RECTIFIED LINEAR SECOND DERIVATIVES

Vector<double> Functions::rectified_linear_second_derivatives(const Vector<double>& x)
{
  const size_t n = x.size();

  const Vector<double> second_derivatives(n, 0.0);

  return second_derivatives;
}


Matrix<double> Functions::rectified_linear_second_derivatives(const Matrix<double>& x)
{

  return Matrix<double>(x.get_rows_number(), x.get_columns_number(), 0.0);

}


Vector<Matrix<double>> Functions::rectified_linear_second_derivatives(const Vector<Matrix<double>>& x)
{

  const size_t n = x.size();

  Vector<Matrix<double>> second_derivatives(n);

  for(size_t i = 0; i < n; i ++)
      second_derivatives[i] = Functions::rectified_linear_second_derivatives(x[i]);

  return second_derivatives;
}


// SCALED EXPONENTIAL LINEAR SECOND DERIVATIVES

Vector<double> Functions::scaled_exponential_linear_second_derivatives(const Vector<double>& x)
{

  const size_t n = x.size();

  const double lambda = 1.0507;
  const double alpha = 1.67326;

  Vector<double> second_derivatives(n);

  for(size_t i = 0; i < n; i++)
  {
      x[i] < 0.0 ? second_derivatives[i] = lambda * alpha * exp(x[i]) : second_derivatives[i] = 0.0;
  }

  return second_derivatives;
}


Matrix<double> Functions::scaled_exponential_linear_second_derivatives(const Matrix<double>& x)
{
  const size_t n = x.size();

  double lambda =1.0507;
  double alpha =1.67326;


  Matrix<double> second_derivate(x.get_rows_number(), x.get_columns_number());


  for(size_t i = 0; i < n; i++)
  {
      x[i] < 0.0 ? second_derivate[i] = lambda * alpha * exp(x[i]) : second_derivate[i] = 0.0;
  }

  return second_derivate;

}


Vector<Matrix<double>> Functions::scaled_exponential_linear_second_derivatives(const Vector<Matrix<double>>& x)
{
  const size_t n = x.size();

  Vector<Matrix<double>> second_derivatives(n);

  for(size_t i = 0; i < n; i ++)
      second_derivatives[i] = Functions::scaled_exponential_linear_second_derivatives(x[i]);

  return second_derivatives;

}


// SOFT PLUS SECOND DERIVATIVES

Vector<double> Functions::soft_plus_second_derivatives(const Vector<double>& x)
{
  const size_t n = x.size();

  Vector<double> second_derivatives(n);

  for(size_t i = 0; i < n; i++)
  {
     second_derivatives[n] = exp(-x[i]) / pow((1 + exp(-x[i])), 2);
  }

  return second_derivatives;

}


Matrix<double> Functions::soft_plus_second_derivatives(const Matrix<double>& x)
{
  const size_t n = x.size();

  Matrix<double> second_derivatives(x.get_rows_number(), x.get_columns_number());

  for(size_t i = 0; i < n; i++)
  {
     second_derivatives[n] = exp(-x[i]) / pow((1 + exp(-x[i])), 2);
  }

  return second_derivatives;
}


Vector<Matrix<double>> Functions::soft_plus_second_derivatives(const Vector<Matrix<double>>& x)
{
  const size_t n = x.size();

  Vector<Matrix<double>> second_derivatives(n);

  for(size_t i = 0; i < n; i ++)
      second_derivatives[i] = Functions::soft_plus_second_derivatives(x[i]);

  return second_derivatives;

}


// SOFT SIGN SECOND DERIVATIVES

Vector<double> Functions::soft_sign_second_derivatives(const Vector<double>& x)
{
  const size_t n = x.size();

  Vector<double> second_derivatives(n);

  for(size_t i = 0; i < n; i++)
  {
     x[i] < 0.0 ? second_derivatives[i] = -(2 * x[i]) / pow((1 - x[i]), 3) : second_derivatives[i] = -(2 * x[i]) / pow((1 + x[i]), 3);
  }

  return second_derivatives;

}


Matrix<double> Functions::soft_sign_second_derivatives(const Matrix<double>& x)
{

  const size_t n = x.size();

  Matrix<double> second_derivatives(x.get_rows_number(), x.get_columns_number());

  for(size_t i = 0; i < n; i++)
  {
     x[i] < 0.0 ? second_derivatives[i] = -(2 * x[i]) / pow((1 - x[i]), 3) : second_derivatives[i] = -(2 * x[i]) / pow((1 + x[i]), 3);
  }

  return second_derivatives;
}


Vector<Matrix<double>> Functions::soft_sign_second_derivatives(const Vector<Matrix<double>>& x)
{

  const size_t n = x.size();

  Vector<Matrix<double>> second_derivatives(n);

  for(size_t i = 0; i < n; i ++)
      second_derivatives[i] = Functions::soft_sign_second_derivatives(x[i]);

  return second_derivatives;
}


// HARD SIGMOID SECOND DERIVATIVES

Vector<double> Functions::hard_sigmoid_second_derivatives(const Vector<double>& x)
{
    return Vector<double>(x.size(), 0.0);
}


Matrix<double> Functions::hard_sigmoid_second_derivatives(const Matrix<double>& x)
{
  return Matrix<double>(x.get_rows_number(), x.get_columns_number(), 0.0);
}


Vector<Matrix<double>> Functions::hard_sigmoid_second_derivatives(const Vector<Matrix<double>>& x)
{

  const size_t n = x.size();

  Vector<Matrix<double>> second_derivatives(n);

  for(size_t i = 0; i < n; i ++)
      second_derivatives[i] = Functions::hard_sigmoid_second_derivatives(x[i]);

  return second_derivatives;
}


// EXPONENTIAL LINEAR SECOND DERIVATIVES

Vector<double> Functions::exponential_linear_second_derivatives(const Vector<double>& x)
{

  const size_t n = x.size();

  Vector<double> second_derivatives(n);

  const double alpha = 1.0;

  for(size_t i = 0; i < n; i++)
  {
      x[i] < 0.0 ? second_derivatives[i] = alpha * exp(x[i]) : second_derivatives[i] = 0.0;
  }

  return second_derivatives;
}


Matrix<double> Functions::exponential_linear_second_derivatives(const Matrix<double>& x)
{
  const size_t n = x.size();

  Matrix<double> second_derivatives(x.get_rows_number(), x.get_columns_number(), 0.0);

  const double alpha = 1.0;

  for(size_t i = 0; i < n; i++)
  {
      x[i] < 0.0 ? second_derivatives[i] = alpha * exp(x[i]) : second_derivatives[i] = 0.0;
  }

  return second_derivatives;
}


Vector<Matrix<double>> Functions::exponential_linear_second_derivatives(const Vector<Matrix<double>>& x)
{
  const size_t n = x.size();

  Vector<Matrix<double>> second_derivatives(n);

  for(size_t i = 0; i < n; i ++)
      second_derivatives[i] = Functions::exponential_linear_second_derivatives(x[i]);

  return second_derivatives;
}

}
