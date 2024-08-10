"""
-*- coding: utf-8 -*-
@Time    : 2024/07/30 17:30 GMT+5
@Author  : Sergey Aiidzhanov
"""
import pytest

from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

LOGIN_BTN_LOC = ("css selector", "[class='accountBtns_btnsPlace___6pn2'] [data-type='btn_header_login']")
SIGNUP_BTN_LOC = ("css selector", "[class='accountBtns_btnsPlace___6pn2'] [data-type='btn_header']")
FB_BTN_LOC = ("css selector", "button.facebook_button__wMrB6")
COOKIE_BTN = ("xpath", "//div[contains(@aria-label, 'cookie') and @tabindex=0]")
FB_LOGO = ("css selector", "#homelink")
CAPITAL_MSG_EL = ("css selector", "#content span")


class CheckLoginFacebookModal(BasePage):
    def click_login_button(self):
        print(f'\n{datetime.now()}   Click the [Log In] button in the header =>')
        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(LOGIN_BTN_LOC))
        el.click()
        print(f'{datetime.now()}   => Done, the Login form is opened')

    def click_signup_button(self):
        print(f'\n{datetime.now()}   Click the [Sign Up] button in the header =>')
        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(SIGNUP_BTN_LOC))
        el.click()
        print(f'{datetime.now()}   => Done, the Sign up form is opened')

    def click_fb_btn(self):
        print(f'\n{datetime.now()}   Click the Facebook button =>')
        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(FB_BTN_LOC))
        el.click()
        if el.is_enabled():
            print(f'{datetime.now()}   => The button is not clicked')
            pytest.fail("The FB button is NOT clicked")
        print(f'{datetime.now()}   => Done, the button is clicked')

    def should_be_fb_modal(self):
        print(f'\n{datetime.now()}   Check if the "Log in to your Facebook account" modal window is opened =>')
        tabs = self.driver.window_handles
        print(f'\n{datetime.now()}   TABS NUMBER: {len(tabs)}')
        if len(tabs) > 1:
            self.driver.switch_to.window(tabs[len(tabs) - 1])
            self.deal_with_cookies()
            if "Facebook" in self.driver.find_element(*FB_LOGO).text:
                if "Capital.com" in self.driver.find_element(*CAPITAL_MSG_EL).text:
                    print(f'{datetime.now()}   => The modal window is opened')
                    self.driver.close()
                    return True
        print(f'{datetime.now()}   => The modal window is not opened')
        return False

    def deal_with_cookies(self):
        print(f'\n{datetime.now()}   Check if the Cookies message is present =>')
        try:
            Wait(self.driver, 5).until(EC.element_to_be_clickable(COOKIE_BTN))
        except TimeoutException:
            print(f'{datetime.now()}   => The message is not present (TimeoutException)')
            return False
        except NoSuchElementException:
            print(f'{datetime.now()}   => The message is not present (NoSuchElementException)')
            return False
        print(f'{datetime.now()}   => The message is present, close the message')
        Wait(self.driver, 5).until(EC.element_to_be_clickable(COOKIE_BTN)).click()
        return True
