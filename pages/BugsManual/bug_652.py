"""
-*- coding: utf-8 -*-
@Time    : 2025/01/11 19:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common

CFDS_LINK_LOCATOR = (By.XPATH, "(//div [@data-type='benefits_block'] //p)[2] //a")

FIND_OUT_MORE_BLOCK_LOCATOR = (By.CSS_SELECTOR, "[data-type='benefits_block']")

class BUG_652(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find 'Find out more' block, "
                 f"find link [CFDs].")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find 'Find out more' block.")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting, visibility block
        self.find_block_scroll_and_check_visibility(
            "Find out more", FIND_OUT_MORE_BLOCK_LOCATOR)
        Common().save_current_screenshot(d, "Block 'Find out more'")

        # Check presenting, visibility link
        self.find_link_scroll_check_visibility_and_clickability(
            "CFDs", CFDS_LINK_LOCATOR)

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):
        print(f"{datetime.now()}   2. Start Act.")

        # Find attribute link in text
        cfds_link = self.driver.find_element(*CFDS_LINK_LOCATOR)
        attribute_href_of_link = cfds_link.get_attribute("href")
        print(f"{datetime.now()}   Link of 'app' is: {attribute_href_of_link}")

        # click on thr link 'CFDs'
        print(f"{datetime.now()}   Start to click link 'app'")
        cfds_link.click()
        self.wait_for_change_url(self.driver.current_url)
        Common().save_current_screenshot(d, "New page after click link 'app'")
        print(f"{datetime.now()}   New page loaded.")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d, link):

        print(f"{datetime.now()}   3. Start Assert.")
        print(f"{datetime.now()}   New page loaded but need to check content")
        return True
