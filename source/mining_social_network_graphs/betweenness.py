from typing import Any

import networkx as nx
from networkx import Graph


def betweenness(graph: Graph) -> dict[tuple[Any, Any], float]:
    return nx.betweenness_centrality(graph)
