"""
-*- coding: utf-8 -*-
@Time    : 2024/12/27 21:30
@Author  : Kasilà
"""


from datetime import datetime
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class LicenseChange(BasePage):
    @allure.step(f"{datetime.now()}   Start testing that the same license remains")
    def license_change(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll down to the block 'Trading calculator'")
        trading_calculator_block = self.driver.find_element(By.CSS_SELECTOR, 'div.componentsContainer > div:nth-child(4)')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center"});', trading_calculator_block
        )

    def element_click(self):
        print(f"{datetime.now()}   2. Act")
        print(f"{datetime.now()}   Click on the link “overnight funding, spread costs”")

        overnight_link = self.driver.find_element(By.XPATH, '//a[contains(text(), "overnight funding, spread costs")]')
        overnight_link.click()

    @allure.step(f"{datetime.now()}   Assert")
    def assert_(self):
        print(f"{datetime.now()}   3.Assert")

        expected_country = 'Australia'
        actual = self.driver.find_element(By.CSS_SELECTOR,
                                          'div.localization_item__KwMiX:nth-child(1) > button')
        actual_country = actual.text
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center"});',
            actual
        )
        self.driver.execute_script("arguments[0].style.border='3px solid red'", actual)

        if expected_country == actual_country:
            print(f"{datetime.now()}   The page with the selected country ({expected_country}) is opened")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        else:
            Common.pytest_fail(f"#Bug # 55!627 "
                               f"\n"
                               f"Expected result: The page with selected country ({expected_country}) is opened"
                               f"\n"
                               f"Actual result: The page with country ({actual_country}) other than the selected one "
                               f"({expected_country}) is opened")
