from collections.abc import Iterable, Sequence
from typing import Any

from source.frequent_itemsets.confidence import confidence


def probability(j, baskets: Sequence[Iterable[Any]]) -> float:
    if not baskets:
        return 0.0
    return sum(j in basket for basket in baskets) / len(baskets)


def interest(
    i: set[Any], j: Any, items: set[Any], baskets: Sequence[Iterable[Any]]
) -> float:
    return confidence(i, j, items, baskets) - probability(j, baskets)
