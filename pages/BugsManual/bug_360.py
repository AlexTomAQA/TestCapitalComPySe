"""
-*- coding: utf-8 -*-
@Time    : 2024/09/03 20:30
@Author  : Kasilà
"""

import random
import time
from datetime import datetime
import allure
from selenium.common import NoSuchElementException
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


    def arrange_v2(self, d, cur_item_link, cur_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll down to the table “Indices markets”")
        indices_markets_table = self.driver.find_element(By.CSS_SELECTOR, 'div.table_table__g1rfk')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            indices_markets_table
        )

        p = 1
        while p <= 3:
            try:
                it40 = self.driver.find_element(By.LINK_TEXT, 'IT40')
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    it40
                )
                it40.click()
                break
            except NoSuchElementException:
                p += 1
                print(f"{datetime.now()}   Click page {p}")
                pagination = self.driver.find_element(By.LINK_TEXT, str(p))
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    pagination
                )
                pagination.click()

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
        expected_country = 'United Arab Emirates'
        actual = self.driver.find_element(By.CSS_SELECTOR,
                                          'div:nth-child(1) > span.localization_btn__9zIyt')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            actual
        )
        time.sleep(2)
        actual_country = actual.text

        if expected_country == actual_country:
            print(f"{datetime.now()}   The page with the selected country ({expected_country}) is opened")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        else:
            Common.pytest_fail(f"#Bug # 55!360 "
                               f"\n"
                               f"Expected result: The page with the selected country ({expected_country}) is opened"
                               f"\n"
                               f"Actual result: The page with a country ({actual_country}) other than the selected one "
                               f"({expected_country}) is opened")
