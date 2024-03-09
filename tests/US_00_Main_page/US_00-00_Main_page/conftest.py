"""
-*- coding: utf-8 -*-
@Time    : 2024/03/03 11:00
@Author  : Artem Dashkov
"""
import pytest


@pytest.fixture(
    scope="function",
    params=[
        "Most_traded",
        "Commodities",
        "Indices",
        "Shares",
        "Forex",
        "ETFs"
    ],
)
def market(request):
    """Fixture"""
    print(f"\n\n\nCurrent market - {request.param}")
    return request.param


@pytest.fixture(
    scope="function",
    params=[
        "First",
        "Last",
        "Middle"
    ],
)
def instrument(request):
    """Fixture"""
    print(f"\n\n\nCurrent instrument - {request.param}")
    return request.param
