"""
-*- coding: utf-8 -*-
@Time    : 2024/09/22 20:50 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime

from pages.base_page import BasePage
from pages.Menu.New.from_about_us_menu_open_why_capital import MenuNew
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

LINK_LEARN_TO_TRADE_LOC = ('xpath', '(//a[@data-type="benefits_block_block_تعلّم_التداول_btn"])[1]')
BLOCK_BEGINNERS_LOC = ('css selector', 'div[data-id="tradingbeginners"]  a[data-type="tiles_w_img_link4_signup"]')


class Bug372(BasePage):
    @staticmethod
    def open_why_capital_com_page(d, cur_language, cur_country, link):
        MenuNew(d).from_about_us_menu_open_why_capital(d, cur_language, cur_country, link)

    def click_the_learn_to_trade_link(self):
        print(f'\n{datetime.now()}   Click the Learn to trade link =>')
        link = Wait(self.driver, 5).until(EC.element_to_be_clickable(LINK_LEARN_TO_TRADE_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            link
        )
        link.click()
        print(f'{datetime.now()}   => Done, the corresponding page is opened')
        print(f'{datetime.now()}   Current URL: "{self.driver.current_url}"')

    def should_be_visible_block_trading_for_beginners(self):
        print(f'\n{datetime.now()}   Check if scroll to the block Trading for beginners is successful => ')
        try:
            Wait(self.driver, 5).until(EC.element_to_be_clickable(BLOCK_BEGINNERS_LOC))
        except TimeoutException:
            print(f'{datetime.now()}   => The block is not into viewport')
            return False
        print(f'{datetime.now()}   => The block is into viewport')
        return True
