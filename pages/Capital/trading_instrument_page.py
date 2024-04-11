from datetime import datetime

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.common import Common


class PageTradingInstrumentLocators:
    PAGE_INSTRUMENT_TITLE = (By.CSS_SELECTOR, "p > span")


class PageTradingInstrument(BasePage):
    @allure.step(f"{datetime.now()}   Check trading instrument page")
    def check_open_trading_instrument_page(self, title_instrument):
        page_instrument_title = self.driver.find_element(PageTradingInstrumentLocators.PAGE_INSTRUMENT_TITLE).text
        page_instrument_title_list = page_instrument_title.replace(" ", "")
        if title_instrument not in page_instrument_title_list:
            print(f"{datetime.now()} Trading instrument page is not opened")
            Common().pytest_fail("Bug ? Trading instrument page is not opened")
