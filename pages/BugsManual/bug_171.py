"""
-*- coding: utf-8 -*-
@Time    : 2024/07/13 20:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.common import Common

BLOCK_NAME = "Search field"

SEARCH_FIELD_LOCATOR = (By.CSS_SELECTOR, '#query')


class BUG_171(BasePage):
    def __init__(self, browser, link, bid):
        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}   1. Start Arrange.")
    def arrange(self, d):
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

    @allure.step(f"{datetime.now()}   2. Start Act.")
    def act(self, d, search_query):
        print(f"{datetime.now()}   2. Start Act.")

        # Start click on SEARCH FIELD
        print(f"{datetime.now()}   Start click on {BLOCK_NAME} =>")
        try:
            self.driver.find_element(*SEARCH_FIELD_LOCATOR).click()
            print(f"{datetime.now()}   => {BLOCK_NAME} clicked!\n")

        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => {BLOCK_NAME} NOT CLICKED")

            print(f"{datetime.now()}   'Sign up' form or page is auto opened")

            page_ = SignupLogin(self.driver)
            if page_.close_signup_form():
                pass
            elif page_.close_login_form():
                pass
            elif page_.close_signup_page():
                pass
            else:
                page_.close_login_page()

        self.driver.find_element(*SEARCH_FIELD_LOCATOR).click()
        print(f"{datetime.now()}   => {BLOCK_NAME} clicked!\n")

        # Start write search query
        print(f"{datetime.now()}   Start write search query in {BLOCK_NAME} =>")
        self.driver.find_element(*SEARCH_FIELD_LOCATOR).send_keys(search_query)
        Common.save_current_screenshot(d, f"Put search_query: '{search_query}' in Search field!")
        print(f"{datetime.now()}   => Put search_query: '{search_query}' in Search field!\n")

        # Press Enter
        self.driver.find_element(*SEARCH_FIELD_LOCATOR).send_keys(Keys.ENTER)
        print(f"{datetime.now()}   => Key 'Enter' pressed!\n")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d, cur_item_link):
        print(f"{datetime.now()}   3. Start Assert.")
        if self.driver.current_url == cur_item_link:
            msg = f"Item link didn't change. Search options doesn't work properly!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        Common.save_current_screenshot(d, "Item link change. Need to analyze result.")
        print(f"{datetime.now()}   => Item link change. But need to analyze result.\n")
        return True
