"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import time

import allure
# from memory_profiler import profile
from datetime import datetime

from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from pages.common import Common
from pages.Header.header_locators import HeaderElementLocators
from pages.Signup_login.signup_login_locators import (
    SignupFormLocators,
    SignupPageLocators,
    TradingPlatformSignupFormLocators,
    LoginFormLocators,
    LoginPageLocators,
    TradingPlatformLoginFormLocators, NewSignupFormLocators, NewLoginFormLocators,
)


class SignupLogin(BasePage):

    @allure.step(f'{datetime.now()}   Check that form [Sign up] opened')
    def check_popup_signup_form(self, timeout=1):
        """
        Check if Sign up form is popped up on the page
        """
        print(f"{datetime.now()}   Start Checking that form [Sign up] popped up on the page =>")

        if self.element_is_visible(SignupFormLocators.SIGNUP_FRAME, timeout):
            print(f"{datetime.now()}   'Sign up' form opened")
            self.close_signup_form()
        else:
            print(f"{datetime.now()}   '[Sign up]' form was not popped up")

    @allure.step('Check that "Sign up" form opened')
    def should_be_new_signup_form(self, cur_language):
        """
        Check there are an elements to on Sign up form
        """
        print(f"{datetime.now()}   Start step Check that new [Sign up] form is opened")
        if self.element_is_visible(NewSignupFormLocators.SIGNUP_FRAME, 3):
            print(f"{datetime.now()}   new 'Sign up' form opened")

            print(f"{datetime.now()}   Assert SIGNUP_HEADER =>")
            assert self.element_is_visible(NewSignupFormLocators.SIGNUP_HEADER), \
                f"{datetime.now()}   The layout of the 'SignUp' form has changed"

            print(f"{datetime.now()}   Assert SIGNUP_REF_LOGIN =>")
            assert self.element_is_visible(NewSignupFormLocators.SIGNUP_REF_LOGIN), \
                f"{datetime.now()}   Problem with 'Login' reference"

            print(f"{datetime.now()}   Assert SIGNUP_PRIVACY_POLICY_ALL_2 =>")
            if not self.element_is_visible(NewSignupFormLocators.SIGNUP_PRIVACY_POLICY):
                print(f"{datetime.now()}   Assert SIGNUP_PRIVACY_POLICY_ALL_1 =>")
            print(f"{datetime.now()}   => SIGNUP_PRIVACY_POLICY_ALL")

            print(f"{datetime.now()}   => new 'Signup' form is checked")
            return True
        else:
            print(f"{datetime.now()}   => new 'Sign up' form not opened")
            return False

    @allure.step('Check that "Sign up Pause" form opened')
    def should_be_signup_pause_form(self, cur_language):
        """
        Check there are an elements to on Sign up form
        """
        print(f"{datetime.now()}   Check that [Sign up Pause] form is opened =>")
        if self.element_is_visible(SignupFormLocators.SIGNUP_PAUSE_FORM, 3):
            print(f"{datetime.now()}   => 'Sign up Pause' form opened")

    @allure.step('Check that "Sign up" form opened')
    def should_be_signup_form(self, cur_language):
        """
        Check there are an elements to on Sign up form
        """
        print(f"{datetime.now()}   Start step Check that [Sign up] form is opened")
        if self.element_is_visible(SignupFormLocators.SIGNUP_FRAME, 3):
            print(f"{datetime.now()}   'Sign up' form opened")

            print(f"{datetime.now()}   Assert SIGNUP_HEADER =>")
            Common().assert_true_false(
                self.element_is_visible(SignupFormLocators.SIGNUP_HEADER),
                f"{datetime.now()}   The layout of the 'SignUp' form has changed"
            )

            print(f"{datetime.now()}   Assert SIGNUP_REF_LOGIN =>")
            Common().assert_true_false(
                self.element_is_visible(SignupFormLocators.SIGNUP_REF_LOGIN),
                f"{datetime.now()})   Problem with 'Login' reference")

            print(f"{datetime.now()}   Assert SIGNUP_PRIVACY_POLICY_ALL_2 =>")
            if not self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_ALL_2):

                print(f"{datetime.now()}   Assert SIGNUP_PRIVACY_POLICY_ALL_1 =>")
                if not self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_ALL_1):
                    Common().assert_true_false(
                        False,
                        f"{datetime.now()}   Problem with 'Privacy policy' reference on '{cur_language}' language!"
                    )

            print(f"{datetime.now()}   => SIGNUP_PRIVACY_POLICY_ALL")

            print(f"{datetime.now()}   => 'Signup' form is checked")
            return True
        else:
            print(f"{datetime.now()}   'Sign up' form not opened")
            return False

    @allure.step("Check that page [Sign up] opened")
    # @profile(precision=3)
    def should_be_signup_page(self, cur_language):
        """
        Check there are an elements to on 'Sign up' page
        """
        print(f"{datetime.now()}   Start method Check that [Sign up] page opened =>")
        time.sleep(1)
        # if self.current_page_is("https://capital.com/trading/signup") or \
        #         self.current_page_is("https://capital.com/trading/signup/"):
        if self.current_page_url_contain_the("https://capital.com/trading/signup"):
            print(f"{datetime.now()}   'Sign up' page opened")

            print(f"{datetime.now()}   Assert SIGNUP_SIGNUP_FRAME =>")
            assert self.element_is_present(*SignupPageLocators.SIGNUP_FRAME), \
                f"{datetime.now()}   The layout of the 'SignUp' page has changed"

            print(f"{datetime.now()}   Assert SIGNUP_REF_LOGIN =>")
            assert self.element_is_visible(SignupPageLocators.REF_LOGIN), \
                f"{datetime.now()}   Problem with 'Login' reference"

            print(f"{datetime.now()}   Assert SIGNUP_PRIVACY_POLICY_ALL_1 =>")
            if not self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_ALL_1):

                print(f"{datetime.now()}   Assert SIGNUP_PRIVACY_POLICY_ALL_2 =>")
                if not self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_ALL_2):
                    assert False, \
                        f"{datetime.now()}   Problem with 'Privacy policy' reference on '{cur_language}' language!"

            print(f"{datetime.now()}   => SIGNUP_PRIVACY_POLICY_ALL")
            print(f"{datetime.now()}   => 'Signup' page is checked")
            time.sleep(1)
            return True
        else:
            print(f"{datetime.now()}   'Sign up' page not opened")
            return False

    @allure.step("Check that [Sign up] form on trading platform page opened")
    def should_be_trading_platform_signup_form(self, cur_language):
        """
        Check there are an elements to on Sign up form
        """
        print(f"{datetime.now()}   Check that [Sign up] form on trading platform opened =>")
        if self.element_is_visible(TradingPlatformSignupFormLocators.SIGNUP_FRAME, 3):
            print(f"{datetime.now()}   => 'Sign up' form on trading platform page opened")

            print(f"{datetime.now()}   Assert SIGNUP_HEADER =>")
            assert self.element_is_visible(TradingPlatformSignupFormLocators.SIGNUP_HEADER), \
                f"{datetime.now()}   The layout of the 'SignUp' form has changed"
            print(f"{datetime.now()}   => SIGNUP_HEADER is OK")

            print(f"{datetime.now()}   Assert SIGNUP_PRIVACY_POLICY_ALL_1 =>")
            if not self.element_is_visible(TradingPlatformSignupFormLocators.SIGNUP_PRIVACY_POLICY_ALL_1):
                assert False, f"Надо уточнять локатор для {cur_language} языка"
            print(f"{datetime.now()}   => SIGNUP_PRIVACY_POLICY_ALL_1 is OK")

            print(f"{datetime.now()}   Assert SIGNUP_REF_LOGIN =>")
            assert self.element_is_visible(TradingPlatformSignupFormLocators.SIGNUP_REF_LOGIN), \
                f"{datetime.now()}   => Problem with 'Login' reference"
            print(f"{datetime.now()}   => SIGNUP_REF_LOGIN is OK")

            print(f"{datetime.now()}   => 'Signup' form on trading platform page is checked")
            # time.sleep(1)
            return True
        else:
            print(f"{datetime.now()}   'Sign up' form on trading platform page not opened")
            return False

    @allure.step("Check that form [Login] is opened")
    def should_be_login_form(self):
        """
        Check there are an elements to on Login form
        """
        print(f"{datetime.now()}   Check that 'Login' form is opened")
        if self.element_is_visible(LoginFormLocators.LOGIN_FRAME, 3):
            print(f"{datetime.now()}   'Login' form opened")

            # print(f"{datetime.now()}   LOGIN_HEADER =>")
            # assert self.element_is_visible(LoginFormLocators.LOGIN_HEADER), \
            #     f"{datetime.now()}   The layout of the 'Login' form has changed"
            #
            print(f"{datetime.now()}   Assert LOGIN_REF_SIGNUP =>")
            assert self.element_is_visible(LoginFormLocators.LOGIN_REF_SIGNUP), \
                f"{datetime.now()}   Problem with 'Sign up' reference"

            # print(f"{datetime.now()}   LOGIN_INPUT_EMAIL =>")
            # assert self.element_is_visible(LoginFormLocators.LOGIN_INPUT_EMAIL), \
            #     f"{datetime.now()}   Problem with 'Email address' field"
            #
            # print(f"{datetime.now()}   LOGIN_INPUT_PASSWORD =>")
            # assert self.element_is_visible(LoginFormLocators.LOGIN_INPUT_PASSWORD), \
            #     f"{datetime.now()}   Problem with 'Password' field"
            #
            print(f"{datetime.now()}   Assert LOGIN_CHECKBOX =>")
            assert self.element_is_visible(LoginFormLocators.LOGIN_CHECKBOX), \
                f"{datetime.now()}   Problem with 'Log me out after 7 days' check box"

            # print(f"{datetime.now()}   LOGIN_CONTINUE =>")
            # assert self.element_is_visible(LoginFormLocators.LOGIN_CONTINUE), \
            #     f"{datetime.now()}   Problem with 'Continue' button"
            #
            print(f"{datetime.now()}   Assert LOGIN_PASS_FORGOT =>")
            assert self.element_is_visible(LoginFormLocators.LOGIN_PASS_FORGOT), \
                f"{datetime.now()}   Problem with 'Forgot password' reference"

            print(f"{datetime.now()}   => 'Login' form is checked")
            # time.sleep(1)
            return True
        else:
            print(f"{datetime.now()}   'Login' form not opened")
            return False

    @allure.step("Check that new form [Login] is opened")
    # @profile(precision=3)
    def should_be_new_login_form(self):
        """
        Check there are an elements to on Login form
        """
        print(f"{datetime.now()}   Check that new 'Login' form is opened")
        if self.element_is_visible(NewLoginFormLocators.LOGIN_FRAME, 2):
            print(f"{datetime.now()}   => New 'Login' form opened")
            print(f"{datetime.now()}   Assert LOGIN_REF_SIGNUP =>")
            assert self.element_is_visible(NewLoginFormLocators.LOGIN_REF_SIGNUP), \
                f"{datetime.now()}   Problem with 'Sign up' reference"
            print(f"{datetime.now()}   Assert LOGIN_CHECKBOX =>")
            assert self.element_is_visible(NewLoginFormLocators.LOGIN_CHECKBOX), \
                f"{datetime.now()}   Problem with 'Log me out after 7 days' check box"
            print(f"{datetime.now()}   Assert LOGIN_PASS_FORGOT =>")
            assert self.element_is_visible(NewLoginFormLocators.LOGIN_PASS_FORGOT), \
                f"{datetime.now()}   Problem with 'Forgot password' reference"

            print(f"{datetime.now()}   => New 'Login' form is checked")
            # time.sleep(1)
            return True
        else:
            print(f"{datetime.now()}   => New 'Login' form not opened")
            return False

    @allure.step("Check that [Login] form on trading platform page opened")
    def should_be_trading_platform_login_form(self, cur_language):
        """
        Check there are an elements to on Login form on trading platform
        """
        if self.element_is_visible(TradingPlatformLoginFormLocators.LOGIN_FRAME, 2):
            print(f"{datetime.now()}   'Login' form on trading platform opened")

            print(f"{datetime.now()}   Assert LOGIN_EMAIL_FILD =>")
            assert self.element_is_visible(TradingPlatformLoginFormLocators.LOGIN_INPUT_EMAIL), \
                f"{datetime.now()}   Problem with 'Login e-mail' TextBox"

            print(f"{datetime.now()}   Assert LOGIN_PASSWORD_FILD =>")
            assert self.element_is_visible(TradingPlatformLoginFormLocators.LOGIN_INPUT_PASSWORD), \
                f"{datetime.now()}   Problem with 'Password' TextBox"

            print(f"{datetime.now()}   Assert LOGIN_CHECKBOX =>")
            assert self.element_is_visible(TradingPlatformLoginFormLocators.LOGIN_CHECKBOX), \
                f"{datetime.now()}   Problem with 'Log me out after 7 days' check box"

            print(f"{datetime.now()}   => 'Login' form on trading platform is checked")
            # time.sleep(1)
            return True
        else:
            print(f"{datetime.now()}   'Login' form on trading platform not opened")
            return False

    @allure.step("Check that page [Login] is opened")
    def should_be_login_page(self):
        """
        Check there are elements to on SignUp page
        """
        # if self.current_page_is("https://capital.com/trading/login"):
        if self.current_page_url_contain_the("https://capital.com/trading/login"):
            print(f"{datetime.now()}   'Login' page is opened")

            print(f"{datetime.now()}   Assert LOGIN_FRAME =>")
            assert self.element_is_present(*LoginPageLocators.LOGIN_FRAME), \
                f"{datetime.now()}   The layout of the 'Login' frame on page has changed"

            print(f"{datetime.now()}   Assert SIGNUP_REF =>")
            assert self.element_is_visible(LoginPageLocators.REF_SIGNUP), \
                f"{datetime.now()}   Problem with 'Sign up' reference"

            print(f"{datetime.now()}   Assert LOGIN_PASS_FORGOT =>")
            assert self.element_is_visible(LoginPageLocators.LOGIN_PASS_FORGOT), \
                f"{datetime.now()}   Problem with 'Forgot password' reference"

            print(f"{datetime.now()}   => 'Login' page is checked")
            time.sleep(1)
            return True
        else:
            print(f"{datetime.now()}   'Login' page not opened")
            return False

    @allure.step("Close [Sign up Pause] form")
    def close_signup_pause_form(self):
        """Method Close [Sign up] form"""
        print(f"{datetime.now()}   Start step close [Sign up Pause] form =>")
        if not self.element_is_clickable(SignupFormLocators.BUTTON_CLOSE_ON_SIGNUP_PAUSE_FORM, 3):
            print(f"{datetime.now()}   => Close button on 'Sign up Pause' form is not clickable")
            Common().assert_true_false(False, "Close button on 'Sign up' form is not clickable")
        print(f"{datetime.now()}   => Close button on 'Sign up Pause' form is clickable")

        elements = self.driver.find_elements(*SignupFormLocators.BUTTON_CLOSE_ON_SIGNUP_PAUSE_FORM)
        elements[0].click()
        print(f"{datetime.now()}   => Close button on 'Sign up Pause' form clicked")
        print(f"{datetime.now()}   => 'Signup Pause' form closed")

        # перемещаем указатель мыши на логотип CAPITAL
        Common().move_pointer_to_capital_com_label(self.driver)
        return True

    @allure.step("Close form [Sign up]")
    def close_signup_form(self):
        """Method Close [Sign up] form"""
        print(f"{datetime.now()}   Start step Close [Sign up] form =>")
        if not self.element_is_clickable(SignupFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM, 2):
            print(f"{datetime.now()}   => Close button on 'Sign up' form is not clickable")
            Common().assert_true_false(False, "Close button on 'Sign up' form is not clickable")

        elements = self.driver.find_elements(*SignupFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM)
        elements[0].click()
        print(f"{datetime.now()}   => 'Signup' form closed")

        # перемещаем указатель мыши на логотип CAPITAL
        Common().move_pointer_to_capital_com_label(self.driver)
        return True

    @allure.step("Close form [Sign up]")
    def close_new_signup_form(self):
        """Method Close new [Sign up] form"""
        print(f"{datetime.now()}   Start step Close new [Sign up] form =>")
        if not self.element_is_clickable(NewSignupFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM, 2):
            print(f"{datetime.now()}   => Close button on new 'Sign up' form is not clickable")
            return False

        elements = self.driver.find_elements(*NewSignupFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM)
        # if len(elements) == 0:
        #     print(f"{datetime.now()}   => 'Sign up' form is not opened")
        #     return False
        elements[0].click()
        print(f"{datetime.now()}   => new 'Signup' form closed")

        # перемещаем указатель мыши на логотип CAPITAL
        elements = self.driver.find_elements(*HeaderElementLocators.NEW_MAIN_LOGO_CAPITAL_COM)
        ActionChains(self.driver) \
            .move_to_element(elements[0]) \
            .perform()

        return True

    @allure.step("Close page [Sign up]")
    def close_signup_page(self):
        """Method Close [Sign up] page"""
        print(f"{datetime.now()}   Start method 'Close [Sign up] page' =>")
        if not (self.current_page_url_contain_the("https://capital.com/trading/signup")):
            print(f"{datetime.now()}   'Sign up' page not opened")
            return False

        self.driver.back()
        print(f"{datetime.now()}   => [Sign up] page is closed")
        return True

    @allure.step("Close [Sign up] form with trading platform page")
    def close_trading_platform_signup_form(self):
        """Method Close [Sign up] form with trading platform page"""
        print(f"{datetime.now()}   Close [Sign up] form with trading platform page =>")
        # if not (self.current_page_url_contain_the("https://capital.com/trading/platform/")):
        #     print(f"{datetime.now()}   'Sign up' page on trading platform page not opened")
        #     return False

        self.driver.back()
        print(f"{datetime.now()}   => [Sign up] form with trading platform page is closed")
        return True

    @allure.step("Close form [Login]")
    def close_login_form(self):
        if not self.element_is_clickable(LoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM, 2):
            print(f"{datetime.now()}   => 'Close' button on 'Login' form not clickable after 2 sec.")
            return False
        print(f"{datetime.now()}   Click 'Close' button on 'Login' form =>")
        self.driver.find_element(*LoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM).click()
        Common().move_pointer_to_capital_com_label(self.driver)
        print(f"{datetime.now()}   => 'Login' form closed")
        return True

    @allure.step("Close new [Login] form")
    def close_new_login_form(self):
        if not self.element_is_clickable(NewLoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM, 2):
            print(f"{datetime.now()}   => 'Close' button on new 'Login' form not clickable after 2 sec.")
            return False
        print(f"{datetime.now()}   Click 'Close' button on new 'Login' form =>")
        self.driver.find_element(*NewLoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM).click()
        print(f"{datetime.now()}   => New 'Login' form closed")
        return True

    @allure.step("Close page [Login]")
    def close_login_page(self):
        if not self.current_page_is("https://capital.com/trading/login"):
            print(f"{datetime.now()}   => 'Login' page not opened")
            return False

        print(f"{datetime.now()}   Close 'Login' page =>")
        self.driver.back()
        print(f"{datetime.now()}   => 'Login' page closed")
        return True

    @allure.step("Close [Login] form on trading platform page")
    def close_trading_platform_login_form(self):
        """Method Close [Login] form with trading platform page"""
        print(f"{datetime.now()}   Start method 'Close [Login] form with trading platform page' =>")
        if not (self.current_page_url_contain_the("https://capital.com/trading/platform")):
            print(f"{datetime.now()}   'Login' form on trading platform page not opened")
            return False

        self.driver.back()
        print(f"{datetime.now()}   => [Login] form with trading platform page is closed")
        return True
