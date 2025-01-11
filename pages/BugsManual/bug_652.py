"""
-*- coding: utf-8 -*-
@Time    : 2025/01/11 19:00
@Author  : Artem Dashkov
"""
import allure
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from src.src import CapitalComPageSrc

RISK_MANAGEMENT_TOOLS_BLOCK_LOCATOR = (
    By.XPATH,
    "(//div [@class='grid_grid__2D3md grid_md__Udd_J grid_gSmLg__B_vHD grid_center__cwyYf grid_fit__9qW_j'])[6]"
)

OUR_TRADING_APP_BLOCK_LOCATOR = (By.XPATH,
    "//div[@class='white cardsImage_bg__4z0G6'][2] //span //p")

APP_LINK_LOCATOR = (By.XPATH,
                    "//div[@class='white cardsImage_bg__4z0G6'][2] //span //p //a")
TRAILING_STOP_LOSS_LINK_LOCATOR = (By.CSS_SELECTOR, "a[href*='capitalcysec.zendesk.com']")
HELP_CENTER_NO_LONGER_EXISTS_LOCATOR = (By.XPATH, "//h1[contains(text(), 'Oops, this help center no longer exists')]")

class BUG_652(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find 'Our trading app' block, "
                 f"find link [Trailing stop loss].")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find 'Our trading app' block.")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting, visibility block
        self.find_block_scroll_and_check_visibility(
            "Our trading app", OUR_TRADING_APP_BLOCK_LOCATOR)

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):
        print(f"{datetime.now()}   2. Start Act.")

        Common().save_current_screenshot(d, "Block 'Our trading app'")
        if len(self.driver.find_elements(*APP_LINK_LOCATOR)) == 0:
            msg = f"The link 'app' is not present"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)

        # Find attribute link in text
        app_link = self.driver.find_element(*APP_LINK_LOCATOR)
        attribute_href_of_link = app_link.get_attribute("href")
        print(f"{datetime.now()}   Link of 'app' is: {attribute_href_of_link}")

        print(f"{datetime.now()}   Start to click link 'app'")
        app_link.click()
        self.wait_for_change_url(self.driver.current_url)
        Common().save_current_screenshot(d, "New page after click link 'app'")
        print(f"{datetime.now()}   New page loaded.")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d, link):

        print(f"{datetime.now()}   3. Start Assert.")
        print(f"{datetime.now()}   New page loaded but need to check content")
        return True
