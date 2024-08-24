"""
-*- coding: utf-8 -*-
@Time    : 2024/08/24 20:00
@Author  : Artem Dashkov
"""
import allure
import random
import time
from datetime import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.common import Common

MENU_NAME = "[Trading]"
SUBMENU_NAME = "menu item [Demo]"
MENU_LOCATOR = (By.CSS_SELECTOR, 'span > a[data-type="nav_id798"]')
SUBMENU_LOCATOR = (By.CSS_SELECTOR, "div.grid_grid__2D3md > a[data-type='nav_id1029']")

SIDEBAR_ITEMS_LOCATOR = (By.CSS_SELECTOR, '.side-nav > a[data-type="sidebar_deeplink"]')

class BUG_334(BasePage):

    def __init__(self, browser, link, bid):
        self.sidebar_title = None
        self.sidebar_title_after_click_sidebar_item = None
        self.sidebar_item = None
        self.number_of_random_item = None

        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}   1. Start Arrange: find all sidebar items in the sidebar 'Shares trading guide'")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find all sidebar items in the sidebar 'Shares trading guide'")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        sidebar_items = d.find_elements(*SIDEBAR_ITEMS_LOCATOR)
        self.sidebar_title = sidebar_items[0].text
        self.number_of_random_item = random.randrange(1, len(sidebar_items))
        self.sidebar_item = d.find_elements(*SIDEBAR_ITEMS_LOCATOR)[self.number_of_random_item].text

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):

        print(f"\n{datetime.now()}   2. Start Act.")
        print(f"\n{datetime.now()}   Start to click of number item: {self.number_of_random_item}")

        d.find_elements(*SIDEBAR_ITEMS_LOCATOR)[self.number_of_random_item].click()
        print(f"\n{datetime.now()}   Number item: {self.number_of_random_item} clicked")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d):
        print(f"{datetime.now()}   3. Start Assert. Find sidebar title [Shares trading guide]")

        self.sidebar_title_after_click_sidebar_item = d.find_element(*SUBMENU_LOCATOR)[0].text
        print(f"{datetime.now()}   Sidebar title after click sidebar item is: "
              f"{self.sidebar_title_after_click_sidebar_item}")

        assert self.sidebar_title == self.sidebar_title_after_click_sidebar_item
