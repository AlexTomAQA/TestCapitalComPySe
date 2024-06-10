"""
-*- coding: utf-8 -*-
@Time    : 2024/03/05 10:00
@Author  : Alexander Tomelo
"""
import pytest


@pytest.fixture(
    scope="class",
    params=[
        "NoReg",
        "Auth",
        "NoAuth",  # "Reg/NoAuth"
    ],
)
def cur_role(request):
    """Fixture"""
    # проверка аргументов командной строки
    cur_role = request.param
    print(f"Current test role - {cur_role}\n")
    return cur_role


# Language parameter
@pytest.fixture(
    scope="class",
    params=[
        "",  # "en" - 21 us
        # "es",  # 20 us
        # "de",  # 15 us
        # "it",  # 15 us
        # "ru",  # 15 us
        # "cn",  # 13 us Education to trade present, financial glossary not present
        # "zh",  # 12 us
        # "fr",  # 11 us
        # "pl",  # 10 us
        # "ro",  # 10 us
        # "ar",  # 8 us
        # "nl",  # 8 us
        # "el",  # 5 us
        # "hu",  # 5 us Magyar
    ],
)
def cur_language(request):
    """Fixture"""
    # проверка аргументов командной строки
    if request.config.getoption("lang"):
        if request.config.getoption("lang") == "en":
            language = ""
        else:
            language = request.config.getoption("lang")
    else:
        language = request.param
    print(f"Current test language - {"en" if language == "" else language}")
    return language


# Country/License parameter
@pytest.fixture(
    scope="class",
    params=[
        # "ae",  # United Arab Emirates - "SCB"
        # "au",  # Australia - "ASIC"
        "de",  # Germany  - "CYSEC"
        # "gb",  # United Kingdom - "FCA"
        #
        # "gr",  # Greece - "CYSEC"
        # "es",  # Spain - "CYSEC"
        # "fr",  # France - "CYSEC"
        # "it",  # Italy - "CYSEC"
        # "hu",  # Hungary - "CYSEC"
        # "nl",  # Netherlands - "CYSEC"
        # "pl",  # Poland - "CYSEC"
        # "ro",  # Romania - "CYSEC"
        # "tw",  # Taiwan - "SCB"
        # "hk",  # Hong Kong - "SCB"

        # # "ru" - not support
        # "NBRB" - not support
        # "SFB",
        # "FSA"
    ],
)
def cur_country(request):
    """Fixture"""
    # проверка аргументов командной строки
    if request.config.getoption("country"):
        country = request.config.getoption("country")
    else:
        country = request.param
    print(f"Current country of trading - {country}")
    return country


@pytest.fixture(
    scope="class",
    params=[
        # "test001.miketar+1@gmail.com"  # для тестирования на Github
        # "aqa.tomelo.an@gmail.com"  # для локального тестирования у Саши
        # "?"  # для локального у Миши
        # "?"  # для локального у Артема
        # "?"  # для локального у Димы
        # "?"  # для локального у Ивана
        # "?"  # для локального у Касилы
        # "?"  # для локального у Милы
        "kraynova-m-a@inbox.ru"  # для локального у Марии
    ],
)
def cur_login(request):
    """Fixture"""
    print(f"Current login - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        # "Qwer1234-!@#$"  # для тестирования на Github
        # "iT9Vgqi6d$fiZ*Z"  # для локального тестирования у Саши
        # "?"  # для локального у Миши
        # "?"  # для локального у Артема
        # "?"  # для локального у Димы
        # "?"  # для локального у Ивана
        # "?"  # для локального у Касилы
        # "?"  # для локального у Милы
        "Wbnj2509/"  # для локального у Марии
    ],
)
def cur_password(request):
    """Fixture"""
    print(f"Current password - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "Shares",
        # "Forex",
        # "Indices",
        # "Commodities",
        # "Cryptocurrencies"
    ],
)
def cur_page(request):
    """Fixture"""
    cur_page = request.param
    print(f"Current page - {cur_page}\n")
    return cur_page
