"""
-*- coding: utf-8 -*-
@Time    : 2024/07/13 22:50 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

BTC_HALVING_ITEM_LOC = ("xpath", "//div[@class='side-nav']/a[contains(@href, 'halving')]")
BTC_GOLD_ITEM_LOC = ("xpath", "//div[@class='side-nav']/a[contains(@href, 'gold')]")
STICKY_BAR_LOC = ("css selector", ".encStickyBar")


class Bug080(BasePage):
    def click_btc_halving_item(self):
        print(f'\n{datetime.now()}   Click the Bitcoin Halving item =>')
        el = Wait(self.driver, 5).until(EC.element_to_be_clickable(BTC_HALVING_ITEM_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()
        print(f'{datetime.now()}   => Done, corresponding page is opened')
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')

    def click_btc_gold_item(self):
        print(f'\n{datetime.now()}   Click the Bitcoin Gold item =>')
        el = Wait(self.driver, 5).until(EC.element_to_be_clickable(BTC_GOLD_ITEM_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()
        print(f'{datetime.now()}   => Done, corresponding page is opened')
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')

    def change_language(self, lang):
        print(f'\n{datetime.now()}   Change language to {lang}')
        el = Wait(self.driver, 5).until(EC.element_to_be_clickable(("css selector", f"a[data-type='nav_lang_{lang}']")))
        el.click()
        print(f'{datetime.now()}   => Done, corresponding page is opened')
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')

    def should_be_sticky_bar(self):
        print(f'{datetime.now()}   Check if the sticky bar is present =>')
        try:
            Wait(self.driver, 5).until(EC.presence_of_element_located(STICKY_BAR_LOC))
        except TimeoutException:
            print(f'{datetime.now()}   The sticky bar is not present')
            return False
        print(f'{datetime.now()}   The sticky bar is present')
        return True
