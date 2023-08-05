"""
Wavefunction simulator device
=============================

**Module name:** :mod:`pennylane_forest.wavefunction`

.. currentmodule:: pennylane_forest.wavefunction

This module contains the :class:`~.WavefunctionDevice` class, a PennyLane device that allows
evaluation and differentiation of Rigetti's WavefunctionSimulator using PennyLane.


Auxiliary functions
-------------------

.. autosummary::
    spectral_decomposition_qubit


Classes
-------

.. autosummary::
   WavefunctionDevice

Code details
~~~~~~~~~~~~
"""
import numpy as np

from pyquil.api import WavefunctionSimulator

from .device import ForestDevice
from ._version import __version__


I = np.identity(2)
X = np.array([[0, 1], [1, 0]]) #: Pauli-X matrix
Y = np.array([[0, -1j], [1j, 0]]) #: Pauli-Y matrix
Z = np.array([[1, 0], [0, -1]]) #: Pauli-Z matrix
H = np.array([[1, 1], [1, -1]])/np.sqrt(2) # Hadamard matrix


expectation_map = {'PauliX': X, 'PauliY': Y, 'PauliZ': Z, 'Identity': I, 'Hadamard': H}


def spectral_decomposition_qubit(A):
    r"""Spectral decomposition of a :math:`2\times 2` Hermitian matrix.

    Args:
        A (array): :math:`2\times 2` Hermitian matrix

    Returns:
        (vector[float], list[array[complex]]): (a, P): eigenvalues and hermitian projectors
        such that :math:`A = \sum_k a_k P_k`.
    """
    d, v = np.linalg.eigh(A)
    P = []
    for k in range(2):
        temp = v[:, k]
        P.append(np.outer(temp, temp.conj()))
    return d, P


class WavefunctionDevice(ForestDevice):
    r"""Wavefunction simulator device for PennyLane.

    Args:
        wires (int): the number of qubits to initialize the device in
        shots (int): Number of circuit evaluations/random samples used
            to estimate expectation values of expectations.

    Keyword args:
        forest_url (str): the Forest URL server. Can also be set by
            the environment variable ``FOREST_SERVER_URL``, or in the ``~/.qcs_config``
            configuration file. Default value is ``"https://forest-server.qcs.rigetti.com"``.
        qvm_url (str): the QVM server URL. Can also be set by the environment
            variable ``QVM_URL``, or in the ``~/.forest_config`` configuration file.
            Default value is ``"http://127.0.0.1:5000"``.
        compiler_url (str): the compiler server URL. Can also be set by the environment
            variable ``COMPILER_URL``, or in the ``~/.forest_config`` configuration file.
            Default value is ``"http://127.0.0.1:6000"``.
    """
    name = 'Forest Wavefunction Simulator Device'
    short_name = 'forest.wavefunction'

    expectations = {'PauliX', 'PauliY', 'PauliZ', 'Hadamard', 'Hermitian', 'Identity'}

    def __init__(self, wires, *, shots=0, **kwargs):
        super().__init__(wires, shots, **kwargs)
        self.qc = WavefunctionSimulator(connection=self.connection)
        self.state = None

    def pre_expval(self):
        self.state = self.qc.wavefunction(self.prog).amplitudes

        # pyQuil uses the convention that the first qubit is the least significant
        # qubit. Here, we reverse this to make it the last qubit, matching PennyLane convention.
        self.state = self.state.reshape([2]*len(self.active_wires)).T.flatten()
        self.expand_state()

    def expand_state(self):
        """The pyQuil wavefunction simulator initializes qubits dymnically as they are requested.
        This method expands the state to the full number of wires in the device."""

        if len(self.active_wires) == self.num_wires:
            # all wires in the device have been initialised
            return

        # there are some wires in the device that have not yet been initialised
        inactive_wires = set(range(self.num_wires)) - self.active_wires

        # place the inactive subsystems in the vacuum state
        other_subsystems = np.zeros([2**len(inactive_wires)])
        other_subsystems[0] = 1

        # expand the state of the device into a length-num_wire state vector
        expanded_state = np.kron(self.state, other_subsystems).reshape([2]*self.num_wires)
        expanded_state = np.moveaxis(expanded_state, range(len(self.active_wires)), self.active_wires)
        expanded_state = expanded_state.flatten()

        self.state = expanded_state

    def expval(self, expectation, wires, par):
        # measurement/expectation value <psi|A|psi>
        if expectation == 'Hermitian':
            A = par[0]
        else:
            A = expectation_map[expectation]

        if self.shots == 0:
            # exact expectation value
            ev = self.ev(A, wires)
        else:
            # estimate the ev
            # sample Bernoulli distribution n_eval times / binomial distribution once
            a, P = spectral_decomposition_qubit(A)
            p0 = self.ev(P[0], wires)  # probability of measuring a[0]
            n0 = np.random.binomial(self.shots, p0)
            ev = (n0*a[0] +(self.shots-n0)*a[1]) / self.shots

        return ev

    def ev(self, A, wires):
        r"""Evaluates a one-qubit expectation in the current state.

        Args:
          A (array): :math:`2\times 2` Hermitian matrix corresponding to the expectation
          wires (Sequence[int]): target subsystem

        Returns:
          float: expectation value :math:`\left\langle{A}\right\rangle = \left\langle{\psi}\mid A\mid{\psi}\right\rangle`
        """
        # Expand the Hermitian observable over the entire subsystem
        A = self.expand_one(A, wires)
        return np.vdot(self.state, A @ self.state).real

    def expand_one(self, U, wires):
        r"""Expand a one-qubit operator into a full system operator.

        Args:
          U (array): :math:`2\times 2` matrix
          wires (Sequence[int]): target subsystem

        Returns:
          array: :math:`2^n\times 2^n` matrix
        """
        if U.shape != (2, 2):
            raise ValueError('2x2 matrix required.')
        if len(wires) != 1:
            raise ValueError('One target subsystem required.')
        wires = wires[0]
        before = 2**wires
        after = 2**(self.num_wires-wires-1)
        U = np.kron(np.kron(np.eye(before), U), np.eye(after))
        return U
