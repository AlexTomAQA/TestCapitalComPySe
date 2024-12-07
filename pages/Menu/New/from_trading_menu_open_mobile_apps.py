"""
-*- coding: utf-8 -*-
@Time    : 2024/08/01 18:45 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import TradingMenuNew
from pages.conditions_v2 import CYSEC_COUNTRIES

SUBMENU_FCA_MOBILE_APPS = ("css selector", "[data-type='nav_id748']")
SUBMENU_SCA_MOBILE_APPS = ("css selector", "[data-type='nav_id821']")
SUBMENU_ASIC_MOBILE_APPS = ("css selector", "[data-type='nav_id1300']")
SUBMENU_CYSEC_MOBILE_APPS = ("css selector", "[data-type='nav_id1717']")


class MenuNew(MenuBase):

    @allure.step('Select "Trading" menu, "Mobile apps" submenu')
    def from_trading_menu_open_mobile_apps(self, d, cur_language, cur_country, link):

        menu_name = "Trading"
        menu_locator = ""
        submenu_name = "Mobile apps"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = TradingMenuNew.MENU_FCA_TRADING
            submenu_locator = SUBMENU_FCA_MOBILE_APPS
        if cur_country == 'ae':
            menu_locator = TradingMenuNew.MENU_SCA_TRADING
            submenu_locator = SUBMENU_SCA_MOBILE_APPS
        if cur_country == 'au':
            menu_locator = TradingMenuNew.MENU_ASIC_TRADING
            submenu_locator = SUBMENU_ASIC_MOBILE_APPS
        if cur_country in CYSEC_COUNTRIES:
            menu_locator = TradingMenuNew.MENU_CYSEC_TRADING
            submenu_locator = SUBMENU_CYSEC_MOBILE_APPS

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
