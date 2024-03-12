import pytest


@pytest.fixture(
    scope="function",
    params=[
        "most_traded",
        "top_risers",
        "top_fallers",
        "most_volatile"
    ],
)
def cur_sort(request):
    """Параметры сортировки трейдинговых инструментов"""
    print(f"\n\n\nCurrent sort - {request.param}")
    return request.param
