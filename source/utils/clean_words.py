def clean_words(document: str) -> list[str]:
    return [
        w
        for word in document.split()
        if (w := word.lower().strip(",.!?;:\"'()[]{}<> "))
    ]
