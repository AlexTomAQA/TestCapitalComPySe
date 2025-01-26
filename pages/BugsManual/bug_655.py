"""
-*- coding: utf-8 -*-
@Time    : 2025/01/18 08:00
@Author  : Kasilà
"""


from datetime import datetime
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class ErrorPage(BasePage):
    @allure.step(f"{datetime.now()}   Start testing that the page 'Cryptocurrency Trading' is opened")
    def error_page(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll down to the block 'لأسواق المتاحة' (Our CFD markets)")
        our_cfd_markets_block = self.driver.find_element(By.CSS_SELECTOR, 'div.grid_jcenter__t8Wx_ > div:nth-child(5)')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center"});', our_cfd_markets_block
        )

    def element_click(self):
        print(f"{datetime.now()}   2. Act")
        print(f"{datetime.now()}   Click on the link [أكثر] (More) in the tile 'العملات المشفرة' (Cryptocurrencies)")

        more_link = self.driver.find_element(By.CSS_SELECTOR, 'a[data-type="tiles_w_img_link5_signup"]')
        more_link.click()

    @allure.step(f"{datetime.now()}   Assert")
    def assert_(self):
        print(f"{datetime.now()}   3.Assert")

        expected_url = 'https://capital.com/ar-ae/markets/cryptocurrencies'
        actual_url = self.driver.current_url

        if expected_url == actual_url:
            print(f"{datetime.now()}   The page with {expected_url} URL is opened")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        else:
            Common.pytest_fail(f"#Bug # 55!655 "
                               f"\n"
                               f"Expected result: The page with ({expected_url}) URL is opened"
                               f"\n"
                               f"Actual result: The page with {actual_url} URL is opened")
