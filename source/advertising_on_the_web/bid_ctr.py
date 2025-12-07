def compute_bid_ctr(bid: float, click_through_rate: float) -> float:
    if bid == 0:
        return 0.0
    return bid * click_through_rate
