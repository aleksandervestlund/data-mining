from collections.abc import Set

import networkx as nx
import numpy as np
from networkx import Graph
from numpy import float64


def topic_specific_page_rank_gaussian(
    graph: Graph,
    topic_nodes: Set[str],
    beta: float = 0.9,
) -> dict[str, float64]:
    nodes = list(graph.nodes())
    n = len(nodes)

    matrix = nx.to_numpy_array(graph, nodelist=nodes)
    col_sums = matrix.sum(axis=0)
    col_sums[col_sums == 0] = 1.0
    matrix /= col_sums

    teleport_vector = np.zeros((n, 1))

    for i, node in enumerate(nodes):
        teleport_vector[i] = float(node in topic_nodes)

    teleport_vector *= (1 - beta) / len(topic_nodes)
    matrix = beta * matrix + teleport_vector.T

    matrix -= np.eye(n)
    matrix[-1, :] = 1.0

    b = np.zeros(n)
    b[-1] = 1.0
    r = np.linalg.solve(matrix, b)
    return dict(zip(nodes, r))


def topic_specific_page_rank_iterative(
    graph: Graph,
    topic_nodes: Set[str],
    beta: float = 0.9,
    epsilon: float = 1e-6,
) -> dict[str, float64]:
    nodes = list(graph.nodes())
    n = len(nodes)

    matrix = nx.to_numpy_array(graph, nodelist=nodes)
    col_sums = matrix.sum(axis=0)
    col_sums[col_sums == 0] = 1.0
    matrix /= col_sums

    teleport_vector = np.zeros((n, 1))

    for i, node in enumerate(nodes):
        teleport_vector[i] = float(node in topic_nodes)

    teleport_vector *= (1 - beta) / len(topic_nodes)
    matrix = beta * matrix + teleport_vector.T

    r_0 = np.ones(n) / n
    r_1 = matrix @ r_0

    while np.linalg.norm(r_1 - r_0, 1) > epsilon:
        r_0 = r_1
        r_1 = matrix @ r_0

    return dict(zip(nodes, r_1))
