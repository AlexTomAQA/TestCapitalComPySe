"""
-*- coding: utf-8 -*-
@Time    : 2025/05/12 21:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from selenium.webdriver.support.ui import WebDriverWait

class BUG_697(BasePage):
    WHAT_IS_INDICES_TRADING_BLOCK = (By.CSS_SELECTOR, '[data-type="tiles_w_img"] [class="grid_grid__2D3md grid_gSmMd__aZHWz"]:nth-child(4) ')
    INDICES_TRADING_GUIDE_LINK = (By.CSS_SELECTOR, '[data-type="tiles_w_img_link4_signup"]')
    VIX_LINK = (By.XPATH, "//a[contains(text(), 'VIX')]")
    SP_100_LINK = (By.XPATH, "//a[contains(text(), 'S&P 100')]")
    TRADE_US_500_TITLE = (By.XPATH, "//h1[contains(text(), 'US 500')]")
    TRADE_US_100_TITLE = (By.XPATH, "//h1[contains(text(), 'US 100')]")


    def __init__(self, driver, link, bid):
        super().__init__(driver, link, bid)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)

    @allure.step(f"{datetime.now()}   Click on [learn about strategies] link")
    def click_indices_trading_guide_link(self):

        # Check presenting, visibility block
        self.find_block_scroll_and_check_visibility(
            "What is indices trading?", self.WHAT_IS_INDICES_TRADING_BLOCK)

        # Check presenting, visibility link
        self.find_link_scroll_check_visibility_and_clickability(
            "Indices trading guide", self.INDICES_TRADING_GUIDE_LINK)

        print(f"{datetime.now()}   Start to click 'Indices trading guide'")
        self.driver.find_element(*self.INDICES_TRADING_GUIDE_LINK).click()
        print(f"{datetime.now()}   End to click 'Indices trading guide'")

        Common().save_current_screenshot(self.driver,
                                         "After click on [Indices trading guide] link")

    @allure.step(f"{datetime.now()}   Click on [VIX] link")
    def click_vix_link(self):

        # Check presenting, visibility link
        self.find_link_scroll_check_visibility_and_clickability(
            "VIX", self.VIX_LINK)

        print(f"{datetime.now()}   Start to click 'VIX'")
        self.driver.find_element(*self.VIX_LINK).click()
        print(f"{datetime.now()}   End to click 'VIX'")

        Common().save_current_screenshot(self.driver,
                                         "After click on [VIX] link")

    @allure.step(f"{datetime.now()}   Click on [S&P 100] link")
    def click_sp_100_link_link(self):

        # Check presenting, visibility link
        self.find_link_scroll_check_visibility_and_clickability(
            "SP_100_LINK", self.SP_100_LINK)

        print(f"{datetime.now()}   Start to click 'SP_100'")
        self.driver.find_element(*self.SP_100_LINK).click()
        print(f"{datetime.now()}   End to click 'SP_100'")

        Common().save_current_screenshot(self.driver,
                                         "After click on [SP_100] link")

    @allure.step(f"{datetime.now()}   Is expected page open?")
    def is_page_us_tech_100_open(self):
        print(f"{datetime.now()}   Start get the URL page.")
        page_url = self.driver.current_url
        print(f"{datetime.now()}   Current url of page is {page_url}.")
        if len(self.driver.find_elements(*self.TRADE_US_500_TITLE)) > 0:
            msg = "Current page 'US Tech 500' instead page 'US Tech 100'."
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        elif len(self.driver.find_elements(*self.TRADE_US_100_TITLE)) > 0:
            msg = "Current page 'US Tech 100'"
            print(f"{datetime.now()}   => {msg}\n")
        else:
            msg = "Current page is not 'Market analysis', need to check screenshot"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
