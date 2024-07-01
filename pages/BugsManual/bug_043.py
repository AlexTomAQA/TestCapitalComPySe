"""
-*- coding: utf-8 -*-
@Time    : 2024/06/22 19:00 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime

from pages.common import Common
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


HEADER_LOCATOR = ("css selector", "header.cc-header.js-header")
SEARCH_FRAME_LOCATOR = ("css selector", ".cc-search.js-searchRef")
SEARCH_FORM_LOCATOR = ("css selector", ".cc-search__form.js-searchNew")
SEARCH_FIELD_LOCATOR = ("id", "headerSearch")


class SearchField(BasePage):
    def __init__(self, browser, link, bid):
        self.search_btn = None

        super().__init__(browser, link, bid)

    def element_click(self):
        print(f'\n{datetime.now()}   Clicking the Search button...')
        self.search_btn = Wait(self.driver, 5).until(EC.element_to_be_clickable(SEARCH_FIELD_LOCATOR))
        self.search_btn.click()
        print(f'{datetime.now()}   The Search button is clicked')

    def should_be_active_search_field(self):
        print(f'\n{datetime.now()}   Check that the Search field is active...')

        if "active" in self.driver.find_element(*HEADER_LOCATOR).get_attribute("class"):
            if "active" in self.driver.find_element(*SEARCH_FRAME_LOCATOR).get_attribute("class"):
                if "focus" in self.driver.find_element(*SEARCH_FORM_LOCATOR).get_attribute("class"):
                    print(f'{datetime.now()}   The Search field is active')
                    return True
        print(f'{datetime.now()}   The Search field is not active')
        return False

    def perform_search(self, search_string):
        print(f'\n{datetime.now()}   Performing search... =>')
        print(f'{datetime.now()}   => Input search string: {search_string} and submit...')
        self.search_btn.send_keys(search_string)
        self.search_btn.submit()

        if "search" not in self.driver.current_url:
            Common().pytest_fail(f"The Search page is NOT opened")

        print(f'{datetime.now()}   The Search page is opened')
        print(f'{datetime.now()}   Current URL: {self.driver.current_url}')
