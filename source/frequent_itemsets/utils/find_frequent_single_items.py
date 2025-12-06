from collections import defaultdict
from collections.abc import Iterable
from typing import Any


def find_frequent_single_items(
    baskets: Iterable[Iterable[Any]], min_count: int
) -> set[Any]:
    counts: defaultdict[Any, int] = defaultdict(int)

    for basket in baskets:
        for item in set(basket):
            counts[item] += 1

    return {item for item, count in counts.items() if count >= min_count}
