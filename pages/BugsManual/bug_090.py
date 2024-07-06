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


def should_be_form_resubmission_window(d):
    print(f'\n{datetime.now()}   Checking if the modal window "Confirm Form Resubmission" is opened')
    try:
        Wait(d, 5).until(EC.alert_is_present())   # returns d.switch_to.alert or False
    except TimeoutException:
        print(f'\n{datetime.now()}   The modal window is not opened')
        return False
    print(f'\n{datetime.now()}   The modal window is opened')
    return True


def accept_form_resubmission_window(d):
    alert = Wait(d, 5).until(EC.alert_is_present())
    alert.accept()
