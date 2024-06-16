import time
from datetime import datetime

import allure
from selenium.common import ElementClickInterceptedException

from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ProductsAndServicesOurMobileApps
from pages.base_page import BasePage
from pages.common import Common

BUTTON_NAME = '[Google Play]'
BUTTON_LOCATOR = ProductsAndServicesOurMobileApps.GOOGLE_PLAY_BUTTON
GOOGLE_PLAY_LOGO = ProductsAndServicesOurMobileApps.GOOGLE_PLAY_LOGO


class GooglePlayButtonOnCFDTradingAppBlock(BasePage):
    global BUTTON_NAME
    global BUTTON_LOCATOR
    global GOOGLE_PLAY_LOGO

    def __init__(self, browser, link, bid):
        self.button_google_play = None
        self.google_play_logo = None

        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}   Start Full test for {BUTTON_NAME} button in CFD Trading App block")
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)
        self.element_click(d)

        test_element = AssertClass(d, cur_item_link, self.bid)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        # Check presenting and visible button
        print(f"{datetime.now()}   Is {BUTTON_NAME} button present on this page? =>")
        self.button_google_play = self.driver.find_elements(*BUTTON_LOCATOR)
        if len(self.button_google_play) == 0:
            msg = f"{BUTTON_NAME} button is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} button present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*BUTTON_LOCATOR)[0])

        print(f"{datetime.now()}   Is {BUTTON_NAME} button visible on this page? =>")
        if not self.element_is_visible(BUTTON_LOCATOR, 5):
            msg = f"{BUTTON_NAME} button is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} button is visible on this page!\n")

        print(f"{datetime.now()}   {BUTTON_NAME} button scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.button_google_play[0])

    @allure.step(f"Click button {BUTTON_NAME} on CFD Trading App block")
    def element_click(self, d):
        print(f"\n{datetime.now()}   2. Act_v0")

        print(f"{datetime.now()}   {BUTTON_NAME} button is clickable? =>")
        time_out = 5
        self.button_google_play = self.driver.find_elements(*BUTTON_LOCATOR)
        if not self.element_is_clickable(self.button_google_play[0], time_out):
            msg = f"{BUTTON_NAME} button is not clickable after {time_out} sec. Stop AT>"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} button is clickable!\n")

        try:
            self.button_google_play[0].click()
            print(f"{datetime.now()}   => {BUTTON_NAME} button clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => {BUTTON_NAME} button NOT CLICKED")

        time.sleep(10)
        self.google_play_logo = self.driver.find_elements(*GOOGLE_PLAY_LOGO)

        if not self.current_page_url_contain_the('google') or not self.google_play_logo:
            msg = f"Not on the Google Play page. Stop AT>"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => Google Play page is opened!\n")