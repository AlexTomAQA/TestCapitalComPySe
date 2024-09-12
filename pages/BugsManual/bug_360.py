"""
-*- coding: utf-8 -*-
@Time    : 2024/09/03 20:30
@Author  : Kasilà
"""

import random
from datetime import datetime
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class IndicesItaly40(BasePage):
    @allure.step(f"{datetime.now()}   Start test that the same license, SCA (AE country), remains after clicking any"
                 f"of 5 links in the block")
    def arrange(self, d, cur_item_link, cur_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll down to the input field of the block “Indices markets”")
        input_field = self.driver.find_element(By.CSS_SELECTOR, 'input#marketlist_search')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            input_field
        )

        print(f"{datetime.now()}   Search indices in the widget “Trading Instruments")
        input_field.send_keys('IT40')
        it40 = self.driver.find_element(By.XPATH, '//strong[contains(text(), "IT40")]')
        print(f"{datetime.now()}   Click the link “IT40” in the widget “Trading Instrument”")
        it40.click()
        self.wait_for_change_url(cur_link)

    def element_click(self, d, cur_link):
        print(f"\n{datetime.now()}   2. Act")

        print(f"{datetime.now()}   Scroll down to the text block “Italy 40”")
        block_italy40 = self.driver.find_element(By.CSS_SELECTOR, 'div.js-ckeContent')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            block_italy40
        )

        print(f"{datetime.now()}   Click a random link in the text block “Italy 40”")
        ferrari_link = self.driver.find_element(By.CSS_SELECTOR, 'a[href*="/ferrari"]')
        enel_link = self.driver.find_element(By.CSS_SELECTOR, 'a[href*="enel"]')
        unicredit_link = self.driver.find_element(By.CSS_SELECTOR, 'a[href*="unicredit"]')
        eni_link = self.driver.find_element(By.CSS_SELECTOR, 'a[href*="eni"]')
        indices_markets_link = self.driver.find_element(By.CSS_SELECTOR,
                                                        'div.js-ckeContent> p > a[href*="markets/indices"]')

        links_list = [ferrari_link, enel_link, unicredit_link, eni_link, indices_markets_link]
        random_link = random.choice(links_list)
        random_link.click()
        self.wait_for_change_url(cur_link)

    @allure.step(f"{datetime.now()}   Assert")
    def assert_(self):
        print(f"\n{datetime.now()}   3.Assert")
        expected_license = 'United Arab Emirates'
        actual_license = self.driver.find_element(By.CSS_SELECTOR,
                                                  'div:nth-child(1) > span.localization_btn__9zIyt').text
        if expected_license == actual_license:
            print(f"{datetime.now()}   The same license, SCA (AE country), remains after clicking any of 5 links in "
                  f"the block “Italy 40”")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        else:
            Common.pytest_fail(f"#Bug # 55!360 "
                               f"\n"
                               f"Expected result: The same license, SCA (AE country), remains after clicking any of 5 "
                               f"links in the block “Italy 40”"
                               f"\n"
                               f"Actual result: Web pages with URLs of the FCA license are opened after clicking any of "
                               f"5 links in the block “Italy 40”")
