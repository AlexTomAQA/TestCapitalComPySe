"""
-*- coding: utf-8 -*-
@Time    : 2024/08/01 18:00 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import TradingMenuNew
from pages.conditions_v2 import CYSEC_COUNTRIES

SUBMENU_FCA_CFD_TRADING = ("css selector", "[data-type='nav_id734']")
SUBMENU_SCA_CFD_TRADING = ("css selector", "[data-type='nav_id800']")
SUBMENU_ASIC_CFD_TRADING = ("css selector", "[data-type='nav_id1296']")
SUBMENU_CYSEC_CFD_TRADING = ("css selector", "[data-type='nav_id1713']")


class MenuNew(MenuBase):

    @allure.step('Select "Trading" menu, "CFD trading" submenu')
    def from_trading_menu_open_cfd_trading(self, d, cur_language, cur_country, link):

        menu_name = "Trading"
        menu_locator = ""
        submenu_name = "CFD trading"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = TradingMenuNew.MENU_FCA_TRADING
            submenu_locator = SUBMENU_FCA_CFD_TRADING
        if cur_country == 'ae':
            menu_locator = TradingMenuNew.MENU_SCA_TRADING
            submenu_locator = SUBMENU_SCA_CFD_TRADING
        if cur_country == 'au':
            menu_locator = TradingMenuNew.MENU_ASIC_TRADING
            submenu_locator = SUBMENU_ASIC_CFD_TRADING
        if cur_country in CYSEC_COUNTRIES:
            menu_locator = TradingMenuNew.MENU_CYSEC_TRADING
            submenu_locator = SUBMENU_CYSEC_CFD_TRADING

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
