"""
-*- coding: utf-8 -*-
@Time    : 2024/08/06 21:33 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import LearnMenuNew
from pages.conditions_v2 import CYSEC_COUNTRIES

SUBMENU_FCA_TRADING_STRATEGIES = ('css selector', '[data-type="nav_id697"]')
SUBMENU_SCA_TRADING_STRATEGIES = ('css selector', '[data-type="nav_id832"]')
SUBMENU_ASIC_TRADING_STRATEGIES = ('css selector', '[data-type="nav_id1217"]')
SUBMENU_CYSEC_TRADING_STRATEGIES = ('css selector', '[data-type="nav_id1634"]')


class MenuNew(MenuBase):

    @allure.step('Select "Learn" menu, "Trading Strategies" submenu')
    def from_learn_menu_open_trading_strategies(self, d, cur_language, cur_country, link):

        menu_name = "Learn"
        menu_locator = ""
        submenu_name = "Trading Strategies"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = LearnMenuNew.MENU_FCA_LEARN
            submenu_locator = SUBMENU_FCA_TRADING_STRATEGIES
        if cur_country == 'ae':
            menu_locator = LearnMenuNew.MENU_SCA_LEARN
            submenu_locator = SUBMENU_SCA_TRADING_STRATEGIES
        if cur_country == 'au':
            menu_locator = LearnMenuNew.MENU_ASIC_LEARN
            submenu_locator = SUBMENU_ASIC_TRADING_STRATEGIES
        if cur_country in CYSEC_COUNTRIES:
            menu_locator = LearnMenuNew.MENU_CYSEC_LEARN
            submenu_locator = SUBMENU_CYSEC_TRADING_STRATEGIES

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
