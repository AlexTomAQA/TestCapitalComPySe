"""
-*- coding: utf-8 -*-
@Time    : 2023/04/20 22:00
@Author  : Suleyman Alirzaev
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import MainBannerLocators
from selenium.common.exceptions import ElementClickInterceptedException


class MainBannerTryDemo(BasePage):

    @allure.step(f'{datetime.now()}   Start Full test for Try demo button of Main banner')
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link, True)

        self.element_click()

        test_element = AssertClass(d, cur_item_link, self.bid)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link, True)

    def full_test(self, d, cur_language, cur_country, cur_role, page_url):
        self.arrange_(d, page_url)

        self.element_click()

        test_element = AssertClass(d, page_url)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, page_url)
            case "NoAuth":
                test_element.assert_login(d, cur_language, page_url)
            case "Auth":
                test_element.assert_trading_platform_v3(d, page_url, True)

    def arrange_(self, d, cur_item_link, always=False):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        button_list = self.driver.find_elements(*MainBannerLocators.BUTTON_TRY_DEMO)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_TRY_DEMO is not present on this page")
            del button_list
            msg = "Testing element 'BUTTON_TRY_DEMO on the main banner' is not present on this page"
            if always:
                pytest.fail(f"Bug № ??? {msg}")
            else:
                pytest.skip(msg)
        else:
            print(f"{datetime.now()}   => BUTTON_TRY_DEMO is present on this page")

        print(f"{datetime.now()}   BUTTON_TRY_DEMO scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', button_list[0]
        )

        print(f"{datetime.now()}   BUTTON_TRY_DEMO is visible? =>")
        if self.element_is_visible(MainBannerLocators.BUTTON_TRY_DEMO):
            print(f"{datetime.now()}   => BUTTON_TRY_DEMO is visible on this page")
        else:
            print(f"{datetime.now()}   => BUTTON_TRY_DEMO is not visible on this page")
            pytest.fail("Bug! Testing element 'BUTTON_TRY_DEMO on main banner' is present on this page, "
                        "but not visible")

    @allure.step("Click button [Try demo] on Main banner")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")

        button_list = self.driver.find_elements(*MainBannerLocators.BUTTON_TRY_DEMO)
        print(f"{datetime.now()}   BUTTON_TRY_DEMO is clickable? =>")
        time_out = 3
        if not self.element_is_clickable(button_list[0], time_out):
            print(f"{datetime.now()}   => BUTTON_TRY_DEMO is not clickable after {time_out} sec. Stop TC>")
            pytest.fail(f"BUTTON_TRY_DEMO is not clickable after {time_out} sec.")

        try:
            # button_list[0].click()
            self.driver.execute_script("arguments[0].click();", button_list[0])
            print(f"{datetime.now()}   => BUTTON_TRY_DEMO clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_TRY_DEMO NOT CLICKED")
            print(f"{datetime.now()}   'Sign up' form or page is auto opened")

            page_ = SignupLogin(self.driver)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()

            # button_list[0].click()
            self.driver.execute_script("arguments[0].click();", button_list[0])
            del page_

        del button_list
        return True
