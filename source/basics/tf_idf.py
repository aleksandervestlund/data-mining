from collections.abc import Sequence

from source.basics.inverse_document_frequency import inverse_document_frequency
from source.basics.term_frequency import term_frequency


def tf_idf(term: str, documents: Sequence[str], idx: int) -> float:
    tf = term_frequency(term, documents[idx])
    idf = inverse_document_frequency(term, documents)
    return tf * idf
