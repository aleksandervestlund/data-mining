from collections.abc import Iterable

import numpy as np

from source.mining_data_streams.utils.generate_random_hash_functions import (
    generate_random_hash_functions,
)


PHI = 0.77351
BIAS = 0.31


def least_zero_bit_index(a: int, b: int, n_bits: int, x: int) -> int:
    h = (a * x + b) % 2**n_bits
    binary = bin(h)[2:][::-1]
    return binary.find("0")


def bias(k: int) -> float:
    return 1 + BIAS / k


def flajolet_martin(items: Iterable[int], n_hashes: int, n_bits: int) -> int:
    hash_functions = generate_random_hash_functions(
        n_hashes, n_bits, least_zero_bit_index
    )
    max_indices: list[int] = []

    for hash_function in hash_functions:
        max_idx = 0

        for item in items:
            idx = hash_function(item)
            max_idx = max(max_idx, idx)

        max_indices.append(max_idx)

    b = np.mean(max_indices)
    return round(2**b / (PHI * bias(n_hashes)))
