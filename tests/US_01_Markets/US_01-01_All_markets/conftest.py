"""
-*- coding: utf-8 -*-
@Time    : 2024/04/16 19:30
@Author  : Ivan
"""

import pytest, random


@pytest.fixture(
    scope="function",
    params=[
        "Most traded",
        "Top risers",
        "Top fallers",
        "Most volatile"
    ],
)
def cur_sort(request):
    """Параметры сортировки трейдинговых инструментов"""
    print(f"\n\n\nCurrent sort - {request.param}")
    return request.param

@pytest.fixture(
    scope="function",
    params=random.sample([
        "Most traded",
        "Top risers",
        "Top fallers",
        "Most volatile"
    ], 1),
)
def cur_sort_all_markets(request):
    """Параметры сортировки трейдинговых инструментов"""
    print(f"\n\n\nCurrent sort - {request.param}")
    return request.param


@pytest.fixture(
    scope="function",
    params=[
        "All",
        "Commodities",
        "Indices",
        "Cryptocurrencies",
        "Shares",
        "Forex",
    ],
)
def cur_market(request):
    """Markets sorting parameters"""
    print(f"\n\n\nCurrent market - {request.param}")
    return request.param
