"""
-*- coding: utf-8 -*-
@Time    : 2024/09/12 18:20 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import TradingMenuNew

SUBMENU_FCA_CFD_CALCULATOR = ("css selector", "[data-type='nav_id1771']")
SUBMENU_SCA_CFD_CALCULATOR = ("css selector", "[data-type='nav_id1775']")


class MenuNew(MenuBase):

    @allure.step('Select "Trading" menu, "CFD trading calculator" submenu')
    def from_trading_menu_open_cfd_calculator(self, d, cur_language, cur_country, link):

        menu_name = "Trading"
        menu_locator = ""
        submenu_name = "CFD trading calculator"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = TradingMenuNew.MENU_FCA_TRADING
            submenu_locator = SUBMENU_FCA_CFD_CALCULATOR
        if cur_country == 'ae':
            menu_locator = TradingMenuNew.MENU_SCA_TRADING
            submenu_locator = SUBMENU_SCA_CFD_CALCULATOR

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
