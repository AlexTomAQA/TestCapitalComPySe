"""
-*- coding: utf-8 -*-
@Time    : 2024/09/10 20:50 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import TradingMenuNew

SUBMENU_ASIC_PROFESSIONAL = ("css selector", "[data-type='nav_id1744']")


class MenuNew(MenuBase):

    @allure.step('Select "Trading" menu, "Professional" submenu')
    def from_trading_menu_open_professional(self, d, cur_language, cur_country, link):

        menu_name = "Trading"
        menu_locator = ""
        submenu_name = "Professional"
        submenu_locator = ""

        if cur_country == 'au':
            menu_locator = TradingMenuNew.MENU_ASIC_TRADING
            submenu_locator = SUBMENU_ASIC_PROFESSIONAL

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
