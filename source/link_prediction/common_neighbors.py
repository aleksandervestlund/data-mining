import networkx as nx
from networkx import Graph


def common_neighbors(graph: Graph, x: str, y: str) -> int:
    neighbors_x = set(nx.neighbors(graph, x))
    neighbors_y = set(nx.neighbors(graph, y))
    return len(neighbors_x & neighbors_y)
