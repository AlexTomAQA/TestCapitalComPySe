"""
-*- coding: utf-8 -*-
@Time    : 2024/03/03 23:12 GMT+3
@Author  : Dmitry Mudrik
"""
import allure
import pytest

from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.Elements.TableTradingInstrumentsBuyButton import TableTradingInstrumentsBuyButton
from pages.Elements.TableTradingInstrumentsSellButton import TableTradingInstrumentsSellButton
from pages.Elements.TradeCFDBlockStartTradingNowButton import TradeCFDBlockStartTradingNowButton
from pages.Elements.testing_elements_locators import SubPages
from pages.Menu.menu import MenuSection
from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.build_dynamic_arg import build_dynamic_arg_v4

count = 1


@pytest.mark.us_01_02_00
class TestShares:
    page_conditions = None

    @allure.step("Start test button [Start Trading Now] in Block 'Trade Share CFDs'")
    @pytest.mark.test_001
    def test_001_block_trade_share_cfds_start_trading_now_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading Now]
        Language: All. License: All,except FCA (GB country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.02", "Markets > Menu item [Shares]",
            ".00_001", "Testing button [Start Trading Now] on Block 'Trade Share CFDs'")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])
        # Common().check_language_in_list_and_skip_if_not_present(cur_language, [])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        cur_page_link = page_menu.open_shares_market_menu(d, cur_language, cur_country, link)

        test_element = TradeCFDBlockStartTradingNowButton(d, cur_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_link)

    @allure.step("Test button [Sell] 'numeric values' in Widget 'Trading instrument'")
    @pytest.mark.test_002
    def test_002_sell_widget_trading_instrument(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_sort):
        """
        Check: Button [Sell]'numeric values' in Widget 'Trading instrument'
        Language: All. License: All,except FCA (GB country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.02", "Markets > Menu item [Shares]",
            ".00_002", "Testing button [Sell] 'numeric values' in Widget 'Trading instrument'")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        cur_page_link = page_menu.open_shares_market_menu(d, cur_language, cur_country, link)

        test_element = TableTradingInstrumentsSellButton(d, cur_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_link, cur_sort)

    @allure.step("Test button [Buy] 'numeric values' in Widget 'Trading instrument'")
    @pytest.mark.test_003
    def test_003_buy_widget_trading_instrument(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_sort):
        """
        Check: Button [Buy]'numeric values' in Widget 'Trading instrument'
        Language: All. License: All,except FCA (GB country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.02", "Markets > Menu item [Shares]",
            ".00_003", "Testing button [Buy] 'numeric values' in Widget 'Trading instrument'")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        cur_page_link = page_menu.open_shares_market_menu(d, cur_language, cur_country, link)

        test_element = TableTradingInstrumentsBuyButton(d, cur_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_link, cur_sort)

    @allure.step("Test button [1.Create & verify your account] in Block 'Still looking for a broker you can trust?'")
    @pytest.mark.test_004
    def test_004_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [1.Create & verify your account] in block "Still looking for a broker you can trust?"
        Language: ALL.
        License: All,except FCA (GB country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.02", "Markets > Menu item [Shares]",
            ".00_004", "Testing button [1.Create & verify your account] "
                       "on Block 'Still looking for a broker you can trust?'")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        cur_page_link = page_menu.open_shares_market_menu(d, cur_language, cur_country, link)

        test_element = BlockStepTrading(d, cur_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_link)

    @allure.step("Start pretest")
    def test_099_shares_trading_instrument_pretest(
            self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password):

        global count

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.02", "Markets > Menu item [Shares]",
            ".00_099", "Pretest for US_01.02_01")

        if count == 0:
            pytest.skip("Links of hrefs already created")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.open_shares_market_menu(d, cur_language, cur_country, link)

        # Записываем ссылки в файл
        file_name = "tests/US_01_Markets/US_01-02_Shares/list_of_href.txt"
        list_items = d.find_elements(*SubPages.SUB_PAGES_MARKETS_TABLE_INSTRUMENTS_LIST)

        Common().creating_file_of_hrefs("Shares trading instrument", list_items, file_name)

        count -= 1
