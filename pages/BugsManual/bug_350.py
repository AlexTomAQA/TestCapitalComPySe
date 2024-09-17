"""
-*- coding: utf-8 -*-
@Time    : 2024/09/05 20:47 GMT+3
@Author  : podchasova11
"""
from datetime import datetime

import allure
from selenium.common import TimeoutException

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from pages.common import Common

HOW_TO_GUIDES_LOC = ('css selector', 'div.grid.gSm > div:nth-child(2) > div > div > a')
ERROR_PAGE_DISPLAYED_LOC = ('css selector', '#main-content > div > section div > h1')
ERROR_PAGE_SCB_LICENSE_DISPLAYED_LOC = ('css selector', 'main > div.lt-start-screen-wrap.lt-container > div.lt-container-inner > div > div.lt-page__heading > h1')


class Bug350(BasePage):
    def click_how_to_guides_link(self):
        print(f'\n{datetime.now()}   Click the [How-to guides] link =>')
        element = Wait(self.driver, 2).until(EC.element_to_be_clickable(HOW_TO_GUIDES_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            element
        )
        element.click()
        allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        print(f'{datetime.now()}   => Done, the link is clicked')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

    def should_be_open_how_to_guides_page(self):
        print(f'\n{datetime.now()}   Check that Corresponding web page with resource is opened => ')
        print(f'{datetime.now()}   Current page is: {self.driver.current_url}')

        try:
            Wait(self.driver, 5).until(EC.element_to_be_clickable(ERROR_PAGE_DISPLAYED_LOC))
        except TimeoutException:
            print(f'{datetime.now()}   => The block is not into page')
            return False

        if 'Oops, this help center no longer exists' in self.driver.find_element(*ERROR_PAGE_DISPLAYED_LOC).text:
            print(f'{datetime.now()}   => The "Bug # 55!350a Error message '
                  f'"Oops, this help center no longer exists"'
                  f' is displayed after clicking the link [How-to guides] page is opened')
            return False
        print(f'{datetime.now()}   => The Corresponding web page with resource is opened')
        return True

    def should_be_open_how_to_guides_page_scb_license(self):
        print(f'\n{datetime.now()}   Check that Corresponding web page with resource is opened => ')
        print(f'{datetime.now()}   Current page is: {self.driver.current_url}')

        try:
            Wait(self.driver, 5).until(EC.element_to_be_clickable(ERROR_PAGE_SCB_LICENSE_DISPLAYED_LOC))
        except TimeoutException:
            print(f'{datetime.now()}   => The block is not into page')
            return False

        if 'The page you were looking for' in self.driver.find_element(*ERROR_PAGE_SCB_LICENSE_DISPLAYED_LOC).text:
            print(f'{datetime.now()}   => The "Bug # 55!350b Error message '
                      f'"The page you were looking for doesnt exist" '
                      f'is displayed after clicking the link [How-to guides]')
            return False
        print(f'{datetime.now()}   => The Corresponding web page with resource is opened')
        return True


