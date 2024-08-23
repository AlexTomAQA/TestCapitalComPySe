"""
-*- coding: utf-8 -*-
@Time    : 2024/07/02 20:00
@Author  : Kasilà
"""

import pytest
import random


@pytest.fixture(
    scope="function",
    params=random.sample([
        "",
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
    params=[
        "Bitcoin",
        "Bitcoin Cash",
        "Bitcoin Gold",
        "Bitcoin halving",
        "Cardano",
        "Crypto vs stocks: What’s the difference?",
        "Dogecoin",
        "EOS",
        "Etherium",
        "Etherium Classic",
        "Litcoin",
        "NEO",
        "Polkadot",
        "QTUM",
        "Ripple",
        "Shiba Inu",
        "Steem",
        "Stellar",
        "TRON"
    ],
)
def sidebar_item(request):
    return request.param


@pytest.fixture(
    scope="function",
    params=random.sample([
        "",
        "de",
        "es",
        "it",
        "pl",
        "ru",
        "zh"
    ], 2),
)
def cur_language_2_rnd_from_7(request):
    print(f"\n\n\nCurrent language - {request.param}")
    return request.param

@pytest.fixture(
    scope='function',
    params=['']
)

def title_instrument(request):
    print(f"\n\n\ntitle instrument - {request.param}")
