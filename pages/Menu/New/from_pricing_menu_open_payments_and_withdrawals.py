"""
-*- coding: utf-8 -*-
@Time    : 2024/09/12 19:00 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import PricingMenuNew

SUBMENU_SCA_PAYMENTS_AND_WITHDRAWALS = ("css selector", "[data-type='nav_id1786']")
SUBMENU_ASIC_PAYMENTS_AND_WITHDRAWALS = ("css selector", "[data-type='nav_id1787']")


class MenuNew(MenuBase):

    @allure.step('Select "Pricing" menu, "Payments and withdrawals" submenu')
    def from_pricing_menu_open_payments_and_withdrawals(self, d, cur_language, cur_country, link):

        menu_name = "Pricing"
        menu_locator = ""
        submenu_name = "Payments and withdrawals"
        submenu_locator = ""

        if cur_country == 'ae':
            menu_locator = PricingMenuNew.MENU_SCA_PRICING
            submenu_locator = SUBMENU_SCA_PAYMENTS_AND_WITHDRAWALS
        if cur_country == 'au':
            menu_locator = PricingMenuNew.MENU_ASIC_PRICING
            submenu_locator = SUBMENU_ASIC_PAYMENTS_AND_WITHDRAWALS

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
