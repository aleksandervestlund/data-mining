from collections.abc import Iterable
from typing import Any

from source.frequent_itemsets.finding_frequent_pcy import pcy
from source.frequent_itemsets.utils.sort_baskets import sort_baskets
from source.mining_data_streams.sample_fixed_size import sample_fixed_size


def sampling(
    items: set[Any],
    baskets: Iterable[Iterable[Any]],
    min_count: int,
    sample_size: int,
    buckets: int,
) -> set[tuple[Any, Any]]:
    baskets2 = sort_baskets(baskets)
    baskets2 = sample_fixed_size(baskets2, sample_size)
    estimate = pcy(items, baskets2, min_count // sample_size, buckets)
    return pcy(estimate, baskets, min_count, buckets)
