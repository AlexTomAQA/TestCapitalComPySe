"""
-*- coding: utf-8 -*-
@Time    : 2024/05/03 20:00
@Author  : Artem Dashkov
"""
import time
from datetime import datetime
import allure

from pages.common import Common
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import MainPageBannerLocators
from pages.Signup_login.signup_login import SignupLogin
from selenium.common.exceptions import ElementClickInterceptedException

BLOCK_NAME = "Main page banner"
BANNER_NAME = "Get involved. Become a trader."
BUTTON_NAME = '[Trade now]'

BLOCK_LOCATOR = MainPageBannerLocators.MAIN_PAGE_BANNER_BLOCK
TAB_LOCATOR = MainPageBannerLocators.GET_INVOLVED_TAB_MAIN_PAGE_BANNER
BUTTON_LOCATOR = MainPageBannerLocators.TRADE_NOW_BUTTON_GET_INVOLVED_TAB


class GetInvolvedBannerTradeNowButton(BasePage):
    global BLOCK_NAME
    global BANNER_NAME
    global BUTTON_NAME

    global BLOCK_LOCATOR
    global TAB_LOCATOR
    global BUTTON_LOCATOR

    def __init__(self, browser, link, bid):
        self.tab = None

        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}   Start Full test for {BUTTON_NAME} button in {BANNER_NAME} banner")
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)
        self.element_click(d)

        test_element = AssertClass(d, cur_item_link, self.bid)
        match cur_role:
            case "NoReg" | "NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link, False, False)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        # Check presenting and visible in block
        print(f"{datetime.now()}   IS '{BLOCK_NAME}' block present on this page? =>")
        if len(self.driver.find_elements(*BLOCK_LOCATOR)) == 0:
            msg = f"'{BLOCK_NAME}' block is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => '{BLOCK_NAME}' block present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*BLOCK_LOCATOR)[0]
        )

        print(f"{datetime.now()}   IS '{BLOCK_NAME}' block visible on this page? =>")
        if not self.element_is_visible(BLOCK_LOCATOR, 5):
            msg = f"'{BLOCK_NAME}' block is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => '{BLOCK_NAME}' block is visible on this page!\n")

        # Check presenting tab
        print(f"{datetime.now()}   IS '{BANNER_NAME}' tab present on this page? =>")
        self.tab = self.driver.find_elements(*TAB_LOCATOR)
        if len(self.tab) == 0:
            msg = f"'{BANNER_NAME}' tab is NOT present on this page"
            print(f"'{datetime.now()}'   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => '{BANNER_NAME}' tab present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*TAB_LOCATOR)
        )

        # Check visible tab
        print(f"{datetime.now()}   IS '{BANNER_NAME}' tab visible on this page? =>")
        if not self.element_is_visible(TAB_LOCATOR, 5):
            msg = f"'{BANNER_NAME}' tab is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => '{BANNER_NAME}' tab is visible on this page!\n")

        # Check clickable tab
        print(f"{datetime.now()}   IS '{BANNER_NAME}' tab clickable on this page? =>")
        time_out = 5
        if not self.element_is_clickable(TAB_LOCATOR, time_out):
            msg = f"'{BANNER_NAME}' tab is NOT clickable on this page after {time_out} seconds!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => '{BANNER_NAME}' tab is clickable on this page!\n")

        print(f"{datetime.now()}   Start '{BANNER_NAME}' tab click.")
        try:
            self.driver.find_element(*TAB_LOCATOR).click()
            print(f"{datetime.now()}   '{BANNER_NAME}' tab is clicked.\n")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   '{BANNER_NAME}' tab not clicked")
            print(f"{datetime.now()}   'Signup' or 'Login' form is automatically opened")

            page_ = SignupLogin(self.driver)
            if page_.close_signup_form():
                pass
            elif page_.close_login_form():
                pass
            elif page_.close_signup_page():
                pass
            else:
                page_.close_login_page()

            del page_
            self.driver.find_element(*TAB_LOCATOR).click()

    @allure.step(f"Click button '{BUTTON_NAME}' on '{BANNER_NAME}' tab")
    def element_click(self, d):
        print(f"\n{datetime.now()}   2. Act_v0")

        # Check presenting button
        print(f"{datetime.now()}   IS '{BUTTON_NAME}' button present on this page? =>")

        if len(self.driver.find_elements(*BUTTON_LOCATOR)) == 0:
            msg = f"'{BUTTON_NAME}' button is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => '{BUTTON_NAME}' button present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*BUTTON_LOCATOR)
        )

        # Check visible button
        print(f"{datetime.now()}   IS '{BUTTON_NAME}' button visible on this page? =>")
        if not self.element_is_visible(BUTTON_LOCATOR, 5):
            msg = f"'{BUTTON_NAME}' button is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => '{BUTTON_NAME}' button is visible on this page!\n")

        # Check clickable button
        print(f"{datetime.now()}   IS '{BUTTON_NAME}' button clickable on this page? =>")
        time_out = 5
        if not self.element_is_clickable(BUTTON_LOCATOR, time_out):
            msg = f"'{BUTTON_NAME}' button is NOT clickable on this page after {time_out} seconds!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => '{BUTTON_NAME}' button is clickable on this page!\n")


        try:
            self.driver.find_element(*BUTTON_LOCATOR).click()
            print(f"{datetime.now()}   => '{BUTTON_NAME}' button clicked!")
        except ElementClickInterceptedException:
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                self.driver.find_element(*TAB_LOCATOR))

            print(f"{datetime.now()}   Start '{BANNER_NAME}' tab click.")
            self.driver.find_element(*TAB_LOCATOR).click()
            print(f"{datetime.now()}   '{BANNER_NAME}' tab is clicked.\n")

            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                self.driver.find_element(*BUTTON_LOCATOR)
            )

            self.driver.find_element(*BUTTON_LOCATOR).click()
            print(f"{datetime.now()}   => '{BUTTON_NAME}' button clicked!")
