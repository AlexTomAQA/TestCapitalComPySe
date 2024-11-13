import time

from pages.Menu.New.from_learn_menu_open_risk_managment_guide import MenuNew
from pages.base_page import BasePage


class Bug467(BasePage):

    @staticmethod
    def open_risk_management_page(d, cur_language, cur_country, link):
        MenuNew.from_learn_menu_open_risk_management_guide(d, cur_language, cur_country, link)