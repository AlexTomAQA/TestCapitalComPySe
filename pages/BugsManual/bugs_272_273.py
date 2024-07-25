"""
-*- coding: utf-8 -*-
@Time    : 2024/07/24 21:30 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

LEARN_MENU_SECTION_LOC = ("xpath", "(//a[@data-type='nav_id831'])[1]")
LINK_272_LOC = ("css selector", ".tile_tile__xTPBI:nth-child(1) a")
BLOCK_272_LOC = ("css selector", "div[data-id='tradingbeginners']  a[data-type='tiles_w_img_link4_signup']")
LINK_273_LOC = ("css selector", ".tile_tile__xTPBI:nth-child(2) a")
BLOCK_273_LOC = ("css selector", "div[data-id='experiencedtraders']  a[data-type='tiles_w_img_link2_signup']")


class LearnToTradePage(BasePage):
    def click_learn_menu_section(self):
        print(f'\n{datetime.now()}   Click the Learn menu section =>')
        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(LEARN_MENU_SECTION_LOC))
        el.click()
        print(f'{datetime.now()}   Done, the corresponding page is opened')
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')

    def click_the_learn_to_trade_link272(self):
        print(f'\n{datetime.now()}   Click the Learn to trade link =>')
        link = Wait(self.driver, 5).until(EC.element_to_be_clickable(LINK_272_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            link
        )
        link.click()
        print(f'{datetime.now()}   => Done, scrolling to the corresponding block')

    def click_the_learn_to_trade_link273(self):
        print(f'\n{datetime.now()}   Click the Learn to trade link =>')
        link = Wait(self.driver, 5).until(EC.element_to_be_clickable(LINK_273_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            link
        )
        link.click()
        print(f'{datetime.now()}   => Done, scrolling to the corresponding block')

    def should_be_visible_block_trading_for_beginners(self):
        print(f'\n{datetime.now()}   Check if scroll to the block Trading for beginners is successful => ')
        try:
            Wait(self.driver, 5).until(EC.element_to_be_clickable(BLOCK_272_LOC))
        except TimeoutException:
            print(f'{datetime.now()}   => The block is not into viewport')
            return False
        print(f'{datetime.now()}   => The block is into viewport')
        return True

    def should_be_visible_block_experienced_traders(self):
        print(f'\n{datetime.now()}   Check if scroll to the block Experienced traders is successful => ')
        try:
            Wait(self.driver, 5).until(EC.element_to_be_clickable(BLOCK_273_LOC))
        except TimeoutException:
            print(f'{datetime.now()}   => The block is not into viewport')
            return False
        print(f'{datetime.now()}   => The block is into viewport')
        return True
