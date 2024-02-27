from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ContentBlockLocators
from selenium.common.exceptions import ElementClickInterceptedException


class ContentBlockCreateARiskFreeDemoAccountButton:
    class ButtonCreateARiskFreeDemoAccountUnleveragedBlock(BasePage):
        @allure.step(f'{datetime.now()}   Start Full test for [Create a risk free demo account button] '
                     f'in Uleveraged trading block')
        def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):

            self.arrange_(d, cur_item_link)
            self.element_click()

            test_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
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

            button_list_1 = self.driver.find_elements(
                *ContentBlockLocators.BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_UNLEVERAGED_TRADING_BLOCK)

            if len(button_list_1) == 0:
                print(f"{datetime.now()} => BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_UNLEVERAGED_TRADING_BLOCK "
                      f"is not present on the page!")
                pytest.skip("BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_UNLEVERAGED_TRADING_BLOCK "
                            "is not present on the page!")
            else:
                print(f"{datetime.now()} => BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_UNLEVERAGED_TRADING_BLOCK "
                      f"is present on the page")

            print(f"{datetime.now()}   BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_UNLEVERAGED_TRADING_BLOCK scroll =>")
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', button_list_1[0]
            )

            del button_list_1

        @allure.step("Click button [Create a risk free demo account button] in Uleveraged trading block")
        def element_click(self):
            print(f"\n{datetime.now()}   2. Act_v0")

            button_list_1 = self.driver.find_elements(
                *ContentBlockLocators.BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_UNLEVERAGED_TRADING_BLOCK)

            time_out = 3
            if not self.element_is_clickable(button_list_1[0], time_out):
                print(f"{datetime.now()} => BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_UNLEVERAGED_TRADING_BLOCK "
                      f" is not clickable after {time_out} sec. Stop TC>")
                pytest.fail("BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_UNLEVERAGED_TRADING_BLOCK "
                            "is not clickable after {time_out} sec.")

            print(f"{datetime.now()}  BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_UNLEVERAGED_TRADING_BLOCK "
                  f"clickable =>")

            try:
                button_list_1[0].click()
                print(f"{datetime.now()} => BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_UNLEVERAGED_TRADING_BLOCK"
                      f" clicked!")
            except ElementClickInterceptedException:
                print(f"{datetime.now()} => BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_UNLEVERAGED_TRADING_BLOCK"
                      f" NOT CLICKED")
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

                    button_list_1.click()
                    del page_

            del button_list_1
            return True

    class ButtonCreateARiskFreeDemoAccountHowToGetStartedTrading(BasePage):
        @allure.step(f'{datetime.now()}   Start Full test for [Create a risk free demo account button] '
                     f'in How to get started trading block')
        def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):

            self.arrange_(d, cur_item_link)
            self.element_click()

            test_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
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

            button_list_2 = self.driver.find_elements(
                *ContentBlockLocators.BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_HOW_TO_GET_STARTED_WITH_TRADING_BLOCK)

            if len(button_list_2) == 0:
                print(f"{datetime.now()} =>BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_HOW_TO_GET_STARTED_WITH_TRADING_BLOCK"
                      f" is not present on the page!")
                pytest.skip("BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_HOW_TO_GET_STARTED_WITH_TRADING_BLOCK "
                            "is not present on the page!")
            else:
                print(f"{datetime.now()} =>BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_HOW_TO_GET_STARTED_WITH_TRADING_BLOCK"
                      f"is present on the page")

            print(f"{datetime.now()}   BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_HOW_TO_GET_STARTED_WITH_TRADING_BLOCK "
                  f"scroll =>")
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', button_list_2[0]
            )

            del button_list_2

        @allure.step("Click button [Create a risk free demo account button] in How to get started trading block")
        def element_click(self):
            print(f"\n{datetime.now()}   2. Act_v0")

            button_list_2 = self.driver.find_elements(
                *ContentBlockLocators.BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_HOW_TO_GET_STARTED_WITH_TRADING_BLOCK)

            time_out = 3
            if not self.element_is_clickable(button_list_2[0], time_out):
                print(f"{datetime.now()} => "
                      f"BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_HOW_TO_GET_STARTED_WITH_TRADING_BLOCK"
                      f" is not clickable after {time_out} sec. Stop TC>")
                pytest.fail("BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_HOW_TO_GET_STARTED_WITH_TRADING_BLOCK "
                            "is not clickable after {time_out} sec.")

            print(f"{datetime.now()}  BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_HOW_TO_GET_STARTED_WITH_TRADING_BLOCK "
                  f"clickable =>")

            try:
                button_list_2[0].click()
                print(f"{datetime.now()} => "
                      f"BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_HOW_TO_GET_STARTED_WITH_TRADING_BLOCK clicked!")
            except ElementClickInterceptedException:
                print(f"{datetime.now()} => "
                      f"BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_HOW_TO_GET_STARTED_WITH_TRADING_BLOCK NOT CLICKED")
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

                    button_list_2.click()
                    del page_

            del button_list_2
            return True
