"""
-*- coding: utf-8 -*-
@Time    : 2024/07/20 21:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By

from src.src import CapitalComPageSrc
from pages.base_page import BasePage
from pages.common import Common
from pages.Elements.testing_elements_locators import TableTradingInstrumentsLocators
from pages.Signup_login.signup_login import SignupLogin

BLOCK_NAME = "[Go to all cryptocurrencies] link"
LINK_LOCATOR = (By.CSS_SELECTOR, '[data-type="wdg_go_to_market_deeplink"]')


class BUG_149(BasePage):

    def __init__(self, browser, link, bid):
        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}   1. Start Arrange.")
    def arrange(self, d, cur_language):
        global LINK_LOCATOR
        if cur_language == "de":
            LINK_LOCATOR = (By.XPATH, '//li[text()="Alle Kryptowährungen"]')
        print(f"{datetime.now()}   1. Start Arrange.")

        # Check presenting SEARCH FIELD
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

        # Check visible SEARCH FIELD
        print(f"{datetime.now()}   IS {BLOCK_NAME} visible on this page? =>")
        if not self.element_is_visible(LINK_LOCATOR, 5):
            msg = f"{BLOCK_NAME} is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} is visible on this page!\n")

        # Check clickable SEARCH FIELD
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

        # Start click on link
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
            print(f"{datetime.now()}   => {BLOCK_NAME} clicked!\n")

        except NoSuchElementException:
            msg = (f"{BLOCK_NAME} is not implemented as a link when the German language is selected "
                   f"in the block 'Why trade cryptocurrency with Capital.com'.")
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        Common.save_current_screenshot(d, f"{BLOCK_NAME} clicked!")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d,):
        print(f"{datetime.now()}   3. Start Assert.")

        # Check presenting LIST of TRADING_INSTRUMENTS
        print(f"{datetime.now()}   Check presenting CFD Instruments.")
        print(f"{datetime.now()}   IS CFD Instruments present on this page? =>")
        if len(self.driver.find_elements(*TableTradingInstrumentsLocators.LINE_TRADING_INSTRUMENT)) == 0:
            msg = f"CFD Instruments is NOT present on this page. Current page is not Cryptocurrencies page."
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => CFD Instruments present on this page!\n")
        self.driver.get(CapitalComPageSrc.URL)
        return True
