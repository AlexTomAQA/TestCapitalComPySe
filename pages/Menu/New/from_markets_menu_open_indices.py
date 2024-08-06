"""
-*- coding: utf-8 -*-
@Time    : 2024/08/06
@Author  : podchasova11
"""
import allure
from selenium.webdriver.common.by import By

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import MarketsMenuNew

SUBMENU_FCA_INDICES = (By.CSS_SELECTOR, ".menuGroup_link__z_L3O[data-type='nav_id693']")
SUBMENU_SCA_INDICES = (By.CSS_SELECTOR, ".menuGroup_link__z_L3O[data-type='nav_id826']")
SUBMENU_SCA_AR_INDICES = (By.CSS_SELECTOR, ".menuGroup_link__z_L3O[data-type='nav_id826']")


class MenuNewIndices(MenuBase):

    @allure.step('Select "Markets" menu, "Indices" submenu')
    def from_markets_menu_open_indices(self, d, cur_language, cur_country, link):

        menu_name = "Markets"
        menu_locator = ""
        submenu_name = "Indices"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = MarketsMenuNew.MENU_FCA_MARKETS
            submenu_locator = SUBMENU_FCA_INDICES
        elif cur_country == 'ae':
            menu_locator = MarketsMenuNew.MENU_SCA_MARKETS
            submenu_locator = SUBMENU_SCA_INDICES
        elif cur_country == 'ae' and cur_language == 'ar':
            menu_locator = MarketsMenuNew.MENU_SCA_MARKETS
            submenu_locator = SUBMENU_SCA_AR_INDICES

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
