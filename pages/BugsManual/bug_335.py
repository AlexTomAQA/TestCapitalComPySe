"""
-*- coding: utf-8 -*-
@Time    : 2024/08/18 17:45 GMT+5
@Author  : Sergey Aiidzhanov
"""
from datetime import datetime

from pages.base_page import BasePage
from pages.Menu.New.from_learn_menu_open_market_guides import MenuNewLearn
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

OIL_TRADING_GUIDE_BTN_LOC = ('css selector', '[data-type="tiles_w_img_link6_signup"]')
SHARES_TRADING_BTN_LOC = ('css selector', '[data-type="benefits_block_block_تعلّم_المزيد_حول_كيفيّة_التداول_على_الأسهم_btn"]')
BREADCRUMB_LOC = ('css selector', '.breadcrumbs_breadcrumbs__UgZeo span')
TITLE_LOC = ('css selector', '.heading_h1__1NQVK')


class Bug335(BasePage):

    @staticmethod
    def open_market_guides_page(d, cur_language, cur_country, link):
        MenuNewLearn(d).from_learn_menu_open_market_guides(d, cur_language, cur_country, link)

    def click_oil_trading_guide_button(self):
        print(f'\n{datetime.now()}   Click the [Oil trading guide] button on the "What is oil trading?" tile =>')
        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(OIL_TRADING_GUIDE_BTN_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()
        print(f'{datetime.now()}   => Done, the button is clicked')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

    def click_learn_more_about_shares_trading_button(self):
        print(f'\n{datetime.now()}   Click the [Learn more about shares trading] button on the "Shares trading" tile =>')
        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(SHARES_TRADING_BTN_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()
        print(f'{datetime.now()}   => Done, the button is clicked')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

    def should_be_what_is_shares_trading_page(self):
        print(f'{datetime.now()}   Check if the "What is shares trading" page is opened => ')

        try:
            self.driver.find_element(*BREADCRUMB_LOC)
        except NoSuchElementException:
            print(f'{datetime.now()}   => The page is not opened (Breadcrumb Element not found)')
            return False

        try:
            self.driver.find_element(*TITLE_LOC)
        except NoSuchElementException:
            print(f'{datetime.now()}   => The page is not opened (Title Element not found)')
            return False

        if 'ما هو تداول الأسهم' in self.driver.find_element(*BREADCRUMB_LOC).text:
            if 'دليلك الشامل للتداول بالأسهم' in self.driver.find_element(*TITLE_LOC).text:
                print(f'{datetime.now()}   => The "What is shares trading" page is opened')
                return True
        print(f'{datetime.now()}   => The wrong page is opened')
        return False
