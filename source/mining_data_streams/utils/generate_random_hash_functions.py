import random
from collections.abc import Callable
from functools import partial


def _hash(a: int, b: int, n_bits: int, x: int) -> int:
    return (a * x + b) % 2**n_bits


def generate_random_hash_functions(
    n_hashes: int,
    n_bits: int,
    hash_function: Callable[[int, int, int, int], int] = _hash,
) -> list[partial[int]]:
    """The last argument of `hash_function` has to be the input value to
    be hashed.
    """
    max_value = 2**n_bits
    hash_functions: list[partial[int]] = []

    for _ in range(n_hashes):
        a = random.randint(1, max_value - 1)
        b = random.randint(0, max_value - 1)
        function = partial(hash_function, a, b, n_bits)
        hash_functions.append(function)

    return hash_functions
