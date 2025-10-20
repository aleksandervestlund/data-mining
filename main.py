from source.finding_similar_items.min_hash import generate_signature_matrix


def main() -> None:
    shingles_matrix = [
        [True, False, True, False],
        [True, False, False, True],
        [False, True, False, True],
        [False, True, False, True],
        [False, True, False, True],
        [True, False, True, False],
        [True, False, True, False],
    ]

    permutations = [
        [1, 2, 6, 5, 0, 4, 3],
        [3, 1, 0, 2, 5, 6, 4],
        [2, 3, 6, 1, 5, 0, 4],
    ]

    sig = generate_signature_matrix(permutations, shingles_matrix)

    # Expected output:
    # [
    #   [1, 0, 1, 0],
    #   [1, 0, 3, 0],
    #   [0, 1, 0, 1],
    # ]

    for row in sig:
        print(row)


if __name__ == "__main__":
    main()
