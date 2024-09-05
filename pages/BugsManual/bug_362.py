"""
-*- coding: utf-8 -*-
@Time    : 2024/09/05 20:20
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from src.src import CapitalComPageSrc

LINK_COUNTRY_FOOTER_LOCATOR = (By.XPATH, '(//span[@class="localization_btn__9zIyt"])[1]')

DROPDOWN_REGIONAL_SETTINGS = (By.CSS_SELECTOR, '.main_chart__prq68')
COMMODITIES_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[name='Commodities']")
SHARES_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[name='Shares']")

class BUG_362(BasePage):

    def __init__(self, browser, link, bid):
        self.button_locator = None

        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}   1. Start Arrange: open dropdown [Regional settings]")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: open dropdown [Regional settings]")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting link country to open dropdown [Regional settings]
        print(f"{datetime.now()}   Start to check link country to open dropdown [Regional settings] "
              f"in DOM on the Main page\n")
        if len(d.find_elements(*LINK_COUNTRY_FOOTER_LOCATOR)) == 0:
            msg = "The main page don't have link country to open dropdown [Regional settings] in DOM"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 362 {msg}")
        print(f"{datetime.now()}   The main page have link country to open dropdown [Regional settings] in DOM\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*LINK_COUNTRY_FOOTER_LOCATOR)
        )

        # Check visibility link country to open dropdown [Regional settings]
        print(f"{datetime.now()}   Start to check visibility link country to open dropdown [Regional settings]\n")
        if not self.element_is_visible(LINK_COUNTRY_FOOTER_LOCATOR):
            msg = ("Link country to open dropdown [Regional settings] don't visible on the main page")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 362 {msg}")
        print(f"{datetime.now()}   Link country to open dropdown [Regional settings] visible "
              f"on the main page\n")

        # Check clickable link
        print(f"{datetime.now()}   Is link country to open dropdown [Regional settings] clickable?")
        if not self.element_is_clickable(LINK_COUNTRY_FOOTER_LOCATOR):
            msg = "Link country to open dropdown [Regional settings] is not clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 362 {msg}")
        print(f"{datetime.now()}   Link country to open dropdown [Regional settings] is clickable\n")

        d.find_element(*LINK_COUNTRY_FOOTER_LOCATOR).click()
        print(f"\n{datetime.now()}   Link country to open dropdown [Regional settings] clicked\n")

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d, cur_tool):

        print(f"\n{datetime.now()}   2. Start Act. Select 'Honk Kong & Taiwan' and click button [Apply]")

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
