"""
-*- coding: utf-8 -*-
@Time    : 2024/12/16 21:30
@Author  : Kasilà
"""


from datetime import datetime
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.Menu.New import from_trading_menu_open_fraud_awareness
from pages.base_page import BasePage
from pages.common import Common


class FraudAwarenessPage(BasePage):
    @allure.step(f"{datetime.now()}   Start testing page display")
    def fraud_awareness_page(self, d, cur_language, cur_country, cur_item_link):
        print(f"{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Select Menu item [Fraud prevention] in the Menu section [Trading]")
        menu = from_trading_menu_open_fraud_awareness.MenuNew(d, cur_item_link)
        menu.from_trading_menu_open_fraud_awareness(d, cur_language, cur_country, cur_item_link)

    @allure.step(f"{datetime.now()}   Assert")
    def assert_(self):
        print(f"{datetime.now()}   3.Assert")
        current_page = self.driver.current_url
        print(f"{datetime.now()}   Current page is '{current_page}")

        try:
            spinner = self.driver.find_element(By.CSS_SELECTOR, '.pageLoader_loader__QsVJC')
            self.element_is_visible((By.CSS_SELECTOR, '.pageLoader_loader__QsVJC'), 2)
            self.driver.execute_script("arguments[0].style.border='3px solid red'", spinner)
            print(f"{datetime.now()}   Spinner is visible")
            Common.pytest_fail("# Bug # 55!622"
                               "\n"
                               "Expected result: Loading spinner is not displayed"
                               "\n"
                               "Actual result: Loading spinner is displayed" )
        except NoSuchElementException:
            print(f"{datetime.now()}   Spinner is not visible")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
