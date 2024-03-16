"""
-*- coding: utf-8 -*-
@Time    : 2024/14/03 12:43
@Author  : podchasova11
"""
import pytest


@pytest.fixture(
    scope="function",
    params=[
        "Most traded",
        "Top risers",
        "Top fallers",
        "Most volatile"
    ],
)
def sorting(request):
    """Fixture"""
    print(f"\n\n\nCurrent sorting - {request.param}")
    return request.param
