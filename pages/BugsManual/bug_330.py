"""
-*- coding: utf-8 -*-
@Time    : 2024/08/19 20:30 GMT+5
@Author  : Sergey Aiidzhanov
"""
import time

from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException

SUPPORT_BTN_LOC = ('css selector', 'button.liveChat_blinger__WJsqh')
CHAT_FRAME_LOC = ('css selector', 'iframe[tabindex="0"]')
CLOSE_CHAT_BTN_LOC = ('xpath', '(//button[@data-garden-id="buttons.icon_button"])[2]')
CHAT_HEADER_LOC = ('css selector', 'h2.sc-vrqbdz-5')
LANG_MAIN_BTN_LOC = ('xpath', '(//span[@role="button"])[2]')
LANG_DROP_BTN_LOC = ('xpath', '(//div[contains(@class, "select_selected__8wH_E")])[2]')
LANG_EN_BTN_LOC = ('css selector', 'button[data-type="nav_country_english"]')
LANG_AR_BTN_LOC = ('css selector', 'button[data-type="nav_country_arabic"]')
LANG_APPLY_BTN_LOC = ('css selector', '.button_btn__vOh9h.button_main__4QZm1.button_primary__raeTg.button_md__Xhil0')


class Bug330(BasePage):

    def open_support_window(self):
        time.sleep(2)
        print(f'\n{datetime.now()}   Click the Support chat button =>')
        Wait(self.driver, 2).until(EC.element_to_be_clickable(SUPPORT_BTN_LOC)).click()
        print(f'{datetime.now()}   => Done, the button is clicked')

    def close_support_window(self):
        print(f'\n{datetime.now()}   Close the Support Chat form =>')
        chat_frame = self.driver.find_element(*CHAT_FRAME_LOC)
        self.driver.switch_to.frame(chat_frame)
        btn = Wait(self.driver, 5).until(EC.element_to_be_clickable(CLOSE_CHAT_BTN_LOC))
        btn.click()
        print(f'{datetime.now()}   => Done, the form is closed')
        self.driver.switch_to.default_content()

    def change_language(self, cur_language):
        print(f'\n{datetime.now()}   Change page language =>')

        lang_main_btn = Wait(self.driver, 2).until(EC.element_to_be_clickable(LANG_MAIN_BTN_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            lang_main_btn
        )
        lang_main_btn.click()

        Wait(self.driver, 2).until(EC.element_to_be_clickable(LANG_DROP_BTN_LOC)).click()

        if cur_language == '':
            Wait(self.driver, 2).until(EC.element_to_be_clickable(LANG_AR_BTN_LOC)).click()
        else:
            Wait(self.driver, 2).until(EC.element_to_be_clickable(LANG_EN_BTN_LOC)).click()
        print(f'{datetime.now()}   => Done, language is changed')

        Wait(self.driver, 2).until(EC.element_to_be_clickable(LANG_APPLY_BTN_LOC)).click()

    def should_be_support_window(self):
        print(f'\n{datetime.now()}   Check if the Support Chat window is opened =>')

        try:
            self.driver.switch_to.frame(Wait(self.driver, 2).until(EC.visibility_of_element_located(CHAT_FRAME_LOC)))
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException):
            print(f'{datetime.now()}   => The window is not opened')
            return False

        if "Capital.com" not in self.driver.find_element(*CHAT_HEADER_LOC).text:
            print(f'{datetime.now()}   => The window is not opened')
            self.driver.switch_to.default_content()
            return False

        print(f'{datetime.now()}   => The window is opened')
        self.driver.switch_to.default_content()
        return True
