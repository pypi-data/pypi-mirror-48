/****************************************************************************************************************/
/*                                                                                                              */
/*   OpenNN: Open Neural Networks Library                                                                       */
/*   www.opennn.net                                                                                             */
/*                                                                                                              */
/*   B O U N D I N G   L A Y E R   C L A S S                                                                    */
/*                                                                                                              */
/*   Artificial Intelligence Techniques SL                                                                      */
/*   artelnics@artelnics.com                                                                                    */
/*                                                                                                              */
/****************************************************************************************************************/

// OpenNN includes

#include "flatten_layer.h"

namespace OpenNN
{

// DEFAULT CONSTRUCTOR

/// Default constructor.
    FlattenLayer::FlattenLayer() : Layer()
    {
        //
    }

    Vector < double > FlattenLayer::calculate_outputs(const Vector < Matrix <double>>& inputs) const
    {
        const size_t input_size = inputs.size();

        Vector<double> output;

        for(size_t i = 0; i < input_size; i++)
        {
            const Vector<double> rows_vector = inputs[i].to_vector();

            output.insert(output.end(), rows_vector.begin(), rows_vector.end());
        }

        return output;
    }


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
