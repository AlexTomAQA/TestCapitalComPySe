"""
-*- codind: utf-8 -*-
@Time     : 24/08/02 09:00 GMT +3
@Author   : podchasova11

"""

import allure
from selenium.webdriver.common.by import By

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import TradingMenuNew

SUB_MENU_FCA_DEMO_EN = (By.CSS_SELECTOR, "div.grid_grid__2D3md > a[data-type='nav_id751']")
SUB_MENU_SCA_DEMO_EN = (By.CSS_SELECTOR, "div.grid_grid__2D3md > a[data-type='nav_id1029']")


class MenuNewDemo(MenuBase):

    @allure.step("Select 'Trading' menu 'Demo' submenu")
    def from_trading_menu_open_demo(self, d, cur_language, cur_country, link):
        menu_name = 'Trading'
        menu_locator = ''
        submenu_name = 'Demo'
        submenu_locator = ''

        if cur_country == 'gb':
            menu_locator = TradingMenuNew.MENU_FCA_TRADING
            submenu_locator = SUB_MENU_FCA_DEMO_EN
        if cur_country == 'ae':
            menu_locator = TradingMenuNew.MENU_SCA_TRADING
            submenu_locator = SUB_MENU_SCA_DEMO_EN

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer





