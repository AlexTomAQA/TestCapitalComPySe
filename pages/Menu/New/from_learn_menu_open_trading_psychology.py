"""
-*- coding: utf-8 -*-
@Time    : 2024/08/06 21:37 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import LearnMenuNew

SUBMENU_FCA_TRADING_PSYCHOLOGY = ('css selector', '[data-type="nav_id755"]')
SUBMENU_SCA_TRADING_PSYCHOLOGY = ('css selector', '[data-type="nav_id883"]')
SUBMENU_ASIC_TRADING_PSYCHOLOGY = ('css selector', '[data-type="nav_id1248"]')


class MenuNew(MenuBase):

    @allure.step('Select "Learn" menu, "Trading Psychology" submenu')
    def from_learn_menu_open_trading_psychology(self, d, cur_language, cur_country, link):

        menu_name = "Learn"
        menu_locator = ""
        submenu_name = "Trading Psychology"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = LearnMenuNew.MENU_FCA_LEARN
            submenu_locator = SUBMENU_FCA_TRADING_PSYCHOLOGY
        if cur_country == 'ae':
            menu_locator = LearnMenuNew.MENU_SCA_LEARN
            submenu_locator = SUBMENU_SCA_TRADING_PSYCHOLOGY
        if cur_country == 'au':
            menu_locator = LearnMenuNew.MENU_ASIC_LEARN
            submenu_locator = SUBMENU_ASIC_TRADING_PSYCHOLOGY

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
