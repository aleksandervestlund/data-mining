import itertools
from collections.abc import Iterable
from typing import Any


def sample_fixed_proportion(
    data: Iterable[tuple[Any, ...]],
    key_idx: int,
    n_buckets: int,
    buckets_to_sample: int,
) -> list[tuple[Any, ...]]:
    if buckets_to_sample > n_buckets:
        raise ValueError()

    buckets: list[list[tuple[Any, ...]]] = [[] for _ in range(n_buckets)]

    for row in data:
        key = row[key_idx]
        bucket_idx = hash(key) % n_buckets
        buckets[bucket_idx].append(row)

    return list(itertools.chain.from_iterable(buckets[:buckets_to_sample]))
