"""
-*- coding: utf-8 -*-
@Time    : 2024/03/13 13:40
@Author  : Artem Dashkov
"""
from datetime import datetime
import allure
import pytest
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ButtonsOnPageLocators
from selenium.common.exceptions import ElementNotInteractableException
import random
import time


class BuyButtonOurMarketsTable(BasePage):
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
                if cur_country == 'gb':
                    test_element.assert_signup_pause(self.driver, cur_language, cur_item_link)
                else:
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

        print(f"{datetime.now()}   IS Our markets block present on this page? =>")
        block_our_market = self.driver.find_elements(*ButtonsOnPageLocators.OUR_MARKETS_BLOCK)
        if len(block_our_market) == 0:
            print(f"{datetime.now()}   => Our markets block is NOT present on this page\n")
            pytest.fail("Our markets block is NOT present on this page")
        print(f"{datetime.now()}   => Our markets block present on this page!\n")

        print(f"{datetime.now()}   IS Our markets block visible on this page? =>")
        if not self.element_is_visible(ButtonsOnPageLocators.OUR_MARKETS_BLOCK, 5):
            print(f"{datetime.now()}   => Our markets block is NOT visible on this page!\n")
            pytest.fail("Our markets block is NOT visible on this page!")
        print(f"{datetime.now()}   => Our markets block is visible on this page!\n")

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

        print(f"{datetime.now()}   IS MARKET '{market}' present on this page? =>")
        market_list = self.driver.find_elements(*self.market_locator)
        if len(market_list) == 0:
            print(f"{datetime.now()}   => MARKET '{market}' is NOT present on this page\n")
            pytest.fail(f"MARKET '{market}' is NOT present on this page")
        print(f"{datetime.now()}   => MARKET '{market}' present on this page!\n")

        print(f"{datetime.now()}   IS MARKET '{market}' visible on this page? =>")
        if not self.element_is_visible(self.market_locator, 5):
            print(f"{datetime.now()}   => MARKET '{market}' is NOT visible on this page!\n")
            pytest.fail(f"MARKET '{market}' is NOT visible on this page!")
        print(f"{datetime.now()}   => MARKET '{market}' is visible on this page!\n")

        print(f"{datetime.now()}   Start Click button '{market}' MARKET =>")
        self.current_market = self.driver.find_element(*self.market_locator)
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.current_market
        )

        try:
            self.current_market.click()
            print(f"{datetime.now()}   => End Click button '{market}' MARKET\n")
        except ElementNotInteractableException:
            print(f"{datetime.now()}   => Button '{market}' MARKET is NOT clicked\n")
            pytest.fail("Checking element is not clickable")

        print(f"{datetime.now()}   Is Instruments present? =>")
        self.instruments_locator = ButtonsOnPageLocators.INSTRUMENTS_OUR_MARKETS
        self.instruments_list = self.driver.find_elements(*self.instruments_locator)
        if len(self.instruments_list) == 0:
            print(f"{datetime.now()}   => Instruments is NOT present on this page\n")
            pytest.fail("Instruments is NOT present on this page")
        print(f"{datetime.now()}   => Instruments is present on this page!\n")

        print(f"{datetime.now()}   Is Instruments visible? =>")
        if not self.element_is_visible(self.instruments_locator, 5):
            print(f"{datetime.now()}   => Instruments is NOT visible on this page!\n")
            pytest.fail("Instruments is NOT visible on this page!")
        print(f"{datetime.now()}   => Instruments is visible on this page!\n")

        print(f"{datetime.now()}   => Start Find and Click button '{instrument}' instrument=>")
        arrow_right_button_locator = ButtonsOnPageLocators.BUTTON_ARROW_RIGHT
        arrow_right_button = self.driver.find_element(*arrow_right_button_locator)
        count = 0
        match instrument:
            case 'First':
                index_instrument = 0
                self.current_instrument = self.instruments_list[index_instrument]
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    self.current_instrument
                )
                self.current_instrument.click()

            case 'Last':
                index_instrument = len(self.instruments_list)-1
                self.current_instrument = self.instruments_list[index_instrument]
                status_current_instrument = self.current_instrument.get_attribute("aria-hidden")
                while status_current_instrument and count < 20:
                    arrow_right_button.click()
                    time.sleep(1)
                    status_current_instrument = self.current_instrument.get_attribute("aria-hidden")
                    count += 1

                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    self.current_instrument
                )
                self.current_instrument.click()

            case 'Middle':
                index_instrument = random.randint(2, len(self.instruments_list)-1)
                self.current_instrument = self.instruments_list[index_instrument]
                status_current_instrument = self.current_instrument.get_attribute("aria-hidden")
                while status_current_instrument and count < 20:
                    arrow_right_button.click()
                    time.sleep(1)
                    status_current_instrument = self.current_instrument.get_attribute("aria-hidden")
                    count += 1

                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    self.current_instrument
                )
                self.current_instrument.click()
        print(f"{datetime.now()}   => End Click button '{instrument}' instrument=>\n")

    @allure.step("Click button BUTTON_TRADING_BUY_IN_TABLES")
    def element_click(self, d, market, instrument):
        print(f"{datetime.now()}   2. Act for '{market}' Market and '{instrument}' Instrument")

        print(f"{datetime.now()}   IS button [Buy] for '{market}' Market and '{instrument}' Instrument"
              f"present on this page? =>")
        self.button_locator = ButtonsOnPageLocators.BUTTON_OUR_MARKETS_BUY

        if len(self.driver.find_elements(*self.button_locator)) == 0:
            print(f"{datetime.now()}   => Button [Buy] for '{market}' Market and '{instrument}' Instrument "
                  f"NOT present on this page!\n")
            pytest.fail("Button [Buy] for '{market}' Market and '{instrument}' Instrument "
                        "NOT present on this page!")
        print(f"{datetime.now()}   => Button [Buy] for '{market}' Market and '{instrument}' Instrument "
              f"present on this page!\n")

        print(f"{datetime.now()}   IS button [Buy] for '{market}' Market and '{instrument}' Instrument "
              f"visible on this page? =>")
        if not self.element_is_visible(self.button_locator, 5):
            print(f"{datetime.now()}   => Button [Buy] for '{market}' Market and '{instrument}' Instrument "
                  f"NOT visible on this page!\n")
            pytest.fail("Button [Buy] for '{market}' Market and '{instrument}' Instrument "
                        "NOT visible on this page!")
        print(f"{datetime.now()}   => Button [Buy] for '{market}' Market and '{instrument}' Instrument "
              f"visible on this page!\n")

        print(f"{datetime.now()}   Start click button [Buy] =>")
        self.button = self.driver.find_element(*self.button_locator)
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.button
        )

        self.trade_instrument = self.current_instrument.text.split('\n')[0]

        self.button.click()
        print(f"{datetime.now()}   => End Click button [Buy]")

