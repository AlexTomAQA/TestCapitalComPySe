import time

import allure
import pytest
from selenium.common import StaleElementReferenceException

# from pages.Elements.AssertClass import AssertClass
from tests.ReTestsManual.pages.markets.markets import MarketsSection, WaysToTradeSection
from tests.ReTestsManual.pages.menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from src.src import CapitalComPageSrc


# @pytest.mark.Bugs_26012024_CCW_WEB
class TestManualBugs:
    page_conditions = None

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth", "NoAuth", "NoReg"])
    @allure.step("Bug#01: Content of the Block ""USD/CHF"" is not loaded in the ""US Dollar / Swiss Franc"" page ")
    @pytest.mark.test_01
    @pytest.mark.skip(reason="Skipped for debugging")
    def test_01(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Content of the Block ""USD/CHF"" is not loaded in the ""US Dollar / Swiss Franc"" page after clicking
        the ""USD/CHF"" trading instrument in the  ""Forex Markets"" Widget"
            1. Hover over the [Markets] menu section
            2. Click the [Forex] menu item
            3. Scroll down to the ""Forex Markets"" Widget
            4. Click USD/CHF trading instruments
            5. Scroll down to ""USD/CHF"" Block"
        """

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".01", "Content of the Block ""USD/CHF"" is not loaded in the ""US Dollar / Swiss Franc"""
                   " page after clicking")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        menu.open_markets_forex_sub_menu(d, cur_language, cur_country, link)

        # определение количества страниц
        markets_page = MarketsSection(d)
        # pagination = markets_page.elements_are_located(markets_page.MARKETS_LIST_PAGINATION)
        # qty_pages = int(pagination[-2].text)
        qty_pages = 1
        print("qty_pages=", qty_pages)

        # перебор страниц
        most_trade_instrument_list = []
        error_trade_instrument_list = []
        for i in range(qty_pages):
            print("page:", i + 1)
            most_traded_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LINK_LIST)
            for j in range(len(most_traded_list)):
                most_traded_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LINK_LIST)

                markets_page.go_to_element(most_traded_list[j])
                most_traded_instrument_name = most_traded_list[j].text
                try:
                    markets_page.element_is_clickable(most_traded_list[j]).click()
                except StaleElementReferenceException:
                    print("StaleElementReferenceException")
                    most_traded_list = markets_page.elements_are_located(
                        markets_page.MARKETS_MOST_TRADE_LINK_LIST)
                    markets_page.element_is_clickable(most_traded_list[j]).click()

                err_404 = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_INSTRUMENT_404, 1)
                if err_404:
                    error_trade_instrument_list.append(most_traded_instrument_name + ":404")
                    d.back()
                else:
                    content_list = markets_page.elements_are_located(
                        markets_page.MARKETS_MOST_TRADE_INSTRUMENT_CONTENT, 1)
                    if content_list:
                        d.back()
                    else:
                        most_trade_instrument_list.append(most_traded_instrument_name)
                        d.back()
            print("trade instrument: ", len(most_trade_instrument_list), most_trade_instrument_list)
            print("error_404: ", error_trade_instrument_list)

            pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
            if i != qty_pages - 1:
                pagination[-1].click()
            time.sleep(1)
        if len(most_trade_instrument_list) > 0:
            assert False, (f"Bug#01. Expected Result: Content of the Block is displayed. \n"
                           f"Actual Result: Content of the Block is not displayed. \n"
                           f"error_404: {error_trade_instrument_list}. \n"
                           f"trade instrument: {len(most_trade_instrument_list)} {most_trade_instrument_list}\n"
                           f"qty_pages: {qty_pages}")

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ['NoReg'])
    @allure.step("Bug#48: 404 status code is displayed on the [USD/JPY-Rate] page and switching to an ASIC license")
    @pytest.mark.test_48
    @pytest.mark.skip(reason="Skipped for debugging")
    def test_48(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        404 status code is displayed on the "USD/JPY-Rate" page and switching to an ASIC license after
        clicking the "USD/JPY" trading instrument in the "Forex Market" Widget in the "Forex" page
        (Floating bug, also open another tab in parallel with another licence(Try all three roles) )
            1. Hover over the [Markets] menu section
            2. Click the [Forex] menu item
            3. Scroll down to the "Forex Market" widget
            4. Click the "USD/JPY"  trading instrument
        """

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".48", "404 status code is displayed on the [USD/JPY-Rate] page and switching to an ASIC license")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        menu.open_markets_forex_sub_menu(d, cur_language, cur_country, link)

        # определение количества страниц
        markets_page = MarketsSection(d)
        pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
        qty_pages = int(pagination[-2].text)
        # qty_pages = 1
        print("qty_pages=", qty_pages)

        # перебор страниц
        error_trade_instrument_list = []
        for i in range(qty_pages):
            print("page:", i + 1)
            most_traded_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LINK_LIST)
            for j in range(len(most_traded_list)):
                most_traded_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LINK_LIST)

                markets_page.go_to_element(most_traded_list[j])
                most_traded_instrument_name = most_traded_list[j].text
                try:
                    markets_page.element_is_clickable(most_traded_list[j]).click()
                except StaleElementReferenceException:
                    print("StaleElementReferenceException")
                    most_traded_list = markets_page.elements_are_located(
                        markets_page.MARKETS_MOST_TRADE_LINK_LIST)
                    markets_page.element_is_clickable(most_traded_list[j]).click()

                err_404 = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_INSTRUMENT_404, 1)
                if err_404:
                    error_trade_instrument_list.append(most_traded_instrument_name + ":404")
                    print("error_404: ", error_trade_instrument_list)
                    assert False, (
                        f"Bug#48. Expected Result: Page of the corresponding trading instrument"
                        f"{error_trade_instrument_list} is opened. \n"
                        f"Actual Result: 404 status code is displayed on the {error_trade_instrument_list} "
                        f"page and switching to an ASIC license . \n"
                        f"error_404: {error_trade_instrument_list}. \n"
                        f"qty_pages: {qty_pages}")
                else:
                    d.back()

            pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
            if i != qty_pages - 1:
                pagination[-1].click()
            time.sleep(1)
            print("Non one 404 error")

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth", "NoAuth", "NoReg"])
    @allure.step('Bug#02:  "Sell"/"Buy" in the Widget "Trading instrument is not clickable')
    @pytest.mark.test_02
    @pytest.mark.skip(reason="Skipped for debugging")
    def test_02(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Page of the corresponding trading instrument is opened  after clicking [numeric values] in the
        column "Sell"/"Buy" in the Widget "Trading instrument"
        1. Hover over the [Markets] menu section
        2. Click the [Forex] menu item
        3. Scroll down to the Widget "Trading instrument"
        4. Click the  button [numeric values] in column "Sell"/"Buy"
        """

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".02", 'Sell"/"Buy" in the Widget "Trading instrument is not clickable')

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        menu.open_markets_forex_sub_menu(d, cur_language, cur_country, link)

        # определение количества страниц
        markets_page = MarketsSection(d)
        # pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
        # qty_pages = int(pagination[-2].text)
        qty_pages = 1
        print("qty_pages=", qty_pages)

        # перебор страниц
        for i in range(qty_pages):
            print("page:", i + 1)
            most_traded_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LIST)
            most_traded_link_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LINK_LIST)
            # проверяем, что ссылки для полей sell/buy существуют
            if len(most_traded_list) == len(most_traded_link_list):
                assert False, (
                    "Bug#02. Expected Result: Sign up form is opened/ unregistered Login form is opened/ unauthorized "
                    "Transition to the trading platform / authorized.\n"
                    "Actual Result: Page of the corresponding trading instrument is opened ")

            pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
            if i != qty_pages - 1:
                pagination[-1].click()
            time.sleep(1)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth", "NoAuth", "NoReg"])
    @allure.step('Bug#04:  Block "Key Stats" is not displayed to the right of the Block "Trading Condition"')
    @pytest.mark.test_04
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_04(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Block "Key Stats" is not displayed to the right of the Block "Trading Condition" after clicking any
        trading instrument in the Widget "Indices Markets""Buy"
        1. Hover over the [Markets] menu section
        2. Click the [Indices] menu item
        3. Scroll down to the Widget "Indices Markets"
        4. Click any trading instrument
        5. Scroll to Block "Trading Condition"
        """

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".04", 'Block "Key Stats" is not displayed to the right of the Block "Trading Condition"')

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        menu.open_markets_indices_sub_menu(d, cur_language, cur_country, link)

        # определение количества страниц
        markets_page = MarketsSection(d)
        # pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
        # qty_pages = int(pagination[-2].text)
        qty_pages = 1
        print("qty_pages=", qty_pages)

        # перебор страниц
        for i in range(qty_pages):
            print("page:", i + 1)
            most_traded_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LINK_LIST)
            for j in range(len(most_traded_list)):
                most_traded_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LINK_LIST)

                markets_page.go_to_element(most_traded_list[j])
                try:
                    markets_page.element_is_clickable(most_traded_list[j]).click()
                except StaleElementReferenceException:
                    print("StaleElementReferenceException")
                    most_traded_list = markets_page.elements_are_located(
                        markets_page.MARKETS_MOST_TRADE_LINK_LIST)
                    markets_page.element_is_clickable(most_traded_list[j]).click()

                key_stat_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_INSTRUMENT_KEY_STATS,
                                                                  1)
                assert len(key_stat_list) == 2, ('Bug#04. '
                                                 'Expected result: Block "Key Stats" is displayed to the right of '
                                                 'the Block "Trading Condition"'
                                                 '\n'
                                                 'Actual result: Block "Key Stats" is not displayed ')
                d.back()
            pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
            if i != qty_pages - 1:
                pagination[-1].click()
            time.sleep(1)
