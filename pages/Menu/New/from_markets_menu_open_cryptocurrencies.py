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
# SUB_MENU_SCA_CRYPTOCURRENCIES = (By.CSS_SELECTOR, 'div.grid_grid__2D3md > a[data-type="nav_id895"')


class Cryptocurrencies(MenuBase):
    @allure.step('Select "Markets" menu, "Cryptocurrencies" submenu')
    def from_markets_menu_open_cryptocurrencies(self, d, cur_language, cur_country, link):

        menu_name = "Markets"
        menu_locator = ""
        submenu_name = "Cryptocurrencies"
        submenu_locator = ""

        if cur_country == 'ae':
            menu_locator = MarketsMenuNew.MARKETS_MENU_SCA_LOCATOR
            submenu_locator = CRYPTOCURRENCIES_SUBMENU_SCA_LOCATOR

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, link, cur_language, cur_country, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
