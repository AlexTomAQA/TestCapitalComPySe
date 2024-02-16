from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ContentBlockLocators
from selenium.common.exceptions import ElementClickInterceptedException


class ContentTryDemoAccount(BasePage):

    @allure.step(f'{datetime.now()}   Start Full test for Try demo account button of the page content')
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

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   BUTTON_TRY_DEMO is visible? =>")
        if self.element_is_visible(ContentBlockLocators.BUTTON_TRY_DEMO_ACCOUNT_CONTENT):
            print(f"{datetime.now()} => BUTTON_TRY_DEMO_ACCOUNT_CONTENT is visible on the page!")
        else:
            print(f"{datetime.now()} => BUTTON_TRY_DEMO_ACCOUNT_CONTENT is not visible on the page!")
            pytest.fail("Bug # 20 Checking element is not on this page")

    @allure.step("Click button [Try demo account] on the page")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")
        print(f"{datetime.now()}   BUTTON_TRY_DEMO_ACCOUNT_CONTENT is present? =>")
        button_list = self.driver.find_elements(*ContentBlockLocators.BUTTON_TRY_DEMO_ACCOUNT_CONTENT)
        if len(button_list) == 0:
            print(f"{datetime.now()} => BUTTON_TRY_DEMO_ACCOUNT_CONTENT is not present on the page!")
            del button_list
            return False
        print(f"{datetime.now()} => BUTTON_TRY_DEMO_ACCOUNT_CONTENT is present on the page!")

        print(f"{datetime.now()}   BUTTON_TRY_DEMO_ACCOUNT_CONTENT scroll =>")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        self.element_is_clickable(button_list[0], 5)

        try:
            self.driver.execute_script("arguments[0].click();", button_list[0])
            print(f"{datetime.now()} => BUTTON_TRY_DEMO_ACCOUNT_CONTENT clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()} => BUTTON_TRY_DEMO_ACCOUNT_CONTENT NOT CLICKED")
            print(f"{datetime.now()}   'Sign up' form or page is auto opened")

            page_ = SignupLogin(self.driver)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()

            self.driver.execute_script("arguments[0].click();", button_list[0])
            del page_

        del button_list
        return True
