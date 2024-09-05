"""
-*- coding: utf-8 -*-
@Time    : 2024/09/03 20:30
@Author  : Kasilà
"""

from datetime import datetime
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class IndicesItaly40(BasePage):
    @allure.step(f"{datetime.now()}   Start test that the same license, SCA (AE country), remains after clicking any"
                 f"of 5 links in the block")
    def IndicesItaly40(self, d, cur_item_link, cur_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll down to the pagination of the block “Indices markets”")
        pagination = self.driver.find_element(By.CSS_SELECTOR, 'nav[aria-label="pagination"]')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            pagination
        )

        print(f"{datetime.now()}   Navigate to the 2nd page of the widget “Trading Instruments")
        next_page = self.driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Go to the next page"]')
        next_page.click()
        self.wait_for_change_url(cur_link)

        print(f"{datetime.now()}   Click the link “IT40” in the widget “Trading Instrument”")
        instrument_it40 = self.driver.find_element(By.CSS_SELECTOR, 'a[href*="/ftse-borsa-italiana-index-40-index"]')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            instrument_it40
        )
        instrument_it40.click()
        self.wait_for_change_url(cur_link)

    def element_click(self, d, cur_link):
        print(f"\n{datetime.now()}   2. Act")

        print(f"{datetime.now()}   Scroll down to the text block “Italy 40”")
        block_italy40 = self.driver.find_element(By.CSS_SELECTOR, 'div.js-ckeContent')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            block_italy40
        )

        ferrari_link = self.driver.find_element(By.CSS_SELECTOR, 'a[href*="/ferrari"]')
        enel_link = self.driver.find_element(By.CSS_SELECTOR, 'a[href*="enel"]')
        unicredit_link = self.driver.find_element(By.CSS_SELECTOR, 'a[href*="unicredit"]')
        eni_link = self.driver.find_element(By.CSS_SELECTOR, 'a[href*="eni"]')
        indices_markets_link = self.driver.find_element(By.CSS_SELECTOR, 'div.js-ckeContent> p > a[href*="markets/indices"]')

        links_list = [ferrari_link, enel_link, unicredit_link, eni_link, indices_markets_link]
        actual_license_list = []
        for n in links_list:
            n.click()
            self.wait_for_change_url(cur_link)
            cur_license = self.driver.find_element(By.CSS_SELECTOR, 'span.localization_btn__9zIyt')
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                cur_license
            )
            cur_license_text = cur_license.text
            actual_license_list += [cur_license_text]

        actual_links_license_dict = dict(zip(links_list, actual_license_list))
        return actual_links_license_dict

class AssertLicenseList(BasePage,):
    @allure.step(f"{datetime.now()}   Assert actual and expected license")
    def assert_license_list(self, actual_links_license_dict):
        expected_license_dict = {
            'ferrari_link': 'United Arab Emirates',
            'enel_link': 'United Arab Emirates',
            'unicredit_link': 'United Arab Emirates',
            'eni_link': 'United Arab Emirates',
            'indices_markets_link': 'United Arab Emirates'}
        print(expected_license_dict)
        print(actual_links_license_dict)
        if expected_license_dict == actual_links_license_dict:
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