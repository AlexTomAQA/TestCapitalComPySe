"""
-*- coding: utf-8 -*-
@Time    : 2024/04/04 19:23
@Author  : Dmitry Mudrik
"""

from datetime import datetime

import allure
import pytest

from pages.Capital.capital_locators import WidgetPromoMarket
from pages.Elements.AssertClass import AssertClass
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage


class PromoMarketTradeNowButton(BasePage):

    @allure.step("Start testing for [TradeNowButton] in widget PromoMarket on the trading instrument page")
    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):

        # Проверяем роль пользователя
        test_element = AssertClass(d, cur_item_link, self.bid)
        print(f'Trade instrument from Full test is {test_element}')

        match cur_role:
            case "NoReg" | "NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

    print(f"{datetime.now()}.   Create button list 'Trade Now' on widget 'Promo Market'.")

    def btn_list_trade_now_on_widget_promo_market(self):
        list_but = self.driver.find_elements(*WidgetPromoMarket.LIST_BUTs_TRADE_NOW_2)
        qty = len(list_but)
        print(f"This widget has {qty} different slider lines with 'Trade Now' button")
        return qty

    print(f"{datetime.now()}.   Click button 'Trade Now({{i}})' on widget 'Promo Market'.")

    def btn_click(self, i):
        # Click по кнопке "Trade now" с соотв. индексом
        button = None
        if i == 0:
            button = self.driver.find_element(*WidgetPromoMarket.BUT_1_TRADE_NOW_ACTIVE)
        elif i == 1:
            button = self.driver.find_element(*WidgetPromoMarket.BUT_2_TRADE_NOW_ACTIVE)
        elif i == 2:
            button = self.driver.find_element(*WidgetPromoMarket.BUT_3_TRADE_NOW_ACTIVE)
        elif i == 3:
            button = self.driver.find_element(*WidgetPromoMarket.BUT_4_TRADE_NOW_ACTIVE)
        if button:
            self.scroll_to_element(button)
            button.click()

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # self.driver.execute_script(
        #     'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', element)

    def arrange_(self, d, cur_role, cur_item_link):
        print(f"\n{datetime.now()} 1.Arrange_v0")
        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        qty = self.btn_list_trade_now_on_widget_promo_market()
        if qty != 0:
            for i in range(qty):
                self.btn_click(i)

                if cur_role == "NoReg":
                    page = SignupLogin(d, cur_item_link)
                    page.should_be_signup_form()
                    page.close_signup_form()
                    self.open_page()
                elif cur_role == "NoAuth":
                    pass
                elif cur_role == "Auth":
                    self.should_be_link("https://capital.com/trading/platform")
                    d.back()
        else:
            pytest.fail("Widget is not present on the current page!")
