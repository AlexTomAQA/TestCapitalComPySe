"""
-*- coding: utf-8 -*-
@Time    : 2024/06/14 20:30
@Author  : Artem Dashkov
"""
from datetime import datetime
import pytest
import allure
from pages.common import Common
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Markets.markets_locators import HeaderElementLocators
from selenium.common.exceptions import ElementNotInteractableException, StaleElementReferenceException

from pages.Signup_login.signup_login_locators import SignupFormLocators


BUTTON_NAME = '[Sign up]'

BUTTON_LOCATOR = HeaderElementLocators.BUTTON_SIGNUP_2

class EmailFieldSignUpForm(BasePage):
    global BUTTON_NAME

    global BUTTON_LOCATOR

    def __init__(self, browser, link, bid):
        self.button = None
        self.page_signup_login = None

        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}  Start Full test for field [email] in Sign up form")
    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link, invalid_login, valid_password):
        self.arrange(d, cur_item_link)
        self.element_click(d, cur_item_link, invalid_login, valid_password)
        self.assert_step(d, cur_item_link, invalid_login, valid_password)

    @allure.step(f"{datetime.now()}  Assert step")
    def assert_step(self, d, cur_item_link, invalid_login, valid_password):
        print(f"\n{datetime.now()}   3. Assert")

        # Test popup message 'Please enter a valid Email'
        self.page_signup_login = SignupLogin(d, cur_item_link)
        print(f"{datetime.now()}   Is 'Please enter a valid Email' message displayed on this page"
              f" after putting invalid email? =>")
        print(f"{datetime.now()}   => Start fill out 'Email address' field.")
        if not self.send_keys(invalid_login, *SignupFormLocators.SIGNUP_INPUT_EMAIL):
            pytest.fail(f'{datetime.now()}   => "Email address" is not inputted')
        print(f"{datetime.now()}   => 'Email address' is inputted\n")

        signup_input_password_field = self.driver.find_element(*SignupFormLocators.SIGNUP_INPUT_PASSWORD)
        signup_input_password_field.click()
        print(f"{datetime.now()}   => Switch to 'Password' field\n")
        email_popup_message = self.driver.find_element(*SignupFormLocators.SIGNUP_EMAIL_POPUP_MESSAGE)

        print('get_attribute: ', email_popup_message.get_attribute('style'))

        if "display: block" not in email_popup_message.get_attribute('style'):
            msg = "'Please enter a valid Email' message is NOT displayed"
            Common().assert_true_false(False, msg)
        print(f"{datetime.now()}   => 'Please enter a valid Email' message is displayed\n")
        Common().save_current_screenshot(d, "'Please enter a valid Email' message is displayed")

        # Test status of [Continue] button
        print(f"{datetime.now()}   Is [Continue] button active after putting invalid email? =>")
        print(f"{datetime.now()}   => Start fill out 'Password' field.")
        if not self.send_keys(valid_password, *SignupFormLocators.SIGNUP_INPUT_PASSWORD):
            msg = f"'Password' is not inputted"
            Common().assert_true_false(False, msg)
        print(f"{datetime.now()}   => 'Password' is inputted\n")

        continue_button = self.driver.find_element(*SignupFormLocators.SIGNUP_SUBMIT_BTN)

        print('continue_button: ', continue_button.get_attribute('class'))
        if "disabled hasPointer" not in continue_button.get_attribute('class'):
            msg = "[Continue] button is active after putting invalid email"
            Common().assert_true_false(False, msg)
        print(f"{datetime.now()}   => '[Continue] button is not active after putting invalid email\n")
        Common().save_current_screenshot(d, "[Continue] button is not active after putting invalid email")
        Common().assert_true_false(True, "")

    @allure.step(f'{datetime.now()}    Arrange')
    def arrange(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        # Check presenting and visible button [Sign Up]
        print(f"{datetime.now()}   IS {BUTTON_NAME} button present on this page? =>")
        self.button = self.driver.find_elements(*BUTTON_LOCATOR)
        if len(self.button) == 0:
            msg = f"{BUTTON_NAME} button is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} button present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*BUTTON_LOCATOR)[0]
        )

        print(f"{datetime.now()}   IS {BUTTON_NAME} button visible on this page? =>")
        if not self.element_is_visible(BUTTON_LOCATOR, 5):
            msg = f"{BUTTON_NAME} button is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} button is visible on this page!\n")

    @allure.step(f"{datetime.now()}    Click button [Sign up]")
    def element_click(self, d, cur_item_link, invalid_login, valid_password):
        print(f"\n{datetime.now()}   2. Act_v0")

        # IS [Sign Up] button clickable?
        print(f"{datetime.now()}   IS {BUTTON_NAME} clickable on the page? =>")
        if not self.element_is_clickable(BUTTON_LOCATOR):
            print(f"{datetime.now()}   => {BUTTON_NAME} is NOT clickable on the page!\n")
            Common().pytest_fail(f" Bug ? Checking element is not clickable on this page")
        print(f"{datetime.now()}   => {BUTTON_NAME} is clickable on the page!\n")

        print(f"\n{datetime.now()}   Start Click button {BUTTON_NAME} =>")

        try:
            self.driver.find_element(*BUTTON_LOCATOR).click()
            print(f"{datetime.now()}   => End Click button {BUTTON_NAME} ")
        except ElementNotInteractableException:
            msg = f"{BUTTON_NAME} is NOT clicked"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(msg)
        except StaleElementReferenceException:
            self.driver.find_elements(*BUTTON_LOCATOR)[0].click()
            print(f"{datetime.now()}   => End Click button {BUTTON_NAME} ")

        if SignupLogin(d, cur_item_link).should_be_signup_form(cur_item_link):
            print(f"{datetime.now()}   => 'Sign up' form is opened")
        else:
            msg = "Problem with Authorisation"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug_045a   {msg}")

        return True

