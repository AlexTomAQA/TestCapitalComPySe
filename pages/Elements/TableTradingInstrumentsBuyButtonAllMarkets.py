"""
-*- coding: utf-8 -*-
@Time    : 2024/04/17 19:30
@Author  : Ivan
"""

import random
from datetime import datetime

from selenium.webdriver import ActionChains
import allure

from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.common import Common
from pages.Elements.testing_elements_locators import (
    ItemSortDropdownLocators,
    TableTradingInstrumentsLocators,
    FieldDropdownMarketsLocator,
    MarketSortAllMarketsLocators,
)
from pages.Elements.AssertClass import AssertClass

COUNT_OF_RUNS = 1


class TableTradingInstrumentsBuyButtonAllMarkets(BasePage):

    def __init__(self, browser, link, bid):
        self.item_sort = None
        self.sort_locator = None
        self.current_sort = None

        self.market_name = None
        self.current_market = None

        self.sell_locator = None
        self.sell_list = None

        self.item = None
        self.trade_instrument = ""

        super().__init__(browser, link, bid)

    @allure.step("Start Full test [Buy] button on Table Widget Trading Instruments")
    def full_test_with_tpi(
        self,
        d,
        cur_language,
        cur_country,
        cur_role,
        cur_item_link,
        cur_market,
        cur_sort,
    ):
        item_list = self.arrange_(d, cur_item_link, cur_market, cur_sort)
        print(f"\n{datetime.now()}   List of random items = {item_list}")

        for i, value in enumerate(item_list):
            self.element_click(self.driver, value, cur_market, cur_sort)
            test_element = AssertClass(self.driver, cur_item_link, self.bid)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(
                        self.driver, cur_item_link, False, True, self.trade_instrument
                    )
            self.driver.get(cur_item_link)

    def arrange_(self, d, cur_item_link, cur_market, cur_sort):
        global COUNT_OF_RUNS
        print(
            f"\n{datetime.now()}   1. Arrange for TABLE_TRADING_INSTRUMENTS and '{cur_sort}' cur_sort"
        )

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   TABLE_TRADING_INSTRUMENTS present on this page? =>")
        table_list = self.driver.find_elements(
            *MarketSortAllMarketsLocators.TABLE_TRADING_INSTRUMENTS
        )
        if len(table_list) == 0:
            print(
                f"{datetime.now()}   => TABLE_TRADING_INSTRUMENTS is NOT present on this page\n"
            )
            Common().pytest_fail("Bug # ??? Testing element is not on this page")

        print(
            f"{datetime.now()}   => TABLE_TRADING_INSTRUMENTS is present on the page!"
        )

        print(f"{datetime.now()}   IS MARKETS_LIST present on this page? =>")
        markets_list = self.driver.find_elements(*MarketSortAllMarketsLocators.ALL_TABS)
        if len(markets_list) == 0:
            print(f"{datetime.now()}   => MARKETS_LIST is NOT present on this page\n")
            Common().pytest_fail("Bug # ??? Testing element is not on this page")
        print(f"{datetime.now()}   => MARKETS_LIST is present on the page!")

        match cur_market:
            case "All":
                self.market_name = MarketSortAllMarketsLocators.ALL_MARKETS_TAB
            case "Commodities":
                self.market_name = MarketSortAllMarketsLocators.COMMODITIES_MARKET_TAB
            case "Indices":
                self.market_name = MarketSortAllMarketsLocators.INDICES_MARKET_TAB
            case "Crypto":
                self.market_name = MarketSortAllMarketsLocators.CRYPTO_MARKET_TAB
            case "Shares":
                self.market_name = MarketSortAllMarketsLocators.SHARES_MARKET_TAB
            case "Forex":
                self.market_name = MarketSortAllMarketsLocators.FOREX_MARKET_TAB

        print(f"{datetime.now()}   Start scroll and click cur_market '{cur_market}' =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            markets_list[0],
        )
        self.current_market = self.driver.find_element(*self.market_name)
        self.current_market.click()

        print(f'{datetime.now()}   => End Click cur_market "{cur_market}"')

        print(
            f"{datetime.now()}   IS FIELD_DROPDOWN_SORT present in the Live prices table? =>"
        )
        field_dropdown_list = self.driver.find_elements(
            *FieldDropdownMarketsLocator.FIELD_DROPDOWN_MARKETS
        )
        if len(field_dropdown_list) == 0:
            Common().pytest_fail(
                "Bug # ??? FIELD_DROPDOWN_SORT is not present in Live table"
            )
        print(f"{datetime.now()}   =>  FIELD_DROPDOWN_SORT is present in the table!")

        print(f"{datetime.now()}   Start scroll and click FIELD_DROPDOWN_SORT =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            field_dropdown_list[0],
        )
        field_dropdown_list[0].click()

        match cur_sort:
            case "Most traded":
                self.item_sort = ItemSortDropdownLocators.ITEM_DROPDOWN_SORT_MOST_TRADED
                self.sort_locator = (
                    FieldDropdownMarketsLocator.FIELD_DROPDOWN_MOST_TRADED
                )

            case "Top risers":
                self.item_sort = ItemSortDropdownLocators.ITEM_DROPDOWN_SORT_TOP_RISERS
                self.sort_locator = (
                    FieldDropdownMarketsLocator.FIELD_DROPDOWN_TOP_RISERS
                )

            case "Top fallers":
                self.item_sort = ItemSortDropdownLocators.ITEM_DROPDOWN_SORT_TOP_FALLERS
                self.sort_locator = (
                    FieldDropdownMarketsLocator.FIELD_DROPDOWN_TOP_FALLERS
                )

            case "Most volatile":
                self.item_sort = (
                    ItemSortDropdownLocators.ITEM_DROPDOWN_SORT_MOST_VOLATILE
                )
                self.sort_locator = (
                    FieldDropdownMarketsLocator.FIELD_DROPDOWN_MOST_VOLATILE
                )

        print(
            f"{datetime.now()}   Is item_sort_list visible on the FIELD_DROPDOWN_SORT ? =>"
        )

        item_sort_list = self.element_is_visible(
            ItemSortDropdownLocators.ALL_ITEM_DROPDOWN_SORT
        )
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            item_sort_list,
        )

        if not item_sort_list:
            print(
                f'{datetime.now()}   => cur_sort "{cur_sort}" is not visible in item_sort_list?'
            )
            Common().pytest_fail("Bug # ??? item_sort_list is not visible")
        print(
            f"{datetime.now()}   => item_sort_list is visible on the FIELD_DROPDOWN_SORT!"
        )

        print(
            f'{datetime.now()}   Is cur_sort "{cur_sort}" present in item_sort_list? =>'
        )
        if not self.driver.find_element(*self.item_sort):
            print(
                f'{datetime.now()}   => cur_sort "{cur_sort}" is not present in item_sort_list!'
            )
            Common().pytest_fail(
                f'Bug # ??? cur_sort "{cur_sort}" is not present in item_sort_list!'
            )
        print(
            f'{datetime.now()}   => cur_sort "{cur_sort}" is present in item_sort_list!'
        )
        print(f'{datetime.now()}   Start click cur_sort "{cur_sort}" =>')

        self.current_sort = self.driver.find_element(*self.item_sort)
        self.current_sort.click()

        print(f'{datetime.now()}   => End Click cur_sort "{cur_sort}"')

        print(
            f"\n{datetime.now()}   Buttons [Buy] is visible and sum buttons no zero? =>"
        )
        if (
            len(
                self.driver.find_elements(
                    *MarketSortAllMarketsLocators.BUTTON_BUY_TRADING_INSTRUMENT_ALL_MARKETS
                )
            )
            != 0
        ):
            print(
                f"{datetime.now()}   => Buttons [Buy] is visible and sum buttons no zero!\n"
            )
            print(
                f'{datetime.now()}   Start find {COUNT_OF_RUNS} random buttons [Buy] on cur_sort "{cur_sort}"=>'
            )
            self.sell_list = self.driver.find_elements(
                *MarketSortAllMarketsLocators.BUTTON_BUY_TRADING_INSTRUMENT_ALL_MARKETS
            )
            qty_buttons = len(self.sell_list)
            count_of_runs = (
                COUNT_OF_RUNS if qty_buttons >= COUNT_OF_RUNS else qty_buttons
            )
            item_list = random.sample(range(qty_buttons), count_of_runs)
            print(
                f"{datetime.now()}   => End find {count_of_runs} random buttons [Buy] on the cur_sort "
                f'"{cur_sort}"'
            )
            return item_list
        else:
            print(
                f"{datetime.now()}   => Buttons [Buy] is NOT visible or sum buttons zero!"
            )
            Common().pytest_fail("Bug # ??? element is not on this page")

    @allure.step("Click Buy button on Table Widget Trading Instruments")
    def element_click(self, wd, value, cur_market, cur_sort):
        print(
            f'{datetime.now()}   2. Act for trading instrument, "{cur_sort}" cur_sort and "{cur_market}" '
            f"cur_market"
        )

        item_list = wd.find_elements(
            *TableTradingInstrumentsLocators.ITEM_TRADING_INSTRUMENT
        )
        item = item_list[value]
        self.trade_instrument = item.text

        print(f"{datetime.now()}   Start click button [Buy] =>")
        sell_list = wd.find_elements(
            *MarketSortAllMarketsLocators.BUTTON_BUY_TRADING_INSTRUMENT_ALL_MARKETS
        )
        button = sell_list[value]
        id_instrument = button.get_attribute("data-iid")
        print(
            f"{datetime.now()}   =>   BUTTON_BUY on item with ID = '{id_instrument}' is present"
        )
        print(
            f"{datetime.now()}   BUTTON_BUY on item with ID = '{id_instrument}' scroll into view =>"
        )
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button,
        )
        print(
            f"{datetime.now()}   => BUTTON_BUY on item with ID = '{id_instrument}' scrolled into view"
        )

        print(
            f"{datetime.now()}   Check that BUTTON_BUY with item '{self.trade_instrument}' clickable =>"
        )
        time_out = 5
        button = self.element_is_clickable(
            wd.find_elements(
                *MarketSortAllMarketsLocators.BUTTON_BUY_TRADING_INSTRUMENT_ALL_MARKETS
            )[0],
            time_out,
        )
        if not button:
            print(
                f"{datetime.now()}   => BUTTON_BUY not clickable after {time_out} sec."
            )
            Common().pytest_fail(
                f"Bug # ??? Buy button not clickable after {time_out} sec."
            )
        print(f"{datetime.now()}   => BUTTON_BUY is clickable")

        ActionChains(wd).move_to_element(button).pause(0.5).click().perform()

        print(
            f"{datetime.now()}   =>   BUTTON_BUY on item '{self.trade_instrument}' clicked"
        )
