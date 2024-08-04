"""
-*- coding: utf-8 -*-
@Time    : 2024/08/04 21:20 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import MarketsMenuNew

SUBMENU_ESG = ("css selector", "[data-type='nav_id830']")


class MenuNew(MenuBase):

    @allure.step('Select "Markets" menu, "ESG" submenu')
    def from_markets_menu_open_esg(self, d, cur_language, cur_country, link):

        menu_name = "Markets"
        menu_locator = MarketsMenuNew.MENU_SCA_MARKETS
        submenu_name = "ESG"
        submenu_locator = SUBMENU_ESG

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, link, cur_language, cur_country, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
