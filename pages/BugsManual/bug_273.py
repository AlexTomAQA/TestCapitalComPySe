"""
-*- coding: utf-8 -*-
@Time    : 2024/09/22 20:30 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime

from pages.base_page import BasePage
from pages.Menu.New.from_learn_menu_open_learn import MenuNewLearn
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

LINK_LEARN_TO_TRADE_LOC = ("css selector", ".tile_tile__xTPBI:nth-child(2) a")
BLOCK_EXPERIENCED_LOC = ("css selector", "div[data-id='experiencedtraders']  a[data-type='tiles_w_img_link2_signup']")


class Bug273(BasePage):
    @staticmethod
    def open_learn_to_trade_page(d, cur_language, cur_country, link):
        MenuNewLearn(d).from_learn_menu_open_learn(d, cur_language, cur_country, link)

    def click_the_learn_to_trade_link(self):
        print(f'\n{datetime.now()}   Click the Learn to trade link =>')
        link = Wait(self.driver, 5).until(EC.element_to_be_clickable(LINK_LEARN_TO_TRADE_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            link
        )
        link.click()
        print(f'{datetime.now()}   => Done, scrolling to the corresponding block')

    def should_be_visible_block_experienced_traders(self):
        print(f'\n{datetime.now()}   Check if scroll to the block Experienced traders is successful => ')
        try:
            Wait(self.driver, 5).until(EC.element_to_be_clickable(BLOCK_EXPERIENCED_LOC))
        except TimeoutException:
            print(f'{datetime.now()}   => The block is not into viewport')
            return False
        print(f'{datetime.now()}   => The block is into viewport')
        return True
