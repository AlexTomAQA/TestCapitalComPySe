"""
-*- coding: utf-8 -*-
@Time    : 2024/11/12 19:00 GMT+5
@Author  : Sergey Aiidzhanov
"""
from datetime import datetime

from pages.base_page import BasePage
from pages.Menu.New.from_markets_menu_open_markets import MenuNewMarkets
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

SEARCH_FIELD_LOC = ('css selector', '#marketlist_search')
AU200au_SEARCH_ITEM_LOC_NEW = ('xpath', '//strong[text()="AU200au"]')
TRADING_CONDITIONS_TABLE_LOC = ('css selector', 'table.tabs_table__SKwf9')

AU200au_TABLE_ITEM_LOC = ('xpath', '//a[text()="AU200au"]')
NEXT_PAGE_BTN_LOC = ('css selector', '[aria-label="Go to the next page"]')


class Bug507(BasePage):

    @staticmethod
    def open_markets_page(d, cur_language, cur_country, link):
        MenuNewMarkets(d).from_markets_menu_open_markets(d, cur_language, cur_country, link)

    def open_trading_australia_200_page(self):
        print(f'\n{datetime.now()}   Opening the "Trade Australia 200 - AU200au CFD" page =>')
        print(f'{datetime.now()}   => Click the "AU200au" item in the "All markets" table =>')

        search_field = Wait(self.driver, 2).until(EC.element_to_be_clickable(SEARCH_FIELD_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            search_field
        )
        search_field.send_keys("AU200au")

        print(f'{datetime.now()}   => Done, clicking the search item =>')

        search_item = Wait(self.driver, 2).until(EC.element_to_be_clickable(AU200au_SEARCH_ITEM_LOC_NEW))
        search_item.click()

        print(f'{datetime.now()}   => Done, the search item is clicked')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

        # flag = False
        # while flag is False:
        #     try:
        #         el = Wait(self.driver, 2).until(EC.element_to_be_clickable(AU200au_TABLE_ITEM_LOC))
        #         self.driver.execute_script(
        #             'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
        #             el
        #         )
        #         el.click()
        #         flag = True
        #     except TimeoutException:
        #         print(f'{datetime.now()}   => The item is not present, go to the next page =>')
        #         next_page_btn = Wait(self.driver, 2).until(EC.element_to_be_clickable(NEXT_PAGE_BTN_LOC))
        #         self.driver.execute_script(
        #             'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
        #             next_page_btn
        #         )
        #         next_page_btn.click()
        #
        # print(f'{datetime.now()}   => Done, the item is clicked')
        # print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

    def should_be_trading_conditions_table(self):
        print(f'\n{datetime.now()}   Check if the table in the block "Trading Conditions" is visible =>')

        try:
            Wait(self.driver, 2).until(EC.visibility_of_element_located(TRADING_CONDITIONS_TABLE_LOC))
            print(f'\n{datetime.now()}   => The table is visible')
            return True

        except TimeoutException:
            print(f'\n{datetime.now()}   => The table is not visible')
            return False
