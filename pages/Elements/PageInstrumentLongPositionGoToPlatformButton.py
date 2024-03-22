"""
-*- coding: utf-8 -*-
@Time    : 2024/03/22 11:00
@Author  : podchasova11
"""

from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import PageTradingInstrumentMarketsLocators
from selenium.webdriver import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException


class PageInstrumentLongPositionGoToPlatformButton(BasePage):

    @allure.step(f"{datetime.now()}   Start test for button [Go to platform] on trading instrument page")
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)

        page_signup_login = SignupLogin(d, cur_item_link)
        page_signup_login.check_popup_signup_form()

        self.element_click()

        test_element = AssertClass(d, cur_item_link, self.bid)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)
        self.driver.get(cur_item_link)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()} Is TOOLINFO_LONG_POSITION_OVERNIGHT_FEE present on the page? =>")
        toolinfo = self.driver.find_element(PageTradingInstrumentMarketsLocators.TOOLINFO_LONG_POSITION_OVERNIGHT_FEE)
        if len(toolinfo) == 0:
            print(f"{datetime.now()}   => TOOLINFO_LONG_POSITION_OVERNIGHT_FEE is not present on the page")
            pytest.fail("Bug ? TOOLINFO_LONG_POSITION_OVERNIGHT_FEE is not present on the page")

        ActionChains(d) \
            .move_to_element(toolinfo[0]) \
            .pause(0.5) \
            .perform()

        print(f"{datetime.now()}   Is TOOLTIP_LONG_POSITION_FEE open?  =>")
        tooltip = self.element_is_visible(PageTradingInstrumentMarketsLocators.TOOLTIP_LONG_POSITION_FEE)
        if tooltip == 0:
            print(f"{datetime.now()}   => TOOLTIP_LONG_POSITION_FEE is not open")
            pytest.fail("TOOLTIP_LONG_POSITION_FEE is not open")

        ActionChains(d) \
            .move_to_element(tooltip) \
            .pause(0.5) \
            .perform()

        button_list = self.driver.find_elements(PageTradingInstrumentMarketsLocators.BUTTON_GO_TO_PLATFORM_LG)
        print(f"{datetime.now()}   Is button BUTTON_GO_TO_PLATFORM_LG present on the page? =>")
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_GO_TO_PLATFORM_LG is not present on the page")
            return False
        print(f"{datetime.now()}   => BUTTON_GO_TO_PLATFORM_LG is present on the page")

        print(f"{datetime.now()}   BUTTON_GO_TO_PLATFORM_LG scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )
        print(f"{datetime.now()}   => BUTTON_GO_TO_PLATFORM_LG scrolled")

    @allure.step("Click button [Go to platform] on the page content")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")
        print(f"{datetime.now()}   Start Click button [Go to platform] =>")

        button_list = self.driver.find_elements(PageTradingInstrumentMarketsLocators.BUTTON_GO_TO_PLATFORM_LG)

        time_out = 3
        if not self.element_is_clickable(button_list[0], time_out):
            print(f"{datetime.now()} => BUTTON_GO_TO_PLATFORM_LG is not clickable after {time_out} sec. Stop TC>")
            pytest.fail(f"BUTTON_GO_TO_PLATFORM_LG is not clickable after {time_out} sec.")

        print(f"{datetime.now()}   BUTTON_GO_TO_PLATFORM_LG is clickable =>")

        try:
            button_list[0].click()
            print(f"{datetime.now()} => BUTTON_GO_TO_PLATFORM_LG clicked")
        except ElementClickInterceptedException:
            print(f"{datetime.now()} => BUTTON_GO_TO_PLATFORM_LG not clicked")
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

            button_list[0].click()
            del page_

        del button_list
        return True
