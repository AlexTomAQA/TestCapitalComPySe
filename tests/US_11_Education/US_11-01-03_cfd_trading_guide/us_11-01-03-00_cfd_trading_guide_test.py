"""
-*- coding: utf-8 -*-
@Time    : 2023/05/23 18:30 GMT+3
@Author  : Suleyman Alirzaev
"""
import pytest
import allure
from datetime import datetime
from pages.common import Common
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v3
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.testing_elements_locators import SubPages
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.BlockStepTrading import BlockStepTrading

count = 1
cur_page_url = ""


def check_language(cur_language, list_languages):
    if cur_language not in list_languages:
        pytest.skip(f"This test is not for '{cur_language}' language")


def check_country(cur_country, list_countries):
    if cur_country in list_countries:
        pytest.skip(f"This test is not for '{cur_country}' country")


@pytest.mark.us_11_01_03
class TestCFDTradingGuide:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        global cur_page_url
        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             ".00_01", "Testing button [Start Trading] on Main banner")

        check_language(cur_language, ["", "de", "es", "fr", "nl", "pl", "ro", "ru", "zh"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_page_url = page_menu.open_education_cfd_trading_menu(d, cur_language, main_page_link)

        test_element = MainBannerStartTrading(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of button [Try demo] on Main banner")
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        global cur_page_url

        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             ".00_02", "Testing button [Try demo] on Main banner")

        check_language(cur_language, ["", "de", "es", "fr", "nl", "pl", "ro", "ru", "zh"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_page_url = page_menu.open_education_cfd_trading_menu(d, cur_language, main_page_link)

        test_element = MainBannerTryDemo(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    def test_03_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        global cur_page_url

        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             ".00_03", "Testing button [Trade] in Most traded block")

        check_language(cur_language, ["", "de", "es", "fr", "nl", "pl", "ro", "ru", "zh"])
        check_country(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_page_url = page_menu.open_education_cfd_trading_menu(d, cur_language, main_page_link)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of button [Create your account] in block [Steps trading]")
    def test_04_block_steps_trading_button_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        global cur_page_url

        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             ".00_04", "Testing button [Create your account] in block [Steps trading]")

        check_language(cur_language, ["", "de", "es", "fr", "nl", "pl", "ro", "ru", "zh"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_page_url = page_menu.open_education_cfd_trading_menu(d, cur_language, main_page_link)

        test_element = BlockStepTrading(d, cur_page_url)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start pretest")
    def test_99(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        global count
        global cur_page_url

        build_dynamic_arg_v3(self, d, worker_id, cur_language, cur_country, cur_role,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             ".00_99", "Pretest for US_11.01.03.01")

        check_language(cur_language, ["", "de", "es", "fr", "nl", "pl", "ro", "ru", "zh"])

        if count == 0:
            pytest.skip('The list of "CFD trading guide" links is already created')

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_page_url = page_menu.open_education_cfd_trading_menu(d, cur_language, main_page_link)

        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)
        file_name = "tests/US_11_Education/US_11-01-03_cfd_trading_guide/list_of_href.txt"

        count_in = len(list_items)
        print(f"{datetime.now()}   CFD Trading include {count_in} items on selected '{cur_language}' language")

        Common().creating_file_of_hrefs(list_items, file_name)

        count -= 1
