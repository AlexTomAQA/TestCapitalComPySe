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

        print(f"{datetime.now()} Is TOOLINFO_SHORT_POSITION_OVERNIGHT_FEE present on the page? =>")
        toolinfo = self.driver.find_elements(*PageTradingInstrumentMarketsLocators.
                                             TOOLINFO_SHORT_POSITION_OVERNIGHT_FEE)
        if len(toolinfo) == 0:
            print(f"{datetime.now()}   => TOOLINFO_SHORT_POSITION_OVERNIGHT_FEE is not present on the page")
            Common.pytest_fail("Bug ? TOOLINFO_SHORT_POSITION_OVERNIGHT_FEE is not present on the page")

        print(f"{datetime.now()}   TOOLINFO_SHORT_POSITION_OVERNIGHT_FEE  scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            toolinfo[0]
        )
        print(f"{datetime.now()}   => TOOLINFO_SHORT_POSITION_OVERNIGHT_FEE  scrolled")
#        ActionChains(d) \
#            .move_to_element(toolinfo[0]) \
#            .pause(0.5) \
#            .perform()

#        print(f"{datetime.now()}   Is TOOLTIP_SHORT_POSITION_FEE open?  =>")
#        tooltip = self.element_is_visible(PageTradingInstrumentMarketsLocators.TOOLTIP_SHORT_POSITION_FEE)
#        if tooltip == 0:
#            print(f"{datetime.now()}   => TOOLTIP_SHORT_POSITION_FEE is not open")
#            pytest.fail("TOOLTIP_SHORT_POSITION_FEE is not open")

#        ActionChains(d) \
#            .move_to_element(tooltip) \
#            .pause(0.5) \
#            .perform()

#        button_list = self.driver.find_elements(PageTradingInstrumentMarketsLocators.BUTTON_GO_TO_PLATFORM)
#        print(f"{datetime.now()}   Is button BUTTON_GO_TO_PLATFORM present on the page? =>")
#        if len(button_list) == 0:
#            print(f"{datetime.now()}   => BUTTON_GO_TO_PLATFORM is not present on the page")
#            return False
#        print(f"{datetime.now()}   => BUTTON_GO_TO_PLATFORM is present on the page")

#        print(f"{datetime.now()}   BUTTON_GO_TO_PLATFORM scroll =>")
#        self.driver.execute_script(
#            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
#            button_list[0]
#        )
#        print(f"{datetime.now()}   => BUTTON_GO_TO_PLATFORM scrolled")

    @allure.step("Hover over tooltip 'Short position overnight fee' --> "
                 "Click button [Go to platform] on trading instrument page")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")
        print(f"{datetime.now()}   Start Click button [Go to platform] =>")

        toolinfo = self.driver.find_elements(
            *PageTradingInstrumentMarketsLocators.TOOLINFO_SHORT_POSITION_OVERNIGHT_FEE)

        ActionChains(self.driver) \
            .move_to_element(toolinfo[0]) \
            .pause(0.5) \
            .perform()

        print(f"{datetime.now()}   Is TOOLTIP_SHORT_POSITION_FEE open?  =>")
        button_go_to_platform = self.element_is_visible(PageTradingInstrumentMarketsLocators.BUTTON_GO_TO_PLATFORM)

        if not button_go_to_platform:
            print(f"{datetime.now()}   => TOOLTIP_SHORT_POSITION_FEE is not open")
            Common.pytest_fail("Bug ? TOOLTIP_SHORT_POSITION_FEE is not open")
        print(f"{datetime.now()}   => TOOLTIP_SHORT_POSITION_FEE is open")

        print(f"{datetime.now()}   Move focus to button [Go to platform] and click on =>")

        ActionChains(self.driver) \
            .move_to_element(button_go_to_platform) \
            .pause(0.5) \
            .perform()

#        button_list = self.driver.find_elements(PageTradingInstrumentMarketsLocators.BUTTON_GO_TO_PLATFORM)

        time_out = 5
        if not self.element_is_clickable(button_go_to_platform, time_out):
            print(f"{datetime.now()} => BUTTON_GO_TO_PLATFORM is not clickable after {time_out} sec. Stop TC>")
            Common.pytest_fail(f"BUTTON_GO_TO_PLATFORM is not clickable after {time_out} sec.")

        print(f"{datetime.now()}   BUTTON_GO_TO_PLATFORM is clickable =>")

        button_go_to_platform.click()
        print(f"{datetime.now()} => BUTTON_GO_TO_PLATFORM clicked")
