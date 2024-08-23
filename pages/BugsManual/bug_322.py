"""
-*- coding: utf-8 -*-
@Time    : 2024/08/19 19:00
@Author  : Kasilà
"""

import random
from datetime import datetime
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common

class TradingInstrumentSell(BasePage):

    def __init__(self, driver, link="", bid=""):
        self.title_instrument = None
        super().__init__(driver, link, bid)

    @allure.step(f"{datetime.now()}   1. Start test that the Clicking [numeric values] in the Sell column in Menu tittle"
                 f" Markets opens the Sign-Up /Login form or page of the corresponding trading instrument on the trading"
                 f" platform.")

    def trading_instruments(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Is the Trading Instruments Table presented on the page? =>")
        trading_instruments_table = self.driver.find_element(By.CSS_SELECTOR, 'div.table_table__g1rfk')
        if not trading_instruments_table:
            print(f"{datetime.now()}   => The Trading Instruments Table is not presented on the page")
            Common.pytest_fail("Bug#??? The Trading Instruments Table is not presented on the page")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            trading_instruments_table
        )
        print(f"{datetime.now()}   => Trading Instruments Table is presented on the page")

        print(f"{datetime.now()}   Are trading instruments presented in the table? =>")
        trading_instruments_list = self.driver.find_elements(By.CSS_SELECTOR, 'div[data-type="markets_list_deep"]')
        if len(trading_instruments_list) == 0:
            print(f"{datetime.now()}   => There are no trading instruments in the table")
            Common.pytest_fail("There are no trading instruments in the table")

        print(f"{datetime.now()}   => Trading instruments are presented in the table")


    def click_button_sell(self, d):
        print(f"\n{datetime.now()}   2. Act for button 'Sell'")

        print(f"{datetime.now()}   Start clicking the random 'Sell' button")
        trading_instruments_list = self.driver.find_elements(By.CSS_SELECTOR, 'div[data-type="markets_list_deep"]')

        value = random.randint(0, len(trading_instruments_list) - 1)
        print(f"{datetime.now()}   => End find a random trading instrument in the trading_instruments_table")

        print(f"{datetime.now()}   Scroll and click random button 'Sell'")
        button_sell_list = self.driver.find_elements(By.CSS_SELECTOR, 'span.row_marketDescription__KNIql')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_sell_list[value]
        )

        self.title_instrument = button_sell_list[value].text
        button_sell_list[value].click()

        print(f"{datetime.now()}   =>   Button 'Sell' ({value}) of trading instrument '{self.title_instrument}' is clicked!")
        return self.title_instrument


class AssertTPI(BasePage):
    def assert_signup(self, d):
        print(f"\n{datetime.now()}   3. Assert")

        try:
            signup_form = self.driver.find_element(By.XPATH, '//strong/span[contains(text(), "Sign up")]')
            if signup_form:
                print(f"{datetime.now()}   Sign Up form is opened")
                allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        except NoSuchElementException:
            print(f"{datetime.now()}   Sign Up form is not opened")
            Common.pytest_fail("Bug # 55!322 "
                               "f\n"
                               "Expected result: Sign Up form is opened"
                               "f\n"
                               "Actual result: Sign Up form is not opened")

    def assert_login(self, d):
        print(f"\n{datetime.now()}   3. Assert")

        try:
            login_form = self.driver.find_element(By.XPATH, '//strong/span[contains(text(), "Login")]')
            if login_form:
                print(f"{datetime.now()}   Login form is opened")
                allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        except NoSuchElementException:
            print(f"{datetime.now()}   Login form is not opened")
            Common.pytest_fail("Bug # 55!322 "
                               "f\n"
                               "Expected result: Login form is opened"
                               "f\n"
                               "Actual result: Login form is not opened")

    def assert_tpi(self, d, title_instrument):
        print(f"\n{datetime.now()}   3. Assert")
        print(title_instrument)

        current_page = self.driver.current_url
        actual_page_title = self.driver.title
        expected_page_title = "Trading Platform | Capital.com"

        if actual_page_title != expected_page_title:
            print(f"{datetime.now()}   Trading Platform is not opened")
            Common.pytest_fail(f"Bug # 55!322  "
                               f"\n"
                               f"Expected result: Trading platform with corresponding trading instrument is opened"
                               f"\n"
                               f"Actual result: Trading platform with corresponding trading instrument is not opened "
                               f"Current page is: {current_page}")
        try:
            segment_ = self.driver.find_element(By.CSS_SELECTOR, 'segment > div > div.text')
            actual_title_instrument = segment_.text

            if actual_title_instrument != title_instrument:
                Common.pytest_fail(f"Bug # 55!322  "
                                   f"\n"
                                   f"Expected result: Trading platform with corresponding trading instrument is opened"
                                   f"\n"
                                   f"Actual result: Trading platform with corresponding trading instrument is not opened "
                                   f"Current page is: {current_page}")
            print(f"{datetime.now()}   Trading platform with corresponding trading instrument is opened")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        except NoSuchElementException:
            print(f"{datetime.now()}   The trading platform is not in chart mode")
            Common.pytest_fail(f"Bug # 55!322  "
                               f"\n"
                               f"Expected result: Trading platform with corresponding trading instrument is opened"
                               f"\n"
                               f"Actual result: Trading platform with corresponding trading instrument is not opened "
                               f"Current page is: {current_page}")
