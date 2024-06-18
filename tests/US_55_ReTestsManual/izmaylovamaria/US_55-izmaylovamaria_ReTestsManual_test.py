"""
-*- coding: utf-8 -*-
@Time    : 2024/05/06 22:00
@Author  : Maria Izmaylova
"""
import pytest
import allure

from pages.Elements.TradeCFDSellButton import TradeCFDSellButton
from pages.Menu.menu import MenuSection
from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55


@pytest.mark.us_55
class TestManualDetectedBugs:
    page_conditions = None

    @allure.step("The page of the trading instrument")
    @pytest.mark.parametrize('cur_language', ["de"])
    # @pytest.mark.parametrize('cur_language',
    #                          ["", "ar", "de", "el", "es", "fr", "it", "hu", "nl", "pl", "ru", "cn", "ro", "zh"])
    @pytest.mark.parametrize('cur_country', ['de', 'au', 'ae'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.parametrize('cur_market', ["Shares"])
    # @pytest.mark.parametrize('cur_market', ["Shares", "Forex", "Indices", "Commodities", "Cryptocurrencies"])
    @pytest.mark.test_010a
    def test_010a(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_market):
        """
        Check: Button [Sell] in widget [ Trading instrument]
        Language: All. License: All(except FCA).
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "Retest of manual detected bugs",
            "10a", "Testing button [Sell] on trading instrument page", False, False)

        page_conditions = Conditions(d, "")

        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = None
        match cur_market:
            case "Shares":
                cur_item_link = menu.open_shares_market_menu(d, cur_language, cur_country, link)
            case "Forex":
                cur_item_link = menu.open_forex_markets_menu(d, cur_language, cur_country, link)
            case "Indices":
                cur_item_link = menu.open_indices_markets_menu(d, cur_language, cur_country, link)
            case "Commodities":
                cur_item_link = menu.open_commodities_markets_menu(d, cur_language, cur_country, link)
            case "Cryptocurrencies":
                cur_item_link = menu.open_cryptocurrencies_market_menu(d, cur_language, cur_country, link)

        test_element = TradeCFDSellButton(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_market)

    # @allure.step("Start test of button [Buy] on trading instrument page'")
    # @pytest.mark.test_55
    # def test_010b(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_button):
    #     """
    #     Check: Button [Buy] on trading instrument page
    #     Language: All. License: All,except FCA.
    #     """
    #     bid = build_dynamic_arg_for_us_55(
    #         d, worker_id, cur_language, cur_country, cur_role,
    #         "55", "Retest of manual detected bugs",
    #         "10b", "Testing button [Buy] on trading instrument page")
    #
    #     Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
    #
    #     page_conditions = Conditions(d, "")
    #     page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     test_element = TradeCFDBuyButton(d, cur_item_link, bid)
    #     test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    # @allure.step("Start test of button [Notification] on trading instrument page")
    # @pytest.mark.test_55
    # def test_010c(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_button):
    #     """
    #     Check: Button [Notification] on trading instrument page
    #     Language: All. License: All, except FCA.
    #     """
    #
    #     bid = build_dynamic_arg_for_us_55(
    #         d, worker_id, cur_language, cur_country, cur_role,
    #         "55", "Retest of manual detected bugs",
    #         "10c", "Testing button [Notification] on trading instrument page")
    #
    #     page_conditions = Conditions(d, "")
    #     page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     test_element = PageInstrumentNotificationButton(d, cur_item_link, bid)
    #     test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)
    #
    # @allure.step("Start test_01.03.01_002 of button [View Detailed Chart] on trading instrument page'")
    # @pytest.mark.test_55
    # def test_010d(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_button):
    #     """
    #     Check: Button [View Detailed Chart] on trading instrument page
    #     Language: All. License: All (except FCA).
    #     """
    #     bid = build_dynamic_arg_for_us_55(
    #         d, worker_id, cur_language, cur_country, cur_role,
    #         "55", "Retest of manual detected bugs",
    #         "10d", "Testing button [View Detailed Chart] on trading instrument page")
    #
    #     Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
    #
    #     page_conditions = Conditions(d, "")
    #     page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     test_element = PageInstrumentViewDetailedChartButton(d, cur_item_link, bid)
    #     test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)
