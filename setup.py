#!/usr/bin/env python3

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

import sys
import os
from collections import OrderedDict

try:
    from distutils.core import setup
    from distutils.extension import Extension
except ImportError:
    print('The distutils package is required to build or install RMG Py.')
    raise

try:
    from Cython.Build import cythonize
    from Cython.Compiler import Options
except ImportError:
    print('Cython (http://www.cython.org/) is required to build or install RMG Py.')
    raise

try:
    import numpy
except ImportError:
    print('NumPy (http://numpy.scipy.org/) is required to build or install RMG Py.')
    raise

# Create annotated HTML files for each of the Cython modules
Options.annotate = True

directives = {
    # Set input language version to python 3
    'language_level': 3,
    # Turn on profiling capacity for all Cython modules
    # 'profile': True,
    # Embed call signatures in cythonized files - enable when building documentation
    # 'embedsignature': True,
}

################################################################################

main_ext_modules = [
    # RMG
    Extension('molecule.rmgobject', ['molecule/rmgobject.pyx']),
    # Kinetics
    Extension('molecule.kinetics.arrhenius', ['molecule/kinetics/arrhenius.pyx']),
    Extension('molecule.kinetics.chebyshev', ['molecule/kinetics/chebyshev.pyx']),
    Extension('molecule.kinetics.kineticsdata', ['molecule/kinetics/kineticsdata.pyx']),
    Extension('molecule.kinetics.falloff', ['molecule/kinetics/falloff.pyx']),
    Extension('molecule.kinetics.model', ['molecule/kinetics/model.pyx']),
    Extension('molecule.kinetics.tunneling', ['molecule/kinetics/tunneling.pyx']),
    Extension('molecule.kinetics.surface', ['molecule/kinetics/surface.pyx']),
    Extension('molecule.kinetics.uncertainties', ['molecule/kinetics/uncertainties.pyx']),
    # Molecules and molecular representations
    Extension('molecule.molecule.atomtype', ['molecule/molecule/atomtype.py'], include_dirs=['.']),
    Extension('molecule.molecule.element', ['molecule/molecule/element.py'], include_dirs=['.']),
    Extension('molecule.molecule.graph', ['molecule/molecule/graph.pyx'], include_dirs=['.']),
    Extension('molecule.molecule.group', ['molecule/molecule/group.py'], include_dirs=['.']),
    Extension('molecule.molecule.molecule', ['molecule/molecule/molecule.py'], include_dirs=['.']),
    Extension('molecule.molecule.symmetry', ['molecule/molecule/symmetry.py'], include_dirs=['.']),
    Extension('molecule.molecule.vf2', ['molecule/molecule/vf2.pyx'], include_dirs=['.']),
    Extension('molecule.molecule.converter', ['molecule/molecule/converter.py'], include_dirs=['.']),
    Extension('molecule.molecule.translator', ['molecule/molecule/translator.py'], include_dirs=['.']),
    Extension('molecule.molecule.util', ['molecule/molecule/util.py'], include_dirs=['.']),
    Extension('molecule.molecule.inchi', ['molecule/molecule/inchi.py'], include_dirs=['.']),
    Extension('molecule.molecule.resonance', ['molecule/molecule/resonance.py'], include_dirs=['.']),
    Extension('molecule.molecule.pathfinder', ['molecule/molecule/pathfinder.py'], include_dirs=['.']),
    Extension('molecule.molecule.kekulize', ['molecule/molecule/kekulize.pyx'], include_dirs=['.']),
    # Thermodynamics
    Extension('molecule.thermo.thermodata', ['molecule/thermo/thermodata.pyx']),
    Extension('molecule.thermo.model', ['molecule/thermo/model.pyx']),
    Extension('molecule.thermo.nasa', ['molecule/thermo/nasa.pyx']),
    Extension('molecule.thermo.wilhoit', ['molecule/thermo/wilhoit.pyx']),
    # Miscellaneous
    Extension('molecule.constants', ['molecule/constants.py'], include_dirs=['.']),
    Extension('molecule.quantity', ['molecule/quantity.py'], include_dirs=['.']),
    Extension('molecule.species', ['molecule/species.py'], include_dirs=['.']),
    Extension('molecule.reaction', ['molecule/reaction.py'], include_dirs=['.']),
    Extension('molecule.chemkin', ['molecule/chemkin.pyx'], include_dirs=['.']),
]
################################################################################

ext_modules = []
if 'install' in sys.argv:
    # This is so users can still do simply `python setup.py install`
    ext_modules.extend(main_ext_modules)
if 'main' in sys.argv:
    # This is for `python setup.py build_ext main`
    sys.argv.remove('main')
    ext_modules.extend(main_ext_modules)
if 'minimal' in sys.argv:
    # This starts with the full install list, but removes anything that has a pure python mode
    # i.e. in only includes things whose source is .pyx
    sys.argv.remove('minimal')
    temporary_list = []
    temporary_list.extend(main_ext_modules)
    for module in temporary_list:
        for source in module.sources:
            if os.path.splitext(source)[1] == '.pyx':
                ext_modules.append(module)

# Remove duplicates while preserving order:
ext_modules = list(OrderedDict.fromkeys(ext_modules))

scripts = []

modules = []
for root, dirs, files in os.walk('molecule'):
    if 'test_data' in root:
        continue
    for f in files:
        if f.endswith('.py') or f.endswith('.pyx'):
            if 'Test' not in f and '__init__' not in f:
                module = 'molecule' + root.partition('molecule')[-1].replace('/', '.') + '.' + f.partition('.py')[0]
                modules.append(module)


# Read the version number
exec(open('molecule/version.py').read())

import logging
logging.error(ext_modules)
# Initiate the build and/or installation
setup(
    name='rmgmolecule',
    version=__version__,
    description='Reaction Mechanism Generator',
    author='William H. Green and the RMG Team',
    author_email='rmg_dev@mit.edu',
    url='http://reactionmechanismgenerator.github.io',
    packages=['molecule',],
    py_modules=modules,
    scripts=scripts,
    ext_modules=cythonize(ext_modules, build_dir='build', compiler_directives=directives),
    include_dirs=['.', numpy.get_include()],
)
