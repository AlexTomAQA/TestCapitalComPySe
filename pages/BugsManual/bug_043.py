"""
-*- coding: utf-8 -*-
@Time    : 2024/06/22 19:00 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


BUTTON_LOCATOR = ("id", "headerSearch")


class SearchField(BasePage):
    def __init__(self, browser, link, bid):
        self.search_btn = None

        super().__init__(browser, link, bid)

    def open_search_page(self, search_string):
        print(f'\n{datetime.now()}   1. Arrange')
        print(f'\n{datetime.now()}   Opening the Search page...')
        self.search_btn = Wait(self.driver, 5).until(EC.element_to_be_clickable(BUTTON_LOCATOR))
        self.search_btn.click()
        print(f'\n{datetime.now()}   Current search string: {search_string}')
        self.search_btn.send_keys(search_string)
        self.search_btn.submit()
        print(f'\n{datetime.now()}   Search page is opened.')
