"""
-*- coding: utf-8 -*-
@Time    : 2024/03/22 19:10
@Author  : Artem Dashkov
"""
from datetime import datetime
import random

import allure
import pytest

from pages.Capital.capital import Capital
from pages.base_page import BasePage
from pages.common import Common
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ButtonsOnPageLocators
from selenium.common.exceptions import ElementNotInteractableException


class TradingInstrumentTradeButton(BasePage):
    def __init__(self, browser, link, bid):
        self.qty_random_buttons = 1
        self.instruments_locator = None
        self.item_list = None

        self.market_locator = None
        self.current_market = None

        self.trade_instrument = None

        super().__init__(browser, link, bid)

    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link, cur_market):
        item_list = self.arrange_(d, cur_item_link, cur_market)
        for i in item_list:
            self.element_click(d, i, cur_market)
            # test_element = AssertClass(self.driver, cur_item_link)
            test_element = AssertClass(self.driver, cur_item_link, self.bid)
            print(f"\n{datetime.now()}   1. Arrange for 'Trading instrument' widget: '{cur_market}' market")
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(self.driver, cur_language, cur_item_link)
                case "NoAuth":
                    test_element.assert_login(self.driver, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(
                        self.driver, cur_item_link, False, True)
            self.driver.get(cur_item_link)

    def arrange_(self, d, cur_item_link, cur_market):
        print(f"\n{datetime.now()}   1. Arrange for 'Trading instrument' widget: '{cur_market}' market")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        # Check presenting and visible 'Trading instrument' widget
        print(f"\n{datetime.now()}   IS 'Trading instrument' widget present on this page? =>")
        widget_trading_instrument = self.driver.find_elements(*ButtonsOnPageLocators.TRADING_INSTRUMENT_WIDGET)
        if len(widget_trading_instrument) == 0:
            msg = "'Trading instrument' widget is NOT present on this page"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => 'Trading instrument' widget present on this page!")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*ButtonsOnPageLocators.TRADING_INSTRUMENT_WIDGET)[0]
        )

        print(f"\n{datetime.now()}   IS 'Trading instrument' widget visible on this page? =>")
        if not self.element_is_visible(ButtonsOnPageLocators.TRADING_INSTRUMENT_WIDGET, 2):
            msg = "'Trading instrument' widget is NOT visible on this page"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => 'Trading instrument' widget is visible on this page!")

        # create self.market_locator for current market
        match cur_market:
            case 'Most_traded':
                self.market_locator = ButtonsOnPageLocators.MOST_TRADED_MARKET_TRADING_INSTRUMENT
            case 'Commodities':
                self.market_locator = ButtonsOnPageLocators.COMMODITIES_MARKET_TRADING_INSTRUMENT
            case 'Indices':
                self.market_locator = ButtonsOnPageLocators.INDICES_MARKET_TRADING_INSTRUMENT
            case 'Cryptocurrencies':
                self.market_locator = ButtonsOnPageLocators.CRYPTOCURRENCIES_MARKET_TRADING_INSTRUMENT
            case 'Shares':
                self.market_locator = ButtonsOnPageLocators.SHARES_MARKET_TRADING_INSTRUMENT
            case 'Forex':
                self.market_locator = ButtonsOnPageLocators.FOREX_MARKET_TRADING_INSTRUMENT
            case 'ETFs':
                self.market_locator = ButtonsOnPageLocators.ETFS_MARKET_TRADING_INSTRUMENT

        # Check presenting and visible current market Tab
        print(f"\n{datetime.now()}   IS MARKET '{cur_market}' present on this page? =>")
        market_list = self.driver.find_elements(*self.market_locator)
        if len(market_list) == 0:
            msg = f"MARKET '{cur_market}' is NOT present on this page"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => MARKET '{cur_market}' present on this page!")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            market_list[0]
        )

        print(f"\n{datetime.now()}   IS MARKET '{cur_market}' visible on this page? =>")
        if not self.element_is_visible(self.market_locator, 2):
            print(f"{datetime.now()}   => MARKET '{cur_market}' is NOT visible right now on page, "
                  f"but need to check in 'Meatballs menu'!")
            meatballs_menu = Capital(d, self.driver.current_url)
            meatballs_menu.meatballs_menu_move_focus()
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                self.driver.find_element(*self.market_locator)
            )

        if not self.element_is_visible(self.market_locator, 2):
            msg = "MARKET '{cur_market}' is NOT visible on this page"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => MARKET '{cur_market}' is visible on this page!")

        if cur_market != "Most_traded":
            # Start click Tab current market
            print(f"\n{datetime.now()}   Start Click Tab '{cur_market}' MARKET =>")
            print(f"{datetime.now()}   Check that Tab '{cur_market}' MARKET is clickable =>")
            if not self.element_is_clickable(self.driver.find_element(*self.market_locator), 2):
                msg = f"Bug # ???   Tab '{cur_market}' MARKET is NOT clickable"
                print(f"{datetime.now()}   => {msg}")
                Common().pytest_fail(msg)
            print(f"{datetime.now()}   => Tab '{cur_market}' MARKET is clickable")

            try:
                self.driver.find_element(*self.market_locator).click()
                print(f"{datetime.now()}   => End Click Tab '{cur_market}' MARKET")
            except ElementNotInteractableException:
                msg = "Tab '{cur_market}' MARKET is NOT clicked"
                print(f"{datetime.now()}   => {msg}")
                Common().pytest_fail(msg)

        # Check presenting and visible Instruments in 'Trading instrument' widget
        print(f"\n{datetime.now()}   Is Instruments present? =>")
        self.instruments_locator = ButtonsOnPageLocators.TRADE_BUTTON_TRADING_INSTRUMENT
        instruments_list = self.driver.find_elements(*self.instruments_locator)
        if len(instruments_list) == 0:
            msg = "Instruments is NOT present on this page"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => Instruments is present on this page")

        print(f"\n{datetime.now()}   Is Instruments visible? =>")
        if not self.element_is_visible(self.instruments_locator, 2):
            msg = "Instruments is NOT visible on this page"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => Instruments is visible on this page")

        # Start find random buttons [Trade]
        print(f"\n{datetime.now()}   Start find random buttons [Trade] on the TAB '{cur_market}'=>")
        qty_buttons = len(instruments_list)
        count_of_runs = qty_buttons if self.qty_random_buttons >= qty_buttons else self.qty_random_buttons
        self.item_list = random.sample(range(qty_buttons), count_of_runs)
        print(f"{datetime.now()}   => End find '{count_of_runs}' random buttons [Trade] "
              f"from list {self.item_list} on the TAB '{cur_market}'")

        return self.item_list

    @allure.step("Click button [Trade] in 'Trading instrument' widget")
    def element_click(self, d, i, cur_market):
        print(f"{datetime.now()}   2. Act for 'Trading instrument' widget and '{cur_market}' tab "
              f"{i}-item from item list {self.item_list}")

        print(f"{datetime.now()}   Start Click button TAB '{cur_market}' in METHOD: element_click =>")
        self.current_market = self.driver.find_element(*self.market_locator)

        if self.current_market.get_attribute("class") != "active js-analyticsClick":
            print(f"{datetime.now()}   IS MARKET '{cur_market}' visible on this page? =>")
            if not self.element_is_visible(self.market_locator, 2):
                meatballs_menu = Capital(d, self.driver.current_url)
                meatballs_menu.meatballs_menu_move_focus()
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    self.driver.find_element(*self.market_locator)
                )

        print(f"{datetime.now()}   Check that MARKET '{cur_market}' is visible on this page =>")
        if not self.element_is_visible(self.market_locator, 2):
            print(f"{datetime.now()}   => MARKET '{cur_market}' is NOT visible on this page!")
            Common().pytest_fail(f"Bug # ???   MARKET '{cur_market}' is NOT visible on this page!")
        print(f"{datetime.now()}   => MARKET '{cur_market}' is visible on this page!")

        # Tab current market scroll
        print(f"{datetime.now()}   Tab '{cur_market}' MARKET is scroll =>")
        self.current_market = self.driver.find_element(*self.market_locator)
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.current_market
        )
        print(f"{datetime.now()}   => Tab '{cur_market}' MARKET is scrolled")

        print(f"{datetime.now()}   Check that Tab '{cur_market}' MARKET is clickable =>")
        if not self.element_is_clickable(self.current_market, 2):
            print(f"{datetime.now()}   => Tab '{cur_market}' MARKET is NOT clickable")
            Common().pytest_fail(f"Bug # ???   Tab '{cur_market}' MARKET is NOT clickable")
        print(f"{datetime.now()}   => Tab '{cur_market}' MARKET is clickable")

        try:
            self.current_market.click()
            print(f"{datetime.now()}   => End Click Tab '{cur_market}' MARKET\n")
        except ElementNotInteractableException:
            print(f"{datetime.now()}   => Tab '{cur_market}' MARKET is NOT clicked\n")
            pytest.fail("Checking element is not clicked")

        # Start click button [Trade]
        print(f"{datetime.now()}   Start click button [Trade] =>")
        button_list = self.driver.find_elements(*self.instruments_locator)
        button = button_list[i]
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button
        )

        button.click()
        print(f"{datetime.now()}   => Button [Trade] for {i}-item clicked!\n")
