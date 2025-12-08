from networkx import Graph


def adjacency_matrix(graph: Graph) -> list[list[int]]:
    nodes = list(graph.nodes)
    index = {node: i for i, node in enumerate(nodes)}
    size = len(nodes)
    matrix = [[0] * size for _ in range(size)]

    for u, v in graph.edges():
        i = index[u]
        j = index[v]
        matrix[i][j] = 1
        matrix[j][i] = 1

    return matrix


def degree_matrix(graph: Graph) -> list[list[int]]:
    nodes = list(graph.nodes)
    size = len(nodes)
    matrix = [[0] * size for _ in range(size)]

    for i, node in enumerate(nodes):
        degree = graph.degree(node)

        if not isinstance(degree, int):
            raise ValueError("Degree must be an integer.")

        matrix[i][i] = degree

    return matrix


def laplacian_matrix(graph: Graph) -> list[list[int]]:
    d = degree_matrix(graph)
    a = adjacency_matrix(graph)
    return [[d[i][j] - a[i][j] for j in range(len(d))] for i in range(len(d))]
