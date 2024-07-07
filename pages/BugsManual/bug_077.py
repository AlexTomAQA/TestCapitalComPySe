"""
-*- coding: utf-8 -*-
@Time    : 2024/07/07 23:30
@Author  : Artem Dashkov
"""

from datetime import datetime
import random
from pages.common import Common
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TradingCalculatorCFDCalculatorPage(BasePage):

    def __init__(self, browser, link, bid):
        super().__init__(browser, link, bid)

    def arrange(self):
        pass