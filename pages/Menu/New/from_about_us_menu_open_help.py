"""
-*- coding: utf-8 -*-
@Time    : 2024/08/06 22:45 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import AboutUsMenuNew
from pages.conditions_v2 import CYSEC_COUNTRIES

SUBMENU_FCA_HELP = ("css selector", "[data-type='nav_id743']")
SUBMENU_SCA_HELP = ("css selector", "[data-type='nav_id871']")
SUBMENU_ASIC_HELP = ("css selector", "[data-type='nav_id1282']")
SUBMENU_CYSEC_HELP = ("css selector", "[data-type='nav_id1699']")


class MenuNew(MenuBase):

    @allure.step('Select "About us" menu, "Help" submenu')
    def from_about_us_menu_open_help(self, d, cur_language, cur_country, link):

        menu_name = "About us"
        menu_locator = ""
        submenu_name = "Help"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = AboutUsMenuNew.MENU_FCA_ABOUT_US
            submenu_locator = SUBMENU_FCA_HELP
        if cur_country == 'ae':
            menu_locator = AboutUsMenuNew.MENU_SCA_ABOUT_US
            submenu_locator = SUBMENU_SCA_HELP
        if cur_country == 'au':
            menu_locator = AboutUsMenuNew.MENU_ASIC_ABOUT_US
            submenu_locator = SUBMENU_ASIC_HELP
        if cur_country in CYSEC_COUNTRIES:
            menu_locator = AboutUsMenuNew.MENU_CYSEC_ABOUT_US
            submenu_locator = SUBMENU_CYSEC_HELP

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
