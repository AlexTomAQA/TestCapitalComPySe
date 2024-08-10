"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
from datetime import datetime

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

LOGO = (By.CSS_SELECTOR, "logo a.logo object[data='./assets/pic/logo.svg']")
ACCOUNT_INFO_ICON = (By.CSS_SELECTOR, "topbar account-info .iconex-arrow-down-mini")
ACCOUNT_INFO_MENU_LOGOUT = (By.CSS_SELECTOR, "topbar account-info button[data-qa='logout']")


class TopBar(BasePage):

    @allure.step("Check if the Logo element is present on the page")
    def trading_platform_logo_is_present(self):
        """Check that the Capital.com Logo is present"""
        # Setup wait for later
        print(f"{datetime.now()}   Start check that the Trading platform page is loaded and LOGO is present on it =>")
        timeout = 15
        print(f"{datetime.now()}   Set timeout = {timeout}")
        wait = WebDriverWait(self.driver, timeout)

        print(f"{datetime.now()}   Is present LOGO on this page? =>")
        if self.element_is_visible(LOGO, timeout):
            print(f"{datetime.now()}   => LOGO is visible on this page")
            return True
        else:
            print(f"{datetime.now()}   => LOGO not present on this page after more 30 seconds")
            return False

    @allure.step("Start Logout from account info menu in top bar")
    def trading_platform_top_bar_account_info_menu_logout(self):
        print(f"{datetime.now()}   Start Logout from account info menu in top bar =>")
        timeout = 15
        print(f"{datetime.now()}   Set timeout = {timeout}")
        wait = WebDriverWait(self.driver, timeout)

        print(f"{datetime.now()}   Is visible account info icon? =>")
        if not self.element_is_visible(ACCOUNT_INFO_ICON, timeout):
            print(f"{datetime.now()}   => Account info icon is not visible on this page")
            return False
        print(f"{datetime.now()}   => Account info icon is visible on this page")

        print(f"{datetime.now()}   Account info icon is click =>")
        button_list = self.driver.find_elements(*ACCOUNT_INFO_ICON)
        if len(button_list) == 0:
            print("Problem")
            return False
        button_list[0].click()
        print(f"{datetime.now()}   => Account info icon is clicked")

        print(f"{datetime.now()}   Is visible logout button in account info menu? =>")
        if not self.element_is_visible(ACCOUNT_INFO_MENU_LOGOUT, timeout):
            print(f"{datetime.now()}   => Logout button from account info menu is not visible")
            return False
        print(f"{datetime.now()}   => Logout button from account info menu is visible")

        print(f"{datetime.now()}   Logout button is click =>")
        button_list = self.driver.find_elements(*ACCOUNT_INFO_MENU_LOGOUT)
        if len(button_list) == 0:
            print("Problem")
            return False
        button_list[0].click()
        print(f"{datetime.now()}   => Logout button from Account info menu is clicked")

        return True
