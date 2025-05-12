"""
-*- coding: utf-8 -*-
@Time    : 2025/05/12 21:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from selenium.webdriver.support.ui import WebDriverWait

class BUG_697(BasePage):
    HOW_TO_START_TRADING_FOR_BEGINNERS_BLOCK = (By.XPATH, "(//summary[@data-type='faq_chevron'])[1]")
    LEARN_ABOUT_STRATEGIES_LINK = (By.XPATH, "//a[contains(text(), 'learn about strategies')]")
    MARKET_ANALYSIS_BREADCRUMB = (By.XPATH, "//div[@class='breadcrumbs_breadcrumbs__UgZeo'] //span[contains(text(), 'Market analysis')]")
    NUMBER_OF_TABS = None

    def __init__(self, driver, link, bid):
        super().__init__(driver, link, bid)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)

    @allure.step(f"{datetime.now()}   Click on [learn about strategies] link")
    def click_learn_about_strategies_link(self):

        # Check presenting, visibility block
        self.find_block_scroll_and_check_visibility(
            "How to start trading for beginners", self.HOW_TO_START_TRADING_FOR_BEGINNERS_BLOCK)

        print(f"{datetime.now()}   Start to click 'How to start trading for beginners'")
        self.driver.find_element(*self.HOW_TO_START_TRADING_FOR_BEGINNERS_BLOCK).click()
        print(f"{datetime.now()}   End to click 'How to start trading for beginners'")

        # Check presenting, visibility link
        self.find_link_scroll_check_visibility_and_clickability(
            "learn about strategies", self.LEARN_ABOUT_STRATEGIES_LINK)

        # How many tabs before click link [learn about strategies]
        tabs_before_click = self.driver.window_handles
        print(f"{datetime.now()}   Number of tabs before click link: {len(tabs_before_click)}")

        # click link
        print(f"{datetime.now()}   Start click [learn about strategies] link")
        self.driver.find_element(*self.LEARN_ABOUT_STRATEGIES_LINK).click()
        print(f"{datetime.now()}   End click [learn about strategies] link\n")

        # How many tabs after click link [learn about strategies]
        tabs_after_click = self.driver.window_handles
        print(f"{datetime.now()}   Number of tabs after click link: {len(tabs_after_click)}")

        if len(tabs_before_click) < len(tabs_after_click):
            self.driver.switch_to.window(tabs_after_click[0])   # switch to first tab
            self.driver.close()                                 # close first tab
            self.driver.switch_to.window(tabs_after_click[-1])  # switch to tab, opened after click [learn about strategies] link
            print(f"{datetime.now()}   Current number of tabs is: {len(self.driver.window_handles)}")

        Common().save_current_screenshot(self.driver,
                                         "After click on [here] link")

    @allure.step(f"{datetime.now()}   Is expected page open?")
    def is_page_with_expected_language_open(self):
        print(f"{datetime.now()}   What is language on the page?")
        print(f"{datetime.now()}   Start get the URL page.")
        page_url = self.driver.current_url
        print(f"{datetime.now()}   Current url of page is {page_url}.")
        if len(self.driver.find_elements(*self.MARKET_ANALYSIS_BREADCRUMB)) > 0:
            msg = "Current page 'Market analysis' instead page 'Trading strategies'."
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        else:
            msg = "Current page is not 'Market analysis', need to check screenshot"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
