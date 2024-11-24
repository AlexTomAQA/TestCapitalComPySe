"""
@Author  : Aleksei Kurochkin
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.Menu.New.from_markets_menu_open_market_analysis import MenuNew


class Locators:
    LINK_COLLAPSE = (By.XPATH, '//a[text()="collapse"]')


class Bug516(BasePage):

    def __init__(self, test):
        super().__init__(test.driver, test.link, test.bid)

    def open_market_analysis_page(self, test):
        MenuNew(self.driver).from_markets_menu_open_market_analysis(test.driver, test.cur_language,
                                                                    test.cur_country, test.link)
    def is_possible_open_collapse_page(self):
        try:
            self.driver.find_element(Locators.LINK_COLLAPSE).click()
            return True
        except:
            return False
