"""
-*- coding: utf-8 -*-
@Time    : 2025/06/10 13:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from selenium.webdriver.support.ui import WebDriverWait
from pages.Signup_login.signup_login_locators import NewSignupFormLocators

class BUG_702(BasePage):
    SECOND_LINK_IN_BREADCRUMBS = (By.CSS_SELECTOR, ".breadcrumbs_breadcrumbs__vTxZd .link_link__lpKUr:nth-child(2)")

    def __init__(self, driver, link, bid):
        super().__init__(driver, link, bid)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)

    @allure.step(f"{datetime.now()}   Is there an expected link?")
    def is_pricing_link_displayed(self):

        # Check presenting, visibility link
        self.find_link_scroll_check_visibility_and_clickability(
            "Second link in breadcrumbs", self.SECOND_LINK_IN_BREADCRUMBS)

        print(f"{datetime.now()}   Start get link of second item of breadcrumbs")
        second_item_of_breadcrumbs = self.driver.find_element(*self.SECOND_LINK_IN_BREADCRUMBS)
        link_of_second_item = second_item_of_breadcrumbs.get_attribute("href")
        print(f"{datetime.now()}   Link of second item of breadcrumbs {link_of_second_item}.")

        if 'about-us' in link_of_second_item:
            msg = "Link [About] is displayed in the Breadcrumbs on the page 'Our business model'."
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        else:
            msg = (f"Opened page don't displayed Link [About] in the Breadcrumbs on the page 'Our business model', "
                   f"but need check screen. Current link is {link_of_second_item}")
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
