from qiskit import QuantumCircuit
import qiskit

def layerlization(qc : qiskit.QuantumCircuit, depth : int):
    """
    function that divide the quantum circuit into different circuits
    given the depth requirements.

    Input:
    qc : QuantumCircuit.
    depth: depth requirements.

    Output:
    circuits : list; list with all the subcircuits.
    
    """

    # Define the list to storage all the subcircuits.
    circuits = []
    qubit_num = qc.num_qubits

    # Define some auxiliars quantum circuits.
    qc_aux = QuantumCircuit(qubit_num, qubit_num)
    qc_add = QuantumCircuit(qubit_num, qubit_num)

    # Define the current layer.
    layer = 1
    # Define the iteration.
    iter = 0

    for gate in qc.data:


        iter += 1 
        # Add the quantum gate to the axiliar circuit.
        qc_add.append(gate)

        # Calculate the current depth to storage the information.
        # or to know about the last quantum gate to add.
        if qc_add.depth() == layer+depth or iter==len(qc.data):
            
            # Check if there is the last gate.
            if iter==len(qc.data) and depth != 1: 
                qc_aux.append(gate)

            # Add the quantum circuit.
            circuits.append(qc_aux)
            qc_aux = QuantumCircuit(qubit_num, qubit_num)
            qc_aux.append(gate)
            layer = layer + depth

            if(depth == 1 and iter==len(qc.data)):
                qc_aux = QuantumCircuit(qubit_num, qubit_num)
                qc_aux.append(gate)
                circuits.append(qc_aux)
        else:
            qc_aux.append(gate)

    return circuits