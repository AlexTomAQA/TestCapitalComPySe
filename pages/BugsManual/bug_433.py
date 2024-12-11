"""
-*- coding: utf-8 -*-
@Time    : 2024/12/02 18:40 GMT+5
@Author  : Sergey Aiidzhanov
"""
from datetime import datetime

from pages.base_page import BasePage
from pages.Menu.New.from_markets_menu_open_markets import MenuNewMarkets
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

SEARCH_FIELD_LOC = ('css selector', '#marketlist_search')
US100_SEARCH_ITEM_LOC = ('xpath', '//div[@class="result_item__rY8mQ"]/strong[text()="US100"]')
GUIDE_LINK_LOC = ('xpath', '//a[text()="guide to trading the US Tech 100"]')
NEW_LOGO_LOC = ('css selector', '[data-testid="logo"]')
NEW_BREADCRUMB_LOC = ('css selector', '.breadcrumbs_breadcrumbs__UgZeo')


class Bug433(BasePage):

    @staticmethod
    def open_markets_page(d, cur_language, cur_country, link):
        MenuNewMarkets(d).from_markets_menu_open_markets(d, cur_language, cur_country, link)

    def open_us100_page(self):
        print(f'\n{datetime.now()}   Opening the "Trade US Tech 100 - US100 CFD" page =>')
        print(f'{datetime.now()}   => Search the "US100" item in the table of shares =>')

        search_field = Wait(self.driver, 2).until(EC.element_to_be_clickable(SEARCH_FIELD_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            search_field
        )
        search_field.send_keys("US100")

        print(f'{datetime.now()}   => Done, clicking the search item =>')

        search_item = Wait(self.driver, 2).until(EC.element_to_be_clickable(US100_SEARCH_ITEM_LOC))
        search_item.click()

        print(f'{datetime.now()}   => Done, the search item is clicked')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

    def click_trading_guide_link(self):
        print(f'\n{datetime.now()}   Click the [NASDAQ stock exchange] link =>')
        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(GUIDE_LINK_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()
        print(f'{datetime.now()}   => Done, the link is clicked')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

    def should_be_new_version_page(self):
        print(f'\n{datetime.now()}   Make sure that new version of the page is opened => ')

        print(f'{datetime.now()}   => Check new logo => ')

        try:
            if Wait(self.driver, 2).until(EC.visibility_of_element_located(NEW_LOGO_LOC)):
                print(f'{datetime.now()}   => New logo is not found on the page')
        except TimeoutException:
            return False

        print(f'{datetime.now()}   => Check new breadcrumbs => ')
        try:
            if not Wait(self.driver, 2).until(EC.visibility_of_element_located(NEW_BREADCRUMB_LOC)):
                print(f'{datetime.now()}   => New breadcrumbs are not found on the page')
        except TimeoutException:
            return False

        print(f'{datetime.now()}   => New version is opened')
        return True
