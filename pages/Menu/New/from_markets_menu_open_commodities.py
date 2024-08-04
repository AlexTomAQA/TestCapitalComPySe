"""
-*- coding: utf-8 -*-
@Time    : 2024/08/04 20:55 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import MarketsMenuNew

SUBMENU_FCA_COMMODITIES = ("css selector", "[data-type='nav_id701']")
SUBMENU_SCA_COMMODITIES = ("css selector", "[data-type='nav_id828']")


class MenuNew(MenuBase):

    @allure.step('Select "Markets" menu, "Commodities" submenu')
    def from_markets_menu_open_commodities(self, d, cur_language, cur_country, link):

        menu_name = "Markets"
        menu_locator = ""
        submenu_name = "Commodities"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = MarketsMenuNew.MENU_FCA_MARKETS
            submenu_locator = SUBMENU_FCA_COMMODITIES
        if cur_country == 'ae':
            menu_locator = MarketsMenuNew.MENU_SCA_MARKETS
            submenu_locator = SUBMENU_SCA_COMMODITIES

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, link, cur_language, cur_country, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
