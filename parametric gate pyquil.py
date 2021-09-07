from pyquil import Program, WavefunctionSimulator
from pyquil.quilatom import Parameter, quil_sin, quil_cos
from pyquil.quilbase import DefGate
import numpy as np
wavefunction_simulator = WavefunctionSimulator()
# Define the new gate from a matrix
theta = Parameter('theta')


crx = np.array([
[1, 0, 0, 0],
[0, 1, 0, 0],
[0, 0, quil_cos(theta / 2), -1j * quil_sin(theta / 2)],[0, 0, -1j * quil_sin(theta / 2), quil_cos(theta / 2)]
])


gate_definition = DefGate('CRX', crx, [theta])
CRX = gate_definition.get_constructor()
# Create our program and use the new parametric gate
p = Program()
p += gate_definition
p += H(0)
p += CRX(np.pi/2)(0, 1)

wavefunction = wavefunction_simulator.wavefunction(p)

print(wavefunction)
