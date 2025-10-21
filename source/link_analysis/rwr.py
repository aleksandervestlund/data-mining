from networkx import Graph
from numpy import float64

from source.link_analysis.topic_specific_page_rank import (
    topic_specific_page_rank_iterative,
)


def random_walk_with_restart(
    graph: Graph, beta: float = 0.9, epsilon: float = 1e-6
) -> dict[str, dict[str, float64]]:
    nodes: set[str] = set(graph.nodes)
    return {
        node: topic_specific_page_rank_iterative(graph, {node}, beta, epsilon)
        for node in nodes
    }
