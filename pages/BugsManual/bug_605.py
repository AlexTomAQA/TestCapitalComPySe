"""
-*- coding: utf-8 -*-
@Time    : 2024/12/22 16:40 GMT+5
@Author  : Sergey Aiidzhanov
"""
import time
from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

COUNTRY_LANG_SWITCHER_LOC = ('css selector', '[data-testid="language_switcher"]')
COUNTRY_DROPDOWN_LOC = ('css selector', '[data-type="country_switcher_ctry"]')
COUNTRY_SEARCH_FIELD_LOC = ('css selector', '#search-country')
COUNTRY_FIRST_SEARCH_ITEM_LOC = ('xpath', '(//button[@class="select_item__GdG7X js-analyticsClick"])[1]')
LANG_DROPDOWN_LOC = ('css selector', '[data-type="country_switcher_lng"]')
LANG_DROPDOWN_TEXT_LOC = ('css selector', '[data-type="country_switcher_lng"]>.select_text__cd1pK]')
APPLY_BTN_LOC = ('xpath', '//button[text()="Υποβάλετε αίτηση"]')
CYPRUS_FLAG_LOC = ('css selector', '.flag_cy__sVpSt.flag_medium__QcXdf')


class Bug605(BasePage):

    def select_cyprus_country(self):
        print(f'\n{datetime.now()}   Changing current country to Cyprus =>')
        print(f'{datetime.now()}   => Opening language switching menu =>')

        country_switcher = Wait(self.driver, 2).until(EC.element_to_be_clickable(COUNTRY_LANG_SWITCHER_LOC))
        country_switcher.click()

        print(f'{datetime.now()}   => Opening country dropdown =>')

        country_dropdown = Wait(self.driver, 2).until(EC.element_to_be_clickable(COUNTRY_DROPDOWN_LOC))
        country_dropdown.click()

        print(f'{datetime.now()}   => Searching and selecting CYPRUS =>')

        country_search_field = Wait(self.driver, 2).until(EC.element_to_be_clickable(COUNTRY_SEARCH_FIELD_LOC))
        country_search_field.send_keys("cyprus")
        time.sleep(1)

        search_item = Wait(self.driver, 2).until(EC.element_to_be_clickable(COUNTRY_FIRST_SEARCH_ITEM_LOC))
        search_item.click()

        apply_btn = Wait(self.driver, 2).until(EC.element_to_be_clickable(APPLY_BTN_LOC))
        apply_btn.click()
        print(f'{datetime.now()}   => Done, current URL: {self.driver.current_url}')

    def should_be_cyprus_country(self):
        print(f'\n{datetime.now()}   Make sure that Cyprus flag is displayed =>')
        try:
            Wait(self.driver, 2).until(EC.visibility_of_element_located(CYPRUS_FLAG_LOC))
            print(f'{datetime.now()}   => The flag is displayed')
            return True
        except TimeoutException:
            print(f'{datetime.now()}   => The flag is not displayed')
            return False
