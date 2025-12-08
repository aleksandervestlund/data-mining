from networkx import Graph

from source.mining_social_network_graphs.girvan_newman import girvan_newman
from source.mining_social_network_graphs.modularity import modularity


def detect_communities(graph: Graph) -> list[Graph]:
    communities = girvan_newman(graph)
    return max(communities, key=modularity)
