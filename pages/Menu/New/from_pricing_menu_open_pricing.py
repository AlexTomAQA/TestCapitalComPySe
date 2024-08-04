"""
-*- coding: utf-8 -*-
@Time    : 2024/08/04 21:35 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import PricingMenuNew

SUBMENU_FCA_PRICING = ("css selector", "div > a[data-type='nav_id737']")
SUBMENU_SCA_PRICING = ("css selector", "div > a[data-type='nav_id804']")


class MenuNew(MenuBase):

    @allure.step('Select "Pricing" menu, "Pricing" submenu')
    def from_pricing_menu_open_pricing(self, d, cur_language, cur_country, link):

        menu_name = "Pricing"
        menu_locator = ""
        submenu_name = "Pricing"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = PricingMenuNew.MENU_FCA_PRICING
            submenu_locator = SUBMENU_FCA_PRICING
        if cur_country == 'ae':
            menu_locator = PricingMenuNew.MENU_SCA_PRICING
            submenu_locator = SUBMENU_SCA_PRICING

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, link, cur_language, cur_country, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
