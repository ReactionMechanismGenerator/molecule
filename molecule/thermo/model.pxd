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

from molecule.quantity cimport ScalarQuantity, ArrayQuantity
from molecule.rmgobject cimport RMGObject

cdef class HeatCapacityModel(RMGObject):

    cdef public ScalarQuantity _Tmin, _Tmax, _E0, _Cp0, _CpInf
    cdef public str comment,label

    cpdef bint is_temperature_valid(self, double T) except -2

    cpdef double get_heat_capacity(self, double T) except -1000000000

    cpdef double get_enthalpy(self, double T) except 1000000000

    cpdef double get_entropy(self, double T) except -1000000000

    cpdef double get_free_energy(self, double T) except 1000000000

    cpdef bint is_similar_to(self, HeatCapacityModel other) except -2

    cpdef bint is_identical_to(self, HeatCapacityModel other) except -2

    cpdef double discrepancy(self, HeatCapacityModel other) except -2
