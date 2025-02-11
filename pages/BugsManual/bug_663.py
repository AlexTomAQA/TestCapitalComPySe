"""
-*- coding: utf-8 -*-
@Time    : 2025/01/21 08:00
@Author  : Artem Dashkov
"""
import time

import allure
import pytest
import random
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
TABLE_CELL_LOCATOR = (By.CSS_SELECTOR, ".table_cell__eiJNQ.helpers_textSmMob__9JkfJ")

WHAT_IS_SHARES_TRADING_LOCATOR = (By.XPATH, "(//div[@class='grid_grid__2D3md grid_gSmMd__aZHWz'])[2]")
SHARES_TRADING_GUIDE_LINK_LOCATOR = (By.CSS_SELECTOR, "[data-type='tiles_w_img_link2_signup']")
BUY_AND_SELL_PHYSICAL_SHARES_LINK_LOCATOR = (By.CSS_SELECTOR, "a[href*='trading-vs-investing']")
MESSAGE_404_LOCATOR = (By.XPATH, "//p[@class='textCenter title404'][contains(text(), '404')]")

class BUG_663(BasePage):

    pagination = None
    text_in_cells = None

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
        print(f"{datetime.now()}   Scrolled to pagination")
        self.pagination = self.driver.find_elements(*PAGINATION_LOCATOR)

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):
        print(f"{datetime.now()}   2. Start Act.")
        inner_text_in_pagination = []
        for text_in_pagination in self.pagination:
            inner_text_in_pagination.append(text_in_pagination.get_property("innerText"))

        print(f"{datetime.now()} Get innerText in pagination: {inner_text_in_pagination}")

        # find random cells on last page
        print(f"{datetime.now()} Start to find text in last page")
        self.pagination[-2].click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("page"))
        print(f"{datetime.now()} Clicked on last page")
        Common().save_current_screenshot(d, "After click on last page'")
        table_cells_last_page = self.driver.find_elements(*TABLE_CELL_LOCATOR)
        list_of_random_cells_last_page = random.choices(table_cells_last_page, k=4) # take only 4 cells
        self.text_in_cells = []
        for value in list_of_random_cells_last_page:
            self.text_in_cells.append(value.get_property("innerText"))

        # find random cells on pre last page
        print(f"{datetime.now()} Start to find text in pre last page")
        self.pagination[-3].click()
        print(f"{datetime.now()} Clicked on pre last page")
        Common().save_current_screenshot(d, "After click on pre last page'")
        table_cells_pre_last_page = self.driver.find_elements(*TABLE_CELL_LOCATOR)
        list_of_random_cells_pre_last_page = random.choices(table_cells_pre_last_page, k=4)
        for value in list_of_random_cells_pre_last_page:
            self.text_in_cells.append(value.get_property("innerText"))

        print(f"{datetime.now()}   text_in_cells: {self.text_in_cells}")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d, link):
        if "" in self.text_in_cells:
            msg = f"Cells in trading instrument have empty value."
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   Cells in trading instrument don't have empty value, but need to check screenshot")

        return True
