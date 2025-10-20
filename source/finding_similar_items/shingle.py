import itertools
from collections.abc import Iterable

from source.finding_similar_items.utils.token import Token
from source.utils.clean_words import clean_words


def shingle(text: str, token: Token, k: int) -> set[str]:
    shingles: set[str] = set()

    if token is Token.WORD:
        words = clean_words(text)

        for i in range(len(words) - k + 1):
            tokens = words[i : i + k]
            s = " ".join(tokens)
            shingles.add(s)
    elif token is Token.CHARACTER:
        for i in range(len(text) - k + 1):
            s = text[i : i + k]
            shingles.add(s)
    else:
        raise ValueError()

    return shingles


def generate_shingles_matrix(
    documents: Iterable[str], token: Token, k: int = 10
) -> list[list[bool]]:
    shingles = [shingle(doc, token, k) for doc in documents]
    all_shingles = sorted(set(itertools.chain.from_iterable(shingles)))
    return [
        [shingle in doc_set for doc_set in shingles]
        for shingle in all_shingles
    ]
