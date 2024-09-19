"""
-*- coding: utf-8 -*-
@Time    : 2024/09/19 19:00
@Author  : Kasilà
"""


from datetime import datetime
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


TILE_FAST_ACCOUNT_OPENING_LOCATOR = (By.CSS_SELECTOR, 'div.grid_xs1__UP7xH.grid_md3__Z5n1N > div:nth-child(2)')
LINK_DISCOVER_CFD_TRADING_LOCATOR = (By.CSS_SELECTOR, 'button.link_link__dH6Jd > b')

class DiscoverCFDTtradingLink(BasePage):
    @allure.step(f"{datetime.now()}   Start testing that the text of the link is “Discover CFD trading”")
    def discover_cfd_trading_link(self, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll to tile 'Fast account opening' in the block 'Why choose Capital.com?'")
        tile_fast_account_opening = self.driver.find_element(TILE_FAST_ACCOUNT_OPENING_LOCATOR)
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            tile_fast_account_opening
        )

    def element_pay_attention(self):
        print(f"\n{datetime.now()}   2. Act for link'")

        print(f"{datetime.now()}   Start clicking link")

        link_discover_cfd_trading = self.driver.find_element(LINK_DISCOVER_CFD_TRADING_LOCATOR)
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            link_discover_cfd_trading
        )
        self.driver.execute_script("arguments[0].style.border='3px solid red'", link_discover_cfd_trading)

    def element_click(self):
        print(f"\n{datetime.now()}   2. Act for link'")

        print(f"{datetime.now()}   Start clicking link")

        link_discover_cfd_trading = self.driver.find_element(LINK_DISCOVER_CFD_TRADING_LOCATOR)
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            link_discover_cfd_trading
        )

        link_discover_cfd_trading.click()

    def assert_link(self):
        print(f"\n{datetime.now()}   3. Assert")

        print(f"{datetime.now()}   Is the text of the link “Discover CFD trading”?")

        link_discover_cfd_trading = self.driver.find_element(LINK_DISCOVER_CFD_TRADING_LOCATOR)
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            link_discover_cfd_trading
        )

        actual_link_text = link_discover_cfd_trading.text
        expected_link_text = 'Discover CFD trading'

        if actual_link_text != expected_link_text:
            print(f"{datetime.now()}   The text of the link is '{actual_link_text} and not '{expected_link_text}")
            Common.pytest_fail(f"Bug # 55!371a "
                               f"\n"
                               f"Expected result: the text of the link is “Discover CFD trading”"
                               f"\n"
                               f"Actual result: the text of the link is '{actual_link_text}")
        else:
            print(f"{datetime.now()}   The text of the link is '{expected_link_text}")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)

    def assert_page(self):
        print(f"\n{datetime.now()}   3. Assert")

        print(f"{datetime.now()}   Is the “CFD trading” page opened?")

        current_page = self.driver.current_url
        actual_page_title = self.driver.title
        expected_title = 'CFD Trading'

        if expected_title not in actual_page_title:
            print(f"{datetime.now()}   The “CFD trading” page is not opened")
            Common.pytest_fail(f"Bug # 55!371b"
                               f"\n"
                               f"Expected result: The “CFD trading” page is opened"
                               f"\n"
                               f"Actual result: The '{current_page} is opened")
        else:
            print(f"{datetime.now()}   The “CFD trading” page is opened")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
