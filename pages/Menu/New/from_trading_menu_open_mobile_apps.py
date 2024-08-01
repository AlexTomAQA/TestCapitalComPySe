"""
-*- coding: utf-8 -*-
@Time    : 2024/08/01 18:45 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase

trading_menu_loc_fca = ("css selector", ".menuGroup_linkfirstLevel__d5JGC > [data-type='nav_id686']")
trading_menu_loc_sca = ("css selector", ".menuGroup_linkfirstLevel__d5JGC > [data-type='nav_id798']")
mobile_apps_submenu_loc_fca = ("css selector", "[data-type='nav_id748']")
mobile_apps_submenu_loc_sca = ("css selector", "[data-type='nav_id821']")


class MenuNew(MenuBase):

    @allure.step('Select "Trading" menu, "Mobile apps" submenu')
    def from_trading_menu_open_mobile_apps(self, d, cur_language, cur_country, link):

        menu_name = "Trading"
        menu_locator = ""
        submenu_name = "Mobile apps"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = trading_menu_loc_fca
            submenu_locator = mobile_apps_submenu_loc_fca
        if cur_country == 'ae':
            menu_locator = trading_menu_loc_sca
            submenu_locator = mobile_apps_submenu_loc_sca

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, link, cur_language, cur_country, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
