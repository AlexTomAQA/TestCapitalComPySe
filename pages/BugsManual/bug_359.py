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
from selenium.common.exceptions import NoSuchElementException

GOOGL_TRADING_ITEM_LOC = ('xpath', '//*[text()="GOOGL"]')
SEARCH_EL_LOC_OLD = ('css selector', '#iqf')
GOOGL_SEARCH_ITEM_OLD = ('css selector', '//div[text()="GOOGL"]')
SEARCH_EL_LOC_NEW = ('css selector', '#marketlist_search')
GOOGL_SEARCH_ITEM_NEW = ('css selector', '//strong[text()="GOOGL"]')


class Bug359(BasePage):

    @staticmethod
    def open_shares_page(d, cur_language, cur_country, link):
        MenuNewShares(d).from_markets_menu_open_shares(d, cur_language, cur_country, link)
