"""
-*- coding: utf-8 -*-
@Time    : 2025/01/18 17:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


WHAT_IS_SHARES_TRADING_LOCATOR = (By.XPATH, "(//div[@class='grid_grid__2D3md grid_gSmMd__aZHWz'])[2]")
SHARES_TRADING_GUIDE_LINK_LOCATOR = (By.CSS_SELECTOR, "[data-type='tiles_w_img_link2_signup']")
BUY_AND_SELL_PHYSICAL_SHARES_LINK_LOCATOR = (By.CSS_SELECTOR, "a[href*='trading-vs-investing']")
MESSAGE_404_LOCATOR = (By.XPATH, "//p[@class='textCenter title404'][contains(text(), '404')]")

class BUG_656(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find block 'What is share trading?', "
                 f"Click link [Shares trading guide], "
                 f"Find the link 'buy and sell physical shares'.")
    def arrange(self, d, link):
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting, visibility block
        self.find_block_scroll_and_check_visibility(
            "What is shares trading?", WHAT_IS_SHARES_TRADING_LOCATOR)

        # Check presenting, visibility link
        self.find_link_scroll_check_visibility_and_clickability(
            "Shares trading guide", SHARES_TRADING_GUIDE_LINK_LOCATOR)

        print(f"{datetime.now()}   Start click link 'Shares trading guide'.")
        self.driver.find_element(*SHARES_TRADING_GUIDE_LINK_LOCATOR).click()
        print(f"{datetime.now()}   End click link 'Shares trading guide'.")
        WebDriverWait(self.driver, 5).until(EC.url_changes(link))

        # Check presenting, visibility link
        self.find_link_scroll_check_visibility_and_clickability(
            "buy and sell physical shares", BUY_AND_SELL_PHYSICAL_SHARES_LINK_LOCATOR)

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):
        print(f"{datetime.now()}   2. Start Act.")

        # click on the link 'buy and sell physical shares'
        print(f"{datetime.now()}   Start to click link 'buy and sell physical shares'")
        link = self.driver.current_url
        self.driver.find_element(*BUY_AND_SELL_PHYSICAL_SHARES_LINK_LOCATOR).click()
        WebDriverWait(self.driver, 10).until(EC.url_changes(link))
        Common().save_current_screenshot(d, "After click on link 'buy and sell physical shares'")

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
