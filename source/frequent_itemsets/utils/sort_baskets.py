from collections.abc import Iterable
from typing import Any


def sort_baskets(baskets: Iterable[Iterable[Any]]) -> list[list[Any]]:
    return [sorted(set(basket)) for basket in baskets]
