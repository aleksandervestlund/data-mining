import itertools
from collections import defaultdict
from collections.abc import Callable, Iterable, Sequence
from typing import Any

from source.frequent_itemsets.utils.sort_baskets import sort_baskets


def pcy(
    items: set[Any],
    baskets: Iterable[Iterable[Any]],
    min_count: int,
    buckets: int,
) -> set[tuple[Any, Any]]:
    item_counts: defaultdict[Any, int] = defaultdict(int)
    bucket_counts: defaultdict[int, int] = defaultdict(int)
    baskets2 = sort_baskets(baskets)

    for basket in baskets2:
        unique = set(basket)

        for item in unique:
            item_counts[item] += 1

        for pair in itertools.combinations(unique, 2):
            h = hash(pair) % buckets
            bucket_counts[h] += 1

    bit_vector = [False] * buckets

    for h, c in bucket_counts.items():
        bit_vector[h] |= c >= min_count

    candidate_counts: dict[tuple[Any, Any], int] = {}

    for pair in itertools.combinations(sorted(items), 2):
        i, j = pair
        h = hash(pair) % buckets

        if (
            item_counts[i] >= min_count
            and item_counts[j] >= min_count
            and bit_vector[h]
        ):
            candidate_counts[pair] = 0

    for basket in baskets2:
        for pair in itertools.combinations(basket, 2):
            if pair in candidate_counts:
                candidate_counts[pair] += 1

    return {
        pair for pair, count in candidate_counts.items() if count >= min_count
    }


def pcy_multihash(
    items: set[Any],
    baskets: Iterable[Iterable[Any]],
    min_count: int,
    buckets: int,
    hash_functions: Sequence[Callable[[tuple[Any, Any]], int]],
) -> set[tuple[Any, Any]]:
    baskets2 = sort_baskets(baskets)
    item_counts: defaultdict[Any, int] = defaultdict(int)

    n_hashes = len(hash_functions)
    bucket_counts_list: list[defaultdict[int, int]] = [
        defaultdict(int) for _ in range(n_hashes)
    ]

    for basket in baskets2:
        for item in basket:
            item_counts[item] += 1

        for pair in itertools.combinations(basket, 2):
            for hash_function, bucket_counts in zip(
                hash_functions, bucket_counts_list
            ):
                h = hash_function(pair) % buckets
                bucket_counts[h] += 1

    bit_vectors: list[list[bool]] = []

    for bucket_counts in bucket_counts_list:
        bit_vector = [False] * buckets

        for h, c in bucket_counts.items():
            bit_vector[h] |= c >= min_count

        bit_vectors.append(bit_vector)

    candidate_counts: dict[tuple[Any, Any], int] = {}

    for pair in itertools.combinations(sorted(items), 2):
        i, j = pair

        if (
            item_counts[i] >= min_count
            and item_counts[j] >= min_count
            and all(
                bit_vectors[k][(hash_functions[k](pair)) % buckets]
                for k in range(n_hashes)
            )
        ):
            candidate_counts[pair] = 0

    for basket in baskets2:
        for pair in itertools.combinations(basket, 2):
            if pair in candidate_counts:
                candidate_counts[pair] += 1

    return {
        pair for pair, count in candidate_counts.items() if count >= min_count
    }
