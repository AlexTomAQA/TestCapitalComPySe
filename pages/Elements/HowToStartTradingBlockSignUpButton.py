"""
-*- coding: utf-8 -*-
@Time    : 2023/05/01 11:30
@Author  : podchasova11
"""

from datetime import datetime
import pytest

import allure
from selenium.common import ElementClickInterceptedException
from pages.base_page import BasePage
from pages.Signup_login.signup_login import SignupLogin
from pages.Elements.testing_elements_locators import (HowToStartTradingSignupLocators)


class HowToStartTradingBlockSignUpButton(BasePage):

    @allure.step(f"{datetime.now()}  Start Full test [Sign up] button on 'How to start trading' Block")
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)
        self.element_click(self.driver)

        # Проверка наличия всех элементов формы Signup в блоке 'How to start trading'
        check_signup_form = SignupLogin(d, cur_item_link)
        check_signup_form.should_be_open_signup_form()
        del check_signup_form

        # проверка assert_signup не используется, тк форма не закрывается и встроена в 'How to start trading' Block
        # test_element = AssertClass(d, cur_item_link, self.bid)
        # match cur_role:
        #     case "NoReg":
        #         test_element.assert_signup(d, cur_language, cur_item_link)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        field_input_email = self.driver.find_element(*HowToStartTradingSignupLocators.SIGNUP_INPUT_EMAIL)
        field_input_email.send_keys("example@example.com")

        field_input_password = self.driver.find_element(*HowToStartTradingSignupLocators.SIGNUP_INPUT_PASSWORD)
        field_input_password.send_keys("example12345")

    @allure.step("Click button [Sign up] button on 'How to start trading' Block")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")

        button_sign_up = self.driver.find_element(*HowToStartTradingSignupLocators.BUTTON_SIGN_UP)
        print(f"{datetime.now()}   BUTTON_SIGN_UP is clickable? =>")
        time_out = 3
        if not self.element_is_clickable(button_sign_up, time_out):
            print(f"{datetime.now()}   => BUTTON_SIGN_UP is not clickable after {time_out} sec. Stop TC>")
            pytest.fail(f"BUTTON_SIGN_UP is not clickable after {time_out} sec.")

        try:
            button_sign_up.click()
            print(f"{datetime.now()}   => BUTTON_SIGN_UP clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_SIGN_UP NOT CLICKED")





