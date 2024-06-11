from datetime import datetime
# import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import PageTradingInstrumentMarketsLocators
from selenium.webdriver import ActionChains
# from selenium.common.exceptions import ElementClickInterceptedException

from pages.common import Common


class PageInstrumentShortPositionGoToPlatformButton(BasePage):
    @allure.step(f"{datetime.now()}   Start test for ViewDetailedChartButton of the trading instrument page")
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_v2(d, cur_item_link)

        # page_signup_login = SignupLogin(d, cur_item_link)
        # page_signup_login.check_popup_signup_form()
        #
        trade_instrument = self.element_act_v2()

        test_element = AssertClass(d, cur_item_link, self.bid)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link, tpd=False, tpi=True,
                                                        trade_instrument=trade_instrument)
        self.driver.get(cur_item_link)

    def arrange_v2(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v2")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()} Is SHORT_POSITION_OVERNIGHT_FEE present on the page? =>")
        tool_info = self.driver.find_elements(*PageTradingInstrumentMarketsLocators.SHORT_POSITION_OVERNIGHT_FEE)
        if len(tool_info) == 0:
            msg = "SHORT_POSITION_OVERNIGHT_FEE is not present on the page"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # ???   {msg}")
        print(f"{datetime.now()}   => SHORT_POSITION_OVERNIGHT_FEE is present on the page")

        print(f"{datetime.now()}   SHORT_POSITION_OVERNIGHT_FEE  scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            tool_info[0]
        )
        print(f"{datetime.now()}   => SHORT_POSITION_OVERNIGHT_FEE  scrolled")

    @allure.step("Hover over tooltip 'Short position overnight fee' --> Click button [Go to platform]")
    def element_act_v2(self):
        print(f"\n{datetime.now()}   2. Act_v2")
        print(f"{datetime.now()}   SHORT_POSITION_OVERNIGHT_FEE open =>")
        tool_info = self.driver.find_elements(*PageTradingInstrumentMarketsLocators.SHORT_POSITION_OVERNIGHT_FEE)
        ActionChains(self.driver) \
            .move_to_element(tool_info[0]) \
            .pause(0.5) \
            .perform()

        print(f"{datetime.now()}   Is SHORT_POSITION_OVERNIGHT_FEE open?  =>")
        button_go_to_platform = self.element_is_visible(
            PageTradingInstrumentMarketsLocators.SHORT_POSITION_BUTTON_GO_TO_PLATFORM)
        if not button_go_to_platform:
            msg = "SHORT_POSITION_FEE is not open"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # ???   {msg}")
        print(f"{datetime.now()}   => TOOLTIP_SHORT_POSITION_FEE is open")

        print(f"{datetime.now()}   Move focus to button [Go to platform] and click on =>")
        ActionChains(self.driver) \
            .move_to_element(button_go_to_platform) \
            .pause(0.5) \
            .perform()

        time_out = 5
        if not self.element_is_clickable(button_go_to_platform, time_out):
            msg = f"BUTTON_GO_TO_PLATFORM is not clickable after {time_out} sec."
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # ???   {msg}")
        print(f"{datetime.now()}   => BUTTON_GO_TO_PLATFORM is clickable")

        button_go_to_platform.click()
        print(f"{datetime.now()} => BUTTON_GO_TO_PLATFORM clicked")
