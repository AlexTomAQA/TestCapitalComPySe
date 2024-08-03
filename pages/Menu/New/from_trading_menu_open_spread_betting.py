"""
-*- coding: utf-8 -*-
@Time    : 2024/07/31
@Author  : podchasova11
"""
# import time
# from datetime import datetime
# import pytest
import allure
from selenium.webdriver.common.by import By

# from pages.base_page import BasePage
# from pages.common import Common
from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import TradingMenuNew

SUB_MENU_FCA_SPREAD_BETTING = (By.CSS_SELECTOR, '[data-type="nav_id735"]')


class MenuNewSpreadBetting(MenuBase):
    """Class for Menu on license FCA and SCA"""
    @allure.step('Select "Trading" menu, "Spread betting" submenu')
    def from_trading_menu_open_spread_betting(self, d, cur_language, cur_country, link):

        menu_name = "Trading"
        menu_locator = TradingMenuNew.MENU_FCA_TRADING
        submenu_name = "Spread betting"
        submenu_locator = SUB_MENU_FCA_SPREAD_BETTING
        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, link, cur_language, cur_country, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
