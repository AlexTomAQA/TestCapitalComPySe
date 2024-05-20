import random
from datetime import datetime

import allure
import pytest
from selenium.common import ElementClickInterceptedException

from conf import QTY_LINKS
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import TableTradingInstrumentsLocators, MarketSortAllMarketsLocators
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.common import Common


class TableTradingInstrumentsItemAllMarkets(BasePage):

    def __init__(self, driver, link="", bid=""):
        self.title_instrument = None
        self.buy_list = None
        self.line_list = None
        self.market_name = None
        self.current_market = None
        super().__init__(driver, link, bid)

    def full_test(self, d, cur_language, cur_country, cur_link, cur_item_link, cur_market):
        self.arrange_(d, cur_item_link, cur_market)

        for i in range(QTY_LINKS + 1):
            self.element_click(d, cur_item_link)
            self.open_page()

            test_element = AssertClass(self.driver, cur_link)
            test_element.assert_page_trading_instrument(d, cur_language, cur_link, self.title_instrument)
            self.driver.back()

    def arrange_(self, d, cur_item_link, cur_market):
        print(f"\n{datetime.now()}   1. Arrange for Trading instrument")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   IS MARKETS_LIST present on this page? =>")

        markets_list = self.driver.find_elements(*MarketSortAllMarketsLocators.ALL_TABS)

        print(f"{datetime.now()}   Start scroll to markets list =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            markets_list[0])

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
            case "Cryptocurrencies":
                self.market_name = MarketSortAllMarketsLocators.CRYPTO_MARKET_TAB
            case "Shares":
                self.market_name = MarketSortAllMarketsLocators.SHARES_MARKET_TAB
            case "Forex":
                self.market_name = MarketSortAllMarketsLocators.FOREX_MARKET_TAB

        print(f"{datetime.now()}   Start scroll and click cur_market '{cur_market}' =>")
        self.current_market = self.driver.find_element(*self.market_name)
        self.current_market.click()
        print(f'{datetime.now()}   => End Click cur_market "{cur_market}"')

        print(f"{datetime.now()}   IS TABLE_TRADING_INSTRUMENTS  present on the page? =>")
        table_list = self.driver.find_elements(*MarketSortAllMarketsLocators.TABLE_TRADING_INSTRUMENTS)
        if len(table_list) == 0:
            print(f"{datetime.now()}   => TABLE_TRADING_INSTRUMENTS is NOT present on the page!\n")
            Common().pytest_fail(f" Bug ? Checking element is not on this page")

        print(f"{datetime.now()}   => TABLE_TRADING_INSTRUMENTS is present on the page!")

        print(f"{datetime.now()}   IS TRADING_INSTRUMENTS  present on the page? =>")
        line_list = self.driver.find_elements(*TableTradingInstrumentsLocators.LINE_TRADING_INSTRUMENT)

        if len(line_list) == 0:
            print(f"{datetime.now()}   => TRADING_INSTRUMENTS is NOT present or quantity buttons zero!\n")
            Common().pytest_fail("Bug ? element is not on this page")

    @allure.step("Click line instrument")
    def element_click(self, d, cur_item_link):
        print(f"{datetime.now()}   2. Act for trading instrument")

        print(f"{datetime.now()}   Start click random TRADING_INSTRUMENT =>")
        self.line_list = self.driver.find_elements(*TableTradingInstrumentsLocators.LINE_TRADING_INSTRUMENT)

        value = random.randint(0, len(self.line_list) - 1)
        print(f"{datetime.now()}   => End find a random TRADING_INSTRUMENTS in TABLE_TRADING_INSTRUMENTS")

        instruments_list = self.driver.find_elements(*TableTradingInstrumentsLocators.ITEM_TRADING_INSTRUMENT_LINK)
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            instruments_list[value]
        )

        time_out = 3
        if not self.element_is_clickable(instruments_list[value], time_out):
            print(f"{datetime.now()}   => {self.title_instrument} is not clickable after {time_out} sec.")
            Common().pytest_fail("Bug  ?  element is not clickable")

        # определяем название инструмента
        self.title_instrument = instruments_list[value].text

        try:
            self.driver.execute_script("arguments[0].click();", instruments_list[value])
        except ElementClickInterceptedException:
            page_ = SignupLogin(self.driver)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()

        instruments_list[value].click()
        print(f"{datetime.now()}   =>   TRADING_INSTRUMENT {value} with trading instrument "
              f"{self.title_instrument} clicked!\n")

        del self.line_list
