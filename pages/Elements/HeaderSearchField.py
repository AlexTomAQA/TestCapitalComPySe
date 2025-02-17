"""
-*- coding: utf-8 -*-
@Time    : 2024/06/22 19:00 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime
from random import randint

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


HEADER_LOCATOR = ("css selector", "header.cc-header.js-header")
SEARCH_FRAME_LOCATOR = ("css selector", ".cc-search.js-searchRef")
SEARCH_FORM_LOCATOR = ("css selector", ".cc-search__form.js-searchNew")
SEARCH_FIELD_LOCATOR = ("id", "headerSearch")
SEARCH_ITEM_LOCATOR = ("css selector", ".global-search__item h4")


class SearchField(BasePage):
    def __init__(self, browser, link, bid):
        self.search_btn = None

        super().__init__(browser, link, bid)

    def element_click(self):
        print(f'\n{datetime.now()}   Clicking the Search button =>')
        self.search_btn = Wait(self.driver, 5).until(EC.element_to_be_clickable(SEARCH_FIELD_LOCATOR))
        self.search_btn.click()
        print(f'{datetime.now()}   => The Search button is clicked')

    def should_be_active_search_field(self):
        print(f'\n{datetime.now()}   Check that the Search field is active =>')

        if "active" in self.driver.find_element(*HEADER_LOCATOR).get_attribute("class"):
            if "active" in self.driver.find_element(*SEARCH_FRAME_LOCATOR).get_attribute("class"):
                if "focus" in self.driver.find_element(*SEARCH_FORM_LOCATOR).get_attribute("class"):
                    print(f'{datetime.now()}   => The Search field is active')
                    return True
        print(f'{datetime.now()}   => The Search field is not active')
        return False

    def perform_search(self, search_string):
        print(f'\n{datetime.now()}   Performing search')
        print(f'{datetime.now()}   Input search string "{search_string}" and submit =>')
        self.search_btn.send_keys(search_string)
        self.search_btn.submit()
        print(f'{datetime.now()}   => The Search page is opened')
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')

    def should_be_any_search_result(self):
        print(f'\n{datetime.now()}   Check if there is any search result is present on the Search page => ')
        try:
            Wait(self.driver, 5).until(EC.element_to_be_clickable(SEARCH_ITEM_LOCATOR))
        except TimeoutException:
            print(f'{datetime.now()}   => No search results are present on the page')
            return False
        print(f'{datetime.now()}   => At least one search result is present')
        return True

    def click_random_search_result_item(self):
        print(f'\n{datetime.now()}   Clicking any search item =>')
        search_items_list = self.driver.find_elements(*SEARCH_ITEM_LOCATOR)
        random_search_item = search_items_list[randint(0, len(search_items_list) - 1)]
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            random_search_item
        )
        Wait(self.driver, 5).until(EC.element_to_be_clickable(random_search_item)).click()
        print(f'\n{datetime.now()}   => Item is clicked, corresponding page is opened')
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')
