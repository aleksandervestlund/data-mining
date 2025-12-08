from collections.abc import Iterable, Sequence

from source.recommendation.baseline_predictor import baseline_predictor


def predicted_rating1(similar_items: Sequence[float]) -> float:
    if not similar_items:
        return 0.0
    return sum(similar_items) / len(similar_items)


def predicted_rating2(
    similar_items: Sequence[float], similarities: Sequence[float]
) -> float:
    if len(similar_items) != len(similarities):
        raise ValueError(
            "Length of similar_items and similarities must be the same."
        )
    if not similar_items:
        return 0.0
    if (sim_sum := sum(similarities)) == 0.0:
        return 0.0
    return (
        sum(s_j * r_ui for s_j, r_ui in zip(similarities, similar_items))
        / sim_sum
    )


def predicted_rating3(
    ratings_u_j: Sequence[float],
    similarities: Sequence[float],
    global_average_rating: float,
    user_average_rating: float,
    item_i_average_rating: float,
    neighbor_item_averages: Iterable[float],
) -> float:
    b_ui = baseline_predictor(
        global_average_rating, user_average_rating, item_i_average_rating
    )

    if not ratings_u_j:
        return b_ui
    if (sim_sum := sum(similarities)) == 0.0:
        return b_ui

    weighted_sum = sum(
        s_j
        * (
            r_uj
            - baseline_predictor(
                global_average_rating, user_average_rating, item_average_rating
            )
        )
        for r_uj, s_j, item_average_rating in zip(
            ratings_u_j, similarities, neighbor_item_averages
        )
    )
    return b_ui + weighted_sum / sim_sum
