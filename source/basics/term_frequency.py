from collections import Counter


def term_frequency(term: str, document: str) -> float:
    terms = document.split()
    counter = Counter(terms)

    if (max_count := max(counter.values())) == 0:
        return 0.0
    return counter[term] / max_count


def main() -> None:
    print(
        term_frequency(
            "Aleksander",
            "Aleksander var en kul mann. Han var kjempekul. Han het Aleksander. Han var en løk",
        )
    )


if __name__ == "__main__":
    main()
