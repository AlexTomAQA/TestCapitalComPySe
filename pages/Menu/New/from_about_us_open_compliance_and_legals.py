"""
-*- coding: utf-8 -*-
@Time    : 2025/30/01 20:00
@Author  : Kasila
"""
import allure
from selenium.webdriver.common.by import By
from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import AboutUsMenuNew
from pages.conditions_v2 import CYSEC_COUNTRIES


SUBMENU_CYSEC_COMPLIANCE_AND_LEGALS = (By.CSS_SELECTOR, "a[data-type='nav_id1808']")


class MenuNew(MenuBase):

    @allure.step('Select "About us" menu, "Compliance and legals" submenu')
    def from_about_us_open_compliance_and_legals(self, d, cur_language, cur_country, link):

        menu_name = "About us"
        menu_locator = ""
        submenu_name = "Compliance and legals"
        submenu_locator = ""

        if cur_country in CYSEC_COUNTRIES:
            menu_locator = AboutUsMenuNew.MENU_FCA_ABOUT_US
            submenu_locator = SUBMENU_CYSEC_COMPLIANCE_AND_LEGALS

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer