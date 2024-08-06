"""
-*- coding: utf-8 -*-
@Time    : 2024/08/06 22:29 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import AboutUsMenuNew

SUBMENU_FCA_OUR_OFFICES = ("css selector", "[data-type='nav_id692']")
SUBMENU_SCA_OUR_OFFICES = ("css selector", "[data-type='nav_id809']")


class MenuNew(MenuBase):

    @allure.step('Select "About us" menu, "Our offices" submenu')
    def from_about_us_menu_open_our_offices(self, d, cur_language, cur_country, link):

        menu_name = "About us"
        menu_locator = ""
        submenu_name = "Our offices"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = AboutUsMenuNew.MENU_FCA_ABOUT_US
            submenu_locator = SUBMENU_FCA_OUR_OFFICES
        if cur_country == 'ae':
            menu_locator = AboutUsMenuNew.MENU_SCA_ABOUT_US
            submenu_locator = SUBMENU_SCA_OUR_OFFICES

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
