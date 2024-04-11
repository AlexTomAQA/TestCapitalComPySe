"""
-*- coding: utf-8 -*-
@Time    : 2024/04/01 10:10
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


class TradeCFDsBlock(BasePage):

    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)
        self.element_click(d)

        tabs = self.driver.window_handles
        if len(tabs) == 1:
            print(f"\n{datetime.now()}   => TradingView Site don't open in new tab")
        else:
            self.driver.switch_to.window(tabs[1])
            self.wait_for_change_url(cur_item_link, 2)

        test_element = AssertClass(d)
        test_element.assert_site_tradingview(d)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange for 'Trade CFDs on Capital.com via TradingView' block")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        # Check presenting and visible 'Trade CFDs on Capital.com via TradingView' block
        print(f"\n{datetime.now()}   IS 'Trade CFDs on Capital.com via TradingView' block present on this page? =>")
        trade_cfds_block = self.driver.find_elements(*ButtonsOnPageLocators.TRADE_CFDS_ON_CAPITAL_BLOCK)
        if len(trade_cfds_block) == 0:
            msg = "'Trade CFDs on Capital.com via TradingView' block is NOT present on this page"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => 'Trade CFDs on Capital.com via TradingView' block present on this page!")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*ButtonsOnPageLocators.TRADE_CFDS_ON_CAPITAL_BLOCK)[0]
        )

        print(f"\n{datetime.now()}   IS 'Trade CFDs on Capital.com via TradingView' block visible on this page? =>")
        if not self.element_is_visible(ButtonsOnPageLocators.TRADE_CFDS_ON_CAPITAL_BLOCK, 2):
            msg = "'Trade CFDs on Capital.com via TradingView' block is NOT visible on this page"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => 'Trade CFDs on Capital.com via TradingView' block is visible on this page!")

        # Check presenting and visible [Explore features] button in 'Trade CFDs on Capital.com via TradingView' block
        print(f"\n{datetime.now()}   IS [Explore features] button present on this page? =>")
        trade_cfds_block = self.driver.find_elements(*ButtonsOnPageLocators.EXPLORE_FEATURES_BUTTON)
        if len(trade_cfds_block) == 0:
            msg = "[Explore features] button is NOT present on this page"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => [Explore features] button present on this page!")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*ButtonsOnPageLocators.EXPLORE_FEATURES_BUTTON)[0]
        )

        print(f"\n{datetime.now()}   IS [Explore features] button visible on this page? =>")
        if not self.element_is_visible(ButtonsOnPageLocators.EXPLORE_FEATURES_BUTTON, 2):
            msg = "[Explore features] button is NOT visible on this page"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => [Explore features] button is visible on this page!")

    @allure.step("Click button [Explore features] in 'Trade CFDs on Capital.com via TradingView' block")
    def element_click(self, d):
        print(f"{datetime.now()}   2. Act for [Explore features] button "
              f"on 'Trade CFDs on Capital.com via TradingView' block ")

        # Start click button [Trade]
        print(f"{datetime.now()}   Start Click [Explore features] button =>")
        button = self.driver.find_element(*ButtonsOnPageLocators.EXPLORE_FEATURES_BUTTON)
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button
        )

        button.click()
        print(f"{datetime.now()}   => [Explore features] button clicked!\n")
