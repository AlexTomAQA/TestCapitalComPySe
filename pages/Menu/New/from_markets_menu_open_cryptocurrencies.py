"""
-*- coding: utf-8 -*-
@Time    : 2024/08/01 20:00
@Author  : Kasilà
"""

import allure
from selenium.webdriver.common.by import By

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import MarketsMenuNew


CRYPTOCURRENCIES_SUBMENU_SCA_LOCATOR = (By.CSS_SELECTOR, 'div.grid_grid__2D3md > a[data-type="nav_id895"]')
CRYPTOCURRENCIES_SUBMENU_ASIC_LOCATOR = (By.CSS_SELECTOR, 'div.grid_grid__2D3md > a[data-type="nav_id1266"]')
CRYPTOCURRENCIES_SUBMENU_CYSEC_LOCATOR = (By.CSS_SELECTOR, 'div.grid_grid__2D3md > a[data-type="nav_id1683"]')

class FromMarketsOpenCryptocurrencies(MenuBase):
    @allure.step('Select "Markets" menu, "Cryptocurrencies" submenu')
    def from_markets_menu_open_cryptocurrencies(self, d, cur_language, cur_country, link):

        menu_name = "Markets"
        menu_locator = ""
        submenu_name = "Cryptocurrencies"
        submenu_locator = ""

        if cur_country == 'ae':
            menu_locator = MarketsMenuNew.MENU_SCA_MARKETS
            submenu_locator = CRYPTOCURRENCIES_SUBMENU_SCA_LOCATOR
        if cur_country == 'au':
            menu_locator = MarketsMenuNew.MENU_ASIC_MARKETS
            submenu_locator = CRYPTOCURRENCIES_SUBMENU_ASIC_LOCATOR
        if cur_country == 'de':
            menu_locator = MarketsMenuNew.MENU_CYSEC_MARKETS
            submenu_locator = CRYPTOCURRENCIES_SUBMENU_CYSEC_LOCATOR

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
