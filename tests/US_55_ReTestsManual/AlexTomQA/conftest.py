"""
-*- coding: utf-8 -*-
@Time    : 2024/07/05 16:25
@Author  : AlexTomQA
"""

import pytest
import random


@pytest.fixture(
    scope="function",
    params=random.sample([
        "",  # "en" - 21 us
        "ar",
        "de",
        "es",
        "it",
        "ru",
        "cn",
        "zh",
        "fr",
        "pl",
        "ro",
        "nl",
        "el",
        "hu",
    ], 3),
)
def cur_language_3_rnd_from_14(request):
    print(f"\n\n\nCurrent language - {request.param}")
    return request.param


@pytest.fixture(
    scope="function",
    params=random.sample([
        "",
        "ar",
        "de",
        "es",
        "fr",
        "it",
        "hu",
        "nl",
        "pl",
        "ru",
        "cn",
        "ro"
    ], 3),
)
def cur_language_3_rnd_from_12(request):
    print(f"\n\n\nCurrent language - {request.param}")
    return request.param


@pytest.fixture(
    scope="function",
    params=random.sample([
        "Shares",
        "Forex",
        "Indices",
        "Commodities",
        "Cryptocurrencies"
    ], 2)
)
def cur_market_2_rnd_from_5(request):
    """Markets sorting parameters"""
    print(f"\n\n\nCurrent market - {request.param}")
    return request.param
