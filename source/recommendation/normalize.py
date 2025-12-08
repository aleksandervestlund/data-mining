from source.clustering.distance import cosine
from source.utils.types import Point


def normalize(point: Point) -> Point:
    if not point:
        return point

    mean = sum(point) / len(point)
    return tuple(x - mean for x in point)


def cosine_distance_normalize(point1: Point, point2: Point) -> float:
    point1_norm = normalize(point1)
    point2_norm = normalize(point2)
    return cosine(point1_norm, point2_norm)
