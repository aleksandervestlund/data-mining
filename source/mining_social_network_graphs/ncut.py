import itertools
from collections.abc import Iterable
from typing import Any

from networkx import Graph


def vol(graph: Graph, group: Any) -> float:
    degrees = graph.degree(group)

    if isinstance(degrees, int):
        return float(degrees)
    return float(sum(dict(degrees).values()))


def cut(graph: Graph, groups: Iterable[Iterable[Any]]) -> int:
    nodes = list(itertools.chain.from_iterable(groups))

    if len(nodes) != len(graph.nodes) or len(set(nodes)) != len(nodes):
        raise ValueError("All nodes must be included in the groups.")

    cut_size = 0
    groups = {node: i for i, group in enumerate(groups) for node in group}

    for u, v in graph.edges():
        cut_size += groups[u] != groups[v]

    return cut_size


def ncut(graph: Graph, group1: Iterable[Any], group2: Iterable[Any]) -> float:
    groups = (group1, group2)
    cut_sum = cut(graph, groups)
    vol_inv = sum(vol(graph, group) ** (-1) for group in groups)
    return cut_sum * vol_inv
