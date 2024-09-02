# -*- coding: utf-8 -*-
"""graph_combined_GroverGitHub.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13KHLUjFAMHc0gS__duuLXNwUdlgBubS8
"""

!pip install qiskit-ibmq-provider

!pip install qiskit-aer

!pip install qiskit

"""small graph with starting node"""

import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_graph(nodes, num_vertices):
    G = nx.Graph()

    # Randomly choose a starting node
    start_node = random.choice(nodes)

    # Add starting node and set a different color
    G.add_node(start_node, color='red')

    # Add other nodes and edges
    for _ in range(num_vertices):
        end_node = f'Node_{len(G.nodes) + 1}'
        G.add_node(end_node)
        G.add_edge(start_node, end_node)

    return G

def visualize_graph(graph):
    pos = nx.spring_layout(graph)
    node_colors = [data['color'] if 'color' in data else 'skyblue' for node, data in graph.nodes(data=True)]
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=8, font_color="black", font_weight="bold")
    plt.show()

# List of nodes
node_list = ['A', 'B', 'C', 'D', 'E']

# Generate and visualize the graph with a randomly chosen starting node and 20 vertices
graph = generate_graph(node_list, num_vertices=20)
#isualize_graph(graph)

import networkx as nx
import random

def generate_graph_with_weights(nodes, num_vertices):
    G = nx.Graph()

    # Randomly choose a starting node
    start_node = random.choice(nodes)

    # Add starting node and set a different color
    G.add_node(start_node, color='red')

    # Add other nodes, edges, and weights
    weights_list = []
    for _ in range(num_vertices):
        end_node = f'Node_{len(G.nodes) + 1}'
        weight = random.randint(1, 99)  # Random integer between 1 and 99
        weights_list.append(weight)
        G.add_node(end_node)
        G.add_edge(start_node, end_node, weight=weight)

    return G, weights_list

# List of nodes
node_list = ['A', 'B', 'C', 'D', 'E']

# Generate the graph with weights and get the weights list
graph, weights_list = generate_graph_with_weights(node_list, num_vertices=20)
visualize_graph(graph)

# Print the list of weights
print("List of Weights:", weights_list)

from qiskit import QuantumCircuit
from math import log2

def create_smallest_item_oracle(n, weights_list):
    qc = QuantumCircuit(n + 1, n)

    # Apply Hadamard gates to all qubits
    qc.h(range(n + 1))

    # Find the index of the smallest item in the list
    smallest_index = weights_list.index(min(weights_list))

    # Convert the index to its binary representation
    binary_representation = format(smallest_index, f'0{n}b')[::-1]

    # Apply a phase inversion on the corresponding qubits
    for i, bit in enumerate(binary_representation):
        if bit == '1':
            qc.z(i)

    # Apply Hadamard gates again
    qc.h(range(n + 1))

    # Measure all qubits except the auxiliary qubit
    qc.measure(range(n), range(n))

    return qc

# Determine the number of qubits based on the list size
n_qubits = int(log2(len(weights_list)))

# Create the oracle that performs a phase inversion on the state corresponding
# to the index of the smallest item in the list
smallest_item_oracle = create_smallest_item_oracle(n_qubits, weights_list)

# Print the weights list and the quantum circuit
print("Weights List:", weights_list)
print(smallest_item_oracle)

from qiskit import Aer, transpile, assemble
from qiskit.visualization import plot_histogram

# Define the backend simulator
backend = Aer.get_backend('qasm_simulator')

# Transpile the quantum circuit for the simulator
transpiled_circuit = transpile(smallest_item_oracle, backend)

# Assemble the transpiled circuit for the simulator
qobj = assemble(transpiled_circuit)

# Run the simulation
result = backend.run(qobj).result()

# Get the counts from the result
counts = result.get_counts()

# Find the most probable state
most_probable_state = max(counts, key=counts.get)

# Convert the binary representation to decimal
decimal_value = int(most_probable_state[::-1], 2)

# Print the most probable state as a decimal value
print("Most Probable State (Decimal):", decimal_value)

# Get all possible states
all_possible_states = [format(i, f'0{n_qubits}b')[::-1] for i in range(2**n_qubits)]

# Create a dictionary with all possible states and set counts to 0 for states that didn't occur
counts_all_states = {state: counts.get(state, 0) for state in all_possible_states}

# Plot the histogram with all possible states on the x-axis
plot_histogram(counts_all_states)

def binary_to_decimal(binary_str):
    decimal_value = int(binary_str, 2)
    return decimal_value

# Example usage:
binary_input = "0101"
decimal_output = binary_to_decimal(binary_input)
print(f"The decimal representation of {binary_input} is: {decimal_output}")
print("Weights List:", weights_list)