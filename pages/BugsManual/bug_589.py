"""
-*- coding: utf-8 -*-
@Time    : 2024/11/23 19:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from src.src import CapitalComPageSrc

HOW_TO_AVOID_A_MARGIN_CLOSE_OUT_BLOCK_LOCATOR = (
    By.XPATH, "(//div[@data-type='benefits_block'] //h2[@class='heading_h2__kkLcC heading_noMargins__P5e_q'])[3]"
)
CHARGES_AND_FEES_PAGE_LINK_LOCATOR = (By.CSS_SELECTOR, "div[class*='helpers_content'] a[href*='fees-and-charges']")
ERROR_16_LOCATOR = (By.CSS_SELECTOR, "[class='error-code']")

class BUG_589(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find 'How to avoid a margin close-out' block, "
                 f"find link [charges and fees page].")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find 'How to avoid a margin close-out' block.")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting, visibility block 'How to avoid a margin close-out'
        self.find_block_scroll_and_check_visibility("How to avoid a margin close-out",
                                                    HOW_TO_AVOID_A_MARGIN_CLOSE_OUT_BLOCK_LOCATOR)

        # Check presenting, visibility and clickability link 'charges and fees page'
        self.find_link_scroll_check_visibility_and_clickability("charges and fees page",
                                                                CHARGES_AND_FEES_PAGE_LINK_LOCATOR)

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):
        print(f"{datetime.now()}   2. Start Act.")
        # Click link 'charges and fees page'
        Common().click_link_and_print(d, 'charges and fees page', CHARGES_AND_FEES_PAGE_LINK_LOCATOR)
        Common().save_current_screenshot(d, "Opened page after click link 'charges and fees page'")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d, link):

        print(f"{datetime.now()}   3. Start Assert.")

        # Check opened page
        print(f'{datetime.now()}   Current page is: {self.driver.current_url}')
        if len(self.driver.find_elements(*ERROR_16_LOCATOR)) == 1:
            msg = f"Current page opened with ERROR_16"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   Current page don't have ERROR_16, but need to analyze page screen.")

        self.driver.get(CapitalComPageSrc.URL_NEW_AR_AE)
        return True
