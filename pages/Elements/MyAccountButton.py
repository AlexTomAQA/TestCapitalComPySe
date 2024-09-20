from datetime import datetime

import allure

from pages.Elements.testing_elements_locators import MyAccountButtonLocators
from pages.base_page import BasePage
from pages.common import Common
from src.src import CapitalComPageSrc


class MyAccountButton(BasePage):
    @allure.step(f"{datetime.now()}   Start full test of 'My account' button in the header")
    def full_test(self, d, cur_language, cur_country, cur_role, link):
        self.arrange_(d)
        self.element_click()

        match cur_role:
            case "Auth":
                self.assert_my_account_menu(d)

    def arrange_(self, link):
        print(f"\n{datetime.now()}   1. Arrange for My account button")

        if not self.current_page_is(link):
            self.link = CapitalComPageSrc.URL_NEW
            self.open_page()

        print(f"{datetime.now()}   Is BUTTON_MY_ACCOUNT present on the page? =>")
        button = self.driver.find_elements(*MyAccountButtonLocators.BUTTON_MY_ACCOUNT)
        if len(button) == 0:
            print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is not present on the page")
            Common().pytest_fail("BUTTON_MY_ACCOUNT is not present on the page")
        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is present on the page")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button[0]
        )

    @allure.step("Click My account button in the page header")
    def element_click(self):
        print(f"{datetime.now()}   2. Act for My account button")
        print(f"{datetime.now()}   Start to click BUTTON_MY_ACCOUNT =>")

        button = self.driver.find_elements(*MyAccountButtonLocators.BUTTON_MY_ACCOUNT)
        button[0].click()

        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is clicked")

    @allure.step('Checking that the "My account" menu is opened')
    def assert_my_account_menu(self, d):
        print(f"\n{datetime.now()}   3. Assert_v0")
        account_btn_link = d.current_url
        print(f"{datetime.now()}   Current URL is account_btn_link")

        if (account_btn_link == "https://capital.com/trading/platform/" or
                account_btn_link == "https://capital.com/trading/platform/?popup=terms-and-conditions"):
            assert False, \
                ('Bug#009. '
                 'Expected result: Menu "My account" is displayed'
                 '\n'
                 'Actual result: The trading platform page is opened')
        else:
            print(f"{datetime.now()}   =>This does not mean that there is no bug")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
