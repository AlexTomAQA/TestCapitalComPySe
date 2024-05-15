"""
-*- coding: utf-8 -*-
@Time    : 2024/03/29 14:00
@Author  : Dmitry Mudrik
"""

from datetime import datetime

import allure
import pytest
from selenium.common.exceptions import ElementClickInterceptedException

from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import PageTradingInstrumentMarketsLocators
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.common import Common


class PageInstrumentNotificationButton(BasePage):

    @allure.step("Start testing for PageInstrumentNotificationButton of the trading instrument page")
    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)

        page_signup_login = SignupLogin(d, cur_item_link)
        page_signup_login.check_popup_signup_form()

        trade_instrument_tag = self.element_click(cur_role)

        print(f'Trade instrument from Full test is {trade_instrument_tag}')
        test_element = AssertClass(d, cur_item_link, self.bid)
        print(f'Test element is {test_element}')
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link, False, True, trade_instrument_tag)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()} 1.Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()} BUTTON_NOTIFICATION is located on the page? =>")
        buttons = self.driver.find_elements(*PageTradingInstrumentMarketsLocators.BUTTON_NOTIFICATION)
        print(f"{datetime.now()}   Is BUTTON_NOTIFICATION present on the page? =>")

        if len(buttons) == 0:
            print(f"{datetime.now()} => BUTTON_NOTIFICATION is not present on the page")
            return False
        print(f"{datetime.now()} => BUTTON_NOTIFICATION is present on the page")

        print(f"{datetime.now()}   [Notification] button scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', buttons[0])

    @allure.step("Click button [Notification]")
    def element_click(self, cur_role):
        print(f"\n{datetime.now()}   2. Act_v0")
        print(f"{datetime.now()}   Start Click 'Notification' button =>")

        # Вытаскиваем уникальный атрибут открытого ТИ
        trade_instrument_tag = self.driver.find_element(
            *PageTradingInstrumentMarketsLocators.TAG_TRADE_INSTRUMENT).text

        buttons = self.driver.find_elements(*PageTradingInstrumentMarketsLocators.BUTTON_NOTIFICATION)

        if not self.element_is_clickable(buttons[0], 5):
            print(f"{datetime.now()} => BUTTON_NOTIFICATION is not clickable after more then 5 sec")
            pytest.fail(f"BUTTON_NOTIFICATION is not clickable more then 5 sec.")

        print(f"{datetime.now()} BUTTON_NOTIFICATION is clickable =>")

        try:
            buttons[0].click()
            print(f"{datetime.now()} => BUTTON_NOTIFICATION clicked")
        except ElementClickInterceptedException:
            print(f"{datetime.now()} => BUTTON_NOTIFICATION not clicked")

            print(f"{datetime.now()}   'Signup' or 'Login' form is automatically opened")

            page_ = SignupLogin(self.driver)
            if page_.close_signup_form():
                pass
            elif page_.close_login_form():
                pass
            elif page_.close_signup_page():
                pass
            else:
                page_.close_login_page()

            buttons[0].click()
            del page_

        return trade_instrument_tag

