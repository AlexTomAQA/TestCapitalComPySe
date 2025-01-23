"""
-*- coding: utf-8 -*-
@Time    : 2025/01/23 19:50 GMT+5
@Author  : Sergey Aiidzhanov
"""
from datetime import datetime

from pages.base_page import BasePage
from pages.Menu.New.from_learn_menu_open_essentials_of_trading import MenuNewLearn
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

INVESTING_LINK_LOC = ('xpath', '//a[text() = "beleggen"]')
ERROR_TITLE_LOC = ('xpath', '//p[text() = "404"]')


class Bug654(BasePage):

    @staticmethod
    def open_trading_essentials_page(d, cur_language, cur_country, link):
        MenuNewLearn(d).from_learn_menu_open_essentials_of_trading(d, cur_language, cur_country, link)

    def open_investing_link(self):
        print(f'\n{datetime.now()}   Clicking "beleggen" (investing) link =>')

        link = Wait(self.driver, 2).until(EC.element_to_be_clickable(INVESTING_LINK_LOC))
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
