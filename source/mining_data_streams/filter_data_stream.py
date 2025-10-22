from collections.abc import Iterable, Sequence

import numpy as np

from source.mining_data_streams.utils.generate_random_hash_functions import (
    generate_random_hash_functions,
)


def bloom_filter(
    original_stream: Sequence[int],
    new_stream: Iterable[int],
    n_bits: int,
    n_hashes: int | None = None,
) -> list[int]:
    if n_hashes is None:
        n_hashes = round(np.log(2) * n_bits / len(original_stream))

    hash_functions = generate_random_hash_functions(n_hashes, n_bits)
    array = [False] * n_bits

    for bit in original_stream:
        for hash_function in hash_functions:
            hash_ = hash_function(bit)
            array[hash_] = True

    return [
        elem
        for elem in new_stream
        if all(array[hash_function(elem)] for hash_function in hash_functions)
    ]
