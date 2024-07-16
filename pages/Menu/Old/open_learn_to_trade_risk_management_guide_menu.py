from datetime import datetime

import allure

from pages.base_page import BasePage
from pages.common import Common

class MenuSection(BasePage):
    """
    MenuSection class - класс работы с меню в хедере
    Аргументы при создании объекта:
        wd - driver
        main_page_link - страница, на которой расположено меню
        flag_set_menu - признак того, что нужное меню выбрано (установлено), необязательный аргумент. По умолчанию =
        False
    """

    def __init__(self, wd, main_page_link, flag_set_menu=False):
        self.flag_set_menu = flag_set_menu
        super().__init__(wd, main_page_link)

    @allure.step('Select "Learn to trade" menu, "Risk-management guide')
    def open_learn_to_trade_risk_management_guide_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Education" menu, "Risk-management guide" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_learn_to_trade_move_focus(d, cur_language, cur_country)
        self.sub_menu_risk_management_guide_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        Common.flag_of_bug = False

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url
