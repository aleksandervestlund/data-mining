from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class Bucket:
    timestamp: int
    count: int


@dataclass
class Buckets:
    buckets: list[Bucket] = field(default_factory=list)
    same_sized: defaultdict[int, list[Bucket]] = field(
        default_factory=lambda: defaultdict(list)
    )
