"""
-*- coding: utf-8 -*-
@Time    : 2024/11/18 13:20
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common

EXPECTED_PAGE = 'https://capital.com/en-ae/learn/market-guides/trade-microsoft'

MARKET_TRADING_GUIDES_BLOCK_LOCATOR = (
    By.CSS_SELECTOR, "[data-type='tiles_w_img'] h2[class='heading_h2__kkLcC heading_noMargins__P5e_q']")
SHARES_TRADING_GUIDE_LINK_LOCATOR = (By.CSS_SELECTOR, "[data-type='tiles_w_img_link2_signup']")
POPULAR_SHARES_TO_TRADE_LOCATOR = (By.CSS_SELECTOR, "[data-id='part_2']")
MICROSOFT_LINK_LOCATOR = (By.XPATH, "//a[contains(text(), 'Microsoft')]")


class BUG_581(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find 'Market trading guides' block, "
                 f"find and click link [Shares trading guide], "
                 f"find 'Popular shares to trade' block, "
                 f"find link [Microsoft]. ")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find 'Market trading guides' block.")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting, visibility block 'Search field'
        self.find_block_scroll_and_check_visibility("Market trading guides",
                                                    MARKET_TRADING_GUIDES_BLOCK_LOCATOR)

        # Check presenting, visibility and clickability link 'Shares trading guide'
        self.find_link_scroll_check_visibility_and_clickability("Shares trading guide",
                                                                SHARES_TRADING_GUIDE_LINK_LOCATOR)
        # Click link 'Shares trading guide'
        Common().click_link_and_print(d, "Shares trading guide", SHARES_TRADING_GUIDE_LINK_LOCATOR)

        # Check presenting, visibility block 'Popular shares to trade'
        self.find_block_scroll_and_check_visibility("Popular shares to trade",
                                                    POPULAR_SHARES_TO_TRADE_LOCATOR)

        # Check presenting, visibility and clickability link 'Microsoft'
        self.find_link_scroll_check_visibility_and_clickability("Microsoft",
                                                                MICROSOFT_LINK_LOCATOR)

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):
        print(f"{datetime.now()}   2. Start Act.")
        # Click link 'Microsoft'
        Common().click_link_and_print(d, 'Microsoft', MICROSOFT_LINK_LOCATOR)
        Common().save_current_screenshot(d, "Opened page after click link 'Microsoft'")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d, link):

        print(f"{datetime.now()}   3. Start Assert.")

        # Check opened page
        print(f"{datetime.now()}   Do current page have 'en-gb'? =>")
        print(f'{datetime.now()}   Current page is: {self.driver.current_url}')
        if 'en-gb' in self.driver.current_url:
            msg = f"Current page opened in FCA License. Current page is: {self.driver.current_url}"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   Current page didn't open in FCA License.")

        print(f"{datetime.now()}   IS opened page in SCA License? =>")
        if not self.current_page_url_contain_the(EXPECTED_PAGE):
            msg = (f"Instead 'expected page opened other page. "
                   f"Expected_page is '{EXPECTED_PAGE}', "
                   f"current page is '{self.driver.current_url}'")
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)

        print(f"{datetime.now()}   => Opened expected page!\n")
        Common.save_current_screenshot(d, f"Opened expected page 'Indices'!")
        self.driver.get(link)
        return True
