"""
-*- coding: utf-8 -*-
@Time    : 2024/11/03 17:45 GMT+5
@Author  : Sergey Aiidzhanov
"""
from datetime import datetime

from pages.base_page import BasePage
from pages.Menu.New.from_pricing_menu_open_charges_and_fees import MenuNew
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


START_TRADING_BTN_LOC = ('xpath', '//button[text()="Start trading now"]')


class Bug414(BasePage):

    @staticmethod
    def open_charges_and_fees_page(d, cur_language, cur_country, link):
        MenuNew(d).from_pricing_menu_open_charges_and_fees(d, cur_language, cur_country, link)

    def click_start_trading_btn(self):
        print(f'\n{datetime.now()}   Click [Start trading now] button =>')

        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(START_TRADING_BTN_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()

        print(f'{datetime.now()}   => Done')
