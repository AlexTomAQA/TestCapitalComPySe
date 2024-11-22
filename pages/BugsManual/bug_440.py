"""
-*- coding: utf-8 -*-
@Time    : 2024/11/21 19:30
@Author  : Kasilà
"""


import random
from datetime import datetime
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class LearnToTrade(BasePage):
    @allure.step(f"{datetime.now()}   Start testing that the 'Learn to trade' page is opened”")
    def learn_to_trade(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll to the 'FAQs' block")
        faqs_block = self.driver.find_element(By.CSS_SELECTOR, 'div[data-type="faq"]')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "start", inline: "center"});',
            faqs_block
        )

        print(f"{datetime.now()}   Expand title 'Can you make money day trading?'")
        can_you_make_title = self.driver.find_element(By.XPATH, '// h4[contains(text(), "هل يمكنك كسب المال من التداول اليومي؟")]')
        can_you_make_title.click()

    def element_click(self, cur_link):
        print(f"{datetime.now()}   2. Act")
        print(f"{datetime.now()}   Click on the link [learning about trading]/ [learn] in the text")

        try:
            learning_about_trading_link = self.driver.find_element(By.LINK_TEXT, 'تعلّم أساسيات التداول')
            learning_about_trading_link.click()
        except NoSuchElementException:
            learn_link = self.driver.find_element(By.LINK_TEXT, 'تعلّم')
            learn_link.click()

        self.wait_for_change_url(cur_link)

    def assert_page(self):
        print(f"{datetime.now()}   3. Assert")

        current_url = self.driver.current_url
        expected_url = 'https://capital.com/ar-ae/learn'

        if current_url != expected_url:
            print(f"{datetime.now()}   The page 'Learn to trade' is not opened")
            Common.pytest_fail(f"# Bug 55!401"
                               f"\n"
                               f"Expected result: The page 'Learn to trade' with URL '{expected_url}' is opened"
                               f"\n"
                               f"Actual result: The page with URL '{current_url}' is opened")
        else:
            print(f"{datetime.now()}   The page 'Learn to trade' is opened")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
