###############################################################################
#                                                                             #
# RMG - Reaction Mechanism Generator                                          #
#                                                                             #
# Copyright (c) 2002-2021 Prof. William H. Green (whgreen@mit.edu),           #
# Prof. Richard H. West (r.west@neu.edu) and the RMG Team (rmg_dev@mit.edu)   #
#                                                                             #
# Permission is hereby granted, free of charge, to any person obtaining a     #
# copy of this software and associated documentation files (the 'Software'),  #
# to deal in the Software without restriction, including without limitation   #
# the rights to use, copy, modify, merge, publish, distribute, sublicense,    #
# and/or sell copies of the Software, and to permit persons to whom the       #
# Software is furnished to do so, subject to the following conditions:        #
#                                                                             #
# The above copyright notice and this permission notice shall be included in  #
# all copies or substantial portions of the Software.                         #
#                                                                             #
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER         #
# DEALINGS IN THE SOFTWARE.                                                   #
#                                                                             #
###############################################################################

cimport numpy as np

from molecule.thermo.model cimport HeatCapacityModel
from molecule.thermo.wilhoit cimport Wilhoit
from molecule.thermo.nasa cimport NASA
from molecule.quantity cimport ScalarQuantity, ArrayQuantity

################################################################################

cdef class ThermoData(HeatCapacityModel):

    cdef public ScalarQuantity _H298, _S298
    cdef public ArrayQuantity _Tdata, _Cpdata

    cpdef double get_heat_capacity(self, double T) except -1000000000

    cpdef double get_enthalpy(self, double T) except 1000000000

    cpdef double get_entropy(self, double T) except -1000000000

    cpdef double get_free_energy(self, double T) except 1000000000

    cpdef Wilhoit to_wilhoit(self, object B=?)

    cpdef NASA to_nasa(self, double Tmin, double Tmax, double Tint, bint fixedTint=?, bint weighting=?, int continuity=?)

    cpdef bint is_all_zeros(self)
