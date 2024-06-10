"""
-*- coding: utf-8 -*-
@Time    : 2024/06/09 20:30
@Author  : Maria Izmaylova
"""

import pytest
import random

@pytest.fixture(
    scope="class",
    params=[
        "Shares",
        "Forex",
        "Indices",
        "Commodities",
        "Cryptocurrencies"],
)
def cur_market(request):
    """Fixture"""
    market = request.config.getoption("market") or request.param
    print(f"Current market of trading - {market}")
    return market

#
# def test_market_trading(cur_market):
#     print(f"Testing trading in market: {cur_market}")
#     assert cur_market in ["Shares", "Forex", "Indices", "Commodities", "Cryptocurrencies"]
#
