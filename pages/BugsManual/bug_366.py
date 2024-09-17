"""
-*- coding: utf-8 -*-
@Time    : 2024/09/17 18:35 GMT+5
@Author  : Sergey Aiidzhanov
"""
import random

from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException

TRADING_INSTRUMENT_LOC = ('css selector', 'tr[data-iid="27045129890124996"]')
BANNER_LOC = ('css selector', '.promoJones > a')


class Bug366(BasePage):

    def open_trading_instrument_page(self):
        print(f'\n{datetime.now()}   Open "Gold" trading instrument page =>')

        instruments_list = self.driver.find_elements(*TRADING_INSTRUMENT_LOC)
        rand_instrument = instruments_list[random.randint(0, len(instruments_list) - 1)]
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            rand_instrument
        )
        rand_instrument.click()

        print(f'{datetime.now()}   => Done, the page is opened')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

    def click_banner(self):
        print(f'\n{datetime.now()}   Click the "Market Outlook with David Jones" banner =>')
        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(BANNER_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()
        print(f'{datetime.now()}   => Done, the banner is clicked')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')
