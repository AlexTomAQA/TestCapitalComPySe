"""
-*- coding: utf-8 -*-
@Time    : 2025/01/21 08:00
@Author  : Artem Dashkov
"""
import time

import allure
import pytest
from datetime import datetime
from selenium.webdriver.common.by import By

from pages.BugsManual.bug_366 import TRADING_INSTRUMENT_LOC
from pages.BugsManual.bug_407 import PAGINATION_LOCATOR
from pages.base_page import BasePage
from pages.common import Common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


TRADING_INSTRUMENT_LOCATOR = (By.CSS_SELECTOR, "[data-type='markets_list']")

REGION_DROPDOWN_LOCATOR = (By.ID, "Region")
REGION_USA_LOCATOR = (By.CSS_SELECTOR, "[for='United States of America']")

SECTOR_DROPDOWN_LOCATOR = (By.ID, "Sector")
SECTOR_FINANCIALS_LOCATOR = (By.CSS_SELECTOR, "[for='Financials']")

PAGINATION_LOCATOR = (By.CSS_SELECTOR, "[data-type='markets_list_pagination']")

WHAT_IS_SHARES_TRADING_LOCATOR = (By.XPATH, "(//div[@class='grid_grid__2D3md grid_gSmMd__aZHWz'])[2]")
SHARES_TRADING_GUIDE_LINK_LOCATOR = (By.CSS_SELECTOR, "[data-type='tiles_w_img_link2_signup']")
BUY_AND_SELL_PHYSICAL_SHARES_LINK_LOCATOR = (By.CSS_SELECTOR, "a[href*='trading-vs-investing']")
MESSAGE_404_LOCATOR = (By.XPATH, "//p[@class='textCenter title404'][contains(text(), '404')]")

class BUG_663(BasePage):

    pagination = None

    @allure.step(f"{datetime.now()}   1. Start Arrange: find block 'What is share trading?', "
                 f"Click link [Shares trading guide], "
                 f"Find the link 'buy and sell physical shares'.")
    def arrange(self, d, link):
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting, visibility block
        self.find_block_scroll_and_check_visibility(
            "Trading instrument", TRADING_INSTRUMENT_LOCATOR)

        # Check Region - United States of America
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*REGION_DROPDOWN_LOCATOR)
        )
        self.driver.find_element(*REGION_DROPDOWN_LOCATOR).click()
        self.driver.find_element(*REGION_USA_LOCATOR).click()
        self.driver.find_element(*REGION_DROPDOWN_LOCATOR).click()

        # Check Sector - Financials
        self.driver.find_element(*SECTOR_DROPDOWN_LOCATOR).click()
        self.driver.find_element(*SECTOR_FINANCIALS_LOCATOR).click()
        self.driver.find_element(*SECTOR_DROPDOWN_LOCATOR).click()

        WebDriverWait(self.driver, 5).until(EC.url_contains("sectors"))

        # Find visible numbers of pages
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*PAGINATION_LOCATOR)[0]
        )
        print(f"Scroll to pagination")
        self.pagination = self.driver.find_elements(*PAGINATION_LOCATOR)


    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):
        print(f"Get innerText: {self.pagination[-2].get_property("innerText")}")
        self.pagination[-2].click
        # stop here

        print(f"{datetime.now()}   2. Start Act.")

        # click on the link 'buy and sell physical shares'
        print(f"{datetime.now()}   Start to click link 'buy and sell physical shares'")
        link = self.driver.current_url
        self.driver.find_element(*BUY_AND_SELL_PHYSICAL_SHARES_LINK_LOCATOR).click()
        WebDriverWait(self.driver, 10).until(EC.url_changes(link))
        Common().save_current_screenshot(d, "After click on link 'buy and sell physical shares'")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d, link):
        print(f"{datetime.now()}   3. Start Assert.")

        print(f"{datetime.now()}   Try to find 404 Message on the page")

        if len(self.driver.find_elements(*MESSAGE_404_LOCATOR)) != 0:
            msg = f"Current page have 404 Message. Current URL is {self.driver.current_url}."
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   Current page don't have 404 Message, but need to check screenshot")

        return True
