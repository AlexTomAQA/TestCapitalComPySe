"""
-*- coding: utf-8 -*-
@Time    : 2024/06/22 19:00 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime

from pages.common import Common
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass


BUTTON_NAME = "[Search] Button"
BUTTON_LOCATOR = ("id", "headerSearch")


class SearchField(BasePage):
    def __init__(self, browser, link, bid):
        self.search_btn = self.driver.find_element(*BUTTON_LOCATOR)

        super().__init__(browser, link, bid)

    def open_search_page(self, search_str):
        self.search_btn.click()
        self.search_btn.send_keys(search_str)
        self.search_btn.submit()

    # def arrange_(self, link):
    #     print(f"\n{datetime.now()}   1. Arrange_v0")
    #
    #     # Check that present and visible button
    #     print(f"{datetime.now()}   IS {BUTTON_NAME} button present on this page? =>")
    #     self.button_platform_overview = self.driver.find_elements(*BUTTON_LOCATOR)
    #     if len(self.button_platform_overview) == 0:
    #         msg = f"{BUTTON_NAME} button is NOT present on this page"
    #         print(f"{datetime.now()}   => {msg}\n")
    #         Common().pytest_fail(msg)
    #     print(f"{datetime.now()}   => {BUTTON_NAME} button present on this page!\n")
    #
    #     self.driver.execute_script(
    #         'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
    #         self.driver.find_elements(*BUTTON_LOCATOR)[0]
    #     )
    #
    #     print(f"{datetime.now()}   IS {BUTTON_NAME} button visible on this page? =>")
    #     if not self.element_is_visible(BUTTON_LOCATOR, 5):
    #         msg = f"{BUTTON_NAME} button is NOT visible on this page!"
    #         print(f"{datetime.now()}   => {msg}\n")
    #         Common().pytest_fail(msg)
    #     print(f"{datetime.now()}   => {BUTTON_NAME} button is visible on this page!\n")
    #
    #     print(f"{datetime.now()}   {BUTTON_NAME} button scroll =>")
    #     self.driver.execute_script(
    #         'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
    #         self.button_platform_overview[0]
    #     )
