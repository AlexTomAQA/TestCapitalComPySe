"""
-*- coding: utf-8 -*-
@Time    : 2024/11/14 20:00
@Author  : Kasilà
"""

from datetime import datetime
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class Links(BasePage):
    @allure.step(f"{datetime.now()}   Start testing links in the block 'What is a contract for difference (CFD)?'")
    def arrange(self, cur_item_link, link):
        print(f"{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll down to the block 'Read more before you trade'")
        read_more_before_block = self.driver.find_element(By.CSS_SELECTOR, 'div.componentsContainer > div:nth-child(7) > div')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            read_more_before_block
        )

        print(f"{datetime.now()}   Click the link [Go CFD trading guide]")
        go_cfd_link = self.driver.find_element(By.CSS_SELECTOR, 'a[href*="ways-to-trade/cfd-trading/what-is-cfd-trading"]')
        go_cfd_link.click()
        self.wait_for_change_url(link)

        print(f"{datetime.now()}   Scroll down to the block 'What is a contract for difference (CFD)?'")
        what_is_a_contract_block = self.driver.find_element(By.CSS_SELECTOR, 'div.content_narrowMedia__I3o5X > p:nth-child(3)')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            what_is_a_contract_block
        )

    @allure.step(f"{datetime.now()}   Assert")
    def assert_links(self):
        print(f"{datetime.now()}   2.Assert")

        expected_links_list = ('cryptocurrencies', 'stocks', 'indices', 'commodities', 'forex')
        actual_links = self.driver.find_elements(By.CSS_SELECTOR, 'div.content_narrowMedia__I3o5X > p:nth-child(3) > a')
        actual_links_list = [link.text for link in actual_links]

        missing_links = set(expected_links_list) - set(actual_links_list)

        if set(actual_links_list) != set(expected_links_list):
            print(f"{datetime.now()}   The words {missing_links} are simple text")
            Common.pytest_fail('# Bug 55!432 '
                               '\n'
                               'Expected result: The words [stocks], [indices], [commodities], [forex]  are links.'
                               '\n'
                               f'Actual result: The words {missing_links} are simple text')
