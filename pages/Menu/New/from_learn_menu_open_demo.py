"""
-*- coding: utf-8 -*-
@Time    : 2024/08/06 21:25 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import LearnMenuNew
from pages.conditions_v2 import CYSEC_COUNTRIES

SUBMENU_FCA_DEMO = ('css selector', '[data-type="nav_id1007"]')
SUBMENU_SCA_DEMO = ('css selector', '[data-type="nav_id822"]')
SUBMENU_ASIC_DEMO = ('css selector', '[data-type="nav_id1178"]')
SUBMENU_CYSEC_DEMO = ('css selector', '[data-type="nav_id1595"]')


class MenuNew(MenuBase):

    @allure.step('Select "Learn" menu, "Demo" submenu')
    def from_learn_menu_open_demo(self, d, cur_language, cur_country, link):

        menu_name = "Learn"
        menu_locator = ""
        submenu_name = "Demo"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = LearnMenuNew.MENU_FCA_LEARN
            submenu_locator = SUBMENU_FCA_DEMO
        if cur_country == 'ae':
            menu_locator = LearnMenuNew.MENU_SCA_LEARN
            submenu_locator = SUBMENU_SCA_DEMO
        if cur_country == 'au':
            menu_locator = LearnMenuNew.MENU_ASIC_LEARN
            submenu_locator = SUBMENU_ASIC_DEMO
        if cur_country in CYSEC_COUNTRIES:
            menu_locator = LearnMenuNew.MENU_CYSEC_LEARN
            submenu_locator = SUBMENU_CYSEC_DEMO

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
