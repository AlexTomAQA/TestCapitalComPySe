"""
-*- coding: utf-8 -*-
@Time    : 2024/07/20 17:00
@Author  : podchasova11
"""

from datetime import datetime

import allure

from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import MyAccountButtonLocators
from pages.base_page import BasePage
from pages.common import Common
from src.src import CapitalComPageSrc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ButtonMyAccount(BasePage):
    def __init__(self, browser, link, bid):
        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}  1. Start Arrange  ")
    def arrange_(self, link):
        print(f"\n{datetime.now()}   1. Arrange for [My account] button")

        if not self.current_page_is(link):
            self.link = CapitalComPageSrc.URL_NEW
            self.open_page()

        print(f"{datetime.now()}   Is BUTTON_MY_ACCOUNT present on the page? => ")
        button = self.driver.find_elements(*MyAccountButtonLocators.BUTTON_MY_ACCOUNT)
        if len(button) == 0:
            print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is not present on the page")
            Common().pytest_fail("BUTTON_MY_ACCOUNT is not present on the page")
        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is present on the page")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button[0]
        )

        print(f"{datetime.now()}   Is BUTTON_MY_ACCOUNT clickable?  => ")
        time_out = 3
        if not self.element_is_clickable(button[0], time_out):
            print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is not clickable after {time_out} sec")
            Common.pytest_fail("Bug ? BUTTON_MY_ACCOUNT is not clickable")
        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is clickable")

    @allure.step(f"{datetime.now()}  2. Start Act  ")
    def element_click(self):
        print(f"{datetime.now()}   2. Act for [My account] button")
        print(f"{datetime.now()}   Start to click BUTTON_MY_ACCOUNT =>")

        button = self.driver.find_elements(*MyAccountButtonLocators.BUTTON_MY_ACCOUNT)
        button[0].click()

        WebDriverWait(self.driver, 10).until(
            EC.url_changes(self.driver.current_url)
        )

        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is clicked")

    @allure.step('Checking that the "My account" menu is opened')
    def assert_my_account_menu_opened_en(self, d):
        print(f"\n{datetime.now()}   3. Assert")
        btn_link = d.current_url
        if btn_link == "https://capital.com/trading/platform/":
            assert False, \
                ('Bug#285en. '
                 'Expected result: Menu [My Account] is displayed'
                 '\n'
                 'Actual result: The trading platform page is opened')
        else:
            print(f"{datetime.now()}   =>This does not mean that there is no bug")

    @allure.step('Checking that the "My account" menu is opened')
    def assert_my_account_menu_opened_ar(self, d):
        print(f"\n{datetime.now()}   3. Assert")
        btn_link = d.current_url
        if btn_link == "https://capital.com/trading/platform/":
            assert False, \
                ('Bug#285ar. '
                 'Expected result: Menu [My Account] is displayed'
                 '\n'
                 'Actual result: The trading platform page is opened')
        else:
            print(f"{datetime.now()}   =>This does not mean that there is no bug")