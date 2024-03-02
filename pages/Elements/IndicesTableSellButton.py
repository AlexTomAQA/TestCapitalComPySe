"""
-*- coding: utf-8 -*-
@Time    : 2024/01/30 08:00
@Author  : Artem Dashkov
"""
from datetime import datetime
import random
import pytest
import allure
# from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import ButtonsOnPageLocators
from selenium.common.exceptions import NoSuchElementException
from pages.Elements.AssertClass import AssertClass
# from selenium.webdriver.common.action_chains import ActionChains
from pages.common import Common
COUNT_OF_RUNS = 2


class SellButtonIndicesTable(BasePage):
    def __init__(self, browser, link, bid):
        self.button_show_all_locator = None
        self.button_show_all = None

        self.tab_locator = None
        self.current_tab = None

        self.button_locator = None
        self.button = None
        self.button_list = None

        self.item_locator = None
        self.trade_instrument = None
        super().__init__(browser, link, bid)

    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link, cur_tab):
        item_list = self.arrange_(d, cur_item_link, cur_tab)
        for i in item_list:
            self.element_click(i, cur_tab)
            test_element = AssertClass(self.driver, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(self.driver, cur_language, cur_item_link)
                case "NoAuth":
                    test_element.assert_login(self.driver, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(
                        self.driver, cur_item_link, False, True, self.trade_instrument)
            self.driver.get(cur_item_link)

    def arrange_(self, d, cur_item_link, cur_tab):
        global COUNT_OF_RUNS
        print(f"\n{datetime.now()}   1. Arrange for Indices finance instrument and \"{cur_tab}\" tab")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        Common().save_current_screenshot(
            d, "SCREENSHOT: 1. Arrange for Indices finance instrument")  # need remove string after catch bug

        print(f"{datetime.now()}   IS CFDs TABLE visible on the page? =>")
        try:
            self.driver.find_element(*ButtonsOnPageLocators.TABLE_CFDS)
            print(f"{datetime.now()}   => CFDs TABLE is visible on the page!\n")

            match cur_tab:
                case 'most_traded':
                    self.tab_locator = ButtonsOnPageLocators.TAB_TRADING_ITEM_MOST_TRADED
                    self.button_locator = ButtonsOnPageLocators.BUTTON_TRADING_SELL_MOST_TRADED
                    self.item_locator = ButtonsOnPageLocators.SPAN_TRADING_ITEM_MOST_TRADED
                    self.button_show_all_locator = ButtonsOnPageLocators.BUTTON_TRADING_SHOW_ALL_TAB_MOSTTRADED
                case 'top_risers':
                    self.tab_locator = ButtonsOnPageLocators.TAB_TRADING_ITEM_TOP_RISERS
                    self.button_locator = ButtonsOnPageLocators.BUTTON_TRADING_SELL_TOP_RISERS
                    self.item_locator = ButtonsOnPageLocators.SPAN_TRADING_ITEM_TOP_RISERS
                    self.button_show_all_locator = ButtonsOnPageLocators.BUTTON_TRADING_SHOW_ALL_TAB_RISERS
                case 'top_fallers':
                    self.tab_locator = ButtonsOnPageLocators.TAB_TRADING_ITEM_TOP_FALLERS
                    self.button_locator = ButtonsOnPageLocators.BUTTON_TRADING_SELL_TOP_FALLERS
                    self.item_locator = ButtonsOnPageLocators.SPAN_TRADING_ITEM_TOP_FALLERS
                    self.button_show_all_locator = ButtonsOnPageLocators.BUTTON_TRADING_SHOW_ALL_TAB_FAILERS
                case 'most_volatile':
                    self.tab_locator = ButtonsOnPageLocators.TAB_TRADING_ITEM_MOST_VOLATILE
                    self.button_locator = ButtonsOnPageLocators.BUTTON_TRADING_SELL_MOST_VOLATILE
                    self.item_locator = ButtonsOnPageLocators.SPAN_TRADING_ITEM_MOST_VOLATILE
                    self.button_show_all_locator = ButtonsOnPageLocators.BUTTON_TRADING_SHOW_ALL_TAB_VOLATILE

            print(f"{datetime.now()}   IS TAB \"{cur_tab}\" visible on the page? =>")
            if self.driver.find_element(*self.tab_locator):
                print(f"{datetime.now()}   => TAB \"{cur_tab}\" is visible on the page!\n")

                Common().save_current_screenshot(
                    d, "SCREENSHOT: TAB is visible on the page!") # need remove string after catch bug

                print(f"{datetime.now()}   Buttons [Sell] is visible and quantity buttons not zero? =>")
                if self.driver.find_elements(*self.button_locator) != 0:
                    print(f"{datetime.now()}   => Buttons [Sell] is visible and quantity buttons not zero!\n")

                    Common().save_current_screenshot(
                        d, "SCREENSHOT: Buttons [Sell] is visible and quantity buttons not zero!")  # need remove string after catch bug

                    print(f"{datetime.now()}   Start Click button TAB \"{cur_tab}\" =>")
                    self.current_tab = self.driver.find_element(*self.tab_locator)
                    self.driver.execute_script(
                        'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                        self.current_tab
                    )
                    Common().save_current_screenshot(
                        d, "SCREENSHOT: After navigate on TAB")  # need remove string after catch bug

                    self.current_tab.click()
                    print(f"{datetime.now()}   => End Click button TAB \"{cur_tab}\"\n")

                    print(f"{datetime.now()}   Start Click button [Show all] on the TAB \"{cur_tab}\" =>")
                    self.button_show_all = self.driver.find_element(*self.button_show_all_locator)
                    self.driver.execute_script(
                        'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                        self.button_show_all
                    )
                    self.button_show_all.click()
                    print(f"{datetime.now()}   => End Click button [Show all] on the TAB \"{cur_tab}\"\n")

                    print(f"{datetime.now()}   Start find two random buttons [Sell] on the TAB \"{cur_tab}\"=>")
                    self.button_list = self.driver.find_elements(*self.button_locator)
                    qty_buttons = len(self.button_list)
                    count_of_runs = COUNT_OF_RUNS if qty_buttons >= COUNT_OF_RUNS else qty_buttons
                    item_list = random.sample(range(qty_buttons), count_of_runs)
                    print(f"{datetime.now()}   => End find two random buttons [Sell] on the TAB \"{cur_tab}\"\n")

                    return item_list

                else:
                    print(f"{datetime.now()}   => Buttons [Sell] is NOT visible or quantity buttons zero!\n")
                    pytest.skip("Checking element is not on this page")

            else:
                print(f"{datetime.now()}   => TAB \"{cur_tab}\" is NOT visible on the page!\n")
                pytest.skip("Checking element is not on this page")

        except NoSuchElementException:
            print(f"{datetime.now()}   => CFDs TABLE is NOT visible on the page!\n")
            pytest.skip("Checking element is not on this page")

    @allure.step("Click button BUTTON_TRADING_SELL_IN_TABLES")
    def element_click(self, i, cur_tab):
        print(f"{datetime.now()}   2. Act for Indices finance instrument and \"{cur_tab}\" tab")

        self.current_tab = self.driver.find_element(*self.tab_locator)
        if self.current_tab.get_attribute("class") != "main__tab--item active":
            print(f"{datetime.now()}   Start Click button TAB \"{cur_tab}\" in METHOD: element_click =>")
            self.current_tab = self.driver.find_element(*self.tab_locator)
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                self.current_tab
            )
            self.current_tab.click()
            print(f"{datetime.now()}   => End Click button TAB \"{cur_tab}\" in METHOD: element_click\n")

        self.button_show_all = self.driver.find_element(*self.button_show_all_locator)
        if self.button_show_all.is_displayed():
            print(f"{datetime.now()}   Start Click button [Show all] on the TAB \"{cur_tab}\" in METHOD: element_click =>")
            self.button_show_all = self.driver.find_element(*self.button_show_all_locator)
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                self.button_show_all
            )
            self.button_show_all.click()
            print(f"{datetime.now()}   Start Click button [Show all] on the TAB \"{cur_tab}\" in METHOD: element_click =>")

        print(f"{datetime.now()}   Start click button [Sell] =>")
        self.button_list = self.driver.find_elements(*self.button_locator)
        button = self.button_list[i]
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button
        )

        # Вытаскиваем линку из кнопки
        button_link = button.get_attribute('href')
        # Берём ID item, на который кликаем для сравнения с открытым ID на платформе
        self.trade_instrument = button_link[button_link.find("spotlight") + 10:button_link.find("?")]

        button.click()
        print(f"{datetime.now()}   => BUTTON_TRADING_SELL with item {self.trade_instrument} clicked!\n")
        # del button, self.button_list, self.button_show_all
