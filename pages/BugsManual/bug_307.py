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
BREADCRUMB_LOC = ('css selector', '.breadcrumbs_breadcrumbs__UgZeo  span')
TITLE_LOC = ('css selector', 'h1.heading_h1__1NQVK')


class Bug307(BasePage):

    def __init__(self, browser, link, bid):
        self.test_link = None

        super().__init__(browser, link, bid)

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
        print(f'\n{datetime.now()}   Click random trading instrument link =>')
        self.test_link = random.sample(self.driver.find_elements(*TRADING_INSTRUMENTS_LINK_LOC), 1)[0]
        print(self.test_link.text)
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.test_link
        )
        self.test_link.click()
        print(f'{datetime.now()}   => Done, the link "{self.test_link.text}" is clicked')
        print(f'{datetime.now()}   Current URL: "{self.driver.current_url}"')

    def should_be_corresponding_page(self):
        print(f'\n{datetime.now()}   Check if the corresponding page of the link is opened =>')
        if self.test_link.text[:-1] in self.driver.find_element(*BREADCRUMB_LOC):
            if self.test_link.text[:-1] in self.driver.find_element(*TITLE_LOC):
                print(f'{datetime.now()}   => The page is opened')
                return True
            print(f'{datetime.now()}   => The page is not opened')
        return False
