from collections.abc import Iterable
from typing import Any

import numpy as np
from numpy.typing import NDArray

from source.dimensionality_reduction.frobenius import frobenius_norm


def svd(
    matrix: Iterable[Iterable[float]],
) -> tuple[NDArray[Any], NDArray[Any], NDArray[Any]]:
    matrix_array = np.array(matrix)
    rank = np.linalg.matrix_rank(matrix_array)

    u, sigma, v_t = np.linalg.svd(matrix_array, full_matrices=False)
    u = u[:, :rank]
    sigma = sigma[:rank]
    v_t = v_t[:rank, :]
    return u, sigma, v_t


def reduce_rank(
    sigma: NDArray[Any],
    min_energy: float,
    initial_frobenius: float | None = None,
) -> NDArray[Any]:
    ranked_indices = np.argsort(-sigma)
    sigma_approx = sigma.copy()

    if initial_frobenius is None:
        initial_frobenius = frobenius_norm(sigma)

    smallest_idx = -1

    while True:
        sigma_approx_approx = sigma_approx.copy()
        sigma_approx_approx[ranked_indices[smallest_idx]] = 0.0
        new_frobenius = frobenius_norm(sigma_approx_approx)

        if new_frobenius**2 / initial_frobenius**2 < min_energy:
            break

        sigma_approx = sigma_approx_approx
        smallest_idx -= 1

    return sigma_approx


def map_to_concept_space(
    vector: NDArray[Any], sigma: NDArray[Any], v_t: NDArray[Any]
) -> NDArray[Any]:
    sigma_inv = np.linalg.inv(np.diag(sigma))
    return vector @ v_t.T @ sigma_inv


def map_to_user_space(
    vector: NDArray[Any],
    u: NDArray[Any],
    sigma: NDArray[Any],
    v_t: NDArray[Any],
) -> NDArray[Any]:
    concept_vector = map_to_concept_space(vector, sigma, v_t)
    return concept_vector @ u.T
