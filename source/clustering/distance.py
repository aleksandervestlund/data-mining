import math


def euclidean(point1: tuple[float, ...], point2: tuple[float, ...]) -> float:
    if len(point1) != len(point2):
        raise ValueError("Points must have the same number of dimensions.")
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))


def cosine(point1: tuple[float, ...], point2: tuple[float, ...]) -> float:
    if len(point1) != len(point2):
        raise ValueError("Points must have the same number of dimensions.")

    dot_product = sum(a * b for a, b in zip(point1, point2))
    magnitude1 = math.sqrt(sum(a**2 for a in point1))
    magnitude2 = math.sqrt(sum(b**2 for b in point2))

    if 0.0 in {magnitude1, magnitude2}:
        raise ValueError("One of the points is a zero vector.")
    return dot_product / (magnitude1 * magnitude2)
