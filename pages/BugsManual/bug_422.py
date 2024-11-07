"""
-*- coding: utf-8 -*-
@Time    : 2024/11/01 20:30
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from pages.base_page import BasePage
from pages.common import Common

BUG_NUMBER = '422'
LINK_MOST_POPULAR_MARKETS_TO_TRADE_LOCATOR = (By.XPATH,
                           "//a[contains(text(), 'most popular markets')]")

LINK_JPMORGAN_LOCATOR = (By.XPATH, "//a[contains(text(), 'JPMorgan Chase & Co')]")
LINK_EXXON_MOBIL_LOCATOR = (By.XPATH, "//a[contains(text(), 'Exxon Mobil')]")
LINK_IBM_LOCATOR = (By.XPATH, "//a[contains(text(), 'IBM')]")

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

        print(f"\n{datetime.now()}   1.2. Start Arrange: find and click link [JPMorgan Chase & Co]/[Exxon Mobil]/[IBM]")
        print(f"\n{datetime.now()}   Target link is: {link_for_check}.")
        global LINK_LOCATOR
        match link_for_check:
            case 'JPMorgan Chase & Co':
                LINK_LOCATOR = LINK_JPMORGAN_LOCATOR
            case 'ETFs':
                LINK_LOCATOR = LINK_EXXON_MOBIL_LOCATOR
            case 'IBM':
                LINK_LOCATOR = LINK_IBM_LOCATOR

        # Check presenting, visibility and clickability link
        self.find_link_scroll_check_visibility_and_clickability(
            f'{link_for_check}', LINK_LOCATOR
        )

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d, link_for_check):

        # Click link
        Common().click_link_and_print(
            d, f'{link_for_check}', LINK_LOCATOR
        )
        Common.save_current_screenshot(d, f"Screen page after click '{link_for_check}'")

    @allure.step(f"{datetime.now()}   3. Start Assert")
    def assert_(self, d, link_for_check):
        print(f"{datetime.now()}   3. Start Assert")

        try:
            # try to reopen page
            self.driver.get(self.driver.current_url)
        except WebDriverException:
            msg = f"No access to page after click '{link_for_check}'"
            Common.save_current_screenshot(d, msg)
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER}: {msg}")
        Common.save_current_screenshot(d, f"Screen page after reopen page: '{self.driver.current_url}'")
        print(f"{datetime.now()}   Current page opened but need check screenshot")
        return True
