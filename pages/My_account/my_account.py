"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import time
from datetime import datetime

import allure
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException
)

from pages.base_page import BasePage
from pages.common import Common
from pages.My_account.my_account_locators import MyAccountLocator


class MyAccount(BasePage):

    @allure.step("Click 'Logout' button")
    def my_account_button_logout_click(self):
        print(f"\n"
              f"{datetime.now()}   Start Click [Logout] button:")

        print(f"{datetime.now()}   BUTTON_LOGOUT is present? =>")
        button_list = self.driver.find_elements(*MyAccountLocator.LOGOUT)
        if len(button_list) == 0:
            msg = "BUTTON_LOGOUT is not present"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # ???   {msg}")
        print(f"{datetime.now()}   => BUTTON_LOGOUT is present")

        print(f"{datetime.now()}   Is BUTTON_LOGOUT visible? =>")
        if not self.element_is_visible(MyAccountLocator.LOGOUT):
            msg = "BUTTON_LOGOUT is not visible"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # ???   {msg}")
        print(f"{datetime.now()}   => BUTTON_LOGOUT is visible")

        print(f"{datetime.now()}   BUTTON_LOGOUT is clickable? =>")
        if not self.element_is_clickable(button_list[0], 10):
            msg = "BUTTON_LOGOUT is not clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # ???   {msg}")
        print(f"{datetime.now()}   => BUTTON_LOGOUT is clickable")

        print(f"{datetime.now()}   BUTTON_LOGOUT click =>")
        try:
            button_list[0].click()
        except ElementNotInteractableException:
            print(f'{datetime.now()}   It\'s problem! Button "Logout" is not clickable, but 1 second later ...')
            time.sleep(1)
            button_list[0].click()
        except ElementClickInterceptedException:
            print(f'{datetime.now()}   It\'s a problem! Button "Logout" are not clicked, but 1 second later ...')
            time.sleep(1)
            button_list[0].click()

        print(f"{datetime.now()}   => BUTTON_LOGOUT is clicked")

    @allure.step("Click 'Trading Platform' button")
    def click_button_trading_platform(self):
        button = self.driver.find_element(*MyAccountLocator.TRADING_PLATFORM)
        self.element_is_clickable(button, 5)
        button.click()

    @allure.step("Click 'Close MyAccount panel'")
    def click_close_user_panel(self):
        button = self.driver.find_element(*MyAccountLocator.CLOSE)
        self.element_is_clickable(button, 5)
        button.click()
