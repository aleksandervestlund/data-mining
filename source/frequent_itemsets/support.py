from collections.abc import Iterable
from typing import Any


def support(items: set[Any], baskets: Iterable[Iterable[Any]]) -> float:
    return sum(items.issubset(basket) for basket in baskets)
