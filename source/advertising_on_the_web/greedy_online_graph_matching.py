from collections.abc import Iterable
from typing import Any


def greedy_online_matching(
    boys: Iterable[Any], girls: Iterable[tuple[Any, Iterable[Any]]]
) -> dict[Any, Any]:
    matching: dict[Any, Any] = {boy: None for boy in boys}

    for girl, preferred_boys in girls:
        if (
            boy := next(
                (
                    preferred_boy
                    for preferred_boy in preferred_boys
                    if matching[preferred_boy] is None
                ),
                None,
            )
        ) is not None:
            matching[boy] = girl

    return matching
