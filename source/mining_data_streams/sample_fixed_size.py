import random
from collections.abc import Sequence
from typing import Any


def sample_fixed_size(data: Sequence[Any], size: int) -> list[Any]:
    if (length := len(data)) <= size:
        return list(data)

    sample = list(data[:size])
    probability = size / length

    for element in data[size:]:
        if random.random() >= probability:
            continue

        replace_idx = random.randint(0, size - 1)
        sample[replace_idx] = element

    return sample
