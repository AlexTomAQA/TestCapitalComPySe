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
    @allure.step(f"{datetime.now()}   1. Start test that the same license, SCA (AE country), remains after clicking any"
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

        print(f"{datetime.now()}   Scroll down to the text block “Italy 40”")
        block_italy40 = self.driver.find_element(By.CSS_SELECTOR, 'div.js-ckeContent')

        license_list = []
        ferrari_link = self.driver.find_element(By.CSS_SELECTOR, 'a[href*="/ferrari"]')
        ferrari_link.click()
        self.wait_for_change_url(cur_link)
        cur_license = self.driver.find_element(By.XPATH, '//span[contains(text(), "United Kingdom")]')
