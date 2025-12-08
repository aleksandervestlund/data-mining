from collections.abc import Iterable

from networkx import Graph


def modularity(graphs: Iterable[Graph]) -> float:
    m = sum(graph.number_of_edges() for graph in graphs)

    return sum(
        graph.has_edge(i, j) - graph.degree[i] * graph.degree[j] / (2 * m)
        for graph in graphs
        for i in graph.nodes
        for j in graph.nodes
    ) / (2 * m)
