from collections.abc import Iterable
from typing import Any

import numpy as np
from numpy.typing import NDArray

from source.dimensionality_reduction.frobenius import frobenius_norm
from source.dimensionality_reduction.svd import svd


def column_probabilities(matrix: NDArray[Any]) -> NDArray[Any]:
    total = frobenius_norm(matrix) ** 2
    return np.sum(matrix**2, axis=0) / total


def row_probabilities(matrix: NDArray[Any]) -> NDArray[Any]:
    total = frobenius_norm(matrix) ** 2
    return np.sum(matrix**2, axis=1) / total


def sample_indices(probabilities: NDArray[Any], sample_size: int) -> list[int]:
    cumsum = np.cumsum(probabilities)
    indices: list[int] = []

    for _ in range(sample_size):
        r = np.random.rand()
        j = int(np.searchsorted(cumsum, r))
        indices.append(j)

    return indices


def cur(
    matrix: Iterable[Iterable[float]], c_size: int, r_size: int
) -> tuple[NDArray[Any], NDArray[Any], NDArray[Any]]:
    a = np.array(matrix)
    m, n = a.shape

    p_cols = column_probabilities(a)
    col_indices = sample_indices(p_cols, c_size)

    c = np.zeros((m, c_size))

    for k, j in enumerate(col_indices):
        c[:, k] = a[:, j] / np.sqrt(c_size * p_cols[j])

    p_rows = row_probabilities(a)
    row_indices = sample_indices(p_rows, r_size)

    r = np.zeros((r_size, n))

    for k, i in enumerate(row_indices):
        r[k, :] = a[i, :] / np.sqrt(r_size * p_rows[i])

    w = a[np.ix_(row_indices, col_indices)]
    x, z, y_t = svd(w)

    z_plus = np.linalg.inv(np.diag(z))
    z_plus_sq = z_plus @ z_plus

    u = y_t.T @ z_plus_sq @ x.T
    return c, u, r
