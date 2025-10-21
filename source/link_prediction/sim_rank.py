from networkx import Graph

from source.link_prediction.preferential_attachment import (
    preferential_attachment,
)


def sim_rank(graph: Graph, x: str, y: str, gamma: float) -> float:
    if x == y:
        return 1.0

    neighbors_x = set(graph.neighbors(x))
    neighbors_y = set(graph.neighbors(y))
    pref_attachment = preferential_attachment(graph, x, y)
    all_scores = sum(
        sim_rank(graph, nx, ny, gamma)
        for nx in neighbors_x
        for ny in neighbors_y
    )
    return gamma * all_scores / pref_attachment
