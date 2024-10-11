"""
-*- coding: utf-8 -*-
@Time    : 2024/10/08 17:30
@Author  : Kasilà
"""


from datetime import datetime
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class ContactUs(BasePage):
    @allure.step(f"{datetime.now()}   Start testing that the 'Contact us' page is opened")
    def contact_us_in_confidence(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll to the 'Your vulnerability risk' block")
        your_vulnerability_risk_block = self.driver.find_element(By.CSS_SELECTOR, 'h2[data-id="part_1"]')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            your_vulnerability_risk_block
        )

    def element_click(self, d, cur_link):
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   Click the “contact us in confidence” link")

        contact_us_in_confidence_link = self.driver.find_element(By.CSS_SELECTOR, 'div > p:nth-child(9) > a')
        ActionChains(d)\
            .move_to_element(contact_us_in_confidence_link)\
            .click(contact_us_in_confidence_link)\
            .perform()
        self.wait_for_change_url(cur_link)

    @allure.step(f"{datetime.now()}   Assert")
    def assert_page(self, d):
        print(f"{datetime.now()},   3. Assert")

        actual_url = self.driver.current_url

        if actual_url != 'https://capital.com/ar-ae/contact-us':
            print(f"{datetime.now()}   The 'Contact us' page is not opened")
            Common.pytest_fail(f"Bug # 55!386"
                               f"\n"
                               f"Expected result: The page 'https://capital.com/ar-ae/contact-us' is opened"
                               f"\n"
                               f"Actual result: The page '{actual_url}' is opened")
        else:
            print(f"{datetime.now()}   The 'https://capital.com/ar-ae/contact-us' page is opened")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
