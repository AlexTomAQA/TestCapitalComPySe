"""
-*- coding: utf-8 -*-
@Time    : 2024/08/04 21:45 GMT+5
@Author  : Sergey Aiidzhanov
"""
import allure

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import PricingMenuNew
from pages.conditions_v2 import CYSEC_COUNTRIES

SUBMENU_FCA_CHARGES_AND_FEES = ("css selector", "[data-type='nav_id1005']")
SUBMENU_SCA_CHARGES_AND_FEES = ("css selector", "[data-type='nav_id1019']")
SUBMENU_ASIC_CHARGES_AND_FEES = ("css selector", "[data-type='nav_id1291']")
SUBMENU_CYSEC_CHARGES_AND_FEES = ("css selector", "[data-type='nav_id1708']")


class MenuNew(MenuBase):

    @allure.step('Select "Pricing" menu, "Charges and fees" submenu')
    def from_pricing_menu_open_charges_and_fees(self, d, cur_language, cur_country, link):

        menu_name = "Pricing"
        menu_locator = ""
        submenu_name = "Charges and fees"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = PricingMenuNew.MENU_FCA_PRICING
            submenu_locator = SUBMENU_FCA_CHARGES_AND_FEES
        if cur_country == 'ae':
            menu_locator = PricingMenuNew.MENU_SCA_PRICING
            submenu_locator = SUBMENU_SCA_CHARGES_AND_FEES
        if cur_country == 'au':
            menu_locator = PricingMenuNew.MENU_ASIC_PRICING
            submenu_locator = SUBMENU_ASIC_CHARGES_AND_FEES
        if cur_country in CYSEC_COUNTRIES:
            menu_locator = PricingMenuNew.MENU_CYSEC_PRICING
            submenu_locator = SUBMENU_CYSEC_CHARGES_AND_FEES

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
