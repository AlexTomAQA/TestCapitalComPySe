"""
-*- coding: utf-8 -*-
@Time    : 2024/08/31 16:09 GMT+3
@Author  : podchasova11
"""
from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

HELP_CENTER_LOC = ('xpath', '//span[normalize-space()="Help Center"]')
BREADCRUMB_LOC = ('css selector', '.cc-breadcrumbs span')


class Bug326(BasePage):
    def click_help_center_link(self):
        print(f'\n{datetime.now()}   Click the [Help Center] link =>')
        element = Wait(self.driver, 2).until(EC.element_to_be_clickable(HELP_CENTER_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            element
        )
        element.click()
        print(f'{datetime.now()}   => Done, the link is clicked')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

    def should_be_help_center_page(self):
        print(f'\n{datetime.now()}   Check if the "Help Center" page is opened => ')

        try:
            self.driver.find_element(*BREADCRUMB_LOC)
        except NoSuchElementException:
            print(f'{datetime.now()}   => The page is not opened (Breadcrumb Element not found)')
            return False

        if 'Help' in self.driver.find_element(*BREADCRUMB_LOC).text:
            print(f'{datetime.now()}   => The "Help Center" page is opened')
            return True
        print(f'{datetime.now()}   => The wrong page is opened')
        return False
