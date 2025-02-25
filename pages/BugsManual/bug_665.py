"""
-*- coding: utf-8 -*-
@Time    : 2025/01/27 22:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


FEATURES_OF_CFD_TRADING_BLOCK = (
    By.CSS_SELECTOR,
    "[data-type='background_banner_block'] ~ .grid_grid__2D3md.grid_gComponent__Xx_xR")
DEDICATED_SUPPORT_24_7_LINK = (By.XPATH, "//a[contains(text(), '24/7')]")
MESSAGE_404_LOCATOR = (By.XPATH, "//p[@class='textCenter title404'][contains(text(), '404')]")

class BUG_665(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find block 'Features of CFD trading', "
                 f"Find the link '24/7 dedicated support'.")
    def arrange(self, d, link):
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting, visibility block
        self.find_block_scroll_and_check_visibility(
            "Features of CFD trading", FEATURES_OF_CFD_TRADING_BLOCK)

        # Check presenting, visibility link
        self.find_link_scroll_check_visibility_and_clickability(
            "24/7 dedicated support", DEDICATED_SUPPORT_24_7_LINK)

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d, link):
        print(f"{datetime.now()}   2. Start Act.")

        print(f"{datetime.now()}   Start click link '24/7 dedicated support'.")
        self.driver.find_element(*DEDICATED_SUPPORT_24_7_LINK).click()
        print(f"{datetime.now()}   End click link '24/7 dedicated support'.")
        WebDriverWait(self.driver, 10).until(EC.url_changes(link))
        Common().save_current_screenshot(d, "After click on link '24/7 dedicated support'")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d, link):
        print(f"{datetime.now()}   3. Start Assert.")
        print(f"{datetime.now()}   Try to find 404 Message on the page")

        if len(self.driver.find_elements(*MESSAGE_404_LOCATOR)) != 0:
            msg = f"Current page have 404 Message. Current URL is {self.driver.current_url}."
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   Current page don't have 404 Message, but need to check screenshot")

        return True
