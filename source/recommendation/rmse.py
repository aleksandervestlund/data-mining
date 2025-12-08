from collections.abc import Sequence

import numpy as np


def rmse(
    ratings: Sequence[float], predicted_ratings: Sequence[float]
) -> float:
    if len(ratings) != len(predicted_ratings):
        raise ValueError(
            "Length of ratings and predicted_ratings must be the same."
        )
    if not ratings:
        return 0.0
    return np.sqrt(
        sum(
            (actual - predicted) ** 2
            for actual, predicted in zip(ratings, predicted_ratings)
        )
    )
