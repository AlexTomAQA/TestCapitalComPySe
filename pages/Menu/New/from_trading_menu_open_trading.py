"""
-*- coding: utf-8 -*-
@Time    : 2024/08/01 18:00 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import TradingMenuNew

SUBMENU_FCA_TRADING = ("css selector", ".helpers_showLg__UPEqH > [data-type='nav_id686']")
SUBMENU_SCA_TRADING = ("css selector", ".helpers_showLg__UPEqH > [data-type='nav_id798']")


class MenuNew(MenuBase):

    @allure.step('Select "Trading" menu, "Trading" submenu')
    def from_trading_menu_open_trading(self, d, cur_language, cur_country, link):

        menu_name = "Trading"
        menu_locator = ""
        submenu_name = "Trading"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = TradingMenuNew.MENU_FCA_TRADING
            submenu_locator = SUBMENU_FCA_TRADING
        if cur_country == 'ae':
            menu_locator = TradingMenuNew.MENU_SCA_TRADING
            submenu_locator = SUBMENU_SCA_TRADING

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, link, cur_language, cur_country, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
