"""
-*- coding: utf-8 -*-
@Time    : 2024/09/03 21:35 GMT+5
@Author  : Sergey Aiidzhanov
"""
from datetime import datetime

from pages.base_page import BasePage
from pages.Menu.New.from_markets_menu_open_shares import MenuNewShares
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

SEARCH_EL_LOC_OLD = ('css selector', '#iqf')
GOOGL_SEARCH_ITEM_LOC_OLD = ('xpath', '//div[text()="GOOGL"]')
BREADCRUMB_LOC_OLD = ('css selector', '.cc-breadcrumbs span')
TITLE_LOC_OLD = ('css selector', '.marketMainTitle > h1')

SEARCH_EL_LOC_NEW = ('css selector', '#marketlist_search')
GOOGL_SEARCH_ITEM_LOC_NEW = ('xpath', '//strong[text()="GOOGL"]')
BREADCRUMB_LOC_NEW = ('css selector', '.breadcrumbs_breadcrumbs__UgZeo span')
TITLE_LOC_NEW = ('css selector', 'h1.heading_h1__1NQVK')
GOOGL_ITEM_LOC = ('xpath', '//a[text()="GOOGL"]')
NEXT_PAGE_BTN_LOC = ('css selector', '[aria-label="Go to the next page"]')

NASDAQ_LINK_LOC = ('xpath', '//a[text()="NASDAQ stock exchange"]')

ERROR_PAGE_BODY_LOC = ('css selector', 'body.neterror')


class Bug359(BasePage):

    @staticmethod
    def open_shares_page(d, cur_language, cur_country, link):
        MenuNewShares(d).from_markets_menu_open_shares(d, cur_language, cur_country, link)

    def open_trade_alphabet_page_new(self):
        print(f'\n{datetime.now()}   Opening the "Trade Alphabet Inc - A - GOOGL CFD" page =>')
        print(f'{datetime.now()}   => Click the "GOOGL" item in the table of shares =>')

        flag = False
        while flag is False:
            try:
                el = Wait(self.driver, 2).until(EC.element_to_be_clickable(GOOGL_ITEM_LOC))
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    el
                )
                el.click()
                flag = True
            except TimeoutException:
                print(f'{datetime.now()}   => The item is not present, go to the next page =>')
                next_page_btn = Wait(self.driver, 2).until(EC.element_to_be_clickable(NEXT_PAGE_BTN_LOC))
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    next_page_btn
                )
                next_page_btn.click()

        print(f'{datetime.now()}   => Done, the item is clicked')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

    def open_trade_alphabet_page_old(self):
        print(f'\n{datetime.now()}   Opening the "Trade Alphabet Inc - A - GOOGL CFD" page =>')
        print(f'{datetime.now()}   => Searching the "GOOGL" in the table of shares =>')

        search_field = Wait(self.driver, 2).until(EC.element_to_be_clickable(SEARCH_EL_LOC_OLD))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            search_field
        )
        search_field.send_keys("GOOGL")

        print(f'{datetime.now()}   => Done, clicking the search item =>')

        search_item = Wait(self.driver, 2).until(EC.element_to_be_clickable(GOOGL_SEARCH_ITEM_LOC_OLD))
        search_item.click()

        print(f'{datetime.now()}   => Done, the search item is clicked')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

    def click_nasdaq_link(self):
        print(f'\n{datetime.now()}   Click the [NASDAQ stock exchange] link =>')
        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(NASDAQ_LINK_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()
        print(f'{datetime.now()}   => Done, the link is clicked')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

    def should_not_be_error_page_new(self):
        print(f'\n{datetime.now()}   Make sure that there are no errors => ')
        if self.driver.find_element(*ERROR_PAGE_BODY_LOC):
            print(f'{datetime.now()}   => ERROR')
            return False
        print(f'{datetime.now()}   => No errors')
        return True

    def should_not_be_error_page_old(self):
        print(f'\n{datetime.now()}   Make sure that there are no errors => ')

        tabs = self.driver.window_handles
        print(f'\n{datetime.now()}   TABS QUANTITY: {len(tabs)}')
        if len(tabs) > 1:
            self.driver.switch_to.window(tabs[len(tabs) - 1])

        if self.driver.find_element(*ERROR_PAGE_BODY_LOC):
            print(f'{datetime.now()}   => ERROR')
            self.driver.close()
            tabs = self.driver.window_handles
            self.driver.switch_to.window(tabs[len(tabs) - 1])
            print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')
            return False
        print(f'{datetime.now()}   => No errors')
        self.driver.close()
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[len(tabs) - 1])
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')
        return True
