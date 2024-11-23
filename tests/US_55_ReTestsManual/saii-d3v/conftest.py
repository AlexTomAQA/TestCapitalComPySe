"""
-*- coding: utf-8 -*-
@Time    : 2024/06/19 18:00 GMT+5
@Author  : Sergey Aiidzhanov
"""

import pytest
import random


# Bug 053
@pytest.fixture(
    params=random.sample([
        "USD",
        "$",
        "BTC",
        "1",
        "CFD",
        "Capital",
        "EUR",
    ], 1))
def random_search_string(request):
    print(f"\n\n\nCurrent search string - {request.param}")
    return request.param


# Bug 378
@pytest.fixture(
    params=[
        ('xpath', '//a[text() = "BARC"]'),
        ('xpath', '//a[text() = "HSBA"]'),
        ('xpath', '//a[text() = "LSE"]')
    ])
def bug_378_link_loc(request):
    return request.param
