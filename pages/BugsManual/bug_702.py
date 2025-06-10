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
    WE_ARE_HERE_TO_HELP_BLOCK = (By.CSS_SELECTOR, "[data-type='banner_in_body_block']")
    OPEN_AN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[data-type='banner_in_body_block_btn1_custom']")

    def __init__(self, driver, link, bid):
        super().__init__(driver, link, bid)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)

    @allure.step(f"{datetime.now()}   Click on [Open an account] button")
    def click_open_an_account_button(self):

        # Check presenting, visibility block
        self.find_block_scroll_and_check_visibility(
            "We’re here to help", self.WE_ARE_HERE_TO_HELP_BLOCK)

        # Check presenting, visibility button
        self.find_link_scroll_check_visibility_and_clickability(
            "Open an account", self.OPEN_AN_ACCOUNT_BUTTON)

        print(f"{datetime.now()}   Start to click 'Open an account'")
        self.driver.find_element(*self.OPEN_AN_ACCOUNT_BUTTON).click()
        print(f"{datetime.now()}   End to click 'Open an account'")

        Common().save_current_screenshot(self.driver,
                                         "After click on [Open an account] button")

    @allure.step(f"{datetime.now()}   Is expected page open?")
    def is_sign_up_form_opened(self):
        print(f"{datetime.now()}   Start get the URL page.")
        page_url = self.driver.current_url
        print(f"{datetime.now()}   Current url of page is {page_url}.")

        if 'contact-us' in page_url:
            msg = "Opened page 'Contact us' instead opening form 'Sign up' form."
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        elif self.element_is_visible(NewSignupFormLocators.SIGNUP_FORM):
            print(f"{datetime.now()}   => There is form 'Sign up, but need check screen'\n")
        else:
            msg = "Opened page don't have opening form 'Sign up' form, need check screen."
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
