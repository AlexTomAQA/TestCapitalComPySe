"""
-*- coding: utf-8 -*-
@Time    : 2024/10/08 18:30 GMT+5
@Author  : Sergey Aiidzhanov
"""
import random

from datetime import datetime

from pages.base_page import BasePage
from pages.Menu.New.from_learn_menu_open_trading_strategies import MenuNew
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


COUNTRY_FLAG_LOC = ('xpath', '//div[@class="localization_item__KwMiX"][1]//i')
LANGUAGE_SWITCHER_LOCK = ('xpath', '//div[@class="localization_item__KwMiX"][2]//span[@data-type="country_switcher_footer"]')
POSITION_TRADING_LINK_LOC = ('css selector', 'a[data-type="benefits_block_block_دليل_استراتيجية_التروّي_btn"]')
TEST_LINK_LOC = ('css selector', 'main a')


class Bug392(BasePage):

    @staticmethod
    def open_trading_strategies_page(d, cur_language, cur_country, link):
        MenuNew(d).from_learn_menu_open_trading_strategies(d, cur_language, cur_country, link)

    def open_position_trading_page(self):
        print(f'\n{datetime.now()}   Click the "Position trading guide" link =>')

        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(POSITION_TRADING_LINK_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()

        print(f'{datetime.now()}   => Done, the corresponding page is opened')
        print(f'{datetime.now()}   Current URL: {self.driver.current_url}')

    def click_random_link(self):
        print(f'\n{datetime.now()}   Click any link in the main content of the page =>')

        link_loc = random.choice(self.driver.find_elements(*TEST_LINK_LOC))

        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(link_loc))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()

        print(f'{datetime.now()}   => Done, current URL: {self.driver.current_url}')

    def should_be_new_version_ar_language_page(self):
        print(f'\n{datetime.now()}   Make sure that the page is opened in the new version and in AR language =>')
        try:
            if 'Arabic' in self.driver.find_element(*LANGUAGE_SWITCHER_LOCK).text:
                print(f'{datetime.now()}   => The new version is opened')
                print(f'{datetime.now()}   => AR language is selected')
                return True
            print(f'{datetime.now()}   => The new version is opened, but in wrong language')
        except NoSuchElementException:
            print(f'{datetime.now()}   => The page is not opened on the new version')
            return False
