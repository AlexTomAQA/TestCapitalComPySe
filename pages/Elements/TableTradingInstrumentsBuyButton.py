from datetime import datetime
import random
import pytest
import allure
from pages.base_page import BasePage
from pages.Signup_login.signup_login import SignupLogin
from pages.Elements.testing_elements_locators import (TableTradingInstrumentsLocators, FieldDropdownMarketsLocator,
                                                      ItemSortDropdownLocators)
from pages.Elements.AssertClass import AssertClass
from selenium.common.exceptions import ElementClickInterceptedException

COUNT_OF_RUNS = 2


class TableTradingInstrumentsBuyButton(BasePage):
    def __init__(self, browser, link, bid):

        self.item_sort = None
        self.sort_locator = None
        self.current_sort = None

        self.buy_locator = None
        self.buy_list = None

        self.item = None
        self.trade_instrument = None

        super().__init__(browser, link, bid)

    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link, cur_sort):
        item_list = self.arrange_(d, cur_item_link, cur_sort)
        for i in item_list:
            self.element_click(i, cur_sort)
            test_element = AssertClass(self.driver, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(
                        self.driver, cur_item_link, False,  True, self.trade_instrument)
            self.driver.get(cur_item_link)

    def arrange_(self, d, cur_item_link, cur_sort):
        global COUNT_OF_RUNS
        print(f"\n{datetime.now()}   1. Arrange for Trading instrument and \"{cur_sort}\" cur_sort")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   IS TABLE_TRADING_INSTRUMENTS  visible on the page? =>")
        if self.driver.find_elements(*TableTradingInstrumentsLocators.TABLE_TRADING_INSTRUMENTS):
            print(f"{datetime.now()}   => TABLE_TRADING_INSTRUMENTS is visible on the page!")
        else:
            print(f"{datetime.now()}   => TABLE_TRADING_INSTRUMENTS is NOT visible on the page!\n")
            pytest.skip("Checking element is not on this page")

        print(f"{datetime.now()}   IS FIELD_DROPDOWN_MARKETS present in the Live prices table? =>")
        if self.driver.find_elements(*FieldDropdownMarketsLocator.FIELD_DROPDOWN_MARKETS):
            print(f"{datetime.now()}   =>  FIELD_DROPDOWN_MARKETS is present in the Live prices table!")

            print(f"{datetime.now()}   Start click FIELD_DROPDOWN_MARKETS =>")
            field_dropdown = self.driver.find_elements(*FieldDropdownMarketsLocator.FIELD_DROPDOWN_MARKETS)
            print(f"{datetime.now()}   FIELD_DROPDOWN_MARKETS scroll =>")
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                field_dropdown[0]
            )
            field_dropdown[0].click()
            print(f"{datetime.now()}   => scrolled to FIELD_DROPDOWN_MARKETS and clicked it")
        else:
            print(f"{datetime.now()} => FIELD_DROPDOWN_MARKETS is not present in Live table!")
            pytest.fail("Bug # ? Checking element is not on this page")

        match cur_sort:
            case 'most_traded':
                self.item_sort = ItemSortDropdownLocators.ITEM_DROPDOWN_SORT_MOST_TRADED   # элемент списка
                self.sort_locator = FieldDropdownMarketsLocator.FIELD_DROPDOWN_MOST_TRADED  # элемент сортировки
                self.buy_locator = TableTradingInstrumentsLocators.BUTTON_BUY_TRADING_INSTRUMENT  # кнопка buy
                self.item = TableTradingInstrumentsLocators.ITEM_TRADING_INSTRUMENT    # трейдинговый инструмент

            case 'top_risers':
                self.item_sort = ItemSortDropdownLocators.ITEM_DROPDOWN_SORT_TOP_RISERS
                self.sort_locator = FieldDropdownMarketsLocator.FIELD_DROPDOWN_TOP_RISERS
                self.buy_locator = TableTradingInstrumentsLocators.BUTTON_BUY_TRADING_INSTRUMENT
                self.item = TableTradingInstrumentsLocators.ITEM_TRADING_INSTRUMENT

            case 'top_fallers':
                self.item_sort = ItemSortDropdownLocators.ITEM_DROPDOWN_SORT_TOP_FALLERS
                self.sort_locator = FieldDropdownMarketsLocator.FIELD_DROPDOWN_TOP_FALLERS
                self.buy_locator = TableTradingInstrumentsLocators.BUTTON_BUY_TRADING_INSTRUMENT
                self.item = TableTradingInstrumentsLocators.ITEM_TRADING_INSTRUMENT

            case 'most_volatile':
                self.item_sort = ItemSortDropdownLocators.ITEM_DROPDOWN_SORT_MOST_VOLATILE
                self.sort_locator = FieldDropdownMarketsLocator.FIELD_DROPDOWN_MOST_VOLATILE
                self.buy_locator = TableTradingInstrumentsLocators.BUTTON_BUY_TRADING_INSTRUMENT
                self.item = TableTradingInstrumentsLocators.ITEM_TRADING_INSTRUMENT

        print(f"{datetime.now()}   Is item_sort_list present on the FIELD_DROPDOWN_MARKETS ? =>")
        item_sort_list = self.driver.find_elements(*ItemSortDropdownLocators.ALL_ITEM_DROPDOWN_SORT)
        if item_sort_list != 0:
            print(f"{datetime.now()}   => item_sort_list is present on the FIELD_DROPDOWN_MARKETS!")
            item_sort_list = self.driver.find_elements(*ItemSortDropdownLocators.ALL_ITEM_DROPDOWN_SORT)
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', item_sort_list[0]
            )

            print(f"{datetime.now()}   Is cur_sort \"{cur_sort}\" present in item_sort_list? =>")
            if self.driver.find_element(*self.item_sort):
                print(f"{datetime.now()}   => cur_sort \"{cur_sort}\" is present in item_sort_list!")
                print(f"{datetime.now()}   Start click cur_sort \"{cur_sort}\" =>")
                self.current_sort = self.driver.find_element(*self.item_sort)
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    self.current_sort
                    )
                self.current_sort.click()
                print(f"{datetime.now()}   => End Click cur_sort \"{cur_sort}\"\n")

                print(f"{datetime.now()}   Buttons [Buy] is visible and quantity buttons not zero? =>")
                if self.driver.find_elements(*self.buy_locator) != 0:
                    print(f"{datetime.now()}   => Buttons [Buy] is visible and quantity buttons not zero!\n")

                    print(f"{datetime.now()}   Start find two random buttons [Buy] on cur_sort \"{cur_sort}\"=>")
                    self.buy_list = self.driver.find_elements(*self.buy_locator)
                    qty_buttons = len(self.buy_list)
                    count_of_runs = COUNT_OF_RUNS if qty_buttons >= COUNT_OF_RUNS else qty_buttons
                    item_list = random.sample(range(qty_buttons), count_of_runs)
                    print(f"{datetime.now()}   => End find two random buttons [Buy] on the cur_sort "
                          f"\"{cur_sort}\"\n")

                    return item_list

                else:
                    print(f"{datetime.now()}   => Buttons [Buy] is NOT visible or quantity buttons zero!\n")
                    pytest.skip("Checking element is not on this page")

            else:
                print(f"{datetime.now()}   => cur_sort \"{cur_sort}\" not present in item_sort_list?")

        else:
            print(f"{datetime.now()} => item_sort_list not present on the FIELD_DROPDOWN_MARKETS!")
            pytest.fail("Bug # ? Checking element is not on this page")

#        del field_dropdown
#        del item_sort_list

    @allure.step("Click button Buy")
    def element_click(self, i, cur_sort):
        print(f"{datetime.now()}   2. Act for trading instrument and \"{cur_sort}\" cur_sort")

        print(f"{datetime.now()}   Start click button [Buy] =>")
        self.buy_list = self.driver.find_elements(*self.buy_locator)
        button = self.buy_list[i]
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button
        )

        # Вытаскиваем линк из кнопки
        button_link = button.get_attribute('data-href')
        # Берём ID item, на который кликаем для сравнения с открытым ID на платформе
        self.trade_instrument = button_link[button_link.find("spotlight") + 10:button_link.find("?")]

        try:
            button.click()
            print(f"{datetime.now()}   =>   BUTTON_BUY with item {self.trade_instrument} clicked!\n")
        except ElementClickInterceptedException:
            print(
                f"{datetime.now()} =>   BUTTON_BUY not clicked")
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

            button.click()
            del page_

        del button
        return True
