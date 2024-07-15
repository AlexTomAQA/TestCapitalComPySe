"""
-*- coding: utf-8 -*-
@Time    : 2024/06/09 20:30
@Author  : Artem
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

@pytest.fixture(
    scope="function",
    params=random.sample([
        "bitcoin",
        "bank",
        "trader",
        "USD",
        "Still looking for a broker you can trust",
        "+49 3046690292",
        "contact",
        "capital.com",
        " ",
        "#$%^*()_%"
    ], 2)
)
def cur_search_query_2_rnd_from_10(request):
    """Markets sorting parameters"""
    print(f"\n\n\nCurrent market - {request.param}")
    return request.param

# @pytest.fixture(
#     scope="function",
#     params=[
#         "EUR/USD",
#         "GBP/USD",
#         "Natural Gas",
#         "US Tech 100",
#         "NVIDIA Corp",
#         "Gold",
#         "Germany 40",
#     ],
# )
# def calc_instrument_1(request):
#     """Fixture - Trading calculator Instrument 1"""
#     print(f"\n\n\nCurrent instrument_1 - {request.param}")
#     return request.param
#
# @pytest.fixture(
#     scope="function",
#     params=[
#         "EUR/USD",
#         "GBP/USD",
#         "Natural Gas",
#         "US Tech 100",
#         "NVIDIA Corp",
#         "Gold",
#         "Germany 40",
#     ],
# )
# def calc_instrument_2(request, calc_instrument_1):
#     """Fixture - Trading calculator Instrument 2"""
#     if calc_instrument_1 == request.param:
#
#     print(f"\n\n\nCurrent instrument_2 - {request.param}")
#     return request.param
