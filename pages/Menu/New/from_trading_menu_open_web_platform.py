"""
-*- coding: utf-8 -*-
@Time    : 2024/07/30
@Author  : Alexander Tomelo
"""
import time
from datetime import datetime

import allure

from pages.base_page import BasePage
from pages.common import Common
from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import TradingMenuNew


class MenuNew(MenuBase):
    """Class for Menu on license FCA and SCA"""
    @allure.step('Select "Trading" menu, "Web platform" submenu')
    def from_trading_menu_open_web_platform(self, d, cur_language, cur_country, link):

        menu_name = "Trading"
        menu_locator = TradingMenuNew.MENU_SCA_TRADING
        submenu_name = "Web platform"
        submenu_locator = TradingMenuNew.SUB_MENU_SCA_WEB_PLATFORM
        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, link, cur_language, cur_country, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
