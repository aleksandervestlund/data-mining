import networkx as nx
from networkx import Graph

from source.mining_social_network_graphs.betweenness import betweenness


def girvan_newman(graph: Graph) -> list[list[Graph]]:
    g = graph.copy()
    components = [[g.copy()]]

    while g.number_of_edges() > 0:
        betweenness_dict = betweenness(g)
        max_betweenness = max(betweenness_dict.values())

        edges = [
            edge
            for edge, value in betweenness_dict.items()
            if value == max_betweenness
        ]

        g.remove_edges_from(edges)
        current_components: list[Graph] = []

        for component_nodes in nx.connected_components(g):
            subgraph = g.subgraph(component_nodes).copy()
            current_components.append(subgraph)

        components.append(current_components)

    return components
