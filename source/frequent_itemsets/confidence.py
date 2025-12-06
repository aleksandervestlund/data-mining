from collections.abc import Iterable
from typing import Any

from source.frequent_itemsets.support import support


def confidence(
    i: set[Any], j: Any, items: set[Any], baskets: Iterable[Iterable[Any]]
) -> float:
    if (supp := support(items, baskets)) == 0.0:
        return 0.0
    return support(i | {j}, baskets) / supp
