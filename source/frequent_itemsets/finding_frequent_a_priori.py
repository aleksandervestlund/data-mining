import itertools
from collections import defaultdict
from collections.abc import Iterable
from typing import Any

from source.frequent_itemsets.finding_frequent_naive import (
    find_frequent_pairs as naive_find_frequent_pairs,
)
from source.frequent_itemsets.utils.find_frequent_single_items import (
    find_frequent_single_items,
)
from source.frequent_itemsets.utils.storage import Storage


def a_priori(
    baskets: Iterable[set[Any]], length: int, min_count: int, storage: Storage
) -> set[tuple[Any, ...]]:
    if length == 1:
        prev_level = find_frequent_single_items(baskets, min_count)
        return {(item,) for item in prev_level}

    items2 = find_frequent_single_items(baskets, min_count)
    prev_level = naive_find_frequent_pairs(items2, baskets, min_count, storage)

    if length == 2:
        return prev_level

    for k in range(3, length + 1):
        candidates: set[tuple[Any, ...]] = set()
        prev_list = sorted(prev_level)

        for i, elem1 in enumerate(prev_list):
            for elem2 in prev_list[i + 1 :]:
                if elem1[: k - 2] != elem2[: k - 2]:
                    continue

                cand = tuple(sorted(set(elem1) | set(elem2)))

                if len(cand) == k:
                    candidates.add(cand)

        pruned_candidates: set[tuple[Any, ...]] = set()
        prev_set = set(prev_level)

        for cand in candidates:
            ok = True

            for subset in itertools.combinations(cand, k - 1):
                if tuple(sorted(subset)) not in prev_set:
                    ok = False
                    break

            if ok:
                pruned_candidates.add(cand)

        counts: defaultdict[tuple[Any, ...], int] = defaultdict(int)
        cand_sets = {c: set(c) for c in pruned_candidates}

        for basket in baskets:
            for c, cset in cand_sets.items():
                counts[c] += cset.issubset(basket)

        if not (
            next_level := {c for c, cnt in counts.items() if cnt >= min_count}
        ):
            return set()

        prev_level = next_level

    return prev_level
