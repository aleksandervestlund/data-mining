import itertools

from networkx import DiGraph


def itemsets_to_bipartite(graph: DiGraph, min_support: int) -> list[DiGraph]:
    itemsets = {i: set(graph.successors(i)) for i in graph.nodes}
    all_items = set(itertools.chain.from_iterable(itemsets.values()))
    bipartite_subgraphs: list[DiGraph] = []
    items_list = list(all_items)

    for r in range(1, len(all_items) + 1):
        for y in itertools.combinations(items_list, r):
            ys = set(y)

            supporting_nodes = [
                i for i, s_i in itemsets.items() if ys.issubset(s_i)
            ]

            if len(supporting_nodes) < min_support:
                continue

            di_graph: DiGraph = DiGraph()
            left_nodes = [f"X_{i}" for i in supporting_nodes]
            right_nodes = [f"Y_{j}" for j in ys]

            for x_i in left_nodes:
                for y_j in right_nodes:
                    di_graph.add_edge(x_i, y_j)

            bipartite_subgraphs.append(di_graph)

    return bipartite_subgraphs
