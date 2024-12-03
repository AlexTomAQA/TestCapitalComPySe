"""
-*- coding: utf-8 -*-
@Time    : 2024/07/30
@Author  : Alexander Tomelo
"""
import allure
from selenium.webdriver.common.by import By

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import TradingMenuNew
from pages.conditions_v2 import CYSEC_COUNTRIES

SUBMENU_FCA_WEB_PLATFORM = (By.CSS_SELECTOR, '[data-type="nav_id704"]')
SUBMENU_SCA_WEB_PLATFORM = (By.CSS_SELECTOR, '[data-type="nav_id818"]')
SUBMENU_ASIC_WEB_PLATFORM = (By.CSS_SELECTOR, '[data-type="nav_id1303"]')
SUBMENU_CYSEC_WEB_PLATFORM = (By.CSS_SELECTOR, '[data-type="nav_id1720"]')


class MenuNew(MenuBase):

    @allure.step('Select "Trading" menu, "Web platform" submenu')
    def from_trading_menu_open_web_platform(self, d, cur_language, cur_country, link):

        menu_name = "Trading"
        menu_locator = ""
        submenu_name = "Web platform"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = TradingMenuNew.MENU_FCA_TRADING
            submenu_locator = SUBMENU_FCA_WEB_PLATFORM
        if cur_country == 'ae':
            menu_locator = TradingMenuNew.MENU_SCA_TRADING
            submenu_locator = SUBMENU_SCA_WEB_PLATFORM
        if cur_country == 'au':
            menu_locator = TradingMenuNew.MENU_ASIC_TRADING
            submenu_locator = SUBMENU_ASIC_WEB_PLATFORM
        if cur_country in CYSEC_COUNTRIES:
            menu_locator = TradingMenuNew.MENU_CYSEC_TRADING
            submenu_locator = SUBMENU_CYSEC_WEB_PLATFORM

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
