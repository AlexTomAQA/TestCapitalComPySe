"""
-*- coding: utf-8 -*-
@Time    : 2024/11/01 20:30
@Author  : Artem Dashkov
"""
import time

import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common

BUG_NUMBER = '422'
LINK_MOST_POPULAR_MARKETS_TO_TRADE_LOCATOR = (By.XPATH,
                           "//a[contains(text(), 'most popular markets')]")

LINK_JPMORGAN_LOCATOR = (By.XPATH, "//a[contains(text(), 'JPMorgan Chase & Co')]")
LINK_EXXON_MOBIL_LOCATOR = (By.XPATH, "//a[contains(text(), 'Exxon Mobil')]")
LINK_IBM_LOCATOR = (By.XPATH, "//a[contains(text(), 'IBM')]")

ACCORDION_HOW_DO_YOU_TRADE_LOCATOR = (By.XPATH, "(//summary[@data-type='faq_chevron'])[2]")
LINK_LOCATOR = ()

class BUG_422(BasePage):

    @allure.step(f"{datetime.now()}   Start Arrange: find and click link 'the most popular markets to trade', "
                 f"find links [JPMorgan Chase & Co]/[Exxon Mobil]/[IBM]")
    def arrange(self, d, link, link_for_check):
        print(f"\n{datetime.now()}   1.1. Start Arrange: find and click link 'the most popular markets to trade'")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting, visibility and clickability link 'the most popular markets to trade'
        self.find_link_scroll_check_visibility_and_clickability(
            'the most popular markets to trade', LINK_MOST_POPULAR_MARKETS_TO_TRADE_LOCATOR
        )
        # Click link 'the most popular markets to trade'
        Common().click_link_and_print(
            d, 'the most popular markets to trade', LINK_MOST_POPULAR_MARKETS_TO_TRADE_LOCATOR
        )

        print(f"\n{datetime.now()}   1.2. Start Arrange: find and click link 'CFDs' or 'exchange traded funds (ETFs)'")
        print(f"\n{datetime.now()}   Target Link is: {link_for_check}.")
        global LINK_LOCATOR
        match link_for_check:
            case 'JPMorgan Chase & Co':
                LINK_LOCATOR = LINK_JPMORGAN_LOCATOR
            case 'ETFs':
                LINK_LOCATOR = LINK_EXXON_MOBIL_LOCATOR
            case 'IBM':
                LINK_LOCATOR = LINK_IBM_LOCATOR

        # Check presenting, visibility and clickability link 'the most popular markets to trade'
        self.find_link_scroll_check_visibility_and_clickability(
            f'{link_for_check}', LINK_LOCATOR
        )

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d, link_for_check):

        # Click link
        Common().click_link_and_print(
            d, f'{link_for_check}', LINK_LOCATOR
        )

    @allure.step(f"{datetime.now()}   3. Start Assert. Check message '404 not found' on the opened page")
    def assert_(self, d):
        print(f"{datetime.now()}   3. Start Assert. Check message '404 not found' on the opened page")

        # Check presenting 'en-gb' in url on the opened page
        print(f"{datetime.now()}   IS 'en-gb' in url on the opened page?")
        if 'en-gb' in self.driver.current_url:
            msg = f"Opened page have FCA license insted of SCA, url is: {self.driver.current_url}"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        elif 'en-ae' in self.driver.current_url:
            if ('cfd-trading' or 'top-etfs') in self.driver.current_url:
                print(f"{datetime.now()}   Current page opened in necessary license but need check screenshot")
                Common.save_current_screenshot(d, f"Need to check content of opened page")
            else:
                msg = f"Need to check content of opened page, url is: {self.driver.current_url}"
                print(f"{datetime.now()}   => {msg}")
                Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        else:
            msg = f"Need to check content of opened page, url is: {self.driver.current_url}"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        return True
