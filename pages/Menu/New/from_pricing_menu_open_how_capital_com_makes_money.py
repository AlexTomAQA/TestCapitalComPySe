"""
-*- coding: utf-8 -*-
@Time    : 2024/08/01
@Author  : Artem Dashkov
"""
# import time
# from datetime import datetime

import allure
from selenium.webdriver.common.by import By

# from pages.base_page import BasePage
# from pages.common import Common
from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import PricingMenuNew

SUB_MENU_FCA_HOW_CAPITAL_COM_MAKES_MONEY = (By.CSS_SELECTOR, 'div.grid_grid__2D3md > a[data-type="nav_id742"')
SUB_MENU_SCA_HOW_CAPITAL_COM_MAKES_MONEY = (By.CSS_SELECTOR, 'div.grid_grid__2D3md > a[data-type="nav_id814"')


class MenuNew(MenuBase):
    """Class for Menu on license FCA and SCA"""
    @allure.step('Select "Pricing" menu, "How Capital.com makes money" submenu')
    def from_pricing_menu_open_how_capital_com_makes_money(self, d, cur_language, cur_country, link):

        menu_name = "Pricing"
        menu_locator = None
        match cur_country:
            case "":
                menu_locator = PricingMenuNew.MENU_FCA_PRICING
            case "ae":
                menu_locator = PricingMenuNew.MENU_SCA_PRICING

        submenu_locator = None
        submenu_name = "How Capital.com makes money"
        match cur_country:
            case "":
                submenu_locator = SUB_MENU_FCA_HOW_CAPITAL_COM_MAKES_MONEY
            case "ae":
                submenu_locator = SUB_MENU_SCA_HOW_CAPITAL_COM_MAKES_MONEY

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
