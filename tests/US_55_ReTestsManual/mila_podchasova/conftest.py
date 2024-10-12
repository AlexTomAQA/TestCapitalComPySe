import pytest


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
