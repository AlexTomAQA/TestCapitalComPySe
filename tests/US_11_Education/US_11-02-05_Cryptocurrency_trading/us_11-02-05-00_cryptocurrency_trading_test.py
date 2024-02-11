"""
-*- coding: utf-8 -*-
@Time    : 2023/05/23 19:00 GMT+3
@Author  : Suleyman Alirzaev
"""
import allure
# import os.path
import pytest

from pages.Elements.ButtonOnHorizontalBanner import ButtonOnHorizontalBanner
from pages.Elements.ButtonOnVerticalBanner import ButtonOnVerticalBanner
from pages.Elements.ButtonStartTradingInContent import ContentStartTrading
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.testing_elements_locators import SubPages
from pages.Menu.menu import MenuSection
from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v4

count = 1


def check_language(cur_language):
    if cur_language not in ["", "de", "es", "fr", "it", "pl", "ro", "ru", "zh", "cn"]:
        pytest.skip(f"This test is not for {cur_language} language")


def check_country(cur_country):
    if cur_country in ["gb"]:
        pytest.skip(f"This test is not for {cur_country} country")


@pytest.mark.us_11_02_05_00
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

    @allure.step("Test button [Try demo] on the Main banner")
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
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
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

    @allure.step("Test button [Trade] on widget Most traded")
    @pytest.mark.test_03
    def test_03_most_traded_widget_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Trade] on widget Most traded
        Language: All, except AR, EL, HU, NL.
        License: All, except FCA (GB country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".00_03", "Testing button [Trade] on widget Most traded")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_country_in_list_and_skip_if_present(
            cur_language, ["ar", "el", "hu", "nl"])
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_cryptocurrency_trading_menu(
            d, cur_language, cur_country, main_page_link)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link)

    @allure.step("Test button [Start trading] in the Content block")
    @pytest.mark.test_04
    def test_04_content_block_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start trading] in the Content block
        Language: All, except AR, EL, HU, NL.
        License: All, except FCA (GB country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".00_04", "Testing button [Start trading] in the Content block")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_present(cur_language, ["ar", "el", "hu", "nl"])
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_cryptocurrency_trading_menu(
            d, cur_language, cur_country, main_page_link)

        test_element = ContentStartTrading(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link)

    @allure.step("Test button on the block [Vertical banner]")
    @pytest.mark.test_05
    def test_05_block_vertical_banner_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button on the block [Vertical banner]
        Language: DE, ES, FR, PL, RO, RU, ZH. License: All,except FCA (GB country)
        For "Authorized user" role:
            The Trading platform (TP) or Demo trading platform (TPD) are opened depending on the banner:
            TP if banner from the Live mode banners list / TPD if banner from the Demo mode banners list
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".00_05", "Testing button on the block [Vertical banner]")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["de", "es", "fr", "pl", "ro", "ru", "zh"])
        Common().check_language_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_cryptocurrency_trading_menu(
            d, cur_language, cur_country, main_page_link)

        # банеры должны открываться в Demo mode for US_11.02.05.00
        banner00_ver_tpd = ["221", "505", "389"]
        # банеры должны открываться в Live mode for US_11.02.05.00
        banner00_ver_tp = ["166", "196", "292", "377", "388", "425"]
        # баннеры открываются в Demo mode for US_11.02.05.01
        banner01_ver_tpd = []
        # баннеры открываются в Live mode for US_11.02.05.01
        banner01_ver_tp = []

        test_element = ButtonOnVerticalBanner(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link,
                                        banner00_ver_tpd, banner00_ver_tp, banner01_ver_tpd, banner01_ver_tp)

    @allure.step("Test button on the block [Horizontal banner]")
    @pytest.mark.test_06
    def test_06_block_horizontal_banner_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button on the block [Horizontal banner]
        Language: DE, ES, FR, IT, PL, RO, RU, ZH. License: All,except FCA (GB country)
        For "Authorized user" role:
            The Trading platform (TP) or Demo trading platform (TPD) are opened depending on the banner:
            TP if banner from the Live mode banners list / TPD if banner from the Demo mode banners list
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".00_06", "Testing button on the block [Horizontal banner]")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["de", "es", "fr", "it", "pl", "ro", "ru", "zh"])
        Common().check_language_in_list_and_skip_if_present(cur_language, ["gb"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_cryptocurrency_trading_menu(
            d, cur_language, cur_country, main_page_link)

        # баннеры открываются в Demo mode for .00_06
        banner00_hor_tpd = ["167", "197", "252"]
        # баннеры открываются в Live mode for .00_06
        banner00_hor_tp = ["220", "291", "378", "390", "427", "428"]
        # банеры должны открываться в Demo mode for .01_06
        banner01_hor_tpd = []
        # банеры должны открываться в Live mode for .01_06
        banner01_hor_tp = []

        test_element = ButtonOnHorizontalBanner(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link,
                                        banner00_hor_tpd, banner00_hor_tp, banner01_hor_tpd, banner01_hor_tp)

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
        check_language(cur_language)
        check_country(cur_country)

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
