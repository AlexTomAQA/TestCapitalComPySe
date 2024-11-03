"""
-*- coding: utf-8 -*-
@Time    : 2024/08/06 22:20 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import AboutUsMenuNew

SUBMENU_FCA_WHY_CAPITAL = ("css selector", "[data-type='nav_id687']")
SUBMENU_SCA_WHY_CAPITAL = ("css selector", "[data-type='nav_id807']")
SUBMENU_ASIC_WHY_CAPITAL = ("css selector", "[data-type='nav_id1280']")
SUBMENU_CYSEC_WHY_CAPITAL = ("css selector", "[data-type='nav_id1697']")


class MenuNew(MenuBase):

    @allure.step('Select "About us" menu, "Why Capital.com?" submenu')
    def from_about_us_menu_open_why_capital(self, d, cur_language, cur_country, link):

        menu_name = "About us"
        menu_locator = ""
        submenu_name = "Why Capital.com?"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = AboutUsMenuNew.MENU_FCA_ABOUT_US
            submenu_locator = SUBMENU_FCA_WHY_CAPITAL
        if cur_country == 'ae':
            menu_locator = AboutUsMenuNew.MENU_SCA_ABOUT_US
            submenu_locator = SUBMENU_SCA_WHY_CAPITAL
        if cur_country == 'au':
            menu_locator = AboutUsMenuNew.MENU_ASIC_ABOUT_US
            submenu_locator = SUBMENU_ASIC_WHY_CAPITAL
        if cur_country in ['at', 'de']:
            menu_locator = AboutUsMenuNew.MENU_CYSEC_ABOUT_US
            submenu_locator = SUBMENU_CYSEC_WHY_CAPITAL

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
