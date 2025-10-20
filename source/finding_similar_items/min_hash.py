from collections.abc import Iterable, Sequence

import numpy as np


def min_hash(set_: Iterable[int], permutation: Sequence[int]) -> int:
    if not set_:
        raise ValueError()
    return min(permutation[i] for i in set_)


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


def compute_similarities(row1: Sequence[int], row2: Sequence[int]) -> float:
    if len(row1) != len(row2):
        raise ValueError()
    return float(np.mean(np.array(row1) == np.array(row2)))
