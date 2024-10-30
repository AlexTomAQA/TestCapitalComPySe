"""
-*- coding: utf-8 -*-
@Time    : 2024/08/01 18:58 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import TradingMenuNew

SUBMENU_FCA_MARGIN_CALLS = ("css selector", "[data-type='nav_id766']")
SUBMENU_SCA_MARGIN_CALLS = ("css selector", "[data-type='nav_id806']")
SUBMENU_ASIC_MARGIN_CALLS = ("css selector", "[data-type='nav_id1306']")
SUBMENU_CYSEC_MARGIN_CALLS = ("css selector", "[data-type='nav_id1723']")


class MenuNew(MenuBase):

    @allure.step('Select "Trading" menu, "Margin Calls" submenu')
    def from_trading_menu_open_margin_calls(self, d, cur_language, cur_country, link):

        menu_name = "Trading"
        menu_locator = ""
        submenu_name = "Margin Calls"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = TradingMenuNew.MENU_FCA_TRADING
            submenu_locator = SUBMENU_FCA_MARGIN_CALLS
        if cur_country == 'ae':
            menu_locator = TradingMenuNew.MENU_SCA_TRADING
            submenu_locator = SUBMENU_SCA_MARGIN_CALLS
        if cur_country == 'au':
            menu_locator = TradingMenuNew.MENU_ASIC_TRADING
            submenu_locator = SUBMENU_ASIC_MARGIN_CALLS
        if cur_country in ['at', 'de']:
            menu_locator = TradingMenuNew.MENU_CYSEC_TRADING
            submenu_locator = SUBMENU_CYSEC_MARGIN_CALLS

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
