"""
-*- coding: utf-8 -*-
@Time    : 2024/09/07 22:40 GMT+5
@Author  : Sergey Aiidzhanov
"""
from datetime import datetime

from pages.base_page import BasePage
from pages.Menu.New.from_trading_menu_open_spread_betting import MenuNewSpreadBetting
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

TRADING_INSTRUMENT_LINK_LOC = ('css selector', 'h3.heading_h3__nTE01.heading_left__9ANWc')
ERROR_PAGE_TITLE_LOC = ('css selector', 'p.title404')


class Bug364(BasePage):

    @staticmethod
    def open_spread_betting_page(d, cur_language, cur_country, link):
        MenuNewSpreadBetting(d).from_trading_menu_open_spread_betting(d, cur_language, cur_country, link)

    def click_trading_instrument_link(self):
        print(f'\n{datetime.now()}   Click the trading instrument link =>')
        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(TRADING_INSTRUMENT_LINK_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()
        print(f'{datetime.now()}   => Done, the link is clicked')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

    def should_not_be_error_page(self):
        print(f'\n{datetime.now()}   Make sure that there are no errors => ')
        if self.driver.find_element(*ERROR_PAGE_TITLE_LOC):
            print(f'{datetime.now()}   => ERROR')
            return False
        print(f'{datetime.now()}   => No errors')
        return True
