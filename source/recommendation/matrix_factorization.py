from collections.abc import Sequence
from typing import Any

import numpy as np
from numpy.typing import NDArray


def learn_weights_by_gd(
    ratings: Sequence[float],
    baselines: Sequence[float],
    residual_matrix: NDArray[Any],
    learning_rate: float = 0.01,
    steps: int = 200,
) -> NDArray[Any]:
    num_examples, num_neighbors = residual_matrix.shape
    w = np.zeros(num_neighbors)

    for _ in range(steps):
        for n in range(num_examples):
            r_ui = ratings[n]
            b_ui = baselines[n]
            residuals = residual_matrix[n]

            pred = b_ui + w @ residuals
            error = r_ui - pred

            w -= learning_rate * error * residuals

    return w


def matrix_factorization(
    r: NDArray[Any],
    dimension: int,
    learning_rate: float = 0.01,
    lambda_: float = 0.1,
    steps: int = 200,
) -> tuple[NDArray[Any], NDArray[Any]]:
    num_users, num_items = r.shape
    p = np.random.normal(scale=lambda_, size=(num_users, dimension))
    q = np.random.normal(scale=lambda_, size=(num_items, dimension))

    for _ in range(steps):
        for user in range(num_users):
            for item in range(num_items):
                if r[user, item] <= 0:
                    continue

                error = r[user, item] - p[user] @ q[item]

                p[user] += learning_rate * (
                    error * q[item] - lambda_ * p[user]
                )
                q[item] += learning_rate * (
                    error * p[user] - lambda_ * q[item]
                )

    return p, q
