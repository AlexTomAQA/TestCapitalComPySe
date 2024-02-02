"""
-*- coding: utf-8 -*-
@Time    : 2023/05/23 19:00 GMT+3
@Author  : Suleyman Alirzaev
"""
import allure
# import os.path
import pytest

from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.testing_elements_locators import SubPages
from pages.Menu.menu import MenuSection
from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v4

count = 1


@pytest.mark.us_11_02_05_pre
class TestCryptocurrencyTradingPretest:
    page_conditions = None

    def check_language(self, cur_language):
        if cur_language not in ["", "de", "es", "fr", "it", "pl", "ro", "ru", "zh", "cn"]:
            pytest.skip(f"This test is not for {cur_language} language")

    def check_country(self, cur_country):
        if cur_country in ["gb"]:
            pytest.skip(f"This test is not for {cur_country} country")

    @allure.step("Start pretest")
    def test_cryptocurrency_trading_item_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        global count

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".00_99", "Pretest")

        if count == 0:
            pytest.skip("Так надо")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        self.check_language(cur_language)
        self.check_country(cur_country)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language, cur_country)
        page_menu.sub_menu_cryptocurrency_trading_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        file_name = "tests/US_11_Education/US_11-02-05_Cryptocurrency_trading/list_of_href.txt"
        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)  # for new method

        Common().creating_file_of_hrefs("Cryptocurrency trading", list_items, file_name)

        count -= 1


@pytest.mark.us_11_02_05
class TestCryptocurrencyTrading:
    page_conditions = None

    @allure.step("Test button [Start Trading] on the Main banner")
    @pytest.mark.test_01
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading] on Main banner
        Language: All, except AR, EL, HU, NL.
        License: All, except FCA (GB country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".00_01", "Testing button [Start Trading] on the Main banner")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_present(
            cur_language, ["ar", "el", "hu", "nl"])
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_cryptocurrency_trading_menu(
            d, cur_language, cur_country, main_page_link)

        test_element = MainBannerStartTrading(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link)

    @allure.step("Test button [Try demo] on the MAin banner")
    @pytest.mark.test_02
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try demo] on the Main banner
        Language: All, except AR, EL, HU, NL.
        License: All, except FCA (GB country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05","Education > Menu item [Cryptocurrency trading]",
            ".00_02", "Testing button [Try demo] on the Main banner")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_present(
            cur_language, ["ar", "el", "hu", "nl"])
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_cryptocurrency_trading_menu(
            d, cur_language, cur_country, main_page_link)

        test_element = MainBannerTryDemo(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link)





