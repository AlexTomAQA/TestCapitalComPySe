"""
@Author  : Aleksei Kurochkin
"""
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.Menu.New.from_markets_menu_open_market_analysis import MenuNew


class Locators:
    LINK_TRY_DEMO = (By.XPATH, "//a[contains(text(), 'Try demo')]")
    SIGN_UP_CLOSE = (By.XPATH, '//button[@data-type="SIGN_UP_close"]')
    PAGE_LOADER = (By.XPATH, "//div[@class='pageLoader_loader__QsVJC']")


class Bug634(BasePage):

    def __init__(self, test):
        super().__init__(test.driver, test.link, test.bid)

    def open_market_analysis_page(self, test):
        MenuNew(self.driver).from_markets_menu_open_market_analysis(test.driver, test.cur_language,
                                                                    test.cur_country, test.link)

    def click_try_demo(self):
        self.driver.find_element(*Locators.LINK_TRY_DEMO).click()

    def close_pop_up_window(self):
        self.driver.find_element(*Locators.SIGN_UP_CLOSE).click()

    def if_page_loader_present(self):
        try:
            self.driver.find_element(*Locators.PAGE_LOADER)
            return True
        except NoSuchElementException:
            return False
