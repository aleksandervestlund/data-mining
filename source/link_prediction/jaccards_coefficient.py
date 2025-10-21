from networkx import Graph

from source.finding_similar_items.jaccard_similarity import jaccard_similarity


def jaccards_coefficient(graph: Graph, x: str, y: str) -> float:
    neighbors_x = set(graph.neighbors(x))
    neighbors_y = set(graph.neighbors(y))
    return jaccard_similarity(neighbors_x, neighbors_y)
