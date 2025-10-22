from typing import Any


def _sim_set(set1: set[Any], set2: set[Any]) -> float:
    intersection = set1 & set2

    if not (union := set1 | set2):
        return 0.0
    return len(intersection) / len(union)


def _sim_bits(int1: int, int2: int) -> float:
    intersection = int1 & int2

    if not (union := int1 | int2):
        return 0.0
    return intersection.bit_count() / union.bit_count()


def jaccard_similarity(
    value1: set[Any] | int, value2: set[Any] | int
) -> float:
    if isinstance(value1, set) and isinstance(value2, set):
        return _sim_set(value1, value2)
    if isinstance(value1, int) and isinstance(value2, int):
        return _sim_bits(value1, value2)
    raise TypeError()
