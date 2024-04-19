from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ContentBlockLocators
from selenium.common.exceptions import ElementClickInterceptedException


class ContentBlockTryDemoAccountButton(BasePage):

    @allure.step(f'{datetime.now()}   Start Full test for Try demo account button of the page content')
    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)

        self.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                if cur_country == "gb":
                    test_element.assert_signup_pause(d, cur_language, cur_item_link)
                else:
                    test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link, True)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   BUTTON_TRY_DEMO_ACCOUNT_CONTENT_BLOCK is visible? =>")
        if self.element_is_visible(ContentBlockLocators.BUTTON_TRY_DEMO_ACCOUNT_CONTENT_BLOCK):
            print(f"{datetime.now()} => BUTTON_TRY_DEMO_ACCOUNT_CONTENT_BLOCK is visible on the page!")
        else:
            print(f"{datetime.now()} => BUTTON_TRY_DEMO_ACCOUNT_CONTENT_BLOCK is not visible on the page!")
            pytest.fail("Bug # ? Checking element is not on this page")

        button_list = self.driver.find_elements(*ContentBlockLocators.BUTTON_TRY_DEMO_ACCOUNT_CONTENT_BLOCK)

        print(f"{datetime.now()}   BUTTON_TRY_DEMO_ACCOUNT_CONTENT_BLOCK scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', button_list[0]
        )

    @allure.step("Click button [Try demo account] on the page")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")

        button_list = self.driver.find_elements(*ContentBlockLocators.BUTTON_TRY_DEMO_ACCOUNT_CONTENT_BLOCK)

        time_out = 3
        if not self.element_is_clickable(button_list[0], time_out):
            print(f"{datetime.now()} => BUTTON_TRY_DEMO_ACCOUNT_CONTENT_BLOCK is not clickable after {time_out} "
                  f"sec. Stop TC>")
            pytest.fail(f"BUTTON_TRY_DEMO_ACCOUNT_CONTENT_BLOCK is not clickable after {time_out} sec.")

        print(f"{datetime.now()}   BUTTON_TRY_DEMO_ACCOUNT_CONTENT_BLOCK clickable =>")

        try:
            self.driver.execute_script("arguments[0].click();", button_list[0])
            print(f"{datetime.now()} => BUTTON_TRY_DEMO_ACCOUNT_CONTENT_BLOCK clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()} => BUTTON_TRY_DEMO_ACCOUNT_CONTENT_BLOCK NOT CLICKED")
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
