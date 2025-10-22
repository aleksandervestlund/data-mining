import networkx as nx
from networkx import Graph


def graph_distance(graph: Graph, x: str, y: str) -> int:
    return -nx.shortest_path_length(graph, x, y)
