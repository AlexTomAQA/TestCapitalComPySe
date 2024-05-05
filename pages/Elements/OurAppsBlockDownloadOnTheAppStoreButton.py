"""
-*- coding: utf-8 -*-
@Time    : 2024/04/23 20:00
@Author  : Artem Dashkov
"""
from datetime import datetime
import allure

from pages.common import Common
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import OurAppsBlock
from selenium.common.exceptions import ElementClickInterceptedException

BUTTON_NAME = '[Download on the App Store]'
BLOCK_NAME = '"Our Apps"'
BUTTON_LOCATOR = OurAppsBlock.DOWNLOAD_ON_THE_APP_STORE_BUTTON_OUR_APPS_BLOCK
BLOCK_LOCATOR = OurAppsBlock.OUR_APPS_BLOCK


class OurAppsBlockDownloadOnTheAppStoreButton(BasePage):
    global BUTTON_NAME
    global BLOCK_NAME
    global BUTTON_LOCATOR
    global BLOCK_LOCATOR

    def __init__(self, browser, link, bid):
        self.button_create_demo_account = None

        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}   Start Full test for {BUTTON_NAME} button in {BLOCK_NAME} block")
    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)
        self.element_click(d)

        test_element = AssertClass(d, cur_item_link, self.bid)
        test_element.assert_app_store(d, cur_item_link)

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

        # Check presenting and visible button
        print(f"{datetime.now()}   IS {BUTTON_NAME} button present on this page? =>")
        self.button_create_demo_account = self.driver.find_elements(*BUTTON_LOCATOR)
        if len(self.button_create_demo_account) == 0:
            msg = f"{BUTTON_NAME} button is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} button present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*BUTTON_LOCATOR)[0]
        )

        print(f"{datetime.now()}   IS {BUTTON_NAME} button visible on this page? =>")
        if not self.element_is_visible(BUTTON_LOCATOR, 5):
            msg = f"{BUTTON_NAME} button is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} button is visible on this page!\n")

        print(f"{datetime.now()}   {BUTTON_NAME} button scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.button_create_demo_account[0]
        )

    @allure.step(f"Click button {BUTTON_NAME} on {BLOCK_NAME} block")
    def element_click(self, d):
        print(f"\n{datetime.now()}   2. Act_v0")

        print(f"{datetime.now()}   {BUTTON_NAME} button is clickable? =>")
        time_out = 5
        self.button_create_demo_account = self.driver.find_elements(*BUTTON_LOCATOR)
        if not self.element_is_clickable(self.button_create_demo_account[0], time_out):
            msg = f"{BUTTON_NAME} button is not clickable after {time_out} sec. Stop AT>"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} button is clickable!\n")

        self.driver.find_elements(*BUTTON_LOCATOR)[0].click()
        print(f"{datetime.now()}   => {BUTTON_NAME} button clicked!")

        del self.button_create_demo_account
        return True
