"""
-*- coding: utf-8 -*-
@Time    : 2024/03/19 13:50
@Author  : Artem Dashkov
"""
from datetime import datetime
import pytest
import allure

from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ButtonsOnPageLocators
from selenium.common.exceptions import ElementClickInterceptedException


class TradingCalculatorStartTradingButton(BasePage):

    def __init__(self, browser, link, bid):
        self.button_start_trading = None

        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}   Start Full test for [Start Trading] button in Widget 'Trading calculator'")
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)
        self.element_click(d)

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

        # Check presenting and visible 'Trading calculator' widget
        print(f"{datetime.now()}   IS 'Trading calculator' widget present on this page? =>")
        widget_trading_calculator = self.driver.find_elements(*ButtonsOnPageLocators.TRADING_CALCULATOR_WIDGET)
        if len(widget_trading_calculator) == 0:
            print(f"{datetime.now()}   => 'Trading calculator' widget is NOT present on this page\n")
            pytest.fail("'Trading calculator' widget is NOT present on this page")
        print(f"{datetime.now()}   => 'Trading calculator' widget present on this page!\n")

        print(f"{datetime.now()}   IS 'Trading calculator' widget present on this page? =>")
        if not self.element_is_visible(ButtonsOnPageLocators.TRADING_CALCULATOR_WIDGET, 5):
            print(f"{datetime.now()}   => 'Trading calculator' widget is NOT visible on this page!\n")
            pytest.fail("'Trading calculator' widget is NOT visible on this page!")
        print(f"{datetime.now()}   => 'Trading calculator' widget is visible on this page!\n")

        # Check presenting and visible [Start Trading] button
        print(f"{datetime.now()}   IS [Start Trading] button present on this page? =>")
        self.button_start_trading = self.driver.find_elements(
            *ButtonsOnPageLocators.BUTTON_START_TRADING_IN_TRADING_CALCULATOR)
        if len(self.button_start_trading) == 0:
            print(f"{datetime.now()}   => [Start Trading] button is NOT present on this page\n")
            pytest.fail("[Start Trading] button is NOT present on this page")
        print(f"{datetime.now()}   => [Start Trading] button present on this page!\n")

        print(f"{datetime.now()}   IS [Start Trading] button present on this page? =>")
        if not self.element_is_visible(
                ButtonsOnPageLocators.BUTTON_START_TRADING_IN_TRADING_CALCULATOR, 5):
            print(f"{datetime.now()}   => [Start Trading] button is NOT visible on this page!\n")
            pytest.fail("[Start Trading] button is NOT visible on this page!")
        print(f"{datetime.now()}   => [Start Trading] button is visible on this page!\n")

        print(f"{datetime.now()}   [Start Trading] button scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', self.button_start_trading[0]
        )

    @allure.step("Click button [Start Trading] on Widget 'Trading calculator'")
    def element_click(self, d):
        print(f"\n{datetime.now()}   2. Act_v0")

        print(f"{datetime.now()}   [Start Trading] button is clickable? =>")
        time_out = 5
        if not self.element_is_clickable(self.button_start_trading[0], time_out):
            print(f"{datetime.now()}   => [Start Trading] button is not clickable after {time_out} sec. Stop AT>")
            pytest.fail(f"[Start Trading] button is not clickable after {time_out} sec.")
        print(f"{datetime.now()}   => [Start Trading] button is clickable!\n")

        try:
            self.button_start_trading[0].click()
            print(f"{datetime.now()}   => [Start Trading] button clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => [Start Trading] button NOT CLICKED")

        del self.button_start_trading
        return True
