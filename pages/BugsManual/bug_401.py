"""
-*- coding: utf-8 -*-
@Time    : 2024/10/28 19:30
@Author  : Kasilà
"""


from datetime import datetime
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class LinkIPO(BasePage):
    @allure.step(f"{datetime.now()}   Start testing page opened after clicking the “initial public offering (IPO)” link")
    def link_ipo(self, d, cur_item_link, cur_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll down to the 'Shares markets' table")
        table = self.driver.find_element(By.CSS_SELECTOR, 'div.table_table__g1rfk')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            table
        )

        print(f"{datetime.now()}   Selected 'RIVN' trading instrument in the 'Shares markets' table")
        p = 1
        while True:
            try:
                rivn = self.driver.find_element(By.LINK_TEXT, 'RIVN')
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    rivn
                )
                rivn.click()
                break
            except NoSuchElementException:
                p += 1
                print(f"{datetime.now()}   Click page {p}")
                pagination = self.driver.find_element(By.LINK_TEXT, str(p))
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    pagination
                )
                pagination.click()

        self.wait_for_change_url(cur_link)

        print(f"{datetime.now()}   Scroll down to the block “Rivian Automotive Inc. Company profile”")
        block_rivn_company_profile = self.driver.find_element(By.CSS_SELECTOR, 'div.content_narrowMedia__I3o5X')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            block_rivn_company_profile
        )


    def element_click(self, d, cur_link):
        print(f"\n{datetime.now()}   2. Act")

        print(f"{datetime.now()}   Click the “initial public offering (IPO)” link")
        ipo_link = self.driver.find_element(By.LINK_TEXT, 'initial public offering (IPO)')
        ipo_link.click()
        self.wait_for_change_url(cur_link)


    @allure.step(f"{datetime.now()}   Assert")
    def assert_url(self, d):
        print(f"{datetime.now()}   3.Assert")
        current_url = self.driver.current_url
        expected_url = 'https://capital.com/en-ae/learn/essentials/what-is-an-ipo'

        if current_url != expected_url:
            print(f"{datetime.now()}   The page “What is an IPO” is not opened")
            Common.pytest_fail(f"# Bug 55!401"
                               f"\n"
                               f"Expected result: The page “What is an IPO” with URL '{expected_url}' is opened"
                               f"\n"
                               f"Actual result: The page with URL '{current_url}' is opened")
        else:
            print(f"{datetime.now()}   The page “What is an IPO” is opened")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
