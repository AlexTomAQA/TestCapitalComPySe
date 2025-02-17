"""
-*- coding: utf-8 -*-
@Time    : 2024/08/06 22:36 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import AboutUsMenuNew
from pages.conditions_v2 import CYSEC_COUNTRIES

SUBMENU_FCA_CLIENT_FUNDS = ("css selector", "[data-type='nav_id706']")
SUBMENU_SCA_CLIENT_FUNDS = ("css selector", "[data-type='nav_id813']")
SUBMENU_ASIC_CLIENT_FUNDS = ("css selector", "[data-type='nav_id1275']")
SUBMENU_CYSEC_CLIENT_FUNDS = ("css selector", "[data-type='nav_id1692']")


class MenuNew(MenuBase):

    @allure.step('Select "About us" menu, "Client funds" submenu')
    def from_about_us_menu_open_client_funds(self, d, cur_language, cur_country, link):

        menu_name = "About us"
        menu_locator = ""
        submenu_name = "Client funds"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = AboutUsMenuNew.MENU_FCA_ABOUT_US
            submenu_locator = SUBMENU_FCA_CLIENT_FUNDS
        if cur_country == 'ae':
            menu_locator = AboutUsMenuNew.MENU_SCA_ABOUT_US
            submenu_locator = SUBMENU_SCA_CLIENT_FUNDS
        if cur_country == 'au':
            menu_locator = AboutUsMenuNew.MENU_ASIC_ABOUT_US
            submenu_locator = SUBMENU_ASIC_CLIENT_FUNDS
        if cur_country in CYSEC_COUNTRIES:
            menu_locator = AboutUsMenuNew.MENU_CYSEC_ABOUT_US
            submenu_locator = SUBMENU_CYSEC_CLIENT_FUNDS

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
