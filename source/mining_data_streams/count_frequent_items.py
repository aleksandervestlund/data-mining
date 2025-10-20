from collections import defaultdict
from collections.abc import Iterable
from typing import Any


THRESHOLD = 0.5


def count_frequent_items(items: Iterable[Any], c: float) -> list[Any]:
    counts: defaultdict[Any, float] = defaultdict(float)

    for item in items:
        for k in counts:
            counts[k] *= 1 - c

        counts[item] += 1

        for k in counts:
            if counts[k] < THRESHOLD:
                counts.pop(k)

    return list(counts)
