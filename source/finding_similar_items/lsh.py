import itertools
from collections import defaultdict
from collections.abc import Sequence

from source.finding_similar_items.jaccard_similarity import jaccard_similarity
from source.finding_similar_items.min_hash import min_hash


def hash_band(band: tuple[int, ...], k: int) -> int:
    return hash(band) % k


def _create_buckets(
    signature_matrix: Sequence[Sequence[int]],
    k: int,
    num_docs: int,
    start_row: int,
    end_row: int,
) -> dict[int, list[int]]:
    buckets: dict[int, list[int]] = defaultdict(list)
    permutation = range(k)

    for doc_idx in range(num_docs):
        band = tuple(
            signature_matrix[row_idx][doc_idx]
            for row_idx in range(start_row, end_row)
        )
        hash_value = min_hash(band, permutation)
        buckets[hash_value].append(doc_idx)

    return buckets


def _create_candidate_pairs(
    signature_matrix: Sequence[Sequence[int]],
    bands: int,
    rows: int,
    k: int,
) -> set[tuple[int, int]]:
    num_docs = len(signature_matrix[0])
    candidate_pairs: set[tuple[int, int]] = set()

    for band_idx in range(bands):
        start_row = band_idx * rows
        end_row = start_row + rows

        buckets = _create_buckets(
            signature_matrix, k, num_docs, start_row, end_row
        )

        for docs_in_bucket in buckets.values():
            for pair in itertools.combinations(sorted(docs_in_bucket), 2):
                candidate_pairs.add(pair)

    return candidate_pairs


def _filter_candidate_pairs(
    similarity_threshold: float,
    shingles_matrix: Sequence[Sequence[bool]],
    candidate_pairs: set[tuple[int, int]],
) -> set[tuple[int, int]]:
    filtered_pairs: set[tuple[int, int]] = set()

    for i, j in candidate_pairs:
        doc_i = {idx for idx, row in enumerate(shingles_matrix) if row[i]}
        doc_j = {idx for idx, row in enumerate(shingles_matrix) if row[j]}

        if jaccard_similarity(doc_i, doc_j) >= similarity_threshold:
            filtered_pairs.add((i, j))

    return filtered_pairs


def locality_sensitive_hashing(
    signature_matrix: Sequence[Sequence[int]],
    shingles_matrix: Sequence[Sequence[bool]],
    bands: int,
    rows: int,
    k: int,
    similarity_threshold: float,
) -> set[tuple[int, int]]:
    candidate_pairs = _create_candidate_pairs(signature_matrix, bands, rows, k)
    return _filter_candidate_pairs(
        similarity_threshold, shingles_matrix, candidate_pairs
    )
