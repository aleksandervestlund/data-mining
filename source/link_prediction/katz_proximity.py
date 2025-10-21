import networkx as nx
import numpy as np
from networkx import Graph
from numpy import float64


def katz_proximity(graph: Graph, x: str, y: str, beta: float) -> float64:
    nodes = list(graph.nodes)
    idx_x = nodes.index(x)
    idx_y = nodes.index(y)

    matrix = nx.to_numpy_array(graph)
    identity = np.eye(len(nodes))
    matrix = np.linalg.inv(identity - beta * matrix) - identity
    return matrix[idx_x, idx_y]
