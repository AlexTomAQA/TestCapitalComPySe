"""
-*- coding: utf-8 -*-
@Time    : 2024/09/29 19:30 GMT+5
@Author  : Sergey Aiidzhanov
"""
import random

from datetime import datetime

from pages.base_page import BasePage
from pages.Menu.New.from_markets_menu_open_market_analysis import MenuNew
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

ANALYSIS_ARTICLE_LOC = ('css selector', '[data-type="latest_articles_block_page_id_541702"]')
NEXT_PAGE_BTN_LOC = ('css selector', '[aria-label="Go to the next page"]')


class Bug378(BasePage):

    def __init__(self, browser, link, bid):
        self.test_text = None

        super().__init__(browser, link, bid)

    @staticmethod
    def open_market_analysis_page(d, cur_language, cur_country, link):
        MenuNew(d).from_markets_menu_open_market_analysis(d, cur_language, cur_country, link)

    def open_lloyds_forecast_page(self):
        print(f'\n{datetime.now()}   Click the "Lloyds forecast" article =>')

        try:
            el = Wait(self.driver, 2).until(EC.element_to_be_clickable(ANALYSIS_ARTICLE_LOC))
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                el
            )
            el.click()
        except TimeoutException:
            while TimeoutException:
                el = Wait(self.driver, 2).until(EC.element_to_be_clickable(NEXT_PAGE_BTN_LOC))
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    el
                )
                el.click()

        print(f'{datetime.now()}   => Done, the corresponding page is opened')
        print(f'{datetime.now()}   Current URL: {self.driver.current_url}')
