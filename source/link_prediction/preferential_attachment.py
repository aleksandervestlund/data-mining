from networkx import Graph


def preferential_attachment(graph: Graph, x: str, y: str) -> int:
    neighbors_x = set(graph.neighbors(x))
    neighbors_y = set(graph.neighbors(y))
    return len(neighbors_x) * len(neighbors_y)
