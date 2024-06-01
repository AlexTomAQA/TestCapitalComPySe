from datetime import datetime

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PageTradingInstrumentLocators:
    MARKET_MAIN_TITLE = (By.CSS_SELECTOR, "div.cc-box.grey.brick.marketMainTitle")
    PAGE_INSTRUMENT_TITLE = (By.CSS_SELECTOR, "nav > p > span")


class PageTradingInstrument(BasePage):
    @allure.step(f"{datetime.now()}. Checking that the corresponding trading instrument page is opened.")
    def should_be_trading_instrument_page(self, title_instrument):
        print(f"\n{datetime.now()}   Checking that the page of expected instrument item =>")
        current_instrument_title = self.driver.find_element(*PageTradingInstrumentLocators.PAGE_INSTRUMENT_TITLE).text

        assert (current_instrument_title == title_instrument),  (f"Expected {current_instrument_title}, but "
                                                                 f"got {title_instrument}")

        print(f"{datetime.now()}   Page of {current_instrument_title} trading instrument on capital.com with "
              f"expected {title_instrument} instrument is opened")
