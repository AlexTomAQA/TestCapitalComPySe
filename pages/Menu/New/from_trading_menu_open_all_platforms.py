"""
-*- coding: utf-8 -*-
@Time    : 2024/08/01 18:35 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import TradingMenuNew

SUBMENU_FCA_ALL_PLATFORMS = ("css selector", "[data-type='nav_id688']")
SUBMENU_SCA_ALL_PLATFORMS = ("css selector", "[data-type='nav_id817']")


class MenuNew(MenuBase):

    @allure.step('Select "Trading" menu, "All platforms" submenu')
    def from_trading_menu_open_all_platforms(self, d, cur_language, cur_country, link):

        menu_name = "Trading"
        menu_locator = ""
        submenu_name = "All platforms"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = TradingMenuNew.MENU_FCA_TRADING
            submenu_locator = SUBMENU_FCA_ALL_PLATFORMS
        if cur_country == 'ae':
            menu_locator = TradingMenuNew.MENU_SCA_TRADING
            submenu_locator = SUBMENU_SCA_ALL_PLATFORMS

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
