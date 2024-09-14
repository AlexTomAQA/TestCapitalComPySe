"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
from datetime import datetime

import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
# from pages.Signup_login.signup_login import SignupLogin
from pages.Header.header_locators import HeaderElementLocators
from pages.My_account.my_account_locators import MyAccountLocator
# from .src.src import HeaderSrc

LOGIN_BUTTON_IN_HEADER_NEW = (By.CSS_SELECTOR, "[class*=panel_holder] [data-type=btn_header_login]")


class Header(BasePage):

    @allure.step("Click button [My account]")
    def header_button_my_account_click(self):
        print(f"{datetime.now()}   1. BUTTON_MY_ACCOUNT is present? =>")
        button_list = self.driver.find_elements(*HeaderElementLocators.BUTTON_MY_ACCOUNT)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is not present on this page")
            del button_list
            return False
        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is present on this page")

        # added block to resolve issue: {"status":60,"value":"[object HTMLButtonElement] has no size and location"}
        print(f"{datetime.now()}   IS BUTTON_MY_ACCOUNT visible on this page? =>")
        if not self.element_is_visible(HeaderElementLocators.BUTTON_MY_ACCOUNT, 5):
            msg = f"BUTTON_MY_ACCOUNT is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            pytest.fail(f"Problem!   {msg}")
        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is visible on this page!\n")
        # end block

        button_list = self.driver.find_elements(*HeaderElementLocators.BUTTON_MY_ACCOUNT)
        ActionChains(self.driver) \
            .pause(0.5) \
            .move_to_element(button_list[0]) \
            .pause(0.5) \
            .perform()
        print(f"{datetime.now()}   => Move to BUTTON_MY_ACCOUNT")

        print(f"{datetime.now()}   2. BUTTON_MY_ACCOUNT is clickable? =>")
        button_list = self.driver.find_elements(*HeaderElementLocators.BUTTON_MY_ACCOUNT)
        if not self.element_is_clickable(button_list[0], 10):
            msg = "Button [My account] is not clickable!"
            print(f"{datetime.now()}   msg")
            pytest.fail(f"Problem!   {msg}")
        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is clickable")

        print(f"{datetime.now()}   BUTTON_MY_ACCOUNT Click =>")
        button_list = self.driver.find_elements(*HeaderElementLocators.BUTTON_MY_ACCOUNT)
        ActionChains(self.driver) \
            .click(button_list[0]) \
            .perform()
        return True

    def check_opened_my_account_panel(self):

        if not self.element_is_visible(MyAccountLocator.LOGOUT, 10):
            print(f"{datetime.now()}   => User panel [My account] is not opened after first BUTTON_MY_ACCOUNT click")

            print(f"{datetime.now()}   BUTTON_MY_ACCOUNT second Click =>")
            button_list = self.driver.find_elements(*HeaderElementLocators.BUTTON_MY_ACCOUNT)
            ActionChains(self.driver) \
                .click(button_list[0]) \
                .perform()

            if self.element_is_visible(MyAccountLocator.LOGOUT, 10):
                print(f"{datetime.now()}   => User panel [My account] is opened after second BUTTON_MY_ACCOUNT click")
                del button_list
                return True

            print(
                f"{datetime.now()}   => User panel [My account] is not opened after second BUTTON_MY_ACCOUNT click")
            del button_list
            return False

        print(f"{datetime.now()}   => User panel [My account] is opened")
        return True

    def check_visible_login_button_in_header_on_capital_com_new_page(self):
        print(f"{datetime.now()}   LogIn button is visible? =>")
        if not self.element_is_visible(LOGIN_BUTTON_IN_HEADER_NEW, 10):
            msg = "LogIn button in header new is not visible"
            print(f"{datetime.now()}   => {msg}")
            pytest.fail(f"Problem!   => {msg}")
        print(f"{datetime.now()}   => LogIn button in header new is visible")
