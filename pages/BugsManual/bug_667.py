"""
-*- coding: utf-8 -*-
@Time    : 2025/01/29 19:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MARGIN_CALL_EXAMPLE_BLOCK_LOCATOR = (
    By.XPATH, "(//div[@class='grid_grid__2D3md grid_gComponent__Xx_xR'])[2]")
CFDS_LINK_LOCATOR = (By.XPATH, "//li //a[contains(text(), 'CFD')]")
MESSAGE_404_LOCATOR = (By.XPATH, "//p[@class='textCenter title404'][contains(text(), '404')]")

class BUG_667(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find block 'Margin call example', "
                 f"Find the link 'CFDs'.")
    def arrange(self, d, link):
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting, visibility block
        self.find_block_scroll_and_check_visibility(
            "Margin call example", MARGIN_CALL_EXAMPLE_BLOCK_LOCATOR)

        # Check presenting, visibility link
        self.find_link_scroll_check_visibility_and_clickability(
            "CFDs", CFDS_LINK_LOCATOR)

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d, link):
        print(f"{datetime.now()}   2. Start Act.")

        print(f"{datetime.now()}   Start click link 'CFDs'.")
        self.driver.find_element(*CFDS_LINK_LOCATOR).click()
        print(f"{datetime.now()}   End click link 'CFDs'.")
        WebDriverWait(self.driver, 10).until(EC.url_changes(link))
        Common().save_current_screenshot(d, "After click on link 'CFDs'")

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
