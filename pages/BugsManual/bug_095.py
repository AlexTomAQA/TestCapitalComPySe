"""
-*- coding: utf-8 -*-
@Time    : 2024/07/13 20:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.common import Common

BLOCK_NAME = "Search field"

SEARCH_FIELD_LOCATOR = (By.CSS_SELECTOR, '#query')


class BUG_095(BasePage):
    def __init__(self, browser, link, bid):
        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}   1. Start Arrange.")
    def arrange(self):
        print(f"{datetime.now()}   1. Start Arrange.")

        #Check presenting SEARCH FIELD
        print(f"{datetime.now()}   Check presenting {BLOCK_NAME}.")
        print(f"{datetime.now()}   IS {BLOCK_NAME} present on this page? =>")
        if self.driver.find_elements(*SEARCH_FIELD_LOCATOR) == 0:
            msg = f"{BLOCK_NAME} is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*SEARCH_FIELD_LOCATOR)[0]
        )

        # Check visible SEARCH FIELD
        print(f"{datetime.now()}   IS {BLOCK_NAME} visible on this page? =>")
        if not self.element_is_visible(SEARCH_FIELD_LOCATOR, 5):
            msg = f"{BLOCK_NAME} is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} is visible on this page!\n")

        # Check clickable SEARCH FIELD
        print(f"{datetime.now()}   IS {BLOCK_NAME} clickable on this page? =>")
        if not self.element_is_clickable(SEARCH_FIELD_LOCATOR, 5):
            msg = f"{BLOCK_NAME} is NOT clickable on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} is clickable on this page!\n")

    @allure.step(f"{datetime.now()}   1. Start Arrange.")
    def act(self, ):
        print(f"{datetime.now()}   1. Start Act.")

        # Start click on SEARCH FIELD
        print(f"{datetime.now()}   Start click on {BLOCK_NAME} =>")
        self.driver.click(*SEARCH_FIELD_LOCATOR)
        print(f"{datetime.now()}   => {BLOCK_NAME} clicked!\n")

        # Start write search query
        print(f"{datetime.now()}   Start write search query in {BLOCK_NAME} =>")
        self.driver.send_keys(*SEARCH_FIELD_LOCATOR)
        print(f"{datetime.now()}   => {BLOCK_NAME} clicked!\n")


