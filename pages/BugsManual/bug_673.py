"""
-*- coding: utf-8 -*-
@Time    : 2025/02/02 18:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BUG_673(BasePage):

    LEARN_MORE_ABOUT_CRYPTOCURRENCY_TRADING_LINK = (By.XPATH, "//a[contains(@href, 'cryptocurrency-trading')]")
    EXPECTED_PAGE = 'https://capital.com/ar-ae/learn/market-guides/what-is-cryptocurrency-trading'

    def __init__(self, driver, link, bid):
        super().__init__(driver, link, bid)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)

    @allure.step(f"{datetime.now()}   Click on [Try demo] button")
    def click_learn_more_about_cryptocurrency_trading_link(self):
        # Check presenting, visibility link
        self.find_link_scroll_check_visibility_and_clickability(
            "Learn more about cryptocurrency trading",
            self.LEARN_MORE_ABOUT_CRYPTOCURRENCY_TRADING_LINK)
        # click link
        print(f"{datetime.now()}   Start click [Learn more about cryptocurrency trading] link")
        self.driver.find_element(*self.LEARN_MORE_ABOUT_CRYPTOCURRENCY_TRADING_LINK).click()
        print(f"{datetime.now()}   End click [Learn more about cryptocurrency trading] link\n")
        Common().save_current_screenshot(self.driver,
            "After click on [Learn more about cryptocurrency trading] link")

    @allure.step(f"{datetime.now()}   Page changed successfully")
    def is_expected_page_open(self):
        print(f"{datetime.now()}   How are many opened window?")
        tabs = self.driver.window_handles
        print(f"{datetime.now()}   Opened window is: {len(tabs)}")
        if len(tabs) > 1:
            self.driver.switch_to.window(tabs[0])
            self.driver.close()
            self.driver.switch_to.window(tabs[-1])
            Common().save_current_screenshot(self.driver,
                                             "After switch on second link")
        print(f"{datetime.now()}   Start match URLs of expected and real page")

        if self.driver.current_url != self.EXPECTED_PAGE:
            msg = (f"Instead 'Expected' page opened other page. "
                   f"Expected_page is '{self.EXPECTED_PAGE}', "
                   f"current page is '{self.driver.current_url}'")
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   End match URLs of expected and real page\n")
        print(f"{datetime.now()}   URLs of expected and real page are the same\n")
