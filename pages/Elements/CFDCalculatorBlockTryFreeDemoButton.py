"""
-*- coding: utf-8 -*-
@Time    : 2023/04/23 20:55
@Author  : Mila Podchasova
"""
from datetime import datetime
import pytest
import allure

from pages.Elements.AssertClass import AssertClass
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Markets.markets_locators import BlockCFDCalculator
from selenium.common.exceptions import ElementClickInterceptedException


class CFDCalculatorBlockTryFreeDemoButton(BasePage):

    @allure.step(f"{datetime.now()}  Start Full test for 'Try free demo' button on 'Block CFD Calculator'")
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)
        self.element_click()

        test_element = AssertClass(d, cur_item_link, self.bid)

        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        button_list = self.driver.find_elements(*BlockCFDCalculator.BUTTON_TRY_FREE_DEMO)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_TRY_FREE_DEMO is not present on this page")
            del button_list
            pytest.fail("Testing element BUTTON_TRY_FREE_DEMO on 'Block CFD Calculator' is not present on this page")
        else:
            print(f"{datetime.now()}   => BUTTON_TRY_FREE_DEMO is present on this page")

        print(f"{datetime.now()}   BUTTON_TRY_FREE_DEMO scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', button_list[0]
        )

        print(f"{datetime.now()}   BUTTON_TRY_FREE_DEMO is visible? =>")
        if self.element_is_visible(BlockCFDCalculator.BUTTON_TRY_FREE_DEMO):
            print(f"{datetime.now()}   => BUTTON_TRY_FREE_DEMO is visible on this page")
        else:
            print(f"{datetime.now()}   => BUTTON_TRY_FREE_DEMO is not visible on this page")
            pytest.fail("Bug! Testing element BUTTON_TRY_FREE_DEMO on 'Block CFD Calculator' is present on this page, "
                        "but not visible")

    @allure.step("Click button [Try free demo] on 'Block CFD Calculator'")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")

        button_list = self.driver.find_elements(*BlockCFDCalculator.BUTTON_TRY_FREE_DEMO)
        print(f"{datetime.now()}   BUTTON_TRY_FREE_DEMO is clickable? =>")
        time_out = 3
        if not self.element_is_clickable(button_list[0], time_out):
            print(f"{datetime.now()}   => BUTTON_TRY_FREE_DEMO is not clickable after {time_out} sec. Stop TC>")
            pytest.fail(f"BUTTON_TRY_FREE_DEMO is not clickable after {time_out} sec.")

        try:
            self.driver.execute_script("arguments[0].click();", button_list[0])
            print(f"{datetime.now()}   => BUTTON_TRY_FREE_DEMO clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_TRY_FREE_DEMO NOT CLICKED")
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

            self.driver.execute_script("arguments[0].click();", button_list[0])
            del page_


