from typing import Any

from source.finding_similar_items.jaccard_similarity import jaccard_similarity


def jaccard_distance(value1: set[Any] | int, value2: set[Any] | int) -> float:
    return 1 - jaccard_similarity(value1, value2)
