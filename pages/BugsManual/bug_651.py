"""
-*- coding: utf-8 -*-
@Time    : 2025/01/10 19:50 GMT+5
@Author  : Sergey Aiidzhanov
"""
from datetime import datetime

import random

from pages.base_page import BasePage
from pages.Menu.New.from_markets_menu_open_commodities import MenuNew
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

TEST_LINK_LOC = ('css selector', '.js-ckeContent.content_content__2ZOcD a')
ERROR_TITLE_LOC = ('xpath', '//p[text() = "404"]')


class Bug651(BasePage):

    @staticmethod
    def open_commodities_page(d, cur_language, cur_country, link):
        MenuNew(d).from_markets_menu_open_commodities(d, cur_language, cur_country, link)

    def open_test_link(self):

        link = random.choice(self.driver.find_elements(*TEST_LINK_LOC))

        print(f'\n{datetime.now()}   Clicking the link "{link.text}" =>')

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            link
        )
        link.click()

        print(f'{datetime.now()}   => Done, the link is clicked')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

    def should_not_be_error_404(self):
        print(f'\n{datetime.now()}   Making sure that corresponding page is opened without error 404 =>')

        try:
            Wait(self.driver, 2).until(EC.visibility_of_element_located(ERROR_TITLE_LOC))
            print(f'\n{datetime.now()}   => The page is opened with error 404')
            return False

        except TimeoutException:
            print(f'\n{datetime.now()}   => The page is opened without error 404')
            return True
