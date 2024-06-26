"""
-*- coding: utf-8 -*-
@Time    : 2023/04/20 22:00
@Author  : Suleyman Alirzaev
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import ButtonsOnPageLocators
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from pages.Elements.AssertClass import AssertClass
# from selenium.webdriver.common.action_chains import ActionChains


class BuyButtonTable(BasePage):

    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link, cur_type_fi, cur_tab):
        self.arrange_(d, cur_item_link, cur_tab)
        self.element_click(cur_item_link, cur_language, cur_role, cur_tab)

    def arrange_(self, d, cur_item_link, tab):

        print(f"\n{datetime.now()}   1. Arrange for \"{tab}\" tab")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        if tab == 'most_traded':
            self.current_tab = ButtonsOnPageLocators.TAB_TRADING_ITEM_MOST_TRADED
            self.locator = ButtonsOnPageLocators.BUTTON_TRADING_BUY_MOST_TRADED
            self.item = ButtonsOnPageLocators.SPAN_TRADING_ITEM_MOST_TRADED
        elif tab == 'top_risers':
            self.current_tab = ButtonsOnPageLocators.TAB_TRADING_ITEM_TOP_RISERS
            self.locator = ButtonsOnPageLocators.BUTTON_TRADING_BUY_TOP_RISERS
            self.item = ButtonsOnPageLocators.SPAN_TRADING_ITEM_TOP_RISERS
        elif tab == 'top_fallers':
            self.current_tab = ButtonsOnPageLocators.TAB_TRADING_ITEM_TOP_FALLERS
            self.locator = ButtonsOnPageLocators.BUTTON_TRADING_BUY_TOP_FALLERS
            self.item = ButtonsOnPageLocators.SPAN_TRADING_ITEM_TOP_FALLERS
        elif tab == 'most_volatile':
            self.current_tab = ButtonsOnPageLocators.TAB_TRADING_ITEM_MOST_VOLATILE
            self.locator = ButtonsOnPageLocators.BUTTON_TRADING_BUY_MOST_VOLATILE
            self.item = ButtonsOnPageLocators.SPAN_TRADING_ITEM_MOST_VOLATILE
        else:
            pass

        print(f"{datetime.now()}   BUTTON_TRADING_BUY_IN_TABLES is visible? =>")
        try:
            if self.driver.find_element(*self.current_tab):
                # print("OK")
                el = self.driver.find_element(*self.current_tab)
                # self.driver.find_element(*self.current_tab).click()
                self.driver.execute_script("arguments[0].click();", el)
                # print(f"{datetime.now()} Current tab {self.current_tab} is opened")
            if self.driver.find_element(*self.locator):
                print(f"{datetime.now()}   => BUTTON_TRADING_BUY_IN_TABLES is visible on the page!")
        except NoSuchElementException:
            print(f"{datetime.now()}   => BUTTON_TRADING_BUY_IN_TABLES is not visible on the page!")
            pytest.skip("Checking element is not on this page")

    @allure.step("Click button BUTTON_TRADING_BUY_IN_TABLES")
    def element_click(self, cur_item_link, cur_language, cur_role, cur_tab):
        print(f"\n{datetime.now()}   2. Act_v0 for \"{cur_tab}\" tab")
        print(f"{datetime.now()}   Start Click button BUTTON_TRADING_BUY_IN_TABLES =>")
        button_list = self.driver.find_elements(*self.locator)
        if len(button_list) >= 1:
            self.click_button_2(len(button_list), cur_item_link, cur_language, cur_role)
        else:
            print(f"{datetime.now()}   => BUTTON_TRADING_BUY_IN_TABLES is not present on the page!")
            del button_list
            pytest.skip("Checking element is not present on this page")

    def click_button_2(self, times, cur_item_link, cur_language, cur_role):
        j = 0
        for i in range(times):
            button_list = self.driver.find_elements(*self.locator)
            item_list = self.driver.find_elements(*self.item)
            cur_tab = self.driver.find_elements(*self.current_tab)
            print()
            print(f"{datetime.now()}   BUTTON_TRADING_BUY_IN_TABLES_#{i + 1} scroll =>")
            try:
                if self.driver.find_elements(*self.current_tab):
                    # ActionChains(self.driver).move_to_element\
                    #     (self.driver.find_elements(*self.current_tab)[j]).perform()
                    self.driver.execute_script(
                        'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                        cur_tab[j]
                    )
                    cur_tab[j].click()
                    if i == 4 or i == 9 or i == 14 or i == 19:
                        j += 1
                if self.driver.find_element(*self.locator):
                    print(f"{datetime.now()}   => BUTTON_TRADING_BUY_IN_TABLES is visible on the page!")
            except NoSuchElementException:
                print(f"{datetime.now()}   => BUTTON_TRADING_BUY_IN_TABLES is not visible on the page!")
                pytest.skip("Checking element is not on this page")

            print(f"{datetime.now()}   Is BUTTON_TRADING_BUY_IN_TABLES_#{i + 1} clickable? =>")
            if self.element_is_clickable(button_list[i], 5):
                print(f"{datetime.now()}   => BUTTON_TRADING_BUY_IN_TABLES_#{i + 1} is clickable")

            # Вытаскиваем линку из кнопки
            link = button_list[i].get_attribute('href')
            # Берём ID итема, на который кликаем для сравнения с открытым ID на платформе
            trade_instrument = link[link.find("spotlight") + 10:link.find("?")]

            print(f"{datetime.now()}   BUTTON_TRADING_BUY_MOST_TRADED_#{i + 1} with item {trade_instrument} click =>")
            try:
                button_list[i].click()
                print(f"{datetime.now()}   => BUTTON_TRADING_BUY_IN_TABLES_#{i + 1} clicked!")

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

            except ElementClickInterceptedException:
                print(f"{datetime.now()}   => BUTTON_TRADING_BUY_IN_TABLES_#{i + 1} not clicked!")
                print(f"{datetime.now()}   'Signup' or 'Login' form is automatically opened, maybe")
                page_ = SignupLogin(self.driver)
                if page_.close_signup_page():
                    pass
                else:
                    page_.close_signup_page()
                del page_
            del button_list

        return True
