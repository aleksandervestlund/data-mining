from collections.abc import Iterable

import numpy as np


def frobenius_norm(matrix: Iterable[Iterable[float]]) -> float:
    terms = sum(element**2 for row in matrix for element in row)
    return np.sqrt(terms)
