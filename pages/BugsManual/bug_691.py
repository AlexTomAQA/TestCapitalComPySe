"""
-*- coding: utf-8 -*-
@Time    : 2025/04/26 23:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from selenium.webdriver.support.ui import WebDriverWait

class BUG_691(BasePage):
    OUR_TRADING_APP_BLOCK = (By.XPATH, "(//div[@data-type='tiles_w_img'])[2]")
    APP_LINK = (By.XPATH, "(//div[@data-type='tiles_w_img'])[2] //a[contains(text(), 'pp')]")

    def __init__(self, driver, link, bid):
        super().__init__(driver, link, bid)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)

    @allure.step(f"{datetime.now()}   Click on [App] link")
    def click_app_link(self):

        # Check presenting, visibility block
        self.find_block_scroll_and_check_visibility(
            "Our trading app", self.OUR_TRADING_APP_BLOCK)

        # Check presenting, visibility link
        self.find_link_scroll_check_visibility_and_clickability(
            "App", self.APP_LINK)

        # click link
        print(f"{datetime.now()}   Start click [App] link")
        self.driver.find_element(*self.APP_LINK).click()
        print(f"{datetime.now()}   End click [App] link\n")
        Common().save_current_screenshot(self.driver,
                                         "After click on [App] link")

    @allure.step(f"{datetime.now()}   Is expected page open?")
    def is_expected_page_open(self):
        print(f"{datetime.now()}   What is language on the page?")
        print(f"{datetime.now()}   Start get the URL page.")
        page_url = self.driver.current_url
        print(f"{datetime.now()}   Current url of page is {page_url}.")
        if "en" in page_url:
            msg = "Current page have english language."
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        elif "at" in page_url:
            print("Current page have expected shortcut 'at', but need to check screenshot")
        else:
            msg = "Current page don't have shortcut 'at' or 'en', need to check screenshot"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
