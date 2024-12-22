"""
-*- coding: utf-8 -*-
@Time    : 2024/12/09 17:20 GMT+5
@Author  : Sergey Aiidzhanov
"""
import time
import random
from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.conditions_v2 import CYSEC_COUNTRIES

COUNTRY_LANG_SWITCHER_LOC = ('css selector', '[data-testid="language_switcher"]')
COUNTRY_DROPDOWN_LOC = ('css selector', '[data-type="country_switcher_ctry"]')
COUNTRY_SEARCH_FIELD_LOC = ('css selector', '#search-country')
COUNTRY_FIRST_SEARCH_ITEM_LOC = ('xpath', '(//button[@class="select_item__GdG7X js-analyticsClick"])[1]')
LANG_DROPDOWN_LOC = ('css selector', '[data-type="country_switcher_lng"]')
LANG_DROPDOWN_TEXT_LOC = ('css selector', '[data-type="country_switcher_lng"]>.select_text__cd1pK]')
ENG_LANG_LOC = ('css selector', '[data-type="nav_country_english"]')
APPLY_BTN_LOC = ('xpath', '//button[text()="Apply"]')
BODY_WITH_DISABLED_SCROLL_LOC = ('css selector', 'body[style="overflow: hidden;"]')


class Bug613(BasePage):

    def change_language(self, cur_country):
        print(f'\n{datetime.now()}   Changing the country to another CYSEC country =>')
        print(f'{datetime.now()}   => Opening language switching menu =>')

        country_switcher = Wait(self.driver, 2).until(EC.element_to_be_clickable(COUNTRY_LANG_SWITCHER_LOC))
        country_switcher.click()

        print(f'{datetime.now()}   => Opening country dropdown =>')

        country_dropdown = Wait(self.driver, 2).until(EC.element_to_be_clickable(COUNTRY_DROPDOWN_LOC))
        country_dropdown.click()

        countries_list = [*CYSEC_COUNTRIES]
        countries_list.remove(cur_country)
        new_country = random.choice(countries_list)

        print(f'{datetime.now()}   => Searching "{new_country}" and selecting the new country =>')

        country_search_field = Wait(self.driver, 2).until(EC.element_to_be_clickable(COUNTRY_SEARCH_FIELD_LOC))
        country_search_field.send_keys(new_country)
        time.sleep(1)

        search_item = Wait(self.driver, 2).until(EC.element_to_be_clickable(COUNTRY_FIRST_SEARCH_ITEM_LOC))
        search_item.click()

        # lang_dropdown = Wait(self.driver, 2).until(EC.element_to_be_clickable(LANG_DROPDOWN_LOC))
        #
        # lang_dropdown_text = Wait(self.driver, 2).until(EC.element_to_be_clickable(LANG_DROPDOWN_TEXT_LOC))
        # if not lang_dropdown_text.text == 'English':
        #     lang_dropdown.click()
        #     eng_lang = Wait(self.driver, 2).until(EC.element_to_be_clickable(LANG_DROPDOWN_TEXT_LOC))
        #     eng_lang.click()

        apply_btn = Wait(self.driver, 2).until(EC.element_to_be_clickable(APPLY_BTN_LOC))
        apply_btn.click()
        print(f'{datetime.now()}   => Done, current URL: {self.driver.current_url}')

    def should_be_enabled_scroll(self):
        print(f'\n{datetime.now()}   Check if scroll is enabled =>')
        try:
            Wait(self.driver, 2).until(EC.visibility_of_element_located(BODY_WITH_DISABLED_SCROLL_LOC))
            print(f'{datetime.now()}   => Scroll is disabled')
            return False
        except TimeoutException:
            print(f'{datetime.now()}   => Scroll is enabled')
            return True
