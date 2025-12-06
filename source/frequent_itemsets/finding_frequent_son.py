from collections.abc import Iterable, Sequence
from typing import Any

from source.frequent_itemsets.finding_frequent_pcy import pcy


def son(
    items: set[Any],
    baskets: Sequence[Iterable[Any]],
    min_count: int,
    chunks: int,
) -> set[tuple[Any, Any]]:
    chunk_size = len(baskets) // chunks
    all_frequent: set[tuple[Any, Any]] = set()

    for i in range(chunks):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < chunks - 1 else len(baskets)
        basket_chunk = baskets[start:end]
        frequent_in_chunk = pcy(items, basket_chunk, min_count // chunks, 1000)
        all_frequent |= frequent_in_chunk

    return pcy(all_frequent, baskets, min_count, 1000)
