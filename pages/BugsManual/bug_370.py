"""
-*- coding: utf-8 -*-
@Time    : 2024/09/17 22:20
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from src.src import CapitalComPageSrc

LINK_LOCATOR = (By.CSS_SELECTOR, '[data-type="tiles_w_img_link4_signup"]')
LINK_NAME = "Discover what you can trade"

class BUG_370(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find link '{LINK_NAME}'")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find link '{LINK_NAME}'")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting link on the page
        if len(d.find_elements(*LINK_LOCATOR)) == 0:
            msg = (f"The page 'Why Capital.com?' don't have link {LINK_NAME} in DOM")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 370 {msg}")
        print(f"{datetime.now()}   The page 'Why Capital.com?' have link {LINK_NAME} in DOM\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*LINK_LOCATOR)
        )

        # Check visibility link on the page
        print(f"{datetime.now()}   Start to check visibility link {LINK_NAME} on the page 'Why Capital.com?'\n")
        if not self.element_is_visible(LINK_LOCATOR):
            msg = f"Link {LINK_NAME} don't visible on the page 'Why Capital.com?'"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 370 {msg}")
        print(f"{datetime.now()}   Link {LINK_NAME} visible on the page 'Why Capital.com?'\n")

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
            Common().pytest_fail(f"Bug # 370 {msg}")
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
            Common().pytest_fail(f"Bug # 370 {msg}")
        print(f"{datetime.now()}   Button {cur_tool} of the block 'Our spread betting markets' is visible "
              f"on the page 'Spread betting'\n")

        # Check clickable button on the page
        print(f"{datetime.now()}   Is button {cur_tool} of the block 'Our spread betting markets' clickable "
              f"on the page 'Spread betting'")
        if not self.element_is_clickable(self.button_locator):
            msg = (f"Button {cur_tool} don't clickable in the block 'Our spread betting markets'")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 370 {msg}")
        print(f"{datetime.now()}   Button {cur_tool} of the block 'Our spread betting markets' is clickable "
              f"on the page 'Spread betting'\n")

        d.find_element(*self.button_locator).click()
        print(f"\n{datetime.now()}   Button {cur_tool} clicked\n")

    @allure.step(f"{datetime.now()}   3. Start Assert. Find link in the block 'Our spread betting markets'")
    def assert_(self, d, cur_tool):
        print(f"{datetime.now()}   3. Start Assert. Find link in the block 'Our spread betting markets'")

        # Check presenting link on the page
        print(f"{datetime.now()}   Do the page 'Spread betting' have link "
              f"of the block 'Our spread betting markets' in DOM?")
        if len(d.find_elements(*LINK_LOCATOR)) == 0:
            msg = (f"The page 'Spread betting' don't have link of the block 'Our spread betting markets' in DOM "
                   f"when button {cur_tool} clicked")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 370 {msg}")
        print(f"{datetime.now()}   The page 'Spread betting' have link "
              f"of the block 'Our spread betting markets' in DOM when button {cur_tool} clicked")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*LINK_LOCATOR)
        )

        # Check visibility link on the page
        print(f"{datetime.now()}   Is link of the block 'Our spread betting markets' visible "
              f"on the page 'Spread betting'?")
        if not self.element_is_visible(LINK_LOCATOR):
            msg = (f"link of the block 'Our spread betting markets' don't visible on the page 'Spread betting' "
                   f"when button {cur_tool} clicked")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 370 {msg}")
        print(f"{datetime.now()}   link of the block 'Our spread betting markets' is visible "
              f"on the page 'Spread betting' when button {cur_tool} clicked")
        Common.save_current_screenshot(d, f"link of the block 'Our spread betting markets' is visible.")
        self.driver.get(CapitalComPageSrc.URL_NEW)
        return True
