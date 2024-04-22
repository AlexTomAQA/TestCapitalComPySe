"""
-*- coding: utf-8 -*-
@Time    : 2024/04/20 20:00
@Author  : Artem Dashkov
"""
import random
from datetime import datetime
import allure

from pages.common import Common
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ContentBlockLocators
from selenium.common.exceptions import ElementClickInterceptedException

BUTTON_NAME = '[Trade]'
BLOCK_NAME = "Trader's Dashboard"
BUTTON_LOCATOR = ContentBlockLocators.TRADE_BUTTON_TRADERS_DASHBOARD_WIDGET
BLOCK_LOCATOR = ContentBlockLocators.TRADERS_DASHBOARD_WIDGET
NAME_OF_TRADING_INSTRUMENT_LOCATOR = ContentBlockLocators.NAME_OF_TRADING_INSTRUMENT


class TradersDashboardWidgetTradeButton(BasePage):
    global BUTTON_NAME
    global BLOCK_NAME
    global BUTTON_LOCATOR
    global BLOCK_LOCATOR
    global NAME_OF_TRADING_INSTRUMENT_LOCATOR

    def __init__(self, browser, link, bid):
        self.list_buttons = None
        self.number_of_button = None
        self.button = None
        self.trade_instrument = None

        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}   Start Full test for {BUTTON_NAME} button in {BLOCK_NAME} widget")
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
                test_element.assert_trading_platform_v4(d, cur_item_link, False, True, self.trade_instrument)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        # Check presenting and visible in widget
        print(f"{datetime.now()}   IS {BLOCK_NAME} widget present on this page? =>")
        block_trading_experience = self.driver.find_elements(*BLOCK_LOCATOR)
        if len(block_trading_experience) == 0:
            msg = f"{BLOCK_NAME} widget is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} widget present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*BLOCK_LOCATOR)[0]
        )

        print(f"{datetime.now()}   IS {BLOCK_NAME} widget visible on this page? =>")
        if not self.element_is_visible(BLOCK_LOCATOR, 5):
            msg = f"{BLOCK_NAME} widget is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} widget is visible on this page!\n")

        # Check presenting and visible button
        print(f"{datetime.now()}   IS {BUTTON_NAME} button present on this page? =>")
        self.list_buttons = self.driver.find_elements(*BUTTON_LOCATOR)
        if len(self.list_buttons) == 0:
            msg = f"{BUTTON_NAME} button is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} button present on this page!\n")

        # Define random number of test button
        self.number_of_button = random.randrange(1, len(self.list_buttons)+1)
        print(f"{datetime.now()}   Defined random number of test button, item is: {self.number_of_button} \n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*BUTTON_LOCATOR)[self.number_of_button-1]
        )

        print(f"{datetime.now()}   IS {BUTTON_NAME} button visible on this page? =>")
        if not self.element_is_visible(self.specific_locator(BUTTON_LOCATOR, self.number_of_button), 5):
            msg = f"{BUTTON_NAME} button is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} button is visible on this page!\n")

        print(f"{datetime.now()}   {BUTTON_NAME} button scroll =>")
        # self.driver.execute_script(
        #     'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
        #     self.driver.find_elements(*BUTTON_LOCATOR)[self.number_of_button]
        # )

    @allure.step(f"Click button {BUTTON_NAME} on {BLOCK_NAME} widget")
    def element_click(self, d):
        print(f"\n{datetime.now()}   2. Act_v0")

        print(f"{datetime.now()}   {BUTTON_NAME} button is clickable? =>")
        time_out = 5
        self.button = self.driver.find_elements(*BUTTON_LOCATOR)[self.number_of_button-1]
        if not self.element_is_clickable(self.button, time_out):
            msg = f"{BUTTON_NAME} button is not clickable after {time_out} sec. Stop AT>"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} button is clickable!\n")

        # Get name of instrument
        print(f"{datetime.now()}   Start get name of trading instrument =>")
        trade_instrument_list = self.driver.find_elements(*NAME_OF_TRADING_INSTRUMENT_LOCATOR)
        self.trade_instrument = trade_instrument_list[self.number_of_button-1].text
        print(f'{datetime.now()}   => Name of trading instrument: {self.trade_instrument}\n')

        try:
            self.button.click()
            print(f"{datetime.now()}   => {BUTTON_NAME} button clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => {BUTTON_NAME} button NOT CLICKED")

        del self.button
        return True
