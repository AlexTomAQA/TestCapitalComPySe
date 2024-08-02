"""
-*- coding: utf-8 -*-
@Time    : 2024/07/30 19:00
@Author  : Kasilà
"""

from datetime import datetime
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common

class LearnMoreAbout(BasePage):
    def learn_more_about(self, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        learn_more_about_link = self.driver.find_element(By.CSS_SELECTOR,
                                                         'a[href*="learn/market-guides/what-is-cryptocurrency-trading"]')
        if learn_more_about_link:
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                learn_more_about_link
            )
            learn_more_about_link.click()
            self.wait_for_change_url()

    def assert_(self):
        print(f"\n{datetime.now()}   2. Assert")

        print(f'{datetime.now()}   Current page is: {self.driver.current_url}')

        if not self.current_page_url_contain_the(
                'https://capital.com/ar-ae/learn/market-guides/what-is-cryptocurrency-trading'):
            print(f"{datetime.now()}   The page 'What is cryptocurrency trading' is not opened")
            Common.pytest_fail(f"#Bug # 55!270 "
                               f"\n"
                               f"Expected result: The page 'What is cryptocurrency trading' is opened"
                               f"\n"
                               f"Actual result: The page 'What is cryptocurrency trading' is not opened")
        else:
            print(f"{datetime.now()}   The page 'What is cryptocurrency trading' is opened")

            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
