from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ContentBlockLocators
from selenium.common.exceptions import ElementClickInterceptedException


class ContentOpenAnAccount(BasePage):

    @allure.step(f"{datetime.now()}   Start Full test for Open an account button of the page content")
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):

        self.arrange_(d, cur_item_link)
        self.element_click(cur_language, cur_country)

        test_element = AssertClass(d, cur_item_link, self.bid)
        match cur_role:
            case "NoReg" | "NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        button_list = self.driver.find_elements(*ContentBlockLocators.BUTTON_OPEN_AN_ACCOUNT_CONTENT)
        if len(button_list) == 0:
            print(f"{datetime.now()} => BUTTON_OPEN_AN_ACCOUNT_CONTENT is not present on the page!")
            del button_list
            pytest.skip("Checking element 'BUTTON_OPEN_AN_ACCOUNT_CONTENT' is not on this page")

        print(f"{datetime.now()}   BUTTON_OPEN_AN_ACCOUNT_CONTENT scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', button_list[0]
        )

        print(f"{datetime.now()}   BUTTON_OPEN_AN_ACCOUNT_CONTENT is visible? =>")
        if self.element_is_visible(ContentBlockLocators.BUTTON_OPEN_AN_ACCOUNT_CONTENT):
            print(f"{datetime.now()}   => BUTTON_OPEN_AN_ACCOUNT_CONTENT is visible on the page!")
        else:
            print(f"{datetime.now()}   => BUTTON_OPEN_AN_ACCOUNT_CONTENT is not visible on the page!")
            pytest.fail("Bug! Checking element 'BUTTON_OPEN_AN_ACCOUNT_CONTENT' is present on this page, "
                        "but not visible")

    @allure.step("Click button [Open an account] on the page content")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")
        print(f"{datetime.now()}   Start Click button [Open an account] =>")
        button_list = self.driver.find_elements(*ContentBlockLocators.BUTTON_OPEN_AN_ACCOUNT_CONTENT)

        print(f"{datetime.now()}   BUTTON_OPEN_AN_ACCOUNT_CONTENT is clickable? =>")
        time_out = 3
        if not self.element_is_clickable(button_list[0], time_out):
            print(f"{datetime.now()} => BUTTON_OPEN_AN_ACCOUNT_CONTENT is not clickable after {time_out} sec. Stop TC>")
            pytest.fail(f"BUTTON_OPEN_AN_ACCOUNT_CONTENT is not clickable after {time_out} sec.")

        print(f"{datetime.now()}   BUTTON_OPEN_AN_ACCOUNT_CONTENT click =>")
        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_OPEN_AN_ACCOUNT_CONTENT clicked")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_OPEN_AN_ACCOUNT_CONTENT not clicked")
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

            del page_
            button_list[0].click()

        del button_list
        return True
