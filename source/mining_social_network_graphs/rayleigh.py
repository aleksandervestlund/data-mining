from collections.abc import Iterable
from typing import Any

import numpy as np
from networkx import Graph
from numpy.typing import NDArray

from source.mining_social_network_graphs.construct_matrices import (
    laplacian_matrix,
)
from source.mining_social_network_graphs.ncut import ncut


def fiedler(l: Iterable[Iterable[float]]) -> tuple[float, NDArray[Any]]:
    matrix = np.array(l)
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    return eigenvalues[1], eigenvectors[:, 1]


def rayleigh(graph: Graph) -> float:
    l = np.array(laplacian_matrix(graph))
    _, y = fiedler(l)
    return float(y.T @ l @ y)


def decompose1(graph: Graph) -> NDArray[Any]:
    l = np.array(laplacian_matrix(graph))
    _, y = fiedler(l)
    return np.sign(y)


def decompose2(graph: Graph) -> tuple[list[Any], list[Any]]:
    l = np.array(laplacian_matrix(graph), dtype=float)
    _, y = fiedler(l)

    nodes = np.array(list(graph.nodes()))
    order = np.argsort(y)
    sorted_nodes = nodes[order]
    sorted_y = y[order]

    best_ncut = float("inf")
    best_split = None

    for i in range(1, len(nodes)):
        thresh = (sorted_y[i - 1] + sorted_y[i]) / 2

        group1: list[Any] = sorted_nodes[sorted_y <= thresh].tolist()
        group2: list[Any] = sorted_nodes[sorted_y > thresh].tolist()

        if (value := ncut(graph, group1, group2)) < best_ncut:
            best_ncut = value
            best_split = (group1, group2)

    if best_split is None:
        raise ValueError("Graph could not be decomposed.")
    return best_split
