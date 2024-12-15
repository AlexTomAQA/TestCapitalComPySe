"""
-*- coding: utf-8 -*-
@Time    : 2024/12/04 19:30
@Author  : Kasilà
"""


import random
from datetime import datetime
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class PageDisplay(BasePage):
    @allure.step(f"{datetime.now()}   Start testing page display")
    def page_display(self, d, cur_item_link, cur_language):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll down to the 'What is oil trading?' tile in the 'Market trading guides' block")
        if cur_language == 'de':
            what_is_oil_tile = self.driver.find_element(By.XPATH, '//h3[contains(text(), "Was ist Öl-Trading?")]')
        elif cur_language == 'ar':
            what_is_oil_tile = self.driver.find_element(By.XPATH, '//h3[contains(text(), "ما هو التداول بالنفط؟")]')
        else:
            what_is_oil_tile = self.driver.find_element(By.XPATH, '//h3[contains(text(), "What is oil trading?")]')

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            what_is_oil_tile
        )

        print(f"{datetime.now()}   Click the link “Oil trading guide”")
        if cur_language == 'de':
            oil_trading_guide_link = self.driver.find_element(By.LINK_TEXT, 'Leitfaden zum Öl-Trading')
        elif cur_language == 'ar':
            oil_trading_guide_link = self.driver.find_element(By.LINK_TEXT, 'دليل التداول بالنفط')
        else:
            oil_trading_guide_link = self.driver.find_element(By.LINK_TEXT, 'Oil trading guide')
        oil_trading_guide_link.click()

        print(f"{datetime.now()}   Scroll down to the block “Why trade oil with Capital.com”")
        why_trade_oil_block = self.driver.find_element(By.CSS_SELECTOR, 'h2[data-id="part_8"]')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            why_trade_oil_block
        )

        print(f"{datetime.now()}   Click on the [Try Demo]/[Start oil trading] button")
        btn_list = self.driver.find_elements(By.CSS_SELECTOR, 'p > a.btn')
        random_button = random.choice(btn_list)
        random_button_text = random_button.text
        random_button.click()
        print(f"{datetime.now()}   '{random_button_text}' is clicked")

    def element_click(self):
        print(f"\n{datetime.now()}   2. Act")

        print(f"{datetime.now()}   Close the “Sign up” form")
        self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="SIGN_UP_close"]').click()

    @allure.step(f"{datetime.now()}   Assert")
    def assert_(self):
        print(f"{datetime.now()}   3.Assert")

        try:
            spinner = self.driver.find_element(By.CSS_SELECTOR, '.pageLoader_loader__QsVJC')
            self.element_is_visible((By.CSS_SELECTOR, '.pageLoader_loader__QsVJC'), 2)
            self.driver.execute_script("arguments[0].style.border='3px solid red'", spinner)
            print(f"{datetime.now()}   Spinner is visible")
            Common.pytest_fail("# Bug # 55!604"
                               "\n"
                               "Expected result: Loading spinner is not displayed"
                               "\n"
                               "Actual result: Loading spinner is displayed" )
        except NoSuchElementException:
            print(f"{datetime.now()}   Spinner is not visible")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
