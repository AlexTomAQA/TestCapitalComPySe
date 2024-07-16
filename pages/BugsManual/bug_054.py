"""
-*- coding: utf-8 -*-
@Time    : 2024/07/16 19:30 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

CORP_ACC_MENU_ITEM_LOC = ("css selector", "a[data-type='nav_id485']")
TRY_NOW_BTN_LOC = ("css selector", "a[data-type='banner_with_counter___']")


class CorporateAccountsPage(BasePage):
    def click_corp_acc_menu_item(self):
        print(f'\n{datetime.now()}   Click the Corporate Accounts menu item =>')
        el = Wait(self.driver, 5).until(EC.element_to_be_clickable(CORP_ACC_MENU_ITEM_LOC))
        el.click()
        print(f'{datetime.now()}   => Done, the corresponding page is opened')
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')

    def click_try_now_btn(self):
        print(f'\n{datetime.now()}   Click the [Try now] button =>')
        btn = Wait(self.driver, 2).until(EC.element_to_be_clickable(TRY_NOW_BTN_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            btn
        )
        btn.click()
        print(f'{datetime.now()}   The button is clicked')
