"""
-*- coding: utf-8 -*-
@Time    : 2024/08/02 10:00 GMT+5
@Author  : podchasova11
"""
import allure
from selenium.webdriver.common.by import By

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import MarketsMenuNew

MARKETS_SUBMENU_FCA_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > div.menuGroup_dropdown__75ey5 a > div > h2")
MARKETS_SUBMENU_SCA_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > div.menuGroup_dropdown__75ey5 a > div > h2")
MARKETS_SUBMENU_SCA_AR_LOCATOR = (By.CSS_SELECTOR, 'div:nth-child(2) > div.menuGroup_dropdown__75ey5 a > div > h2')
MARKETS_SUBMENU_FCA_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > div.menuGroup_dropdown__75ey5 a > div")
MARKETS_SUBMENU_SCA_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > div.menuGroup_dropdown__75ey5 a > div")

class MenuNewMarkets(MenuBase):

    @allure.step('Select "Trading" menu, "Trading" submenu')
    def from_markets_menu_open_markets(self, d, cur_language, cur_country, link):

        menu_name = "Markets"
        menu_locator = ""
        submenu_name = "Markets"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = MarketsMenuNew.MENU_FCA_MARKETS
            submenu_locator = MARKETS_SUBMENU_FCA_LOCATOR
        elif cur_country == 'ae':
            menu_locator = MarketsMenuNew.MENU_SCA_MARKETS
            submenu_locator = MARKETS_SUBMENU_SCA_LOCATOR
        elif cur_country == 'ae' and cur_language == 'ar':
            menu_locator = MarketsMenuNew.MENU_SCA_MARKETS
            submenu_locator = MARKETS_SUBMENU_SCA_AR_LOCATOR

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
