"""
-*- coding: utf-8 -*-
@Time    : 2024/06/19 18:00 GMT+5
@Author  : Sergey Aiidzhanov
"""

import pytest
import random


@pytest.fixture(
    params=random.sample([
        "usd",
        "doge",
        "how to trade"
        "bitcoin",
        "platform",
        "trading",
        "course",
        "1",
        "graph",
        "meta trader",
    ], 1))
def random_search_string(request):
    print(f"\n\n\nCurrent search string - {request.param}")
    return request.param


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
    ], 3),
)
def cur_language_3_rnd_from_14(request):
    return request.param
