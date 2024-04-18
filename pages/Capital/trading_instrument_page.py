from datetime import datetime

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PageTradingInstrumentLocators:
    MARKET_MAIN_TITLE = (By.CSS_SELECTOR, "div.cc-box.grey.brick.marketMainTitle")
    PAGE_INSTRUMENT_TITLE = (By.CSS_SELECTOR, "p > span")


class PageTradingInstrument(BasePage):
    @allure.step(f"{datetime.now()}. Checking that the trading instrument page is opened.")
    def should_be_trading_instrument_page(self, title_instrument):
        if self.should_be_page_title_v3(title_instrument):
            return True
        print(f"{datetime.now()}   Page of trading instrument on capital.com with corresponding instrument is opened")
