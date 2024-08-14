"""
-*- coding: utf-8 -*-
@Time    : 2024/08/13 16:45
@Author  : Kasilà
"""

from datetime import datetime
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common

class InvestmateAppPage(BasePage):
    @allure.step(f"{datetime.now()}   1. Start test that the 'Investmate' app page is opened on Google Play/App Store "
                 f"OR “educational app Investmate” is presented as simple text.")
    def investmate_app_page(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Look for the block_investmate and scroll to it")
        block_investmate = self.driver.find_element(By.CSS_SELECTOR,
                                            'div:nth-child(2) > div > div > div.grid_grid__2D3md.grid_gXsMd__43_QE')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            block_investmate
        )

        print(f"{datetime.now()}   Check that the 'educational app Investmate' is a link or simple text")
        try:
            simple_text_educational_app_investmate = self.driver.find_element(By.XPATH,
                                                              '//p[contains(text(), "educational app Investmate")]')
            if simple_text_educational_app_investmate:
                print(f"{datetime.now()}   'educational app Investmate' is presented as simple text")
                allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
                Common.pytest_skip("'educational app Investmate' link is presented as simple text")
        except NoSuchElementException:
            print(f"{datetime.now()}   'educational app Investmate' is presented not as simple text")
            link_educational_app_investmate = self.driver.find_element(By.XPATH,
                                                              '//a[contains(text(), "educational app Investmate")]')
            if link_educational_app_investmate:
                print(f"{datetime.now()}   'educational app Investmate' is presented as a link")
                link_educational_app_investmate.click()
                print(f"{datetime.now()}   Link 'educational app Investmate' is clicked")


    @allure.step('Checking that the "Investmate" app page is opened on Google Play/App Store.')
    def assert_(self, d):
        print(f"{datetime.now()}   2. Assert")

        expexted_page_title_google_play = "investmate - Android Apps on Google Play"
        expexted_page_title_apple_store = "Investmate - learn to trade on the App&nbsp;Store"

        current_page = self.driver.current_url
        actual_page_title = self.driver.title
        if actual_page_title == expexted_page_title_google_play:
            print(f"{datetime.now()}   'Investmate' app page is opened on Google Play")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        elif actual_page_title == expexted_page_title_apple_store:
            print(f"{datetime.now()}   'Investmate' app page is opened on App Store")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        else:
            print(f'{datetime.now()}   Current page is: {current_page}')
            Common.pytest_fail(f"#Bug # 55!308 "
                               f"\n"
                               f"Expected result: The 'Investmate' app page is opened on Google Play/App Store OR "
                               f"'educational app Investmate' is presented as simple text."
                               f"\n"
                               f"Actual result: “educational app Investmate” is presented as link and after clicking on "
                               f"it the 'Investmate' app page is not opened on Google Play/App Store. "
                               f"Current page is: {current_page}")
