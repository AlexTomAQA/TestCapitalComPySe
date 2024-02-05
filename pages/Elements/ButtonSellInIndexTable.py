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
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from pages.Elements.AssertClass import AssertClass
# from selenium.webdriver.common.action_chains import ActionChains

COUNT_OF_RUNS = 2


class SellButtonIndexTable(BasePage):
    def __init__(self, browser, link, bid):
        self.button_show_all_locator = None
        self.button_show_all = None

        self.tab_locator = None
        self.current_tab = None

        self.button_locator = None
        self.button = None

        self.item_locator = None
        super().__init__(browser, link, bid)

    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link, cur_tab):
        self.arrange_(d, cur_item_link, cur_tab)
        self.element_click(d, cur_item_link, cur_language, cur_role, cur_tab)

    def arrange_(self, d, cur_item_link, cur_tab):
        print(f"\n{datetime.now()}   1. Arrange for Indicies finance instrument and \"{cur_tab}\" tab")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        if cur_tab == 'most_traded':
            self.tab_locator = ButtonsOnPageLocators.TAB_TRADING_ITEM_MOST_TRADED
            self.button_locator = ButtonsOnPageLocators.BUTTON_TRADING_SELL_MOST_TRADED
            self.item_locator = ButtonsOnPageLocators.SPAN_TRADING_ITEM_MOST_TRADED
            self.button_show_all_locator = ButtonsOnPageLocators.BUTTON_TRADING_SHOW_ALL_TAB_MOSTTRADED
        elif cur_tab == 'top_risers':
            self.tab_locator = ButtonsOnPageLocators.TAB_TRADING_ITEM_TOP_RISERS
            self.button_locator = ButtonsOnPageLocators.BUTTON_TRADING_SELL_TOP_RISERS
            self.item_locator = ButtonsOnPageLocators.SPAN_TRADING_ITEM_TOP_RISERS
            self.button_show_all_locator = ButtonsOnPageLocators.BUTTON_TRADING_SHOW_ALL_TAB_RISERS
        elif cur_tab == 'top_fallers':
            self.tab_locator = ButtonsOnPageLocators.TAB_TRADING_ITEM_TOP_FALLERS
            self.button_locator = ButtonsOnPageLocators.BUTTON_TRADING_SELL_TOP_FALLERS
            self.item_locator = ButtonsOnPageLocators.SPAN_TRADING_ITEM_TOP_FALLERS
            self.button_show_all_locator = ButtonsOnPageLocators.BUTTON_TRADING_SHOW_ALL_TAB_FAILERS
        elif cur_tab == 'most_volatile':
            self.tab_locator = ButtonsOnPageLocators.TAB_TRADING_ITEM_MOST_VOLATILE
            self.button_locator = ButtonsOnPageLocators.BUTTON_TRADING_SELL_MOST_VOLATILE
            self.item_locator = ButtonsOnPageLocators.SPAN_TRADING_ITEM_MOST_VOLATILE
            self.button_show_all_locator = ButtonsOnPageLocators.BUTTON_TRADING_SHOW_ALL_TAB_VOLATILE
        else:
            print(f"Unknown cur_tab={cur_tab} parameter.")

        print(f"{datetime.now()} TAB {cur_tab} IN_TABLES is visible? =>")

        try:
            self.driver.find_element(*self.tab_locator)
            print(f"{datetime.now()} TAB {cur_tab} IN_TABLES is visible!")
        except NoSuchElementException:
            print(f"{datetime.now()}   => TAB {cur_tab} IN_TABLES is not visible on the page!")
            pytest.skip("Checking element is not on this page")

    @allure.step("Click button BUTTON_TRADING_SELL_IN_TABLES")
    def element_click(self, d, cur_item_link, cur_language, cur_role, cur_tab):
        global COUNT_OF_RUNS

        if self.driver.find_elements(*self.button_locator):

            print(f"{datetime.now()}   Start Click button TAB {cur_tab} IN_TABLES")
            self.current_tab = self.driver.find_element(*self.tab_locator)
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                self.current_tab
            )
            self.current_tab.click()

            print(f"\n{datetime.now()}   2. Act_v0 for \"{cur_tab}\" tab")
            print(f"{datetime.now()}   Start Click button BUTTON_TRADING_SELL_IN_TABLES =>")

            button_list = self.driver.find_elements(*self.button_locator)
            qty_buttons = len(button_list)
            count_of_runs = COUNT_OF_RUNS if qty_buttons >= COUNT_OF_RUNS else qty_buttons
            item_list = random.sample(range(qty_buttons), count_of_runs)
            for i in item_list:
                print(f"{datetime.now()}   Start Click button TAB {cur_tab} IN_TABLES in cycle 'for'")
                self.current_tab = self.driver.find_element(*self.tab_locator)
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    self.current_tab
                )
                self.current_tab.click()
                self.click_button_2(i, cur_item_link, cur_language, cur_role)

        else:
            print(f"{datetime.now()}   => BUTTON_TRADING_SELL_IN_TABLES is not present on the page!")
            pytest.skip("Checking element is not present on this page")

    def click_button_2(self, i, cur_item_link, cur_language, cur_role):
        print(f"{datetime.now()} Start click_button_2")
        self.button_show_all = self.driver.find_element(*self.button_show_all_locator)
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.button_show_all
        )
        self.button_show_all.click()

        button_list = self.driver.find_elements(*self.button_locator)
        button = button_list[i]

        try:
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button
            )
            print(f"{datetime.now()}   => BUTTON_TRADING_SELL_IN_TABLES is visible on the page!")
        except NoSuchElementException:
            print(f"{datetime.now()}   => BUTTON_TRADING_SELL_IN_TABLES is not visible on the page!")
            pytest.fail("Problem. Checking element is not on this page now")

        # Вытаскиваем линку из кнопки
        button_link = button.get_attribute('href')
        # Берём ID итема, на который кликаем для сравнения с открытым ID на платформе
        trade_instrument = button_link[button_link.find("spotlight") + 10:button_link.find("?")]

        print(f"{datetime.now()}   BUTTON_TRADING_SELL with item {trade_instrument} click =>")

        button.click()
        print(f"{datetime.now()}   => BUTTON_TRADING_SELL clicked!")
        test_element = AssertClass(self.driver, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(self.driver, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(self.driver, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(
                    self.driver, cur_item_link, False, True, trade_instrument)
        self.driver.get(cur_item_link)
        del button, button_list, self.button_show_all
        return True
