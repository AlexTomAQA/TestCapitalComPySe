import random
from datetime import datetime

import allure
import pytest

from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import TableTradingInstrumentsLocators
from pages.base_page import BasePage


class TableTradingInstrumentsItem(BasePage):

    def __init__(self, driver, link="", bid=""):
        self.title_instrument = None
        self.buy_list = None
        self.line_list = None
        super().__init__(driver, link, bid)

    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)
        self.element_click(d, cur_item_link)
        test_element = AssertClass(self.driver, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_page_trading_instrument(
                    self.driver, cur_language, cur_item_link, self.title_instrument)
            case "NoAuth":
                test_element.assert_page_trading_instrument(
                    self.driver, cur_language, cur_item_link, self.title_instrument)
            case "Auth":
                test_element.assert_page_trading_instrument(
                    self.driver, cur_language, cur_item_link, self.title_instrument)
        self.driver.get(cur_item_link)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange for Trading instrument")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   IS TABLE_TRADING_INSTRUMENTS  present on the page? =>")
        table_list = self.driver.find_elements(*TableTradingInstrumentsLocators.TABLE_TRADING_INSTRUMENTS)
        if len(table_list) == 0:
            print(f"{datetime.now()}   => TABLE_TRADING_INSTRUMENTS is NOT present on the page!\n")
            pytest.fail(f" Bug ? Checking element is not on this page")

        print(f"{datetime.now()}   => TABLE_TRADING_INSTRUMENTS is present on the page!")

        print(f"{datetime.now()}   IS TRADING_INSTRUMENTS  present on the page? =>")
        line_list = self.driver.find_elements(*TableTradingInstrumentsLocators.LINE_TRADING_INSTRUMENT)

        if len(line_list) == 0:
            print(f"{datetime.now()}   => TRADING_INSTRUMENTS is NOT present or quantity buttons zero!\n")
            pytest.fail("Bug ? element is not on this page")

    @allure.step("Click line instrument")
    def element_click(self, d, cur_item_link):
        print(f"{datetime.now()}   2. Act for trading instrument")

        print(f"{datetime.now()}   Start click random TRADING_INSTRUMENT =>")
        self.line_list = self.driver.find_elements(*TableTradingInstrumentsLocators.LINE_TRADING_INSTRUMENT)

        value = random.randint(0, len(self.line_list) - 1)
        print(f"{datetime.now()}   => End find a random TRADING_INSTRUMENTS in TABLE_TRADING_INSTRUMENTS")

        line_instrument = self.line_list[value]
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            line_instrument
        )

        # определяем название инструмента
        instruments_list = self.driver.find_elements(*TableTradingInstrumentsLocators.ITEM_TRADING_INSTRUMENT)
        self.title_instrument = instruments_list[value].text

        line_instrument.click()
        print(f"{datetime.now()}   =>   LINE_TRADING_INSTRUMENT {value} with trading instrument "
              f"{self.title_instrument} clicked!\n")
