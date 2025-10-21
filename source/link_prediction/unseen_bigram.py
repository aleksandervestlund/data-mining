from collections.abc import Callable, Set

from networkx import Graph


def unseen_bigram_unweighted(
    graph: Graph, y: str, similar_to_x: Set[str]
) -> float:
    neighbors_y = set(graph.neighbors(y))
    return len(similar_to_x & neighbors_y)


def unseen_bigram_weighted(
    graph: Graph,
    x: str,
    y: str,
    similar_to_x: Set[str],
    score_function: Callable[[Graph, str, str], float],
) -> float:
    neighbors_y = set(graph.neighbors(y))
    common_neighbors = similar_to_x & neighbors_y
    return sum(score_function(graph, x, z) for z in common_neighbors)
