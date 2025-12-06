from collections.abc import Iterable, Sequence

from source.clustering.distance import Point, euclidean


def k_means(
    data: Iterable[Point], centroids: Sequence[Point]
) -> dict[Point, list[Point]]:
    if not centroids:
        raise ValueError("At least one starting centroid is required.")

    k = len(centroids)

    while True:
        clusters: dict[int, list[Point]] = {i: [] for i in range(k)}

        for point in data:
            nearest = min(
                range(k),
                key=lambda i: euclidean(point, centroids[i]),
            )
            clusters[nearest].append(point)

        new_centroids: list[Point] = []
        changed = False

        for i, points in clusters.items():
            old_centroid = centroids[i]
            new_centroid = (
                tuple(sum(coords) / len(points) for coords in zip(*points))
                if points
                else old_centroid
            )

            new_centroids.append(new_centroid)
            changed |= new_centroid != old_centroid

        if not changed:
            break

        centroids = new_centroids

    return {centroids[i]: clusters[i] for i in range(k)}
