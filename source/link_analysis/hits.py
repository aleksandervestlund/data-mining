import networkx as nx
import numpy as np
from networkx import Graph
from numpy import float64


def hypertext_induced_topic_search(
    graph: Graph, delta: float = 1e-6
) -> tuple[dict[str, float64], dict[str, float64]]:
    nodes: list[str] = list(graph.nodes())
    matrix = nx.to_numpy_array(graph, nodelist=nodes)
    matrix_t = matrix.T

    hub_0 = np.ones_like(nodes, dtype=float64)
    hub_0 /= np.linalg.norm(hub_0, 1)
    authority_0 = hub_0.copy()

    hub_matrix = matrix @ matrix_t
    hub_1 = hub_matrix @ hub_0

    while np.linalg.norm(hub_1 - hub_0, 1) >= delta:
        hub_0 = hub_1
        hub_1 = hub_matrix @ hub_0
        hub_1 /= np.linalg.norm(hub_1, 1)

    authority_matrix = matrix_t @ matrix
    authority_1 = authority_matrix @ authority_0

    while np.linalg.norm(authority_1 - authority_0, 1) >= delta:
        authority_0 = authority_1
        authority_1 = authority_matrix @ authority_0
        authority_1 /= np.linalg.norm(authority_1, 1)

    return dict(zip(nodes, hub_1)), dict(zip(nodes, authority_1))
