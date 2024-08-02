"""
-*- coding: utf-8 -*-
@Time    : 2024/07/30
@Author  : Alexander Tomelo
"""
from datetime import datetime

import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import LearnMenuNew
from pages.common import Common

SUB_MENU_NEW_RISK = ()


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
        menu_locator = LearnMenuNew.MENU_NEW_LEARN
        submenu_name = "Risk-management guide"
        submenu_locator = SUB_MENU_NEW_RISK
        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, link, cur_language, cur_country, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
