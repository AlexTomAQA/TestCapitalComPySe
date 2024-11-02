"""
-*- coding: utf-8 -*-
@Time    : 2024/10/20 21:30 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

BTN_LOC = ('xpath', '//a[@class="tag"][text()="Inflation news"]')


class Bug379(BasePage):

    def should_be_present(self):
        print(f'\n{datetime.now()}   Make sure that button is present on the page =>')
        try:
            Wait(self.driver, 2).until(EC.visibility_of_element_located(BTN_LOC))
            print(f'{datetime.now()}   => The button is present')
            return True
        except TimeoutException:
            print(f'{datetime.now()}   => The button is not present')
            return False

    def should_be_visible(self):
        print(f'\n{datetime.now()}   Make sure that button is visible =>')
        try:
            Wait(self.driver, 2).until(EC.visibility_of_element_located(BTN_LOC))
            print(f'{datetime.now()}   => The button is visible')
            return True
        except TimeoutException:
            print(f'{datetime.now()}   => The button is not visible')
            return False

    def should_be_clickable(self):
        print(f'\n{datetime.now()}   Make sure that button is clickable =>')

        try:
            Wait(self.driver, 2).until(EC.element_to_be_clickable(BTN_LOC))
            print(f'{datetime.now()}   => The button is clickable')
            return True
        except TimeoutException:
            print(f'{datetime.now()}   => The button is not clickable')
            return False

    def should_be_existent_and_active_btn(self):
        self.should_be_present()
        self.should_be_visible()
        self.should_be_clickable()
