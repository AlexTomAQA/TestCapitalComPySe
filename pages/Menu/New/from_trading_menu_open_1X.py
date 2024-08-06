"""
-*- coding: utf-8 -*-
@Time    : 2024/08/01 19:30
@Author  : Kasilà
"""

import allure
from selenium.webdriver.common.by import By

from pages.Menu.New.menu_new_base import MenuBase

TRADING_MENU_FCA_LOCATOR = (By.CSS_SELECTOR, ".menuGroup_linkfirstLevel__d5JGC > [data-type='nav_id686']")
ONEX_SUBMENU_FCA_LOCATOR = (By.CSS_SELECTOR, "a[data-type='nav_id733']")

class OneX(MenuBase):
    @allure.step('Select "Trading" menu, "1X" submenu')
    def from_trading_menu_open_1X(self, d, cur_language, cur_country, link):

        menu_name = "Trading"
        menu_locator = ""
        submenu_name = "1X"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = TRADING_MENU_FCA_LOCATOR
            submenu_locator = ONEX_SUBMENU_FCA_LOCATOR

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
    