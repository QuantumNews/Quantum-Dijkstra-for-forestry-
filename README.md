# Quantum-Enhanced Dijkstra Algorithm for Forestry Data

## Project Overview

This repository is part of a broader project aimed at optimizing the Dijkstra algorithm using quantum computing techniques, with specific applications in the forestry sector. Our work focuses on leveraging Grover's algorithm to enhance the efficiency of pathfinding algorithms, particularly within the context of forestry data analysis.

### Introduction

The forestry sector, particularly in regions like British Columbia, Canada, is crucial for both environmental sustainability and economic prosperity. Managing complex forestry operations, such as post-fire salvage and bioenergy utilization, requires advanced modeling techniques. Traditional methods often fall short in handling the scale and dynamics of these systems. By integrating quantum computing, we aim to overcome these limitations and significantly enhance modeling capabilities.

Our primary objective is to develop a quantum-enhanced version of the Dijkstra algorithm by incorporating Grover's search algorithm. This approach promises to speed up finding the shortest path, which has direct applications in forestry data analysis, such as optimizing supply chains, reducing costs, and mitigating greenhouse gas emissions.

### Alternative Approaches

- **Quantum Annealing**: Explored as a probabilistic approach to optimization, potentially providing faster solutions by leveraging quantum fluctuations.
- **Grover Search**: Our focus is on the gate-based quantum computing approach, utilizing Grover's algorithm to exploit quantum parallelism and amplitude amplification, accelerating the search for the shortest path.

### Grover's Algorithm

Grover's algorithm provides a quadratic speedup for searching an unsorted database compared to classical algorithms. It operates through two key components: the oracle, which marks the target solution, and the diffuser, which amplifies the amplitude of all states except the target states.

### Quantum Hardware

Our project leverages the NRCan Quantum Launch Pad initiative, which provides access to various quantum hardware platforms via AWS and Microsoft Azure, including IBM, Rigetti, and IonQ systems. We adopt a hardware-agnostic approach to ensure that our algorithms can run across different setups, facilitating cross-validation and benchmarking.

### The Toy Model

We developed a toy model to demonstrate the effectiveness of our approach. The model generates a graph with a predefined number of nodes and edges, assigns weights to these edges, and uses Grover's algorithm to identify the smallest weight. This model has been tested on both quantum simulators and actual hardware, including IBM, Rigetti, and IonQ systems.

### Extended Dijkstra's Algorithm

The project involves initializing a graph, establishing distances, and iteratively selecting nodes to compute the shortest paths. Our quantum-enhanced Dijkstra algorithm aims to optimize this process by integrating Grover's search algorithm.

## Code Overview

### Graph Generation and Visualization

The script generates a random graph with nodes, edges, and weights, and visualizes the graph.

### Quantum Oracle for Smallest Weight Detection

The quantum oracle is created using Grover's algorithm, identifying the smallest weight in the graph.

### Simulation and Results

The quantum circuit is simulated using Qiskit's \`qasm_simulator\`, and the results are visualized.

## Requirements

To run this project, you will need the following Python packages:

- \`networkx\`
- \`matplotlib\`
- \`qiskit\`

## Next Steps

Our next steps involve testing the quantum-enhanced Dijkstra algorithm, validating results, and expanding to real-world forestry datasets.

## Contributing

Feel free to fork the repository and submit pull requests. Contributions should include documentation and, where applicable, tests.

## License



## Acknowledgments

This project was supported by the NRCan Quantum Launch Pad initiative and utilizes IBM's Qiskit and Rigetti's PyQuil frameworks for quantum programming and simulation.
[README.md](https://github.com/user-attachments/files/16840549/README.md)
he efficiency of pathfinding algorithms, particularly within the context of forestry data analysis.

Introduction
The forestry sector, particularly in regions like British Columbia, Canada, is crucial for both environmental sustainability and economic prosperity. Managing complex forestry operations, such as post-fire salvage and bioenergy utilization, requires advanced modeling techniques. Traditional methods often fall short in handling the scale and dynamics of these systems. By integrating quantum computing, we aim to overcome these limitations and significantly enhance modeling capabilities.

Our primary objective is to develop a quantum-enhanced version of the Dijkstra algorithm by incorporating Grover's search algorithm. This approach promises to speed up finding the shortest path, which has direct applications in forestry data analysis, such as optimizing supply chains, reducing costs, and mitigating greenhouse gas emissions.

Alternative Approaches
Quantum Annealing: Explored as a probabilistic approach to optimization, potentially providing faster solutions by leveraging quantum fluctuations.
Grover Search: Our focus is on the gate-based quantum computing approach, utilizing Grover's algorithm to exploit quantum parallelism and amplitude amplification, accelerating the search for the shortest path.
Grover's Algorithm
Grover's algorithm provides a quadratic speedup for searching an unsorted database compared to classical algorithms. It operates through two key components: the oracle, which marks the target solution, and the diffuser, which amplifies the amplitude of all states except the target states.

Quantum Hardware
Our project leverages the NRCan Quantum Launch Pad initiative, which provides access to various quantum hardware platforms via AWS and Microsoft Azure, including IBM, Rigetti, and IonQ systems. We adopt a hardware-agnostic approach to ensure that our algorithms can run across different setups, facilitating cross-validation and benchmarking.

The Toy Model
We developed a toy model to demonstrate the effectiveness of our approach. The model generates a graph with a predefined number of nodes and edges, assigns weights to these edges, and uses Grover's algorithm to identify the smallest weight. This model has been tested on both quantum simulators and actual hardware, including IBM, Rigetti, and IonQ systems.

Extended Dijkstra's Algorithm
The project involves initializing a graph, establishing distances, and iteratively selecting nodes to compute the shortest paths. Our quantum-enhanced Dijkstra algorithm aims to optimize this process by integrating Grover's search algorithm.

Code Overview
Graph Generation and Visualization
The script generates a random graph with nodes, edges, and weights, and visualizes the graph.

python
Copy code
node_list = ['A', 'B', 'C', 'D', 'E']
graph, weights_list = generate_graph_with_weights(node_list, num_vertices=20)
visualize_graph(graph)
Quantum Oracle for Smallest Weight Detection
The quantum oracle is created using Grover's algorithm, identifying the smallest weight in the graph.

python
Copy code
smallest_item_oracle = create_smallest_item_oracle(n_qubits, weights_list)
Simulation and Results
The quantum circuit is simulated using Qiskit's qasm_simulator, and the results are visualized.

python
Copy code
result = backend.run(qobj).result()
plot_histogram(counts_all_states)
Requirements
To run this project, you will need the following Python packages:

networkx
matplotlib
qiskit
Install the dependencies with:

bash
Copy code
pip install networkx matplotlib qiskit
Next Steps
Our next steps involve testing the quantum-enhanced Dijkstra algorithm, validating results, and expanding to real-world forestry datasets.

Contributing
Feel free to fork the repository and submit pull requests. Contributions should include documentation and, where applicable, tests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project was supported by the NRCan Quantum Launch Pad initiative and utilizes IBM's Qiskit and Rigetti's PyQuil frameworks for quantum programming and simulation.
