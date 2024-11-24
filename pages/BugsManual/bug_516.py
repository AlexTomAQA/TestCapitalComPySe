"""
@Author  : Aleksei Kurochkin
"""
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.Menu.New.from_markets_menu_open_market_analysis import MenuNew


class Locators:
    LINK_PART2_IN_TABLE_OF_CONTENT = (By.CSS_SELECTOR, 'nav.grid_grid__2D3md [href="#part_2"]')
    PART2_IN_TITLE = (By.CSS_SELECTOR, '[data-id="part_2"]')


class Bug516(BasePage):

    def __init__(self, test):
        super().__init__(test.driver, test.link, test.bid)

    def open_market_analysis_page(self, test):
        MenuNew(self.driver).from_markets_menu_open_market_analysis(test.driver, test.cur_language,
                                                                    test.cur_country, test.link)

    def is_link_to_part2_present_in_table_of_content(self):
        return True if self.driver.find_element(*Locators.LINK_PART2_IN_TABLE_OF_CONTENT) else False

    def is_part2_present_in_titles(self):
        try:
            self.driver.find_element(*Locators.PART2_IN_TITLE)
            return True
        except NoSuchElementException:
            return False
