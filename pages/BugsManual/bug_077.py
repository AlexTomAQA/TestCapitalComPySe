"""
-*- coding: utf-8 -*-
@Time    : 2024/07/07 23:30
@Author  : Artem Dashkov
"""

import allure
import random
from datetime import datetime
from pages.common import Common
from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

TRADING_CALCULATOR_WIDGET_LOCATOR = (By.CSS_SELECTOR, 'div#calcWrap')

DROPDOWN_LIST_LOCATOR = (By.CSS_SELECTOR, '.fieldDropdown.js-fieldDropdown')

EUR_USD_LOCATOR = (By.CSS_SELECTOR, 'li[data-sort="93810675766468"]')
GBP_USD_LOCATOR = (By.CSS_SELECTOR, 'li[data-sort="123763777688772"]')
NATURAL_GAS_LOCATOR = (By.CSS_SELECTOR, 'li[data-sort="426090820621508"]')
US_TECH_100_LOCATOR = (By.CSS_SELECTOR, 'li[data-sort="15839732013552836"]')
NVIDIA_CORP_LOCATOR = (By.CSS_SELECTOR, 'li[data-sort="16150730595456196"]')
GOLD_LOCATOR = (By.CSS_SELECTOR, 'li[data-sort="27045129890124996"]')
GERMANY_40_LOCATOR = (By.CSS_SELECTOR, 'li[data-sort="508931114652423506"]')

BLOCK_NAME = "[Trading calculator] widget"

class TradingCalculatorCFDCalculatorPage(BasePage):

    def __init__(self, browser, link, bid):
        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}   1. Start Arrange.")
    def arrange(self):
        print(f"{datetime.now()}   1. Start Arrange.")

        # Check presenting and visible widget
        print(f"{datetime.now()}   Check presenting and visible {BLOCK_NAME}")
        print(f"{datetime.now()}   IS  {BLOCK_NAME} present on this page? =>")
        if self.driver.find_elements(*TRADING_CALCULATOR_WIDGET_LOCATOR) == 0:
            msg = f"{BLOCK_NAME} is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*TRADING_CALCULATOR_WIDGET_LOCATOR)[0]
        )

        print(f"{datetime.now()}   IS {BLOCK_NAME} visible on this page? =>")
        if not self.element_is_visible(TRADING_CALCULATOR_WIDGET_LOCATOR, 5):
            msg = f"{BLOCK_NAME} widget is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} is visible on this page!\n")

        # Check presenting and visible Dropdown list
        print(f"{datetime.now()}   Check presenting and visible Dropdown list")
        print(f"{datetime.now()}   IS  [Dropdown list] present on this page? =>")
        if self.driver.find_elements(*DROPDOWN_LIST_LOCATOR) == 0:
            msg = f"[Dropdown list] is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => [Dropdown list] present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*DROPDOWN_LIST_LOCATOR)[0]
        )

        print(f"{datetime.now()}   IS [Dropdown list] visible on this page? =>")
        if not self.element_is_visible(DROPDOWN_LIST_LOCATOR, 5):
            msg = f"[Dropdown list] is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => [Dropdown list] is visible on this page!\n")

        # Check clickable Dropdown list
        print(f"{datetime.now()}   IS [Dropdown list] clickable on this page? =>")
        if not self.element_is_clickable(DROPDOWN_LIST_LOCATOR, 5):
            msg = f"[Dropdown list] is NOT clickable on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => [Dropdown list] is clickable on this page!\n")

    @allure.step(f"{datetime.now()}   2. Start Act.")
    def act(self, d, cur_language, cur_country, cur_role, cur_item_link, calc_instrument_1,
                             calc_instrument_2):
        print(f"{datetime.now()}   2. Start Act.")

        # Start open Dropdown list and choose first trading instrument
        print(f"{datetime.now()}   Start open Dropdown list and choose first trading instrument")
        first_element = list()
        match calc_instrument_1:
            case "EUR/USD":
                first_element = d.find_elements(*EUR_USD_LOCATOR)
            case "GBP/USD":
                first_element = d.find_elements(*GBP_USD_LOCATOR)
            case "Natural Gas":
                first_element = d.find_elements(*NATURAL_GAS_LOCATOR)
            case "US Tech 100":
                first_element = d.find_elements(*US_TECH_100_LOCATOR)
            case "NVIDIA Corp":
                first_element = d.find_elements(*NVIDIA_CORP_LOCATOR)
            case "Gold":
                first_element = d.find_elements(*GOLD_LOCATOR)
            case "Germany 40":
                first_element = d.find_elements(*GERMANY_40_LOCATOR)

        if len(first_element) == 0:
            Common().pytest_fail(f"Bug # ??? For Trading Instrument '{calc_instrument_1}' doesn't exist on production")

        # STOPED HERE!

        ActionChains(d) \
            .move_to_element(self.driver.find_element(*DROPDOWN_LIST_LOCATOR)) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => 'CFD Calculator' sub-menu clicked")

        del sub_menu
        return d.current_url


