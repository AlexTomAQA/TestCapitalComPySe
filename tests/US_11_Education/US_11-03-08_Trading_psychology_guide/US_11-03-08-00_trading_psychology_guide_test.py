"""
-*- coding: utf-8 -*-
@Time    : 2023/09/06 18:10
@Author  : Mila Podchasova
"""
import allure
import pytest
from datetime import datetime

from pages.common import Common
from pages.Education.Trading_psychology_guide_locators import TradingPsychologyContentList
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v3
from pages.conditions import Conditions
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.BlockStepTrading import BlockStepTrading
from src.src import CapitalComPageSrc

count = 1


@pytest.mark.us_11_03_08
class TestTradingPsychologyGuideMain:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_01(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.03.08",
                             "Education > Menu item [Trading Psychology Guide]",
                             ".00_01",
                             "Testing button [Start Trading] on Main banner")

        if cur_language not in [""]:
            pytest.skip(f"Test-case not for '{cur_language}' language")

        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_trading_psychology_guide_move_focus_click(d, cur_language)
        del page_menu

        test_element = MainBannerStartTrading(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Try demo] on Main banner")
    def test_02(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.03.08",
                             "Education > Menu item [Trading Psychology Guide]",
                             ".00_02",
                             "Testing button [Try demo] on Main banner")

        if cur_language not in [""]:
            pytest.skip(f"Test-case not for '{cur_language}' language")

        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_trading_psychology_guide_move_focus_click(d, cur_language)
        del page_menu

        test_element = MainBannerTryDemo(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Trade] in Widget Most traded block")
    def test_03(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.03.08",
                             "Education > Menu item [Trading Psychology Guide]",
                             ".00_03",
                             "Testing button [Trade] in Most traded block")

        if cur_language not in [""]:
            pytest.skip(f"Test-case not for '{cur_language}' language")
        if cur_country == "gb":
            pytest.skip("This test-case not for FCA licence")

        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_trading_psychology_guide_move_focus_click(d, cur_language)
        del page_menu

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Create_verify_your_account] in block [Steps trading].")
    def test_06(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Create_verify_your_account] in block [Steps trading]
        Language: All. License: All.
        """
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.03.08",
                             "Education > Menu item [Trading Psychology Guide]",
                             ".00_06",
                             "Testing button [Create_verify_your_account] in block [Steps trading]")

        if cur_language != "":
            pytest.skip("This test-case only for english language")

        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_trading_psychology_guide_move_focus_click(d, cur_language)
        del page_menu

        test_element = BlockStepTrading(d, cur_item_link)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test_11.03.08_99 pretest")
    def test_trading_psychology_guide_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        global count

        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.03.08", "Education > Menu item [Trading Psychology Guide]",
                             ".00_99", "Pretest")

        if count == 0:
            pytest.skip('The list of "Trading psychology guide" links is already created')

        if cur_language not in [""]:
            pytest.skip(f"Test-case not for '{cur_language}' language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_trading_psychology_guide_move_focus_click(d, cur_language)
        del page_menu

        file_name = "tests/US_11_Education/US_11-03-08_Trading_psychology_guide/list_of_href.txt"
        list_items = d.find_elements(*TradingPsychologyContentList.LISTS)
        count_in = len(list_items)
        print(f"{datetime.now()}   Trading Psychology Guide page include {count_in} lists item(s)")  # for new method

        Common().creating_file_of_hrefs(list_items, file_name)

        count -= 1
