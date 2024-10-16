"""
-*- coding: utf-8 -*-
@Time    : 2024/10/14 19:00
@Author  : Kasilà
"""

from datetime import datetime
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class TextIsNotLink(BasePage):
    @allure.step(f"{datetime.now()}   1. Start testing the text.")
    def text_is_not_link(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}    Scroll down to the block 'دوات لإدارة المخاطر' (Risk-management tools)")
        risk_management_tools_block = self.driver.find_element(By.CSS_SELECTOR, 'div.grid_gMdLg__9Xp_H > div:nth-child(6)')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            risk_management_tools_block
        )

    @allure.step(f"{datetime.now()}   2. Assert")
    def assert_text(self, d):
        print(f"\n{datetime.now()}   2. Assert")
        print(f"{datetime.now()}   Check the text")

        try:
            text_being_check = self.driver.find_element(By.LINK_TEXT, 'وقف الخسائر المتحركة')
            if text_being_check:
                print(f"{datetime.now()}   The text 'وقف الخسائر المتحركة' is a link")
                Common.pytest_fail("#Bug # 55!388"
                                   "\n"
                                   "Expected result: The text 'وقف الخسائر المتحركة' is not a link"
                                   "\n"
                                   "Actual result: The text 'وقف الخسائر المتحركة' is a link")
        except NoSuchElementException:
            print(f"{datetime.now()}   The text 'وقف الخسائر المتحركة' is not a link")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
