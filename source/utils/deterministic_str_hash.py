import hashlib


def deterministic_str_hash(value: str, bits: int) -> int:
    digest = hashlib.sha256(value.encode("utf-8")).digest()
    return int.from_bytes(digest) & (2**bits - 1)
