"""
-*- coding: utf-8 -*-
@Time    : 2024/10/06 20:00
@Author  : Kasilà
"""

from datetime import datetime
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class MenuItemPayments(BasePage):
    @allure.step(f"{datetime.now()}   Start testing Menu item [Payments and withdrawals] in the footer")
    def arrange(self, link):
        print(f"{datetime.now()}   1. Arrange")

        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        print(f"{datetime.now()}   Scroll down to the Menu in the Footer")
        footer_menu = self.driver.find_element(By.CSS_SELECTOR, 'div.grid_gMd__Cwsg7.grid_fit__9qW_j')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"})',
            footer_menu
        )


    @allure.step(f"{datetime.now()}   Assert")
    def assert_menu_items(self):
        print(f"{datetime.now()}   2.Assert")
        footer_pricing_menu = self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(4) > div.menu_secondLevel__I7YiZ')
        self.driver.execute_script("arguments[0].style.border='3px solid red'", footer_pricing_menu)
        try:
            payments_item = self.driver.find_element(
                By.CSS_SELECTOR,
                'div.menu_thirdLevel__0Wd4s > div:nth-child(3) > a[href="/en-au/./about-us/payments-and-withdrawals"]')
            if payments_item:
                print(f"{datetime.now()}   Menu item [Payments and withdrawals] is present in the footer")
                allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        except NoSuchElementException:
            print(f"{datetime.now()}   Menu item [Payments and withdrawals] is missed in the footer")
            Common.pytest_fail("# Bug 55!420"
                               "\n"
                               "Expected result: Menu item [Payments and withdrawals] is in the footer"
                               "\n"
                               "Actual result: Menu item [Payments and withdrawals] is missed in the footer")
