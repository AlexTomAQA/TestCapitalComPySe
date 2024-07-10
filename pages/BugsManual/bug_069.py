"""
-*- coding: utf-8 -*-
@Time    : 2024/07/10 11:00
@Author  : podchasova11
"""

from datetime import datetime

import allure

from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import MyAccountButtonLocators
from pages.base_page import BasePage
from pages.common import Common
from src.src import CapitalComPageSrc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# class CreateARiskFreeDemoAccountButton(BasePage):
#
#     def __init__(self, browser, link, bid):
#         self.search_btn = None
#
#         super().__init__(browser, link, bid)

