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
    DEPOSITS_AND_WITHDRAWALS_BLOCK = (By.CSS_SELECTOR, "[data-id='part_1']")
    HERE_LINK = (By.CSS_SELECTOR, "[data-testid='link-with-safety']")
    NUMBER_OF_TABS = None

    def __init__(self, driver, link, bid):
        super().__init__(driver, link, bid)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)

    @allure.step(f"{datetime.now()}   Click on [here] link")
    def click_here_link(self):

        # Check presenting, visibility block
        self.find_block_scroll_and_check_visibility(
            "Deposits and withdrawals", self.DEPOSITS_AND_WITHDRAWALS_BLOCK)

        # Check presenting, visibility link
        self.find_link_scroll_check_visibility_and_clickability(
            "App", self.HERE_LINK)

        # How many tabs before click link [here]
        tabs_before_click = self.driver.window_handles
        print(f"{datetime.now()}   Number of tabs before click link: {len(tabs_before_click)}")

        # click link
        print(f"{datetime.now()}   Start click [here] link")
        self.driver.find_element(*self.HERE_LINK).click()
        print(f"{datetime.now()}   End click [here] link\n")

        # How many tabs after click link [here]
        tabs_after_click = self.driver.window_handles
        print(f"{datetime.now()}   Number of tabs after click link: {len(tabs_after_click)}")

        if len(tabs_before_click) < len(tabs_after_click):
            self.driver.close()                                 # close active tab
            self.driver.switch_to.window(tabs_after_click[-1])  # switch to tab, opened after click [here] link
            print(f"{datetime.now()}   Current number of tabs is: {len(self.driver.window_handles)}")

        Common().save_current_screenshot(self.driver,
                                         "After click on [here] link")

    @allure.step(f"{datetime.now()}   Is expected page open?")
    def is_page_with_expected_language_open(self):
        print(f"{datetime.now()}   What is language on the page?")
        print(f"{datetime.now()}   Start get the URL page.")
        page_url = self.driver.current_url
        print(f"{datetime.now()}   Current url of page is {page_url}.")
        if "/en" in page_url:
            msg = "Current page have english language."
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        elif "/it" in page_url:
            print("Current page have expected shortcut '/it' in url, but need to check screenshot")
        else:
            msg = "Current page don't have shortcut '/it' or '/en' in url, need to check screenshot"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
