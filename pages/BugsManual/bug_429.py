"""
-*- coding: utf-8 -*-
@Time    : 2024/11/17
@Author  : Aleksei Kurochkin
"""
from pages.base_page import BasePage
from pages.Menu.New.from_markets_menu_open_market_analysis import MenuNew


class Locators:
    SILVER_COMMODITY = (
        'xpath', "//div[@class='grid_grid__2D3md helpers_frameLoader__7Uhll grid_gXs__xir6K']//a[text()='Silver']")
    FIRST_PARAGRAPH_THAT_STARTS_WITH_BOLD = (
        'xpath', "//strong[text()='What is the outlook for silver prices?']/../..//p/strong")


class Bug429(BasePage):

    def __init__(self, test):
        super().__init__(test.driver, test.link, test.bid)

    def open_market_analysis_page(self, test):
        MenuNew(self.driver).from_markets_menu_open_market_analysis(test.driver, test.cur_language,
                                                                    test.cur_country, test.link)

    def is_paragraph_with_bold_text_present(self):
        if self.driver.find_element(*Locators.FIRST_PARAGRAPH_THAT_STARTS_WITH_BOLD):
            return True
        return False
