def baseline_predictor(
    global_average_rating: float,
    user_average_rating: float,
    item_average_rating: float,
) -> float:
    b_u = user_average_rating - global_average_rating
    b_i = item_average_rating - global_average_rating
    return global_average_rating + b_i + b_u
