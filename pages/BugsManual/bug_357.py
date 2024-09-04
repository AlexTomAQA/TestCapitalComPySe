"""
-*- coding: utf-8 -*-
@Time    : 2024/09/02 22:40
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from src.src import CapitalComPageSrc

WIDGET_LOCATOR = (By.CSS_SELECTOR, '.main_chart__prq68')
COMMODITIES_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[name='Commodities']")
SHARES_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[name='Shares']")

class BUG_357(BasePage):

    def __init__(self, browser, link, bid):
        self.button_locator = None

        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}   1. Start Arrange: find widget in the block 'Our spread betting markets'")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find widget in the block 'Our spread betting markets'")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting widget on the page
        print(f"{datetime.now()}   Start to check widget of the block 'Our spread betting markets' "
              f"in DOM on the page 'Spread betting'\n")
        if len(d.find_elements(*WIDGET_LOCATOR)) == 0:
            msg = (f"The page 'Spread betting' don't have widget of the block 'Our spread betting markets' in DOM")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 357 {msg}")
        print(f"{datetime.now()}   The page 'Spread betting' have widget "
              f"of the block 'Our spread betting markets' in DOM\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*WIDGET_LOCATOR)
        )

        # Check visibility widget on the page
        print(f"{datetime.now()}   Start to check visibility widget of the block 'Our spread betting markets' "
              f"on the page 'Spread betting'\n")
        if not self.element_is_visible(WIDGET_LOCATOR):
            msg = ("Widget of the block 'Our spread betting markets' don't visible on the page 'Spread betting'")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 357 {msg}")
        print(f"{datetime.now()}   Widget of the block 'Our spread betting markets' visible "
              f"on the page 'Spread betting'\n")

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d, cur_tool):

        print(f"\n{datetime.now()}   2. Start Act. Click on the button {cur_tool}")

        match cur_tool:
            case "Commodities":
                self.button_locator = COMMODITIES_BUTTON_LOCATOR
            case "Shares":
                self.button_locator = SHARES_BUTTON_LOCATOR

        # Check presenting button on the page
        print(f"{datetime.now()}   Start check button {cur_tool} in DOM of the block 'Our spread betting markets' ")
        if len(d.find_elements(*self.button_locator)) == 0:
            msg = (f"The block 'Our spread betting markets' don't have button {cur_tool} in DOM")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 357 {msg}")
        print(f"{datetime.now()}   The block 'Our spread betting markets' have button {cur_tool} in DOM\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*self.button_locator)
        )

        # Check visibility button on the page
        print(f"{datetime.now()}   Is Button {cur_tool} of the block 'Our spread betting markets' visible "
              f"on the page 'Spread betting'?")
        if not self.element_is_visible(self.button_locator):
            msg = (f"Button {cur_tool} don't visible in the block 'Our spread betting markets'")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 357 {msg}")
        print(f"{datetime.now()}   Button {cur_tool} of the block 'Our spread betting markets' is visible "
              f"on the page 'Spread betting'\n")

        # Check clickable button on the page
        print(f"{datetime.now()}   Is button {cur_tool} of the block 'Our spread betting markets' clickable "
              f"on the page 'Spread betting'")
        if not self.element_is_clickable(self.button_locator):
            msg = (f"Button {cur_tool} don't clickable in the block 'Our spread betting markets'")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 357 {msg}")
        print(f"{datetime.now()}   Button {cur_tool} of the block 'Our spread betting markets' is clickable "
              f"on the page 'Spread betting'\n")

        d.find_element(*self.button_locator).click()
        print(f"\n{datetime.now()}   Button {cur_tool} clicked\n")

    @allure.step(f"{datetime.now()}   3. Start Assert. Find widget in the block 'Our spread betting markets'")
    def assert_(self, d, cur_tool):
        print(f"{datetime.now()}   3. Start Assert. Find widget in the block 'Our spread betting markets'")

        # Check presenting widget on the page
        print(f"{datetime.now()}   Do the page 'Spread betting' have widget "
              f"of the block 'Our spread betting markets' in DOM?")
        if len(d.find_elements(*WIDGET_LOCATOR)) == 0:
            msg = (f"The page 'Spread betting' don't have widget of the block 'Our spread betting markets' in DOM "
                   f"when button {cur_tool} clicked")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 357 {msg}")
        print(f"{datetime.now()}   The page 'Spread betting' have widget "
              f"of the block 'Our spread betting markets' in DOM when button {cur_tool} clicked")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*WIDGET_LOCATOR)
        )

        # Check visibility widget on the page
        print(f"{datetime.now()}   Is Widget of the block 'Our spread betting markets' visible "
              f"on the page 'Spread betting'?")
        if not self.element_is_visible(WIDGET_LOCATOR):
            msg = (f"Widget of the block 'Our spread betting markets' don't visible on the page 'Spread betting' "
                   f"when button {cur_tool} clicked")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 357 {msg}")
        print(f"{datetime.now()}   Widget of the block 'Our spread betting markets' is visible "
              f"on the page 'Spread betting' when button {cur_tool} clicked")
        Common.save_current_screenshot(d, f"Widget of the block 'Our spread betting markets' is visible.")
        self.driver.get(CapitalComPageSrc.URL_NEW)
        return True
