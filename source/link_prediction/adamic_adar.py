import numpy as np
from networkx import Graph


def adamic_adar(graph: Graph, x: str, y: str) -> float:
    neighbors_x = set(graph.neighbors(x))
    neighbors_y = set(graph.neighbors(y))
    common_neighbors = neighbors_x & neighbors_y

    return sum(
        np.log(len(set(graph.neighbors(z)))) ** (-1) for z in common_neighbors
    )
