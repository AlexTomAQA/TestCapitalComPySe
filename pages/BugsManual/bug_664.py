"""
-*- coding: utf-8 -*-
@Time    : 2025/01/30 20:30
@Author  : Kasilà
"""


from datetime import datetime
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class Bug664(BasePage):
    @allure.step(f"{datetime.now()}   Start testing")
    def arrange(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll down to the “Spread” block")
        spread_block = self.driver.find_element(By.CSS_SELECTOR, 'div > p:nth-child(12) > a')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center"});', spread_block
        )

    def element_click(self):
        print(f"{datetime.now()}   2. Act")
        print(f"{datetime.now()}   Click on the link  'Spread'")

        spread_link = self.driver.find_element(By.CSS_SELECTOR, 'div > p:nth-child(12) > a')
        spread_link.click()

    @allure.step(f"{datetime.now()}   Assert")
    def assert_(self):
        print(f"{datetime.now()}   3.Assert")

        expected_url = 'https://capital.com/el-gr/ways-to-trade/fees-and-charges'
        actual_url = self.driver.current_url

        if actual_url != expected_url:
            Common.pytest_fail(f"#Bug # 55!664 "
                               f"\n"
                               f"Expected result: The page “Χρεώσεις και προμήθειες” (Fees and Charges) with URL "
                               f"'{expected_url}' is displayed"
                               f"\n"
                               f"Actual result: The page with URL '{actual_url}' is displayed")
        else:
            print(f"{datetime.now()}   The page “Χρεώσεις και προμήθειες” (Fees and Charges) with URL '{expected_url}' "
                  f"is displayed")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
