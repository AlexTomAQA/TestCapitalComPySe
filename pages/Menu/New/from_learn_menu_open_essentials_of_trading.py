"""
-*- coding: utf-8 -*-
@Time    : 2024/08/06
@Author  : podchasova11
"""
import allure
from selenium.webdriver.common.by import By

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import LearnMenuNew
from pages.conditions_v2 import CYSEC_COUNTRIES

SUBMENU_FCA_ESSENTIAL_TRADING = (
    By.CSS_SELECTOR, "div:nth-child(4) > div.menuGroup_dropdown__75ey5 a[data-type='nav_id754']")
SUBMENU_SCA_ESSENTIAL_TRADING = (
    By.CSS_SELECTOR, "div:nth-child(3) > div.menuGroup_dropdown__75ey5 a[data-type='nav_id868']")
SUBMENU_SCA_AR_ESSENTIAL_TRADING = (
    By.CSS_SELECTOR, "div:nth-child(3) > div.menuGroup_dropdown__75ey5 a[data-type='nav_id868']")
SUBMENU_CYSEC_ESSENTIAL_TRADING = ('css selector', 'a[data-type="nav_id1631"]')


class MenuNewLearn(MenuBase):

    @allure.step('Select "Learn" menu, "Essentials of trading" submenu')
    def from_learn_menu_open_essentials_of_trading(self, d, cur_language, cur_country, link):

        menu_name = "Learn"
        menu_locator = ""
        submenu_name = "Essentials of trading"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = LearnMenuNew.MENU_FCA_LEARN
            submenu_locator = SUBMENU_FCA_ESSENTIAL_TRADING
        elif cur_country == 'ae':
            menu_locator = LearnMenuNew.MENU_SCA_LEARN
            submenu_locator = SUBMENU_SCA_ESSENTIAL_TRADING
        elif cur_country == 'ae' and cur_language == 'ar':
            menu_locator = LearnMenuNew.MENU_SCA_LEARN
            submenu_locator = SUBMENU_SCA_AR_ESSENTIAL_TRADING
        if cur_country in CYSEC_COUNTRIES:
            menu_locator = LearnMenuNew.MENU_CYSEC_LEARN
            submenu_locator = SUBMENU_CYSEC_ESSENTIAL_TRADING

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
