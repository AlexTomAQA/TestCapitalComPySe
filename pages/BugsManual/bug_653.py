"""
-*- coding: utf-8 -*-
@Time    : 2025/01/12 21:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common

CONNECT_YOUR_ACCOUNT_BLOCK_LOCATOR = (
    By.XPATH,
    "(//div [@class='white cardsImage_bg__4z0G6'] //div[@data-type='tiles_w_img'])[1]"
)
HOW_TO_CREATE_ACCOUNT_LINK_LOCATOR = (By.XPATH, "(//b[contains(text(), 'MT4')])[1]")

class BUG_653(BasePage):

    url_before_click = None
    tabs_before_click = None
    tabs_after_click = None


    @allure.step(f"{datetime.now()}   1. Start Arrange: find 'Connect your account to MT4...' block, "
                 f"find link [CFDs].")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find 'Connect your account to MT4...' block.")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting, visibility block
        self.find_block_scroll_and_check_visibility(
            "Connect your account to MT4...", CONNECT_YOUR_ACCOUNT_BLOCK_LOCATOR)

        # Check presenting, visibility link
        self.find_link_scroll_check_visibility_and_clickability(
            "How to create on MT4 account", HOW_TO_CREATE_ACCOUNT_LINK_LOCATOR)

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):
        print(f"{datetime.now()}   2. Start Act.")

        # Define parameters before click
        self.tabs_before_click = self.driver.window_handles
        print(f"{datetime.now()}   Current qty windows is: {len(self.tabs_before_click)}")
        self.url_before_click = self.driver.current_url
        print(f"{datetime.now()}   Current link before click: {self.url_before_click}")

        # click on the link 'How to create an MT4 account'
        print(f"{datetime.now()}   Start to click link 'How to create an MT4 account'")
        self.driver.find_element(*HOW_TO_CREATE_ACCOUNT_LINK_LOCATOR).click()
        Common().save_current_screenshot(d, "After click on link 'How to create an MT4 account'")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d, link):
        print(f"{datetime.now()}   3. Start Assert.")
        # Define parameters after click
        self.tabs_after_click = self.driver.window_handles
        print(f"{datetime.now()}   Current qty windows is: {len(self.tabs_after_click)}")
        current_link_after_click = self.driver.current_url
        print(f"{datetime.now()}   Current link before click: {current_link_after_click}")

        if len(self.tabs_before_click) != len(self.tabs_after_click):
            print(f"{datetime.now()}   Numbers of Tabs before and after click are difference")
            print(f"{datetime.now()}   Start to switch on the last opened tab")
            self.driver.switch_to.window(self.tabs_after_click[-1])
            print(f"{datetime.now()}   URL after switch is: {self.driver.current_url}")
            print(f"{datetime.now()}   Title of page is: {self.driver.title}")
            if "metatrader" not in self.driver.title.lower():
                msg = "Title of page don't have 'MetaTrader'. It's not expected page."
                print(f"{datetime.now()}   => {msg}\n")
                Common().pytest_fail(msg)
            print(f"{datetime.now()}   Title of page have 'MetaTrader'")

        else:
            if "metatrader" not in self.driver.title.lower():
                msg = "Title of page don't have 'MetaTrader'. It's not expected page."
                print(f"{datetime.now()}   => {msg}\n")
                Common().pytest_fail(msg)
            print(f"{datetime.now()}   Title of page have 'MetaTrader'")
        return True
