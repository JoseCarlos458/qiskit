# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""A property set is maintained by the PassManager to keep information
about the current state of the circuit """


from qiskit.passmanager import propertyset as passmanager_propertyset


def __getattr__(name):
    # Just redirect to new module. This will be deprecated.
    return getattr(passmanager_propertyset, name)
