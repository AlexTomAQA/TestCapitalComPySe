"""
-*- coding: utf-8 -*-
@Time    : 2024/10/23 19:30
@Author  : Kasilà
"""


from datetime import datetime
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class ValueItems(BasePage):
    @allure.step(f"{datetime.now()}   Start testing value items in the block “Why Open a Corporate Account with "
                 f"Capital.com?”")
    def value_items(self, d, link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        print(f"{datetime.now()}   Click on the “CORPORATE” tab in the Header")
        corporate_tab = self.driver.find_element(By.LINK_TEXT, 'CORPORATE')
        corporate_tab.click()

        print(f"{datetime.now()}   Scroll down to the block “Why Open a Corporate Account with Capital.com?”")
        block_why_open = self.driver.find_element(By.CSS_SELECTOR, 'div.primary_heading__U6ynX')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            block_why_open
        )

    @allure.step(f"{datetime.now()}   Assert")
    def assert_value_traders(self, d):
        print(f"{datetime.now()}   2. Assert")

        item_traders = self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > span.primary_blockTitle__kCa_F')
        self.driver.execute_script("arguments[0].style.border='3px solid red'", item_traders)
        value_item = item_traders.text
        expected_value = '650K+'

        if value_item != expected_value:
            print(f"{datetime.now()}   The value of the 'Traders' item is displayed as '{value_item}' and not "
                  f"'{expected_value}'")
            Common.pytest_fail(f"# Bug 55!399a"
                               f"\n"
                               f"Expected result: The value of the 'Traders' item is displayed as '{expected_value}' "
                               f"\n"
                               f"Actual result: The value of the 'Traders' item is displayed as '{value_item}'")
        else:
            print(f"{datetime.now()}   The value of the 'Traders' item is displayed as '{value_item}'")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)

    @allure.step(f"{datetime.now()}   Assert")
    def assert_value_active_clients_monthly(self, d):
        print(f"{datetime.now()}   2. Assert")

        item_active_clients_monthly = self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > span.primary_blockTitle__kCa_F')
        self.driver.execute_script("arguments[0].style.border='3px solid red'", item_active_clients_monthly)
        value_item = item_active_clients_monthly.text
        expected_value = '82K+'

        if value_item != expected_value:
            print(f"{datetime.now()}   The value of the 'Active clients monthly' item is displayed as '{value_item}' "
                  f"and not '{expected_value}'")
            Common.pytest_fail(f"# Bug 55!399b"
                               f"\n"
                               f"Expected result: The value of the 'Active clients monthly' item is displayed as '{expected_value}'"
                               f"\n"
                               f"Actual result: The value of the 'Active clients monthly' item is displayed as "
                               f"'{value_item}'")
        else:
            print(f"{datetime.now()}   The value of the 'Traders' item is displayed as '{value_item}'")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
