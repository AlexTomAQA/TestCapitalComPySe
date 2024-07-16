"""
-*- coding: utf-8 -*-
@Time    : 2024/06/27 17:30 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

PROF_ACC_SUBMENU_LOC = ("css selector", "a[data-type='nav_id89']")
APPLY_BTN_LOC = ("css selector", ".button-main.btn-pro")


class ProfessionalAccountPage(BasePage):
    def click_the_professional_account_menu_item(self):
        print(f'\n{datetime.now()}   Click the Professional Account menu item =>')
        btn = Wait(self.driver, 2).until(EC.element_to_be_clickable(PROF_ACC_SUBMENU_LOC))
        btn.click()
        print(f'{datetime.now()}   => Done, the corresponding page is opened')
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')

    def click_the_apply_button(self):
        print(f'\n{datetime.now()}   Click the [Apply] button')
        btn = Wait(self.driver, 2).until(EC.element_to_be_clickable(APPLY_BTN_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            btn
        )
        btn.click()
        print(f'\n{datetime.now()}   The [Apply] button is clicked')
