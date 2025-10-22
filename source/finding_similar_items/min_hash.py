from collections.abc import Iterable, Sequence

import numpy as np
from numpy import float64


def min_hash(items: Iterable[int], permutation: Sequence[int]) -> int:
    if not items:
        raise ValueError()
    return min(permutation[i] for i in items)


def generate_signature_matrix(
    permutations: Sequence[Sequence[int]],
    shingles_matrix: Sequence[Sequence[bool]],
) -> list[list[int]]:
    num_hashes = len(permutations)
    num_docs = len(shingles_matrix[0])
    signature_matrix = [[num_hashes] * num_docs for _ in range(num_hashes)]

    for hash_idx, permutation in enumerate(permutations):
        for row_idx, shingle in enumerate(shingles_matrix):
            for doc_idx in range(num_docs):
                if not shingle[doc_idx]:
                    continue

                signature_matrix[hash_idx][doc_idx] = min(
                    signature_matrix[hash_idx][doc_idx], permutation[row_idx]
                )

    return signature_matrix


def compute_similarities(row1: Sequence[int], row2: Sequence[int]) -> float64:
    if len(row1) != len(row2):
        raise ValueError()
    return np.mean(np.array(row1) == np.array(row2))
