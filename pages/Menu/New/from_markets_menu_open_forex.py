"""
-*- coding: utf-8 -*-
@Time    : 2024/08/05
@Author  : podchasova11
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import MarketsMenuNew

SUBMENU_FCA_FOREX = ("css selector", ".menuGroup_link__z_L3O[data-type='nav_id690']")
SUBMENU_SCA_FOREX = ("css selector", ".menuGroup_link__z_L3O[data-type='nav_id825']")
SUBMENU_SCA_AR_LOCATOR = ("css selector", ".menuGroup_link__z_L3O[data-type='nav_id825']")


class MenuNewForex(MenuBase):

    @allure.step('Select "Markets" menu, "Forex" submenu')
    def from_markets_menu_open_forex(self, d, cur_language, cur_country, link):

        menu_name = "Markets"
        menu_locator = ""
        submenu_name = "Forex"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = MarketsMenuNew.MENU_FCA_MARKETS
            submenu_locator = SUBMENU_FCA_FOREX
        elif cur_country == 'ae':
            menu_locator = MarketsMenuNew.MENU_SCA_MARKETS
            submenu_locator = SUBMENU_SCA_FOREX
        elif cur_country == 'ae' and cur_language == 'ar':
            menu_locator = MarketsMenuNew.MENU_SCA_MARKETS
            submenu_locator = SUBMENU_SCA_AR_LOCATOR

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, link, cur_language, cur_country, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
