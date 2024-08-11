"""
-*- coding: utf-8 -*-
@Time    : 2024/08/06 12:00 GMT+3
@Author  : podchasova11
"""
import allure
from selenium.webdriver.common.by import By

from pages.Menu.New.menu_new_base import MenuBase
from pages.Menu.New.menu_new_locators import LearnMenuNew

SUBMENU_FCA_LEARN = (By.CSS_SELECTOR, "div:nth-child(4) > div.menuGroup_dropdown__75ey5 a > div > h2")
SUBMENU_SCA_LEARN = (By.CSS_SELECTOR, "div:nth-child(3) > div.menuGroup_dropdown__75ey5 a > div > h2")
SUBMENU_SCA_AR_LEARN = (By.CSS_SELECTOR, 'div:nth-child(3) > div.menuGroup_dropdown__75ey5 a > div > h2')


class MenuNewLearn(MenuBase):

    @allure.step('Select "Learn" menu, "Learn" submenu')
    def from_learn_menu_open_learn(self, d, cur_language, cur_country, link):

        menu_name = "Learn"
        menu_locator = ""
        submenu_name = "Learn"
        submenu_locator = ""

        if cur_country == 'gb':
            menu_locator = LearnMenuNew.MENU_FCA_LEARN
            submenu_locator = SUBMENU_FCA_LEARN
        elif cur_country == 'ae':
            menu_locator = LearnMenuNew.MENU_SCA_LEARN
            submenu_locator = SUBMENU_SCA_LEARN
        elif cur_country == 'ae' and cur_language == 'ar':
            menu_locator = LearnMenuNew.MENU_SCA_LEARN
            submenu_locator = SUBMENU_SCA_AR_LEARN

        answer = MenuBase(d, link).move_focus_menu_pause_move_focus_to_submenu_and_click(
            d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator)

        return answer
