# Holographic Teleportation Protocol (HTP)
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

def bell_teleportation_circuit():
    """
    Create a Bell-state based teleportation circuit.
    Returns:
        QuantumCircuit object representing the teleportation process
    """
    qreg = QuantumRegister(3, 'q')
    creg = ClassicalRegister(2, 'c')
    qc = QuantumCircuit(qreg, creg)

    # Prepare entanglement
    qc.h(qreg[1])
    qc.cx(qreg[1], qreg[2])

    # Bell measurement
    qc.cx(qreg[0], qreg[1])
    qc.h(qreg[0])
    qc.measure([qreg[0], qreg[1]], [creg[0], creg[1]])

    # Conditional operations on receiver
    qc.x(qreg[2]).c_if(creg, 1)
    qc.z(qreg[2]).c_if(creg, 2)

    return qc
