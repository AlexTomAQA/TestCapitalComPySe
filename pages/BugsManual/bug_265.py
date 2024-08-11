"""
-*- coding: utf-8 -*-
@Time    : 2024/08/07 21:00
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

BUTTON_NAME = "[Open an account] button"
BUTTON_LOCATOR = (By.CSS_SELECTOR, '[data-type="banner_in_body_block_btn1_custom"]')
MESSAGE_404_LOCATOR = (By.XPATH, '//p[text()="404"]')


class BUG_265(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange.")
    def arrange(self, d, cur_language, cur_item_link):
        global BUTTON_LOCATOR
        print(f"{datetime.now()}   1. Start Arrange.")

        if not self.current_page_is(cur_item_link):
            print(f"{datetime.now()}   => current_url != cur_item_link")
            self.link = cur_item_link
            time.sleep(1)
            self.open_page()
        else:
            print(f"{datetime.now()}   => current_url == cur_item_link")

        # Check presenting [Open an account] button
        print(f"{datetime.now()}   Check presenting {BUTTON_NAME}.")
        print(f"{datetime.now()}   IS {BUTTON_NAME} present on this page? =>")
        if len(self.driver.find_elements(*BUTTON_LOCATOR)) == 0:
            msg = f"{BUTTON_NAME} is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*BUTTON_LOCATOR)[0]
        )

        # Check visible [Open an account] button
        print(f"{datetime.now()}   IS {BUTTON_NAME} visible on this page? =>")
        if not self.element_is_visible(BUTTON_LOCATOR, 5):
            msg = f"{BUTTON_NAME} is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} is visible on this page!\n")

        # Check clickable [Open an account] button
        print(f"{datetime.now()}   IS {BUTTON_NAME} clickable on this page? =>")
        if not self.element_is_clickable(BUTTON_LOCATOR, 5):
            msg = f"{BUTTON_NAME} is NOT clickable on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} is clickable on this page!\n")
        Common.save_current_screenshot(d, f"{BUTTON_NAME} is clickable on this page!")

    @allure.step(f"{datetime.now()}   2. Start Act.")
    def act(self, d):
        print(f"{datetime.now()}   2. Start Act.")

        # Start click [Open an account] button
        print(f"{datetime.now()}   Start click on {BUTTON_NAME} =>")
        try:
            self.driver.find_element(*BUTTON_LOCATOR).click()
            print(f"{datetime.now()}   => {BUTTON_NAME} clicked!\n")

        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => {BUTTON_NAME} NOT CLICKED")

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

            self.driver.find_element(*BUTTON_LOCATOR).click()
            time.sleep(1)
            print(f"{datetime.now()}   => {BUTTON_NAME} clicked!\n")

        Common.save_current_screenshot(d, f"{BUTTON_NAME} clicked!")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d, cur_language):
        print(f"{datetime.now()}   3. Start Assert.")

        # Check opened page
        print(f"{datetime.now()}   Check page with '404 error' message is displayed instead 'Contact us' page.")
        print(f"{datetime.now()}   IS page with '404 error' message is displayed instead 'Contact us' page.? =>")
        print(f'{datetime.now()}   Current page is: {self.driver.current_url}')
        if self.driver.find_elements(*MESSAGE_404_LOCATOR):
            msg = f"Page with '404 error' message is displayed instead 'Contact us' page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   Current page don't have '404 error' message.")
        expected_page = 'https://capital.com/ar-ae/contact-us'

        print(f"{datetime.now()}   Check opened page is 'Contact us' page.")
        print(f"{datetime.now()}   IS opened page 'Contact us' page.? =>")
        if not self.current_page_url_contain_the(expected_page):
            msg = (f"Instead 'Contact us' page and page with '404 error' message opened other page. "
                   f"Expected_page is '{expected_page}', "
                   f"current page is '{self.driver.current_url}'")
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)

        print(f"{datetime.now()}   => Opened expected page 'Contact us'!\n")
        Common.save_current_screenshot(d, f"Opened expected page 'Contact us'!")
        return True
