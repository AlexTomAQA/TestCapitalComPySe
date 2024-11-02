"""
-*- coding: utf-8 -*-
@Time    : 2024/08/06 22:33 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import AboutUsMenuNew

SUBMENU_FCA_LEADERSHIP_TEAM = ("css selector", "[data-type='nav_id702']")
SUBMENU_SCA_LEADERSHIP_TEAM = ("css selector", "[data-type='nav_id811']")
SUBMENU_ASIC_LEADERSHIP_TEAM = ("css selector", "[data-type='nav_id811']")
SUBMENU_CYSEC_LEADERSHIP_TEAM = ("css selector", "[data-type='nav_id1694']")


class MenuNew(MenuBase):

    @allure.step('Select "About us" menu, "Leadership team" submenu')
    def from_about_us_menu_open_leadership_team(self, d, cur_language, cur_country, link):

        menu_name = "About us"
        menu_locator = ""
        submenu_name = "Leadership team"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = AboutUsMenuNew.MENU_FCA_ABOUT_US
            submenu_locator = SUBMENU_FCA_LEADERSHIP_TEAM
        if cur_country == 'ae':
            menu_locator = AboutUsMenuNew.MENU_SCA_ABOUT_US
            submenu_locator = SUBMENU_SCA_LEADERSHIP_TEAM
        if cur_country == 'au':
            menu_locator = AboutUsMenuNew.MENU_ASIC_ABOUT_US
            submenu_locator = SUBMENU_ASIC_LEADERSHIP_TEAM
        if cur_country in ['at', 'de']:
            menu_locator = AboutUsMenuNew.MENU_CYSEC_ABOUT_US
            submenu_locator = SUBMENU_CYSEC_LEADERSHIP_TEAM

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
