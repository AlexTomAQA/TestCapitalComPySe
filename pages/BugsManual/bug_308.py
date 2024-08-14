"""
-*- coding: utf-8 -*-
@Time    : 2024/08/13 16:45
@Author  : Kasilà
"""

from datetime import datetime
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common

class InvestmateAppPage(BasePage):
    @allure.step(f"{datetime.now()}   1. Start test that the 'Investmate' app page is opened on Google Play/App Store.")
    def investment_app_page(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        block_investment = self.driver.find_element(By.CSS_SELECTOR,
                                            'div:nth-child(2) > div > div > div.grid_grid__2D3md.grid_gXsMd__43_QE')

        print(f"{datetime.now()}   Scroll to block_investment")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            block_investment
        )

        link_education_app_investmate = self.driver.find_element(By.CSS_SELECTOR,
                'div:nth-child(2) > div > div > div.grid_grid__2D3md.grid_gXsMd__43_QE > div > p > a:nth-child(2)')

        if link_education_app_investmate:
            link_education_app_investmate.click()
            print(f"{datetime.now()}   Link is clicked")


    def assert_(self, d):
        print(f"{datetime.now()}   2. Assert")

        print(f'{datetime.now()}   Current page is: {self.driver.current_url}')
        expexted_page_title_google_play = "investmate - Android Apps on Google Play"
        expexted_page_title_apple_store = "Investmate - learn to trade on the App&nbsp;Store"

        actual_page_title = self.driver.title
        if actual_page_title == expexted_page_title_google_play:
            print(f"{datetime.now()}   'Investmate' app page is opened on Google Play")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        elif actual_page_title == expexted_page_title_apple_store:
            print(f"{datetime.now()}   'Investmate' app page is opened on App Store")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        else:
            Common.pytest_fail(f"#Bug # 55!308 "
                               f"\n"
                               f"Expected result: The 'Investmate' app page is opened on Google Play/App Store."
                               f"\n"
                               f"Actual result: The 'Investmate' app page is not opened on Google Play/App Store.")
