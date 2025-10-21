import random
from collections.abc import Sequence

import numpy as np

from source.mining_data_streams.sample_fixed_size import sample_fixed_size


def f(moment: int, n: int, c: int) -> int:
    constant = c**moment - (c - 1) ** moment
    return n * constant


def ams(
    stream: Sequence[int], moment: int, n_estimates: int, k_samples: int | None
) -> float:
    """Alon-Matias-Szegedy."""
    if k_samples is None:
        k_samples = n_estimates

    stream = sample_fixed_size(stream, k_samples)
    counts: list[int] = []

    for _ in range(n_estimates):
        n = len(stream)
        idx = random.randint(0, n - 1)
        el = stream[idx]
        c = 0

        for item in stream:
            c += item == el

        counts.append(f(moment, n, c))

    return float(np.mean(counts))
