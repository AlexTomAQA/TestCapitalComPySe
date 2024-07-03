"""
-*- coding: utf-8 -*-
@Time    : 2024/07/03 22:00 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


def should_be_form_resubmission_window(d):
    print(f'\n{datetime.now()}   Checking if the modal window "Confirm Form Resubmission" is opened')
    if "neterror" in d.find_element("css selector", "body").get_attribute("class"):
        return False
    return True
