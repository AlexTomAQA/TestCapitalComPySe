"""
-*- coding: utf-8 -*-
@Time    : 2024/08/29 18:15 GMT+5
@Author  : Sergey Aiidzhanov
"""
from datetime import datetime

from pages.base_page import BasePage
from pages.Menu.New.from_trading_menu_open_cfd_trading import MenuNew
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

TRADE_CFDS_BTN_LOC = ('css selector', '[data-type="cross_promo_block_btn1"]')


class Bug327(BasePage):

    @staticmethod
    def open_cfd_trading_page(d, cur_language, cur_country, link):
        MenuNew(d).from_trading_menu_open_cfd_trading(d, cur_language, cur_country, link)

    def hover_over_trade_cfds_button(self):
        print(f'\n{datetime.now()}   Hover over the [Trade CFDs on the web] button on the "Web platform" tile =>')

        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(TRADE_CFDS_BTN_LOC))

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )

        action = ActionChains(self.driver)
        action.move_to_element_with_offset(el, -50, -10).perform()

        ael = self.driver.switch_to.active_element

        print(f'\n{datetime.now()}   {ael.get_attribute("class")}')

        # if self.driver.switch_to.active_element == el:
        #     print(f'{datetime.now()}   same element')
        # else:
        #     print(f'{datetime.now()}   wrong element')

        print(f'{datetime.now()}   => Done')
