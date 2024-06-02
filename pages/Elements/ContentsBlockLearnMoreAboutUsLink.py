"""
-*- coding: utf-8 -*-
@Time    : 2024/05/26 18:00
@Author  : Artem Dashkov
"""
import time
from datetime import datetime
import allure

from pages.common import Common
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ContentBlockLocators
from selenium.common.exceptions import ElementClickInterceptedException

BUTTON_NAME = '[Learn more about us]'
BLOCK_NAME = '"Contents"'
TITLE_NAME = '"Learn more about us"'
BUTTON_LOCATOR = ContentBlockLocators.LEARN_MORE_ABOUT_US_LINK_CONTENTS_BLOCK
BLOCK_LOCATOR = ContentBlockLocators.CONTENTS_BLOCK
TITLE_LEARN_MORE_ABOUT_US_LOCATOR = ContentBlockLocators.TITLE_LEARN_MORE_ABOUT_US


class ContentsBlockLearnMoreAboutUsLink(BasePage):
    global BUTTON_NAME
    global BLOCK_NAME
    global TITLE_NAME

    global BUTTON_LOCATOR
    global BLOCK_LOCATOR
    global TITLE_LEARN_MORE_ABOUT_US_LOCATOR

    def __init__(self, browser, link, bid):
        self.button = None

        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}   Start Full test for {BUTTON_NAME} link in {BLOCK_NAME} block")
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)
        self.element_click(d)

        # Check presenting Title
        print(f"\n{datetime.now()}   3. Assert")
        print(f"{datetime.now()}   IS {TITLE_NAME} title present on this page? =>")
        if len(self.driver.find_elements(*TITLE_LEARN_MORE_ABOUT_US_LOCATOR)) == 0:
            msg = f"{TITLE_NAME} title is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {TITLE_NAME} title present on this page!\n")

        # Check visible Title
        print(f"{datetime.now()}   IS {TITLE_NAME} title visible on this page? =>")
        if not self.element_is_visible(TITLE_LEARN_MORE_ABOUT_US_LOCATOR, 5):
            msg = f"{TITLE_NAME} title is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {TITLE_NAME} title is visible on this page!\n")

        # Check visibility Title on area of window
        print(f"{datetime.now()}   IS {TITLE_NAME} title visible on area of window? =>")

        title = self.driver.find_element(*TITLE_LEARN_MORE_ABOUT_US_LOCATOR)
        title_y = title.location['y'] # height coordinate of title
        time.sleep(1)
        current_y = self.driver.execute_script("return window.scrollY;") # current height coordinate
        window_height = self.driver.execute_script("return window.innerHeight;") # height inner window
        print('Height coordinate of title:', title_y)
        print('Current height coordinate:', current_y)
        print('Height inner window', window_height)

        if title_y >= current_y and title_y <= (current_y + window_height):
            print(f"{datetime.now()}   {TITLE_NAME} title IS visible on area of window. =>")
        else:
            msg = f"{TITLE_NAME} title is NOT visible on area of window!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        del title, title_y, current_y, window_height

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        # Check presenting and visible in block
        print(f"{datetime.now()}   IS {BLOCK_NAME} block present on this page? =>")
        block_trading_experience = self.driver.find_elements(*BLOCK_LOCATOR)
        if len(block_trading_experience) == 0:
            msg = f"{BLOCK_NAME} block is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} block present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*BLOCK_LOCATOR)[0]
        )

        print(f"{datetime.now()}   IS {BLOCK_NAME} block visible on this page? =>")
        if not self.element_is_visible(BLOCK_LOCATOR, 5):
            msg = f"{BLOCK_NAME} block is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} block is visible on this page!\n")

        # Check presenting and visible link
        print(f"{datetime.now()}   IS {BUTTON_NAME} link present on this page? =>")
        self.button = self.driver.find_elements(*BUTTON_LOCATOR)
        if len(self.button) == 0:
            msg = f"{BUTTON_NAME} link is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} link present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*BUTTON_LOCATOR)[0]
        )

        print(f"{datetime.now()}   IS {BUTTON_NAME} link visible on this page? =>")
        if not self.element_is_visible(BUTTON_LOCATOR, 5):
            msg = f"{BUTTON_NAME} link is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} link is visible on this page!\n")

        print(f"{datetime.now()}   {BUTTON_NAME} link scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.button[0]
        )

    @allure.step(f"Click link {BUTTON_NAME} on {BLOCK_NAME} block")
    def element_click(self, d):
        print(f"\n{datetime.now()}   2. Act_v0")

        print(f"{datetime.now()}   {BUTTON_NAME} link is clickable? =>")
        time_out = 5
        self.button = self.driver.find_elements(*BUTTON_LOCATOR)
        if not self.element_is_clickable(self.button[0], time_out):
            msg = f"{BUTTON_NAME} link is not clickable after {time_out} sec. Stop AT>"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} link is clickable!\n")

        try:
            self.button[0].click()
            print(f"{datetime.now()}   => {BUTTON_NAME} link clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => {BUTTON_NAME} link NOT CLICKED\n")

        del self.button
        return True
