"""
-*- coding: utf-8 -*-
@Time    : 2024/08/12 21:05 GMT+5
@Author  : Sergey Aiidzhanov
"""
import random

from datetime import datetime

from pages.base_page import BasePage
from pages.Menu.New.from_markets_menu_open_shares import MenuNewShares
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

STOCK_EXCHANGE_BTN_LOC = ('xpath', '//a[contains(text(), "stock exchange")]')
TRADING_INSTRUMENTS_LINK_LOC = ('css selector', '.js-ckeContent > p > a:not([data-type="plain_button"])')


class Bug305(BasePage):

    @staticmethod
    def open_shares_trading_page(d, cur_language, cur_country, link):
        MenuNewShares(d).from_markets_menu_open_shares(d, cur_language, cur_country, link)

    def open_stock_market_trading_hours_page(self):
        print(f'\n{datetime.now()}   Click the [stock exchange] link in the "What is shares trading?" block =>')
        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(STOCK_EXCHANGE_BTN_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()
        print(f'{datetime.now()}   => Done, the "Stock Market Trading Hours" page is opened')

    def click_any_trading_instrument_link(self):
        links_list = self.driver.find_elements(*TRADING_INSTRUMENTS_LINK_LOC)
