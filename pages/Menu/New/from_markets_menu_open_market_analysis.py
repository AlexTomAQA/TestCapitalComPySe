"""
-*- coding: utf-8 -*-
@Time    : 2024/08/04 21:25 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import MarketsMenuNew
from pages.conditions_v2 import CYSEC_COUNTRIES

SUBMENU_FCA_MARKET_ANALYSIS = ("css selector", "[data-type='nav_id771']")
SUBMENU_SCA_MARKET_ANALYSIS = ("css selector", "[data-type='nav_id869']")
SUBMENU_ASIC_MARKET_ANALYSIS = ("css selector", "[data-type='nav_id1268']")
SUBMENU_CYSEC_MARKET_ANALYSIS = ("css selector", "[data-type='nav_id1685']")


class MenuNew(MenuBase):

    @allure.step('Select "Markets" menu, "Market analysis" submenu')
    def from_markets_menu_open_market_analysis(self, d, cur_language, cur_country, link):

        menu_name = "Markets"
        menu_locator = ""
        submenu_name = "Market analysis"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = MarketsMenuNew.MENU_FCA_MARKETS
            submenu_locator = SUBMENU_FCA_MARKET_ANALYSIS
        if cur_country == 'ae':
            menu_locator = MarketsMenuNew.MENU_SCA_MARKETS
            submenu_locator = SUBMENU_SCA_MARKET_ANALYSIS
        if cur_country == 'au':
            menu_locator = MarketsMenuNew.MENU_ASIC_MARKETS
            submenu_locator = SUBMENU_ASIC_MARKET_ANALYSIS
        if cur_country in CYSEC_COUNTRIES:
            menu_locator = MarketsMenuNew.MENU_CYSEC_MARKETS
            submenu_locator = SUBMENU_CYSEC_MARKET_ANALYSIS

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
