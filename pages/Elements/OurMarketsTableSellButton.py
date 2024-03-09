"""
-*- coding: utf-8 -*-
@Time    : 2024/03/03 11:00
@Author  : Artem Dashkov
"""
from datetime import datetime
import allure
import pytest
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ButtonsOnPageLocators
from selenium.common.exceptions import NoSuchElementException
import time

class SellButtonOurMarketsTable(BasePage):
    def __init__(self, browser, link, bid):
        self.instruments_locator = None
        self.instruments_list = None
        self.current_instrument = None

        self.market_locator = None
        self.current_market = None

        self.button_locator = None
        self.button = None

        self.trade_instrument = None

        super().__init__(browser, link, bid)

    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link, market, instrument):
        self.arrange_(d, cur_item_link, market, instrument)
        self.element_click(d,  market, instrument)
        test_element = AssertClass(self.driver, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(self.driver, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(self.driver, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(
                    self.driver, cur_item_link, False, True, self.trade_instrument)
        self.driver.get(cur_item_link)

    def arrange_(self, d, cur_item_link, market, instrument):
        print(f"\n{datetime.now()}   1. Arrange for Our Markets block: '{market}' market, '{instrument}' instrument")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   IS Our markets block visible on the page? =>")
        try:
            self.driver.find_element(*ButtonsOnPageLocators.OUR_MARKETS_BLOCK)
            print(f"{datetime.now()}   => Our markets block is visible on the page!\n")

            match market:
                case 'Most_traded':
                    self.market_locator = ButtonsOnPageLocators.MOST_TRADED_MARKET
                case 'Commodities':
                    self.market_locator = ButtonsOnPageLocators.COMMODITIES_MARKET
                case 'Indices':
                    self.market_locator = ButtonsOnPageLocators.INDICES_MARKET
                case 'Shares':
                    self.market_locator = ButtonsOnPageLocators.SHARES_MARKET
                case 'Forex':
                    self.market_locator = ButtonsOnPageLocators.FOREX_MARKET
                case 'ETFs':
                    self.market_locator = ButtonsOnPageLocators.ETFS_MARKET

            print(f"{datetime.now()}   IS MARKET '{market}' visible on the page? =>")
            if self.driver.find_element(*self.market_locator):
                print(f"{datetime.now()}   => MARKET '{market}' is visible on the page!\n")

                print(f"{datetime.now()}   Start Click button '{market}' MARKET =>")
                self.current_market = self.driver.find_element(*self.market_locator)
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    self.current_market
                )

                self.current_market.click()
                print(f"{datetime.now()}   => End Click button '{market}' MARKET\n")

                print(f"{datetime.now()}   Instruments is visible and quantity not zero? =>")
                self.instruments_locator = ButtonsOnPageLocators.INSTRUMENTS_OUR_MARKETS
                time.sleep(1)
                self.instruments_list = self.driver.find_elements(*self.instruments_locator)
                len_instruments_list = len(self.instruments_list)
                if len_instruments_list != 0:
                    print(f"{datetime.now()}   => Instruments is visible and quantity buttons not zero!\n")
                    match instrument:
                        case 'First':
                            self.current_instrument = self.instruments_list[0]
                            self.driver.execute_script(
                                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                                self.current_instrument
                            )
                            self.current_instrument.click()

                        case 'Last':
                            arrow_right_button_locator = ButtonsOnPageLocators.BUTTON_ARROW_RIGHT
                            arrow_right_button = self.driver.find_element(*arrow_right_button_locator)
                            status_arrow_right = arrow_right_button.get_attribute("disabled")
                            count = 0
                            while status_arrow_right == None and count != 20:
                                arrow_right_button.click()
                                time.sleep(1)
                                status_arrow_right = arrow_right_button.get_attribute("disabled")
                                count += 1

                            self.instruments_list = self.driver.find_elements(*self.instruments_locator)
                            self.current_instrument = self.instruments_list[len_instruments_list-1]
                            self.driver.execute_script(
                                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                                self.current_instrument
                            )
                            self.current_instrument.click()

                        case 'Middle':
                            pass

                else:
                    print(f"{datetime.now()}   => Instruments is NOT visible or quantity Instruments zero!\n")
                    pytest.fail("Checking element is not on this page")

            else:
                print(f"{datetime.now()}   => MARKET '{market}' is NOT visible on the page!\n")
                pytest.fail("Checking element is not on this page")

        except NoSuchElementException:
            print(f"{datetime.now()}   => Our markets block is NOT visible on the page!\n")
            pytest.fail("Checking element is not on this page")

    @allure.step("Click button BUTTON_TRADING_SELL_IN_TABLES")
    def element_click(self, d, market, instrument):
        print(f"{datetime.now()}   2. Act for '{market}' Market and '{instrument}' Instrument")

        print(f"{datetime.now()}   IS button [Sell] for '{market}' Market visible on the page? =>")
        self.button_locator = ButtonsOnPageLocators.BUTTON_OUR_MARKETS_SELL
        if self.driver.find_element(*self.button_locator):
            print(f"{datetime.now()}   => Button [Sell] for '{market}' Market is visible on the page!\n")

            print(f"{datetime.now()}   Start click button [Sell] =>")
            self.button = self.driver.find_element(*self.button_locator)
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                self.button
            )

            self.trade_instrument = self.current_instrument.text.split('\n')[0]

            self.button.click()
            print(f"{datetime.now()}   => End Click button [Sell]")
        else:
            print(f"{datetime.now()}   => Button [Sell] for '{market}' Market is NOT visible on the page!\n")
            pytest.fail("Checking element is not on this page")
