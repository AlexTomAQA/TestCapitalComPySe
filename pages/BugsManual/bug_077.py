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
from selenium.webdriver.common.by import By

TRADING_CALCULATOR_WIDGET_LOCATOR = (By.CSS_SELECTOR, 'div#calcWrap')
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
        trading_calculator_widget = self.driver.find_elements(*TRADING_CALCULATOR_WIDGET_LOCATOR)
        if len(trading_calculator_widget) == 0:
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
