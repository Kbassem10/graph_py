# Graph Path Counter

This project allows users to create a graph by specifying the number of nodes and edges, and then count the possible paths between two specified nodes.

## Requirements

- Python 3.x
- NetworkX
- Matplotlib

## Installation

To install the required packages, run:

```bash
pip install networkx matplotlib
```

## Usage

1. Run the script:

```bash
python graph.py
```
or 
```bash
python3 graph.py
```

2. Follow the prompts to input the number of nodes and edges, and then specify the edges.

3. The script will display the adjacency matrix and visualize the graph.

4. Input the start and end nodes to count the possible paths between them.

## Example

```
The number of Nodes: 4
The Number of links: 5
U: 1
V: 2
U: 1
V: 3
U: 1
V: 4
U: 2
V: 3
U: 3
V: 4
The Adjacent Matrix: 
[0, 1, 1, 1]
[1, 0, 1, 0]
[1, 1, 0, 1]
[1, 0, 1, 0]
Start of counting: 1
End of counting: 4
Number of paths between 1 and 4: 2
```

## Code Overview

- The script creates an adjacency matrix based on user input.
- It visualizes the graph using NetworkX and Matplotlib.
- It includes a function `count_paths` to count the possible paths between two nodes using recursion.

## License

This project is licensed under the MIT License.