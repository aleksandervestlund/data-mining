import itertools
import math
from collections import defaultdict
from collections.abc import Iterable
from typing import Any

from source.frequent_itemsets.utils.compute_array_idx import compute_array_idx
from source.frequent_itemsets.utils.sort_baskets import sort_baskets
from source.frequent_itemsets.utils.storage import Storage


def find_frequent_pairs(
    items: set[Any],
    baskets: Iterable[Iterable[Any]],
    min_count: int,
    storage: Storage,
) -> set[tuple[Any, Any]]:
    baskets2 = sort_baskets(baskets)

    if storage is Storage.ARRAY:
        return _find_frequent_pairs_array(items, baskets2, min_count)
    if storage is Storage.MATRIX:
        return _find_frequent_pairs_matrix(items, baskets2, min_count)
    if storage is Storage.TABLE:
        return _find_frequent_pairs_table(items, baskets2, min_count)
    raise ValueError(f"Unknown storage type: {storage}")


def _find_frequent_pairs_matrix(
    items: set[Any], baskets: Iterable[Iterable[Any]], min_count: int
) -> set[tuple[Any, Any]]:
    items2 = list(items)
    matrix = [[0] * len(items2) for _ in range(len(items2))]

    for basket in baskets:
        for combination in itertools.combinations(basket, 2):
            item1, item2 = combination
            i = items2.index(item1)
            j = items2.index(item2)
            matrix[i][j] += 1

    return {
        (items2[i], items2[j])
        for i in range(len(items2))
        for j in range(i + 1, len(items2))
        if matrix[i][j] >= min_count
    }


def _find_frequent_pairs_array(
    items: set[Any], baskets: Iterable[Iterable[Any]], min_count: int
) -> set[tuple[Any, Any]]:
    items2 = list(items)
    n = len(items2)
    array = [0] * math.comb(n, 2)

    for basket in baskets:
        for combination in itertools.combinations(basket, 2):
            item1, item2 = combination
            i = items2.index(item1)
            j = items2.index(item2)
            idx = compute_array_idx(i, j, n)
            array[idx] += 1

    return {
        (items2[i], items2[j])
        for i in range(n)
        for j in range(i + 1, n)
        if array[compute_array_idx(i, j, n)] >= min_count
    }


def _find_frequent_pairs_table(
    items: set[Any], baskets: Iterable[Iterable[Any]], min_count: int
) -> set[tuple[Any, Any]]:
    counts: defaultdict[tuple[Any, Any], int] = defaultdict(int)

    for basket in baskets:
        for combination in itertools.combinations(
            sorted(set(basket) & items), 2
        ):
            counts[combination] += 1

    return {pair for pair, count in counts.items() if count >= min_count}
