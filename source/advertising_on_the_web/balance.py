from collections.abc import Iterable, Mapping

import numpy as np


def ypsilon(bid: float, spent: float, budget: float) -> float:
    fraction_left = 1.0 - spent / budget
    return bid * (1 - np.exp(-fraction_left))


def balance(
    advertisers: Iterable[tuple[str, float, Mapping[str, float]]],
    query_keywords: Iterable[str],
) -> tuple[float, list[str | None]]:
    revenue = 0.0
    order: list[str | None] = []
    amount_spent = {advertiser: 0.0 for advertiser, _, _ in advertisers}

    for query_keyword in query_keywords:
        best_advertiser: str | None = None
        best_bid = 0.0
        best_ypsilon = -float("inf")

        for advertiser, budget, bids in advertisers:
            if (bid := bids.get(query_keyword, 0.0)) == 0.0:
                continue

            spent = amount_spent[advertiser]

            if spent + bid > budget:
                continue
            if (current_ypsilon := ypsilon(bid, spent, budget)) < best_ypsilon:
                continue
            if (
                current_ypsilon == best_ypsilon
                and bid <= best_bid
                and best_advertiser is not None
                and advertiser >= best_advertiser
            ):
                continue

            best_ypsilon = current_ypsilon
            best_advertiser = advertiser
            best_bid = bid

        if best_advertiser is None:
            order.append(None)
        else:
            order.append(best_advertiser)
            amount_spent[best_advertiser] += best_bid
            revenue += best_bid

    return revenue, order
