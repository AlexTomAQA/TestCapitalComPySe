"""
-*- coding: utf-8 -*-
@Time    : 2024/10/27 22:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from src.src import CapitalComPageSrc

LINK_GO_CFD_TRADING_GUIDE_LOCATOR = (By.CSS_SELECTOR,
                                     '[data-type="benefits_block_block_go_cfd_trading_guide_btn"]')
LINK_INDICES_LOCATOR = (By.CSS_SELECTOR,
                "h2 ~ p ~ p a[href='http://https://capital.com/en-gb/markets/indices']")
EXPECTED_URL_INDICES = "https://capital.com/en-gb/markets/indices"

class BUG_411(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find and click link 'Go CFD trading guide'. "
                 f"Find link 'indices'.")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find and click link 'Go CFD trading guide'. "
              f"Find link 'indices'.")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting, visibility and clickability link 'Go CFD trading guide'
        self.find_link_scroll_check_visibility_and_clickability(
            'Go CFD trading guide', LINK_GO_CFD_TRADING_GUIDE_LOCATOR
        )
        # Click link 'Go CFD trading guide'
        Common().click_link_and_print(
            d, 'Go CFD trading guide', LINK_GO_CFD_TRADING_GUIDE_LOCATOR
        )

        # Check presenting, visibility and clickability link 'indices'
        self.find_link_scroll_check_visibility_and_clickability(
             'indices', LINK_INDICES_LOCATOR
        )


    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):

        # Click link 'indices'
        Common().click_link_and_print(
            d, 'indices', LINK_INDICES_LOCATOR
        )

    @allure.step(f"{datetime.now()}   3. Start Assert. Opened page")
    def assert_(self, d):
        Common().save_current_screenshot(d, "Opened page after click link 'indices'")
        current_url = d.current_url
        if current_url != EXPECTED_URL_INDICES:
            msg = f"Page doesn't correspond expected link. Current url is: '{current_url}'"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"{msg}")
        msg = f"Page corresponds expected link. But need to check screenshot."
        print(f"{datetime.now()}   => {msg}")
        return True
