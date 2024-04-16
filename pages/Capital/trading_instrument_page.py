from datetime import datetime

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
# from pages.common import Common
from test_data.trading_instrument_page_data import data


class PageTradingInstrumentLocators:
    MARKET_MAIN_TITLE = (By.CSS_SELECTOR, "div.cc-box.grey.brick.marketMainTitle")
    PAGE_INSTRUMENT_TITLE = (By.CSS_SELECTOR, "head > title")


class PageTradingInstrument(BasePage):
    @allure.step(f"{datetime.now()}. Checking that the trading instrument page is opened.")
    def should_be_trading_instrument_page(self):
        if self.should_be_page_title_v3(data["PAGE_TITLE"]):
            return True
        else:
            print(f"{datetime.now()}   Trading instrument page is not opened")
            return False

#    def check_market_main_title(self):
#        assert self.element_is_visible(PageTradingInstrumentLocators.MARKET_MAIN_TITLE)

#    @allure.step(f"{datetime.now()}   Check trading instrument page")
#    def check_open_trading_instrument_page(self, cur_link):
