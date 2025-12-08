from collections import defaultdict, deque
from typing import Any

from networkx import Graph


def betweenness(graph: Graph) -> dict:
    edge_bet: defaultdict[tuple[Any, Any], float] = defaultdict(float)

    for s in graph.nodes():
        pred: dict[Any, list[Any]] = {v: [] for v in graph.nodes()}
        sigma: defaultdict[Any, float] = defaultdict(float)
        dist = dict.fromkeys(graph.nodes(), -1.0)

        sigma[s] = 1.0
        dist[s] = 0.0

        queue = deque([s])
        stack: list[Any] = []

        while queue:
            v = queue.popleft()
            stack.append(v)

            for w in graph.neighbors(v):
                if dist[w] < 0.0:
                    dist[w] = dist[v] + 1.0
                    queue.append(w)

                if dist[w] == dist[v] + 1.0:
                    sigma[w] += sigma[v]
                    pred[w].append(v)

        delta: defaultdict[tuple[Any, Any], float] = defaultdict(float)

        while stack:
            w = stack.pop()

            for v in pred[w]:
                edge_credit = (1.0 + delta[w]) * sigma[v] / sigma[w]
                edge = tuple(sorted((v, w)))
                edge_bet[edge] += edge_credit
                delta[v] += edge_credit

    return {edge: centrality / 2.0 for edge, centrality in edge_bet.items()}


def construct_graph() -> Graph:
    return Graph(
        (
            ("A", "B"),
            ("A", "C"),
            ("B", "C"),
            ("B", "D"),
            ("D", "E"),
            ("D", "F"),
            ("D", "G"),
            ("F", "E"),
            ("F", "G"),
        )
    )


def main() -> None:
    graph = construct_graph()
    betweenness_values = betweenness(graph)

    for u, centrality in betweenness_values.items():
        print(f"{u}: {centrality}")


if __name__ == "__main__":
    main()
