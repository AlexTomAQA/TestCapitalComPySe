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
HOW_TO_CREATE_ACCOUNT_LINK_LOCATOR = (By.CSS_SELECTOR, "(//b[contains(text(), 'MT4')])[1]")

class BUG_653(BasePage):

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
        Common().save_current_screenshot(d, "Block 'Connect your account to MT4...'")

        # Check presenting, visibility link
        self.find_link_scroll_check_visibility_and_clickability(
            "CFDs", HOW_TO_CREATE_ACCOUNT_LINK_LOCATOR)

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):
        print(f"{datetime.now()}   2. Start Act.")

        # # Find attribute link in text
        how_to_create_account_link = self.driver.find_element(*HOW_TO_CREATE_ACCOUNT_LINK_LOCATOR)
        #
        # attribute_href_of_link = how_to_create_account_link.get_attribute("href")
        # print(f"{datetime.now()}   Link of 'app' is: {self.attribute_href_of_link}")

        # Define parameters before click
        tabs_before_click = self.driver.window_handles
        print(f"{datetime.now()}   Current qty windows is: {len(tabs_before_click)}")
        self.url_before_click = self.driver.current_url
        print(f"{datetime.now()}   Current link before click: {self.url_before_click}")

        # click on the link 'How to create an MT4 account'
        print(f"{datetime.now()}   Start to click link 'How to create an MT4 account'")
        how_to_create_account_link.click()
        Common().save_current_screenshot(d, "After click on link 'How to create an MT4 account'")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d, link):

        # Define parameters after click
        tabs_after_click = self.driver.window_handles
        print(f"{datetime.now()}   Current qty windows is: {len(tabs_after_click)}")
        current_link_after_click = self.driver.current_url
        print(f"{datetime.now()}   Current link before click: {current_link_after_click}")

        if len(tabs_before_click) != len(tabs_after_click):
            print(f"{datetime.now()}   Numbers of Tabs before and after click are difference")
            print(f"{datetime.now()}   Start to switch on the last opened tab")
            self.driver.switch_to.window(tabs_after_click[-1])
            print(f"{datetime.now()}   URL after switch is: {self.driver.current_url}")
            print(f"{datetime.now()}   Title of page is: {self.driver.title}")
        else:
            if current_link_before_click == current_link_after_click:
                msg = "URLs before and after click 'How to create an MT4 account' are the same"
                print(f"{datetime.now()}   => {msg}\n")
                Common().pytest_fail(msg)
            print(f"{datetime.now()}   URLs before and after click 'How to create an MT4 account' are the same")

        # STOP HERE

        self.wait_for_change_url(self.driver.current_url)

        print(f"{datetime.now()}   New page loaded.")

        print(f"{datetime.now()}   3. Start Assert.")
        print(f"{datetime.now()}   New page loaded but need to check content")
        return True
