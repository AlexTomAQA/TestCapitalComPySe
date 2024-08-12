"""
-*- coding: utf-8 -*-
@Time    : 2024/07/30 21:16 GMT+5
@Author  : Sergey Aiidzhanov
"""
from datetime import datetime

from pages.base_page import BasePage
from pages.Menu.New.from_learn_menu_open_demo import MenuNew
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

MORE_BTN_LOC = ('css selector', '[data-type="tiles_w_img_link5_signup"]')
BREADCRUMB_LOC = ('css selector', '.breadcrumbs_breadcrumbs__UgZeo span')
TITLE_LOC = ('css selector', '.heading_h1__1NQVK')


class Bug305(BasePage):

    @staticmethod
    def open_demo_account_page(d, cur_language, cur_country, link):
        MenuNew(d).from_learn_menu_open_demo(d, cur_language, cur_country, link)

    def click_more_button(self):
        print(f'\n{datetime.now()}   Click the [More] button on the Cryptocurrencies tile =>')
        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(MORE_BTN_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()
        print(f'{datetime.now()}   => Done, the button is clicked')

    def should_be_cryptocurrency_trading_page(self):
        print(f'{datetime.now()}   Check if the Cryptocurrency Trading page is opened => ')

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

        if 'العملات المشفرة' in self.driver.find_element(*BREADCRUMB_LOC).text:
            if 'التداول على العملات المشفّرة' in self.driver.find_element(*TITLE_LOC).text:
                print(f'{datetime.now()}   => The Cryptocurrency Trading page is opened')
                return True
        print(f'{datetime.now()}   => The wrong page is opened')
        return False
