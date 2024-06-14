"""
-*- coding: utf-8 -*-
@Time    : 2024/06/14 20:30
@Author  : Artem Dashkov
"""
from datetime import datetime
import pytest
import allure
from pages.common import Common
from pages.Elements.AssertClass import AssertClass
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Markets.markets_locators import HeaderElementLocators
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException


BUTTON_NAME = '[Sign up]'

BUTTON_LOCATOR = HeaderElementLocators.BUTTON_SIGNUP_2



class EmailFieldSignUpForm(BasePage):
    global BUTTON_NAME

    global BUTTON_LOCATOR

    def __init__(self, browser, link, bid):
        self.button = None

        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}  Start Full test for field [email] in Sign up form")
    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link, invalid_login, valid_password):
        self.arrange(d, cur_item_link)
        self.element_click(d, invalid_login, valid_password)

    @allure.step("Click button [Trade] in 'Trading instrument' widget")
    def arrange(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange for 'Trading instrument' widget: market")

        # Check presenting and visible button [Sign Up]
        print(f"{datetime.now()}   IS {BUTTON_NAME} button present on this page? =>")
        self.button = self.driver.find_elements(*BUTTON_LOCATOR)
        if len(self.button) == 0:
            msg = f"{BUTTON_NAME} button is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} button present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*BUTTON_LOCATOR)[0]
        )

        print(f"{datetime.now()}   IS {BUTTON_NAME} button visible on this page? =>")
        if not self.element_is_visible(BUTTON_LOCATOR, 5):
            msg = f"{BUTTON_NAME} button is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} button is visible on this page!\n")

        # IS [Sign Up] button clickable?
        print(f"{datetime.now()}   IS {BUTTON_NAME} clickable on the page? =>")
        if not self.element_is_clickable(BUTTON_LOCATOR):
            print(f"{datetime.now()}   => {BUTTON_NAME} is NOT clickable on the page!\n")
            Common().pytest_fail(f" Bug ? Checking element is not clickable on this page")
        print(f"{datetime.now()}   => {BUTTON_NAME} is clickable on the page!\n")

        print(f"\n{datetime.now()}   Start Click button {BUTTON_NAME} =>")

        try:
            self.driver.find_element(*BUTTON_LOCATOR).click()
            print(f"{datetime.now()}   => End Click button {BUTTON_NAME} ")
        except ElementNotInteractableException:
            msg = "Tab '{cur_market}' MARKET is NOT clicked"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(msg)

    @allure.step(f"Fill out fields")
    def element_fill_out(self, d, invalid_login, valid_password):
        print(f"\n{datetime.now()}   2. Act_v0")



        """
        Stopped here
        """

        return True

