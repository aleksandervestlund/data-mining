def compute_array_idx(i: int, j: int, n: int) -> int:
    return (i - 1) * (n - i // 2) + j - i - 1