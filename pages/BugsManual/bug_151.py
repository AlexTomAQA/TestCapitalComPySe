"""
-*- coding: utf-8 -*-
@Time    : 2024/07/23 14:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.common import Common
from pages.Signup_login.signup_login import SignupLogin

BLOCK_NAME = "[demo account] link"
# LINK_LOCATOR = (By.CSS_SELECTOR, '.arrowLink.js-mWidget-link.js-mWidget--mosttraded')


class BUG_151(BasePage):

    def __init__(self, browser, link, bid):
        super().__init__(browser, link, bid)
"""
    @allure.step(f"{datetime.now()}   1. Start Arrange.")
    def arrange(self, d, cur_language):
        global LINK_LOCATOR
        print(f"{datetime.now()}   1. Start Arrange.")

        # Check presenting "Browse all markets" link
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

        # Check visible "Browse all markets" link
        print(f"{datetime.now()}   IS {BLOCK_NAME} visible on this page? =>")
        if not self.element_is_visible(LINK_LOCATOR, 5):
            msg = f"{BLOCK_NAME} is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} is visible on this page!\n")

        # Check clickable "Browse all markets" link
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

        Common.save_current_screenshot(d, f"{BLOCK_NAME} clicked!")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d, cur_language):
        print(f"{datetime.now()}   3. Start Assert.")

        # Check language version of page "Markets"
        print(f"{datetime.now()}   Check language version of page 'Markets'. ")
        print(f"{datetime.now()}   IS page 'Markets' opened EN-language version? =>")
        print(f'{datetime.now()}   Current page is: {self.driver.current_url}')
        if self.current_page_url_contain_the('https://capital.com/derivative-financial-instruments'):
            msg = f"Page 'Markets' opened in EN-language version."
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        expected_page = ''
        match cur_language:
            case "de":
                expected_page = 'https://capital.com/de/alle-maerkte'
            case "es":
                expected_page = 'https://capital.com/es/instrumentos-financieros-derivados'
            case "it":
                expected_page = 'https://capital.com/it/derivati'
            case "ru":
                expected_page = 'https://capital.com/ru/proizvodnyye-finansovyye-instrumenty'
            case "cn":
                expected_page = 'https://capital.com/cn/derivative-financial-instruments'
            case "zh":
                expected_page = 'https://capital.com/zh/derivative-financial-instruments'
            case "fr":
                expected_page = 'https://capital.com/fr/instruments-financiers-derives'
            case "pl":
                expected_page = 'https://capital.com/pl/pochodne-instrumenty-finansowe'
            case "ro":
                expected_page = 'https://capital.com/ro/instrumente-financiare-derivate'
            case "nl":
                expected_page = 'https://capital.com/nl/derivaat-financieel-instrument'
            case "el":
                expected_page = 'https://capital.com/el/paragoga-xrimatopistotika-mesa'
            case "hu":
                expected_page = 'https://capital.com/hu/derivativ-penzugyi-eszkozok'

        if not self.current_page_url_contain_the(expected_page):
            msg = (f"Page 'Markets' opened in not EN-language version and not expected language."
                   f"Current language is {cur_language}, expected_page is {expected_page},"
                   f"current page is {self.driver.current_url}")
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)

        print(f"{datetime.now()}   => Page 'Markets' present on expected language!\n")
        Common.save_current_screenshot(d, f"Page 'Markets' present on expected language!")
        return True
"""