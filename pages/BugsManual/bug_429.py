"""
-*- coding: utf-8 -*-
@Time    : 2024/11/17
@Author  : Aleksei Kurochkin
"""
from pages.base_page import BasePage
from pages.Menu.New.from_markets_menu_open_commodities import MenuNew


class Locators:
    SILVER_COMMODITY = (
        'xpath', "//div[@class='grid_grid__2D3md helpers_frameLoader__7Uhll grid_gXs__xir6K']//a[text()='Silver']")
    TO_THE_ARTICLE = (
        'xpath', "//b[text()='Why is the silver price falling? Sinks further below the pivotal $20 mark']")
    FIRST_PARAGRAPH_THAT_STARTS_WITH_BOLD = (
        'xpath', "//strong[text()='What is the outlook for silver prices?']/../..//p/strong")


class Bug429(BasePage):

    @staticmethod
    def open_commodities_page(d, cur_language, cur_country, link):
        MenuNew(d).from_markets_menu_open_commodities(d, cur_language, cur_country, link)

    def open_silver_commodity(self):
        self.driver.find_element(*Locators.SILVER_COMMODITY).click()

    def open_the_article(self):
        self.driver.find_element(*Locators.TO_THE_ARTICLE).click()

    def is_paragraph_with_bold_text_present(self):
        if self.driver.find_element(*Locators.FIRST_PARAGRAPH_THAT_STARTS_WITH_BOLD):
            return True
        return False
