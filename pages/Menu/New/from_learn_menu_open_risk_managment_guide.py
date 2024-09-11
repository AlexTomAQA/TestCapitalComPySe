"""
-*- coding: utf-8 -*-
@Time    : 2024/07/30
@Author  : Alexander Tomelo
"""
from datetime import datetime

import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import LearnMenuNew

SUBMENU_FCA_RISK_MANAGEMENT_GUIDE = ("css selector", "[data-type='nav_id720']")
SUBMENU_SCA_RISK_MANAGEMENT_GUIDE = ("css selector", "[data-type='nav_id867']")
SUBMENU_ASIC_RISK_MANAGEMENT_GUIDE = ("css selector", "[data-type='nav_id1213']")


class MenuNew(MenuBase):
    """
    MenuSection class - класс работы с меню в хедере
    Аргументы при создании объекта:
        wd - driver
        main_page_link - страница, на которой расположено меню
        flag_set_menu - признак того, что нужное меню выбрано (установлено), необязательный аргумент. По умолчанию =
        False
    """

    def __init__(self, wd, main_page_link, flag_set_menu=False):
        self.flag_set_menu = flag_set_menu
        super().__init__(wd, main_page_link)

    @allure.step('Select "Learn to trade" menu, "Risk-management guide')
    def from_learn_menu_open_risk_management_guide(self, d, cur_language, cur_country, link):

        menu_name = "Learn"
        menu_locator = ""
        submenu_name = "Risk-management guide"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = LearnMenuNew.MENU_FCA_LEARN
            submenu_locator = SUBMENU_FCA_RISK_MANAGEMENT_GUIDE
        if cur_country == 'ae':
            menu_locator = LearnMenuNew.MENU_SCA_LEARN
            submenu_locator = SUBMENU_SCA_RISK_MANAGEMENT_GUIDE
        if cur_country == 'au':
            menu_locator = LearnMenuNew.MENU_ASIC_LEARN
            submenu_locator = SUBMENU_ASIC_RISK_MANAGEMENT_GUIDE

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
