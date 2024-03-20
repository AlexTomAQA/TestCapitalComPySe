from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import PageTradingInstrumentMarketsLocators
from selenium.common.exceptions import ElementClickInterceptedException


class PageInstrumentViewDetailedChartButton(BasePage):
    @allure.step(f"{datetime.now()}   Start test for ViewDetailedChartButton of the trading instrument page")
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

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        button_list = self.driver.find_elements(*PageTradingInstrumentMarketsLocators.BUTTON_VIEW_DETAILED_CHART)
        print(f"{datetime.now()}   Is button BUTTON_VIEW_DETAILED_CHART present on the page? =>")
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_VIEW_DETAILED_CHART is not present on the page")
            return False
        print(f"{datetime.now()}   => BUTTON_VIEW_DETAILED_CHART is present on the page")

        print(f"{datetime.now()}   BUTTON_VIEW_DETAILED_CHART scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )
        print(f"{datetime.now()}   => BUTTON_VIEW_DETAILED_CHART scrolled")

    @allure.step("Click button [View Detailed Chart] on the page content")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")
        print(f"{datetime.now()}   Start Click button [View Detailed Chart] =>")

        button_list = self.driver.find_elements(*PageTradingInstrumentMarketsLocators.BUTTON_VIEW_DETAILED_CHART)

        time_out = 3
        if not self.element_is_clickable(button_list[0], time_out):
            print(f"{datetime.now()} => BUTTON_VIEW_DETAILED_CHART is not clickable after {time_out} sec. Stop TC>")
            pytest.fail(f"BUTTON_VIEW_DETAILED_CHART is not clickable after {time_out} sec.")

        print(f"{datetime.now()}   BUTTON_VIEW_DETAILED_CHART is clickable =>")

        try:
            button_list[0].click()
            print(f"{datetime.now()} => BUTTON_VIEW_DETAILED_CHART clicked")
        except ElementClickInterceptedException:
            print(f"{datetime.now()} => BUTTON_VIEW_DETAILED_CHART not clicked")
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
