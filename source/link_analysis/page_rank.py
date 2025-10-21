import networkx as nx
import numpy as np
from networkx import Graph
from numpy import float64


def page_rank_gaussian(graph: Graph) -> dict[str, float64]:
    nodes = set(graph.nodes)
    n = len(nodes)

    matrix = nx.to_numpy_array(graph, nodelist=nodes)
    col_sums = matrix.sum(axis=0)
    col_sums[col_sums == 0] = 1.0
    matrix /= col_sums

    matrix = np.eye(n) - matrix
    matrix[-1, :] = 1.0

    b = np.zeros(n)
    b[-1] = 1.0

    r = np.linalg.solve(matrix, b)
    return dict(zip(nodes, r))


def page_rank_iterative(
    graph: Graph, epsilon: float = 1e-6
) -> dict[str, float64]:
    nodes = set(graph.nodes)
    n = len(nodes)

    matrix = nx.to_numpy_array(graph, nodelist=nodes)
    col_sums = matrix.sum(axis=0)
    col_sums[col_sums == 0] = 1.0
    matrix /= col_sums

    r_0 = np.ones(n) / n
    r_1 = matrix @ r_0

    while np.linalg.norm(r_1 - r_0, 1) > epsilon:
        r_0 = r_1
        r_1 = matrix @ r_0

    return dict(zip(nodes, r_1))


def page_rank_google(
    graph: Graph, beta: float = 0.9, epsilon: float = 1e-6
) -> dict[str, float64]:
    nodes = set(graph.nodes)
    n = len(nodes)

    matrix = nx.to_numpy_array(graph, nodelist=nodes)
    col_sums = matrix.sum(axis=0)
    col_sums[col_sums == 0] = 1.0
    matrix /= col_sums

    r_0 = np.ones(n) / n
    r_1 = (beta * matrix + (1 - beta) / n) @ r_0

    while np.linalg.norm(r_1 - r_0, 1) > epsilon:
        r_0 = r_1
        r_1 = (beta * matrix + (1 - beta) / n) @ r_0

    return dict(zip(nodes, r_1))


def page_rank_google_sparse(
    graph: Graph, beta: float = 0.9, epsilon: float = 1e-6
) -> dict[str, float64]:
    nodes = list(graph.nodes)
    n = len(nodes)

    matrix = nx.to_numpy_array(graph, nodelist=nodes)
    col_sums = matrix.sum(axis=0)
    col_sums[col_sums == 0] = 1.0
    matrix /= col_sums

    r_0 = np.ones(n) / n
    r_1 = beta * matrix @ r_0 + (1 - beta) / n

    while np.linalg.norm(r_1 - r_0, 1) > epsilon:
        r_0 = r_1
        r_1 = beta * matrix @ r_0 + (1 - beta) / n

    return dict(zip(nodes, r_1))
