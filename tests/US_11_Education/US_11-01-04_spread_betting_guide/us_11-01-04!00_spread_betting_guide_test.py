"""
-*- coding: utf-8 -*-
@Time    : 2023/05/23 18:30 GMT+3
@Author  : Suleyman Alirzaev
"""
import pytest
import allure
from datetime import datetime

from src.src import CapitalComPageSrc
from pages.common import Common
from pages.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from pages.Menu.menu import MenuSection
from pages.Elements.testing_elements_locators import SubPages
from pages.Elements.MainBannerStartTradingButton import MainBannerStartTrading
from pages.Elements.MainBannerTryDemoButton import MainBannerTryDemo
from pages.Elements.MostTradedWidgetTradeButton import ButtonTradeOnWidgetMostTraded
from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.Elements.ContentPageStartTradingButton import ContentStartTrading
from pages.Elements.ContentBlockCreateAccountButton import ArticleCreateAccount

count = 1
cur_page_url = "?"


@pytest.mark.us_11_01_04_00
class TestSpreadBettingGuidePretest:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    @pytest.mark.test_01
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading] on Main banner
        Language: EN, ES, CN. License: FCA.
        """
        global cur_page_url

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.04", "Education > Menu item [Spread betting guide]",
            ".00_01", "Testing button [Start Trading] on Main banner")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(cur_language, ["", "es", "cn", "ru"])
        # Common().check_country_in_list_and_skip_if_not_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if d.current_url != cur_page_url or Common.flag_of_bug:
            page_menu = MenuSection(d, main_page_link)
            cur_page_url = page_menu.open_education_spread_betting_guide_menu(
                d, cur_language, cur_country, main_page_link)
            Common.flag_of_bug = False

        test_element = MainBannerStartTrading(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of button [Try demo] on Main banner")
    @pytest.mark.test_02
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try demo] on Main banner
        Language: EN, ES, CN. License: FCA.
        """
        global cur_page_url

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.04", "Education > Menu item [Spread betting guide]",
            ".00_02", "Testing button [Try demo] on Main banner")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(cur_language, ["", "es", "cn", "ru"])
        # Common().check_country_in_list_and_skip_if_not_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if d.current_url != cur_page_url or Common.flag_of_bug:
            page_menu = MenuSection(d, main_page_link)
            cur_page_url = page_menu.open_education_spread_betting_guide_menu(
                d, cur_language, cur_country, main_page_link)
            Common.flag_of_bug = False

        test_element = MainBannerTryDemo(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    @pytest.mark.test_03
    def test_03_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        global cur_page_url

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.04", "Education > Menu item [Spread betting guide]",
            ".00_03", "Testing button [Trade] in Most traded block")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(cur_language, ["", "es", "cn", "ru"])
        # Common().check_country_in_list_and_skip_if_not_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if d.current_url != cur_page_url or Common.flag_of_bug:
            page_menu = MenuSection(d, main_page_link)
            cur_page_url = page_menu.open_education_spread_betting_guide_menu(
                d, cur_language, cur_country, main_page_link)
            Common.flag_of_bug = False

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of button [Create your account] in block [Steps trading]")
    @pytest.mark.test_04
    def test_04_block_steps_trading_button_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: EN, ES, CN. License: FCA.
        """
        global cur_page_url

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.04", "Education > Menu item [Spread betting guide]",
            ".00_04", "Testing button [Create your account] in block [Steps trading]")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(cur_language, ["", "es", "cn", "ru"])
        # Common().check_country_in_list_and_skip_if_not_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if d.current_url != cur_page_url or Common.flag_of_bug:
            page_menu = MenuSection(d, main_page_link)
            cur_page_url = page_menu.open_education_spread_betting_guide_menu(
                d, cur_language, cur_country, main_page_link)
            Common.flag_of_bug = False

        test_element = BlockStepTrading(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of button [Start trading] in article")
    @pytest.mark.test_05
    def test_05_start_trading_in_article_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start trading] in article
        Language: EN, ES, CN. License: FCA.
        """
        global cur_page_url

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.04", "Education > Menu item [Spread betting guide]",
            ".00_05", "Testing button [Start trading] in article")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(cur_language, ["", "es", "cn", "ru"])
        # Common().check_country_in_list_and_skip_if_not_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if d.current_url != cur_page_url or Common.flag_of_bug:
            page_menu = MenuSection(d, main_page_link)
            cur_page_url = page_menu.open_education_spread_betting_guide_menu(
                d, cur_language, cur_country, main_page_link)
            Common.flag_of_bug = False

        test_element = ContentStartTrading(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of button [Create account] in article")
    @pytest.mark.test_06
    def test_06_create_account_in_article_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Create account] in article
        Language: EN, ES, CN. License: FCA.
        """
        global cur_page_url

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.04", "Education > Menu item [Spread betting guide]",
            ".00_06", "Testing button [Create account] in article")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(cur_language, [""])
        # Common().check_country_in_list_and_skip_if_not_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if d.current_url != cur_page_url or Common.flag_of_bug:
            page_menu = MenuSection(d, main_page_link)
            cur_page_url = page_menu.open_education_spread_betting_guide_menu(
                d, cur_language, cur_country, main_page_link)
            Common.flag_of_bug = False

        test_element = ArticleCreateAccount(d, cur_page_url, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start pretest")
    def test_99_spread_betting_guide_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        global count
        global cur_page_url

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.04", "Education > Menu item [Spread betting guide]",
            ".00_99", "Pretest for US_11.01.04.01")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(cur_language, [""])
        # Common().check_country_in_list_and_skip_if_not_present(cur_country, ["gb"])

        if count == 0:
            pytest.skip('The list of "Spread betting guide" links is already created')

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if d.current_url != cur_page_url or Common.flag_of_bug:
            page_menu = MenuSection(d, main_page_link)
            cur_page_url = page_menu.open_education_spread_betting_guide_menu(
                d, cur_language, cur_country, main_page_link)
            Common.flag_of_bug = False

        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)
        file_name = "tests/US_11_Education/US_11-01-04_spread_betting_guide/list_of_href.txt"

        Common().creating_file_of_hrefs("Spread betting guide", list_items, file_name)

        count -= 1
