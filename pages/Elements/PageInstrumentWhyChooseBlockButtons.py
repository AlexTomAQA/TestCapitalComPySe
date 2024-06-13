from datetime import datetime
import allure
from selenium.webdriver import ActionChains

from pages.Elements.testing_elements_locators import WhyChooseLocators
from pages.common import Common
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass


class PageInstrumentWhyChooseBlockButton(BasePage):
    @allure.step(f"{datetime.now()}   Start Full test for button [Try now] in the Block 'Why choose Capital.com?'")
    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)
        self.element_click(d)

        test_element= AssertClass(d, cur_item_link, self.bid)
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

        print(f"{datetime.now()}   IS 'Why choose Capital.com?' block present on the page? =>")
        why_choose_block = self.driver.find_element(*WhyChooseLocators.BLOCK_WHY_CHOOSE)
        if not why_choose_block:
            print(f"{datetime.now()},   => 'Why choose Capital.com?' is not present on the page")
            Common.pytest_fail("'Why choose Capital.com?' is not present on the page")

        print(f"{datetime.now()},   => Block 'Why choose Capital.com? is present. Scroll to block")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*WhyChooseLocators.BLOCK_WHY_CHOOSE)
        )

        print(f"{datetime.now()},   Is BUTTON_TRY_NOW_BLOCK_WHY_CHOOSE present in the block? =>")
        button_try_now = self.driver.find_element(
            *WhyChooseLocators.BUTTON_TRY_NOW_BLOCK_WHY_CHOOSE)
        if not button_try_now:
            Common.pytest_fail("Bug ? BUTTON_TRY_NOW_BLOCK_WHY_CHOOSE is not present in the block")
        print(f"{datetime.now()},   => BUTTON_TRY_NOW_BLOCK_WHY_CHOOSE is present in the block")

    @allure.step("Click button [Try now] button in Block 'Why choose Capital.com?' ")
    def element_click(self, d):
        print(f"\n{datetime.now()}   2. Act_v0")
        print(f"{datetime.now()}   Start Click [Try now] button =>")

        if not self.element_is_clickable(WhyChooseLocators.BUTTON_TRY_NOW_BLOCK_WHY_CHOOSE):
            print(f"{datetime.now()},   => BUTTON_TRY_NOW_BLOCK_WHY_CHOOSE is not clickable")
            Common.pytest_fail("Bug ? BUTTON_TRY_NOW_BLOCK_WHY_CHOOSE is not clickable")

        ActionChains(d)\
            .move_to_element(self.driver.find_element(*WhyChooseLocators.BUTTON_TRY_NOW_BLOCK_WHY_CHOOSE))\
            .pause(0.5)\
            .click(self.driver.find_element(*WhyChooseLocators.BUTTON_TRY_NOW_BLOCK_WHY_CHOOSE))\
            .perform()
        print(f"{datetime.now()}, Bug ? BUTTON_TRY_NOW_BLOCK_WHY_CHOOSE is not clickable")
