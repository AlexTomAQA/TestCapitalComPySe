"""
@Author  : Aleksei Kurochkin
"""
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.Menu.New.from_pricing_menu_open_charges_and_fees import MenuNew


class Locators:
    LINK_FIND_OUT_MORE = (By.XPATH, "//a[contains(text(), 'Find out more')]")
    PAGE_LOADER = (By.XPATH, "//div[@class='pageLoader_loader__QsVJC']")


class Bug603(BasePage):

    def __init__(self, test):
        super().__init__(test.driver, test.link, test.bid)

    def open_charges_and_fees_page(self, test):
        MenuNew(self.driver).from_pricing_menu_open_charges_and_fees(test.driver, test.cur_language,
                                                                     test.cur_country, test.link)

    def click_find_out_more_link(self):
        self.driver.find_element(*Locators.LINK_FIND_OUT_MORE).click()

    def if_page_loader_present(self):
        try:
            self.driver.find_element(*Locators.PAGE_LOADER)
            return True
        except NoSuchElementException:
            return False
