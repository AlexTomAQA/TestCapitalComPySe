"""
-*- coding: utf-8 -*-
@Time    : 2024/08/06 23:05 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import AboutUsMenuNew

SUBMENU_FCA_TERMS_AND_POLICIES = ("css selector", "[data-type='nav_id768']")
SUBMENU_SCA_TERMS_AND_POLICIES = ("css selector", "[data-type='nav_id874']")
SUBMENU_ASIC_TERMS_AND_POLICIES = ("css selector", "[data-type='nav_id1285']")


class MenuNew(MenuBase):

    @allure.step('Select "About us" menu, "Terms and Policies" submenu')
    def from_about_us_menu_open_terms_and_policies(self, d, cur_language, cur_country, link):

        menu_name = "About us"
        menu_locator = ""
        submenu_name = "Terms and Policies"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = AboutUsMenuNew.MENU_FCA_ABOUT_US
            submenu_locator = SUBMENU_FCA_TERMS_AND_POLICIES
        if cur_country == 'ae':
            menu_locator = AboutUsMenuNew.MENU_SCA_ABOUT_US
            submenu_locator = SUBMENU_SCA_TERMS_AND_POLICIES
        if cur_country == 'au':
            menu_locator = AboutUsMenuNew.MENU_ASIC_ABOUT_US
            submenu_locator = SUBMENU_ASIC_TERMS_AND_POLICIES

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
