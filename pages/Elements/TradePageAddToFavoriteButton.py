from datetime import datetime
import pytest
import allure
import random

from pages.base_page import BasePage
from pages.common import Common
from pages.Elements.AssertClass import AssertClass
from pages.Signup_login.signup_login import SignupLogin
from pages.Elements.testing_elements_locators import TableTradingInstrumentsLocators
from pages.Elements.testing_elements_locators import TradeCFDLocators
from pages.Elements.testing_elements_locators import TradingPlatformWatchlistTabs
from selenium.common.exceptions import ElementClickInterceptedException


class TradePageAddToFavoriteButton(BasePage):
    def __init__(self, driver, link="", bid=""):
        self.title_instrument = None
        self.line_list = None
        self.trade_instrument = None
        super().__init__(driver, link, bid)

    @allure.step(f"{datetime.now()}   Start test for [Add to favorite] Button of the trading instrument page")
    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link, cur_market):
        self.arrange_1(d, cur_item_link, cur_market)
        self.arrange_2(d, cur_item_link, cur_market)

        tab = TradingPlatformWatchlistTabs.FAVOURITES_TAB
        self.trade_instrument = self.element_click(cur_role, cur_market)
        print(f"{datetime.now()}   Trade instrument from Full test is '{self.trade_instrument}'")
        test_element = AssertClass(d, cur_item_link, self.bid)
        test_element.assert_trading_platform_v4(
                        self.driver, cur_item_link, False, True, self.trade_instrument)

    def arrange_1(self, d, cur_item_link, cur_market):
        print(f"\n{datetime.now()}   1.1. Arrange_1: for {cur_market} Market of Trading instrument")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        # IS TABLE_TRADING_INSTRUMENTS present?
        print(f"{datetime.now()}   IS TABLE_TRADING_INSTRUMENTS present on the page? =>")
        if len(self.driver.find_elements(*TableTradingInstrumentsLocators.TABLE_TRADING_INSTRUMENTS)) == 0:
            print(f"{datetime.now()}   => TABLE_TRADING_INSTRUMENTS is NOT present on the page!\n")
            Common().pytest_fail(f" Bug ? Checking element is not on this page")
        print(f"{datetime.now()}   => TABLE_TRADING_INSTRUMENTS is present on the page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*TableTradingInstrumentsLocators.TABLE_TRADING_INSTRUMENTS)[0]
        )

        # IS TABLE_TRADING_INSTRUMENTS visible?
        print(f"{datetime.now()}   IS TABLE_TRADING_INSTRUMENTS visible on the page? =>")
        if not self.element_is_visible(TableTradingInstrumentsLocators.TABLE_TRADING_INSTRUMENTS):
            print(f"{datetime.now()}   => TABLE_TRADING_INSTRUMENTS is NOT visible on the page!\n")
            Common().pytest_fail(f" Bug ? Checking element is not visible on this page")
        print(f"{datetime.now()}   => TABLE_TRADING_INSTRUMENTS is visible on the page!\n")

        # IS TRADING_INSTRUMENTS present?
        print(f"{datetime.now()}   IS TRADING_INSTRUMENTS present on the page? =>")
        if len(self.driver.find_elements(*TableTradingInstrumentsLocators.LINE_TRADING_INSTRUMENT)) == 0:
            print(f"{datetime.now()}   => TRADING_INSTRUMENTS is NOT present or quantity buttons zero!\n")
            Common().pytest_fail("Bug ? element is not on this page")
        print(f"{datetime.now()}   => TRADING_INSTRUMENTS is present on the page!\n")

        # IS TRADING_INSTRUMENTS visible?
        print(f"{datetime.now()}   IS TRADING_INSTRUMENTS visible on the page? =>")
        if not self.element_is_visible(TableTradingInstrumentsLocators.LINE_TRADING_INSTRUMENT):
            print(f"{datetime.now()}   => TRADING_INSTRUMENTS is NOT visible on the page!\n")
            Common().pytest_fail(f" Bug ? Checking element is not visible on this page")
        print(f"{datetime.now()}   => TRADING_INSTRUMENTS is visible on the page!\n")

        # Start click on random TRADING_INSTRUMENT
        print(f"{datetime.now()}   Start click on random TRADING_INSTRUMENT =>")
        self.line_list = self.driver.find_elements(*TableTradingInstrumentsLocators.LINE_TRADING_INSTRUMENT)

        value = random.randint(0, len(self.line_list) - 1)
        print(f"{datetime.now()}   => End find random value: {value} TRADING_INSTRUMENTS in TABLE_TRADING_INSTRUMENTS")

        instruments_list = self.driver.find_elements(*TableTradingInstrumentsLocators.ITEM_TRADING_INSTRUMENT_LINK)
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            instruments_list[value]
        )

        self.title_instrument = instruments_list[value].text

        time_out = 3
        if not self.element_is_clickable(instruments_list[value], time_out):
            print(f"{datetime.now()}   => {self.title_instrument} is not clickable after {time_out} sec.")
            Common().pytest_fail("Bug  ?  element is not clickable")

        instruments_list[value].click()
        print(f"{datetime.now()}   =>   TRADING_INSTRUMENT {value} with trading instrument "
              f"{self.title_instrument} clicked!\n")

        if not self.wait_for_change_url(cur_item_link, time_out):
            print(f"{datetime.now()}   => Page with TRADING_INSTRUMENTS didn't change after {time_out} sec.")
        print(f"{datetime.now()}   => Page with TRADING_INSTRUMENTS changed.\n")

        del self.line_list

    def arrange_2(self, d, cur_item_link, cur_market):
        print(f"\n{datetime.now()}   1.2. Arrange_2. For Market: '{cur_market}' and Instrument: '{self.title_instrument}'.")

        # IS BUTTON_ADD_TO_FAVOURITE present?
        print(f"{datetime.now()}   BUTTON_ADD_TO_FAVOURITE is present on the page? =>")
        if len(self.driver.find_elements(*TradeCFDLocators.ADD_TO_FAVORITE_BUTTON)) == 0:
            print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE is NOT present on the page!\n")
            Common().pytest_fail(f" Bug ? Checking element is not on this page")
        print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE is present on the page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*TradeCFDLocators.ADD_TO_FAVORITE_BUTTON)[0]
        )

        # IS BUTTON_ADD_TO_FAVOURITE visible?
        print(f"{datetime.now()}   IS BUTTON_ADD_TO_FAVOURITE visible on the page? =>")
        if not self.element_is_visible(TradeCFDLocators.ADD_TO_FAVORITE_BUTTON):
            print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE is NOT visible on the page!\n")
            Common().pytest_fail(f" Bug ? Checking element is not visible on this page")
        print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE is visible on the page!\n")

        # IS BUTTON_ADD_TO_FAVOURITE clickable?
        print(f"{datetime.now()}   IS BUTTON_ADD_TO_FAVOURITE clickable on the page? =>")
        if not self.element_is_clickable(TradeCFDLocators.ADD_TO_FAVORITE_BUTTON):
            print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE is NOT clickable on the page!\n")
            Common().pytest_fail(f" Bug ? Checking element is not clickable on this page")
        print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE is clickable on the page!\n")

    @allure.step("Click button [Add to favourite]")
    def element_click(self, cur_role, cur_market):
        print(f"\n{datetime.now()}   2. Act. For Market: '{cur_market}' and Instrument: '{self.title_instrument}'.")
        button_list = self.driver.find_elements(*TradeCFDLocators.ADD_TO_FAVORITE_BUTTON)

        trade_instrument = self.driver.find_element(*TradeCFDLocators.ITEM_NAME).text.split(' Spot')[0]

        print(f"{datetime.now()}   BUTTON_ADD_TO_FAVOURITE is clickable? =>")
        if not self.element_is_clickable(button_list[0], 5):
            print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE is not clickable more then 5 sec.")
            pytest.fail("BUTTON_ADD_TO_FAVOURITE is not clickable more then 5 sec.")

        try:
            print(f"{datetime.now()}   BUTTON_ADD_TO_FAVOURITE CLICK =>")
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE clicked!\n")

        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE NOT CLICKED")

            print(f"{datetime.now()}   'Sign up' form or page is auto opened")

            page_ = SignupLogin(self.driver)
            if page_.close_signup_form():
                pass
            elif page_.close_login_form():
                pass
            elif page_.close_signup_page():
                pass
            else:
                page_.close_login_page()

            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE clicked!")
            del page_

        del button_list
        print(f'{datetime.now()}   Trade instrument from element click is {trade_instrument}')
        return trade_instrument
