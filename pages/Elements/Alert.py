"""
-*- coding: utf-8 -*-
@Time    : 2024/07/03 22:00 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Alert(BasePage):
    def should_be_alert(self):
        print(f'\n{datetime.now()}   Checking if the alert is opened')
        try:
            Wait(self.driver, 5).until(EC.alert_is_present())  # returns d.switch_to.alert or False
        except TimeoutException:
            print(f'\n{datetime.now()}   The alert is not opened')
            return False
        print(f'\n{datetime.now()}   The alert is opened')
        return True

    def accept_alert(self):
        alert = Wait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()

    def dismiss_alert(self):
        alert = Wait(self.driver, 5).until(EC.alert_is_present())
        alert.dismiss()
