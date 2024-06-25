"""
-*- coding: utf-8 -*-
@Time    : 2024/11/05 23:10 GMT+3
@Author  : Dmitry Mudrik
"""
import allure
import pytest

from pages.Elements.TradeCFDBlockStartTradingNowButton import TradeCFDBlockStartTradingNowButton
from pages.Elements.TableTradingInstrumentsSellButton import TableTradingInstrumentsSellButton
from pages.Menu.menu import MenuSection
from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.build_dynamic_arg import build_dynamic_arg_v4

count = 1


@pytest.mark.us_01_06_00
class TestCryptocurrencies:
    page_conditions = None

    @allure.step("Start test button [Start Trading Now] in Block 'Trade Cryptocurrency CFDs'")
    @pytest.mark.test_001
    def test_001_block_trade_cryptocurrency_cfds_start_trading_now_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading Now]
        Language: All. License: All,except FCA (GB country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.06", "Markets > Menu item [Cryptocurrencies]",
            ".00_001", "Testing button [Start Trading Now] on Block 'Trade Cryptocurrency CFDs'")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        cur_page_link = page_menu.open_cryptocurrencies_market_menu(d, cur_language, cur_country, link)

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
            "01.06", "Markets > Menu item [Cryptocurrencies]",
            ".00_002", "Testing button [Sell] 'numeric values' in Widget 'Trading instrument'")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        cur_page_link = page_menu.open_cryptocurrencies_market_menu(d, cur_language, cur_country, link)

        test_element = TableTradingInstrumentsSellButton(d, cur_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_link, cur_sort)
