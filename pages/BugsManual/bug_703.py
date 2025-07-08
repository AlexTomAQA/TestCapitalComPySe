"""
-*- coding: utf-8 -*-
@Time    : 2025/07/07 23:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from selenium.webdriver.support.ui import WebDriverWait


class BUG_703(BasePage):
    FIRST_LEVEL_IN_BREADCRUMBS = (By.CSS_SELECTOR, ".breadcrumbs_breadcrumbs__vTxZd .link_link__lpKUr:nth-child(1)")
    SECOND_LEVEL_IN_BREADCRUMBS = (
        By.CSS_SELECTOR, ".breadcrumbs_breadcrumbs__vTxZd .link_link__lpKUr:nth-child(2)") # if there are three levels
    LAST_LEVEL_IN_BREADCRUMBS = (By.CSS_SELECTOR, ".breadcrumbs_breadcrumbs__vTxZd span")

    def __init__(self, driver, link, bid):
        super().__init__(driver, link, bid)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)

    @allure.step(f"{datetime.now()}   Is there an expected link?")
    def is_payments_and_withdrawals_breadcrumbs_displayed(self):

        # Check numbers of levels breadcrumbs
        first_level_in_breadcrumbs = self.driver.find_elements(*self.FIRST_LEVEL_IN_BREADCRUMBS)
        second_level_in_breadcrumbs = self.driver.find_elements(*self.SECOND_LEVEL_IN_BREADCRUMBS)
        last_level_in_breadcrumbs = self.driver.find_elements(*self.LAST_LEVEL_IN_BREADCRUMBS)

        # first level
        if len(first_level_in_breadcrumbs) > 0:
            print(f"{datetime.now()}   First level is: '{first_level_in_breadcrumbs[0].text}'")
        else:
            print(f"{datetime.now()}   Current page don't have first level in breadcrumbs")

        # second level
        if len(second_level_in_breadcrumbs) > 0:
            print(f"{datetime.now()}   Second level is: '{first_level_in_breadcrumbs[0].text}'")
        elif len(last_level_in_breadcrumbs) > 0:
            msg = (f"Current page has only two levels in breadcrumbs. "
                   f"Second level is: '{last_level_in_breadcrumbs[0].text}'")
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        else:
            msg = "Current page doesn't have second level in breadcrumbs"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)

        # third level
        if len(last_level_in_breadcrumbs) > 0:
            print(f"{datetime.now()}   Current page have three levels in breadcrumbs")
            print(f"{datetime.now()}   Third level is: '{last_level_in_breadcrumbs[0].text}'")


        if 'pricing' not in first_level_in_breadcrumbs.text.lower:
            msg = (f"Second level in breadcrumbs doesn't have name of link 'pricing'. "
                   f"Name of second level is: '{first_level_in_breadcrumbs.text}'")
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        elif 'payments and withdrawals' not in last_level_in_breadcrumbs.text.lower:
            msg = (f"Third level in breadcrumbs doesn't have name of link 'payments and withdrawals'. "
                   f"Name of third level is: '{last_level_in_breadcrumbs.text}'")
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
