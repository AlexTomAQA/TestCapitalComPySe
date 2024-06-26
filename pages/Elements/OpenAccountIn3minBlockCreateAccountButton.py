"""
-*- coding: utf-8 -*-
@Time    : 2023/08/08 18:00
@Author  : Aleksandr Tomelo
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException
from pages.Elements.testing_elements_locators import CounterBanner


class ButtonCreateAccountInBlockOpenAccountIn3min(BasePage):

    def arrange_(self, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   CREATE_ACCOUNT_BUTTON is visible? =>")
        if self.element_is_visible(CounterBanner.CREATE_ACCOUNT_BUTTON):
            print(f"{datetime.now()}   => CREATE_ACCOUNT_BUTTON is visible on the page!")
            return True
        else:
            print(f"{datetime.now()}   => CREATE_ACCOUNT_BUTTON is not visible on the page!")
            pytest.skip("Checking element is not present on this page")

    @allure.step("Click button [Create account]")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   CREATE_ACCOUNT_BUTTON is present? =>")
        button_list = self.driver.find_elements(*CounterBanner.CREATE_ACCOUNT_BUTTON)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => CREATE_ACCOUNT_BUTTON is not present on the page!")
            del button_list
            return False
        print(f"{datetime.now()}   => CREATE_ACCOUNT_BUTTON is present on the page!")

        print(f"{datetime.now()}   CREATE_ACCOUNT_BUTTON scroll =>")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        self.element_is_clickable(button_list[0], 5)

        try:
            button_list[0].click()
            print(f"{datetime.now()}   => CREATE_ACCOUNT_BUTTON clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => CREATE_ACCOUNT_BUTTON NOT CLICKED")
            print(f"{datetime.now()}   'Sign up' form or page is auto opened")

            page_ = SignupLogin(self.driver)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()

            button_list[0].click()
            del page_

        del button_list
        return True
