"""
-*- coding: utf-8 -*-
@Time    : 2024/12/20 23:30
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from pages.Menu.New import from_trading_menu_open_demo

SLIDER_BLOCK_LOCATOR = (By.CSS_SELECTOR, "[data-type='slider_block']")


class BUG_621(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find 'Risk-management tools' block, "
                 f"find link [Trailing stop loss].")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find 'Risk-management tools' block.")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d, cur_language, cur_country, link):
        print(f"{datetime.now()}   2. Start Act.")
        # Click link

        page_menu = from_trading_menu_open_demo.MenuNewDemo(d, self.link)
        page_menu.from_trading_menu_open_demo(d, cur_language, cur_country, link)

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d, link):

        print(f"{datetime.now()}   3. Start Assert.")
        current_y_before = self.driver.execute_script("return window.scrollY;")
        # Check presenting, visibility block
        self.find_block_scroll_and_check_visibility("slider_block",
                                                    SLIDER_BLOCK_LOCATOR)
        Common().save_current_screenshot(d, "After scrolling on slider_block")
        current_y_after = self.driver.execute_script("return window.scrollY;")

        if current_y_before == current_y_after:
            msg = f"Scrolling functionality is not availabled"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   Scrolling functionality is availabled")

        return True
