"""
-*- coding: utf-8 -*-
@Time    : 2024/08/24 21:00
@Author  : Artem Dashkov
"""
import allure
import time
from datetime import datetime
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.common import Common
from pages.Signup_login.signup_login import SignupLogin

# BLOCK_NAME = "[How we manage your money] link"
# LINK_LOCATOR = (By.CSS_SELECTOR, 'ul > li [href*="what-capital-does-with-your-money"]')
# LINK_LOCATOR = (By.CSS_SELECTOR, 'p ~ ul > li:nth-child(2) > a')


class BUG_265(BasePage):
    pass

    """
    @allure.step(f"{datetime.now()}   1. Start Arrange.")
    def arrange(self, d, cur_language, cur_item_link):
        global LINK_LOCATOR
        print(f"{datetime.now()}   1. Start Arrange.")

        if not self.current_page_is(cur_item_link):
            print(f"{datetime.now()}   => current_url != cur_item_link")
            self.link = cur_item_link
            time.sleep(1)
            self.open_page()
        else:
            print(f"{datetime.now()}   => current_url == cur_item_link")

        # Check presenting [How we manage your money] link
        print(f"{datetime.now()}   Check presenting {BLOCK_NAME}.")
        print(f"{datetime.now()}   IS {BLOCK_NAME} present on this page? =>")
        if len(self.driver.find_elements(*LINK_LOCATOR)) == 0:
            msg = f"{BLOCK_NAME} is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*LINK_LOCATOR)[0]
        )

        # Check visible [How we manage your money] link
        print(f"{datetime.now()}   IS {BLOCK_NAME} visible on this page? =>")
        if not self.element_is_visible(LINK_LOCATOR, 5):
            msg = f"{BLOCK_NAME} is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} is visible on this page!\n")

        # Check clickable [How we manage your money] link
        print(f"{datetime.now()}   IS {BLOCK_NAME} clickable on this page? =>")
        if not self.element_is_clickable(LINK_LOCATOR, 5):
            msg = f"{BLOCK_NAME} is NOT clickable on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} is clickable on this page!\n")
        Common.save_current_screenshot(d, f"{BLOCK_NAME} is clickable on this page!")

    @allure.step(f"{datetime.now()}   2. Start Act.")
    def act(self, d):
        print(f"{datetime.now()}   2. Start Act.")

        # Start click [How we manage your money] link
        print(f"{datetime.now()}   Start click on {BLOCK_NAME} =>")
        try:
            self.driver.find_element(*LINK_LOCATOR).click()
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

            self.driver.find_element(*LINK_LOCATOR).click()
            time.sleep(1)
            print(f"{datetime.now()}   => {BLOCK_NAME} clicked!\n")

        Common.save_current_screenshot(d, f"{BLOCK_NAME} clicked!")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d, cur_language):
        print(f"{datetime.now()}   3. Start Assert.")

        # Check opened page
        print(f"{datetime.now()}   Check 'Charges and fees' page is opened instead 'Client funds' page. ")
        print(f"{datetime.now()}   IS 'Charges and fees' page open instead 'Client funds' page? =>")
        print(f'{datetime.now()}   Current page is: {self.driver.current_url}')
        if self.current_page_url_contain_the('https://capital.com/ar-ae/ways-to-trade/fees-and-charges'):
            msg = f"'Charges and fees' page is opened instead 'Client funds' page."
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        expected_page = 'https://capital.com/ar-ae/about-us/what-capital-does-with-your-money'

        if not self.current_page_url_contain_the(expected_page):
            msg = (f"Instead 'Client funds' page opened other page. "
                   f"Expected_page is '{expected_page}', "
                   f"current page is '{self.driver.current_url}'")
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)

        print(f"{datetime.now()}   => Opened expected page 'Client funds'!\n")
        Common.save_current_screenshot(d, f"Opened expected page 'Client funds'!")
        return True
    """