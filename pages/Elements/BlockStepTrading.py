"""
-*- coding: utf-8 -*-
@Time    : 2023/04/14 08:30
@Author  : Alexander Tomelo
"""
import time
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import BlockStepTradingLocators
from pages.Elements.AssertClass import AssertClass
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


class BlockStepTrading(BasePage):

    @allure.step(f"{datetime.now()}   Start full test for Step trading block")
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):

        self.arrange_(d, cur_item_link,cur_language, cur_country)
        self.element_click(cur_language, cur_country)

        test_element = AssertClass(d, cur_item_link, self.bid)
        match cur_role:
            case "NoReg" | "NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            # case "NoAuth":
            #     test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)
        self.element_click()

        test_element = AssertClass(d, cur_item_link, self.bid)
        match cur_role:
            case "NoReg" | "NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

    def arrange_(self, d, cur_item_link,cur_language="", cur_country=""):
        print(f"\n{datetime.now()}   1. Arrange_v0")
        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   BUTTON_CREATE_YOUR_ACCOUNT is located on the page? =>")
        if cur_language == "" and cur_country == "gb":
            button_list = self.elements_are_located(BlockStepTradingLocators.BUT_CREATE_YOUR_ACCOUNT_EN, 5)
        else:
            button_list = self.elements_are_located(BlockStepTradingLocators.BUT_CREATE_YOUR_ACCOUNT, 5)

        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT is not located on this page after 10 sec")
            print(f"{datetime.now()}   => Current URL = {d.current_url}")
            pytest.fail("Bug! Checking element (Button create your account) is not in DOM after 10 sec")

    @allure.step(f"{datetime.now()}   Click '1. Create your account' button in 'Three first steps' section")
    def element_click(self, cur_language="", cur_country=""):
        """Method"""
        print(f"\n{datetime.now()}   2. Act_v0: Define of locator")
        if cur_language == "" and cur_country == "gb":
            button_list_locator = BlockStepTradingLocators.BUT_CREATE_YOUR_ACCOUNT_EN
        else:
            button_list_locator = BlockStepTradingLocators.BUT_CREATE_YOUR_ACCOUNT
        print(f"\n{datetime.now()}   2. Act_v0: Go to web element")

        if not self.element_is_present_and_visible(button_list_locator, 5):
            print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT is not visible after 5 sec")
            pytest.fail(f"Bug! Checking element is present in DOM, but not visible after 5 sec")
        time.sleep(1)
        if not self.element_is_clickable(button_list_locator, 5):
            print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT is not clickable after 5 sec")
            pytest.fail(f"Bug! Checking element is present in DOM, visible, but not clickable after 5 sec")

        print(f"\n{datetime.now()}   2. Act_v0: Click web element")
        button = self.element_is_clickable(button_list_locator, 5)
        self.driver.execute_script("arguments[0].click();", button)
        print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT is clicked")

        return True
