from collections.abc import Sequence

import numpy as np

from source.utils.clean_words import clean_words


def inverse_document_frequency(term: str, documents: Sequence[str]) -> float:
    if (
        n_term := sum(term.lower() in clean_words(doc) for doc in documents)
    ) == 0:
        return 0.0

    n = len(documents)
    return np.log2(n / n_term)
