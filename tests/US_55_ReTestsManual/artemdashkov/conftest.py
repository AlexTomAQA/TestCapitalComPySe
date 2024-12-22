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
    ], 2),
)
def cur_language_2_rnd_from_14(request):
    print(f"\n\n\nCurrent language - {request.param}")
    return request.param


@pytest.fixture(
    scope="function",
    params=random.sample([
        ("", "bank"),
        ("ar", "بنك"),
        ("de", "bank"),
        ("es", "banco"),
        ("it", "banca"),
        ("ru", "банк"),
        ("cn", "银行"),
        ("zh", "銀行"),
        ("fr", "banque"),
        ("pl", "bank"),
        ("ro", "bancă"),
        ("nl", "bank"),
        ("el", "τράπεζα"),
        ("hu", "bank")
    ], 2),
)
def cur_language_and_query(request):
    print(f"\n\n\nCurrent language - {request.param}")
    return request.param

@pytest.fixture(
    scope="function",
    params=random.sample([
        ("GBP/USD", "EUR/USD"),
        ("EUR/USD", "GBP/USD"),
        ("Gold", "Natural Gas"),
        ("Natural Gas", "Gold"),
        ("Germany 40", "US Tech 100"),
        ("US Tech 100", "Germany 40")
    ], 1),
)
def calc_1_and_calc_2(request):
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
    ], 2),
)
def cur_language_2_rnd_from_12(request):
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
    ], 1)
)
def cur_market_1_rnd_from_5(request):
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

@pytest.fixture(
    scope="function",
    params=random.sample([
        "de",
        # "au",
        "ua"
    ], 1)
)
def cur_country_1_rnd_from_2(request):
    """Country sorting parameters"""
    print(f"\n\n\nCurrent country - {request.param}")
    return request.param

@pytest.fixture(
    scope="function",
    params=[
        ["", "gb"],
        ["", "ae"],
        ["ar", "ae"],
        ["", "au"]
    ]
)
def cur_language_country_for_fca_and_sca(request):
    """Country sorting parameters"""
    print(f"\n\n\nCurrent country - {request.param}")
    return request.param

@pytest.fixture(
    scope="function",
    params=[
        ["", "gb"],
        ["", "ae"],
        ["", "au"]
    ]
)
def cur_language_country_for_fca_sca_for_en_language(request):
    """Country sorting parameters"""
    print(f"\n\n\nCurrent country - {request.param}")
    return request.param

@pytest.fixture(
    scope="function",
    params=random.sample([
        ["", "gb"],     # FCA
        ["", "ae"],     # SCA
        ["ar", "ae"],   # SCA
        ["", "au"],     # ASIC
        ["", "eu"],     # CYSEC
        ["de", "de"],   # CYSEC
    ], 2)
)
def cur_language_country_for_fca_sca_asic_cysec_2_rnd(request):
    """Country sorting parameters"""
    print(f"\n\n\nCurrent country - {request.param}")
    return request.param
