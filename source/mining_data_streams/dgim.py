from source.mining_data_streams.utils.buckets import Bucket, Buckets


def dgim(data: int, n: int) -> int:
    """Datar-Gionis-Indyk-Motwani."""
    if n == 0:
        return 0

    buckets = Buckets()

    for timestamp, bit in enumerate(bin(data)[2:]):
        if bit == "0":
            continue

        bucket = Bucket(timestamp=timestamp, count=1)
        buckets.buckets.insert(0, bucket)
        buckets.same_sized[1].append(bucket)

        for bucket in reversed(buckets.buckets):
            if bucket.timestamp > timestamp - n:
                break

            buckets.buckets.pop()
            buckets.same_sized[bucket.count].remove(bucket)

        size = 1

        while len(buckets.same_sized[size]) > 2:
            oldest_buckets: list[Bucket] = []

            for _ in range(2):
                oldest_buckets.append(buckets.same_sized[size].pop(0))

            idx = buckets.buckets.index(oldest_buckets[0])

            for _ in range(2):
                buckets.buckets.pop(idx)

            bucket = Bucket(
                timestamp=oldest_buckets[-1].timestamp, count=size * 2
            )
            buckets.buckets.insert(idx, bucket)
            buckets.same_sized[size * 2].append(bucket)

            size *= 2

    estimate = sum(bucket.count for bucket in buckets.buckets[:-1])
    estimate += buckets.buckets[-1].count // 2
    return estimate
