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
def cur_sort(request):
    """Параметры сортировки трейдинговых инструментов"""
    print(f"\n\n\nCurrent sort - {request.param}")
    return request.param
