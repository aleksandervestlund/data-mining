from collections import Counter


def term_frequency(term: str, document: str) -> float:
    terms = document.split()
    counter = Counter(terms)

    if (max_count := max(counter.values())) == 0:
        return 0.0
    return counter[term] / max_count
