"""
-*- coding: utf-8 -*-
@Time    : 2023/09/06 18:10
@Author  : Mila Podchasova
"""
import pytest
import allure
from datetime import datetime

from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonStartTradingInContent import ContentStartTrading
from pages.Elements.ButtonPractiseForFreeInContentBlock import ButtonPractiseForFreeInContentBlock
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v3

count = 1


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    if "cur_item_link" in metafunc.fixturenames:
        name_file = "tests/US_11_Education/US_11-03-08_Trading_psychology_guide/list_of_href.txt"

        list_item_link = list()
        try:
            file = open(name_file, "r")
        except FileNotFoundError:
            print(f"{datetime.now()}   There is no file with name {name_file}!")
        else:
            for line in file:
                list_item_link.append(line[:-1])
            file.close()

        # if len(list_item_link) == 0:
        #     pytest.skip("Отсутствуют тестовые данные: отсутствует список ссылок на страницы")
        #
        metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_11_03_08_01
class TestTradingPsychologyGuideItem:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_01(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.03.08",
                             "Education > Menu item [Trading Psychology Guide]",
                             ".01_01",
                             "Testing button [Start Trading] on Main banner")

        if cur_language not in [""]:
            pytest.skip(f"Test-case not for '{cur_language}' language")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerStartTrading(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Try demo] on Main banner")
    def test_02(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.03.08",
                             "Education > Menu item [Trading Psychology Guide]",
                             ".01_02",
                             "Testing button [Try demo] on Main banner")

        if cur_language not in [""]:
            pytest.skip(f"Test-case not for '{cur_language}' language")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerTryDemo(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Trade] in Widget Most traded block")
    def test_03(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.03.08",
                             "Education > Menu item [Trading Psychology Guide]",
                             ".01_03",
                             "Testing button [Trade] in Most traded block")

        if cur_language not in [""]:
            pytest.skip(f"Test-case not for '{cur_language}' language")
        if cur_country == "gb":
            pytest.skip("This test-case not for FCA licence")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Start trading] in Content block")
    def test_04(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Start trading] in Content block
        Language: All. License: All.
        """
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.03.08",
                             "Education > Menu item [Trading Psychology Guide]",
                             ".01_04",
                             "Testing button [Start trading] in Content block")

        if cur_language not in [""]:
            pytest.skip(f"This test not for {cur_language} language")
        if cur_country == 'gb':
            pytest.skip("This test is not supported on UK location")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ContentStartTrading(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Practise for free] in Content block")
    def test_05(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Practise for free] in Content block
        Language: All. License: All.
        """
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.03.08",
                             "Education > Menu item [Trading Psychology Guide]",
                             ".01_05",
                             "Testing button [Practise for free] in Content block")

        if cur_language not in [""]:
            pytest.skip(f"This test not for {cur_language} language")
        if cur_country == 'gb':
            pytest.skip("This test is not supported on UK location")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonPractiseForFreeInContentBlock(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Create_verify_your_account] in block [Steps trading].")
    def test_06(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Create_verify_your_account] in block [Steps trading]
        Language: All. License: All.
        """
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.03.08",
                             "Education > Menu item [Trading Psychology Guide]",
                             ".01_06",
                             "Testing button [Create_verify_your_account] in block [Steps trading]")

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)
