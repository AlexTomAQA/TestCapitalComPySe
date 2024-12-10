"""
-*- coding: utf-8 -*-
@Time    : 2024/12/10 19:30
@Author  : Kasilà
"""


import random
from datetime import datetime
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class PageCFDCalcDisplay(BasePage):
    @allure.step(f"{datetime.now()}   Start testing 'CFD calculator' page display")
    def page_cfd_calc_display(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll down to the 'How to start trading' block")
        how_to_start_block = self.driver.find_element(By.CSS_SELECTOR, '.list-way')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            how_to_start_block
        )

        print(f"{datetime.now()}   Click on the [Sign up] button")
        signup_btn = self.driver.find_element(By.CSS_SELECTOR, 'a[data-type="plain_button"]')
        signup_btn.click()

    def element_click(self):
        print(f"\n{datetime.now()}   2. Act")

        print(f"{datetime.now()}   Close the “Sign up” form")
        self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="SIGN_UP_close"]').click()

    @allure.step(f"{datetime.now()}   Assert")
    def assert_(self):
        print(f"{datetime.now()}   3.Assert")

        try:
            spinner = self.driver.find_element(By.CSS_SELECTOR, '.pageLoader_loader__QsVJC')
            self.element_is_visible((By.CSS_SELECTOR, '.pageLoader_loader__QsVJC'), 2)
            self.driver.execute_script("arguments[0].style.border='3px solid red'", spinner)
            print(f"{datetime.now()}   Spinner is visible")
            Common.pytest_fail("# Bug # 55!612"
                               "\n"
                               "Expected result: Loading spinner is not displayed"
                               "\n"
                               "Actual result: Loading spinner is displayed" )
        except NoSuchElementException:
            print(f"{datetime.now()}   Spinner is not visible")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
