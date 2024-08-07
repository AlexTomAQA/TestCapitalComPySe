"""
-*- coding: utf-8 -*-
@Time    : 2024/07/03 20:30
@Author  : Kasilà
"""

from datetime import datetime
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class Sidebar(BasePage):
    def __init__(self, browser, link, bid):
        self.item_sidebar = None
        super().__init__(browser, link, bid)

    def sidebar_en(self, d, cur_item_link, sidebar_item):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        sidebar = self.driver.find_element(By.CSS_SELECTOR, "div.side-nav")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            sidebar
        )

        match sidebar_item:
            case 'Crypto vs stocks: What’s the difference?':
                self.item_sidebar = self.driver.find_element(By.CSS_SELECTOR, "a[href*='stocks-vs-crypto']")
                if self.item_sidebar:
                    self.item_sidebar.click()
                else:
                    print(f"{datetime.now()}   The {sidebar_item} is missing from the sidebar")
                    Common.pytest_skip("The item is missing from the sidebar")

    def sidebar_en_de_zh(self, d, cur_item_link, sidebar_item):

        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll to the sidebar")
        sidebar = self.driver.find_element(By.CSS_SELECTOR, "div.side-nav")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            sidebar
        )

        print(f"{datetime.now()}   Click the item")
        match sidebar_item:
            case 'Bitcoin Gold':
                self.item_sidebar = self.driver.find_element(By.CSS_SELECTOR, "a[href*='trade-bitcoingold']")
                if self.item_sidebar:
                    self.item_sidebar.click()
                    print(f"{datetime.now()}   The item '{sidebar_item}' is clicked")
                else:
                    print(f"{datetime.now()}   The {sidebar_item} is missing from the sidebar")
                    Common.pytest_skip("The item is missing from the sidebar")


    def sidebar_ru_es_it_pl(self, d, cur_item_link, sidebar_item):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll to the sidebar")
        sidebar = self.driver.find_element(By.CSS_SELECTOR, "div.side-nav")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            sidebar
        )

        print(f"{datetime.now()}   Click the item")
        match sidebar_item:
            case 'Bitcoin Gold':
                self.item_sidebar = self.driver.find_element(By.CSS_SELECTOR, "a[href*='bitcoin-gold']")
                if self.item_sidebar:
                    self.item_sidebar.click()
                    print(f"{datetime.now()}   The item '{sidebar_item}' is clicked")
                else:
                    print(f"{datetime.now()}   The {sidebar_item} is missing from the sidebar")
                    Common.pytest_skip("The item is missing from the sidebar")

    def assert_a(self, sidebar_item):
        print(f"\n{datetime.now()}   2. Assert")
        try:
            sidebar = self.driver.find_element(By.CSS_SELECTOR, 'div.side-nav')
            print(f"{datetime.now()}   Sidebar is present on the {sidebar_item} page")
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                sidebar
            )
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        except NoSuchElementException:
            self.driver.execute_script("window.scrollBy(0, 1000);")
            print(f"{datetime.now}   Sidebar is absent on the {sidebar_item} page")
            Common.pytest_fail(f"#Bug # 55!077a "
                               f"\n"
                               f"Expected result: Sidebar 'Crypto trading guide' is on the '{sidebar_item}' page"
                               f"\n"
                               f"Actual result: Sidebar is absent on the '{sidebar_item}' page")

    def assert_b(self, sidebar_item):
        print(f"\n{datetime.now()}   2. Assert")
        try:
            sidebar = self.driver.find_element(By.CSS_SELECTOR, 'div.side-nav')
            print(f"{datetime.now()}   Sidebar is present on the {sidebar_item} page")
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                sidebar
            )
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        except NoSuchElementException:
            self.driver.execute_script("window.scrollBy(0, 1000);")
            print(f"{datetime.now()}   Sidebar is absent on the {sidebar_item} page")
            Common.pytest_fail(f"#Bug # 55!077b "
                               f"\n"
                               f"Expected result: Sidebar 'Crypto trading guide' is on the '{sidebar_item}' page"
                               f"\n"
                               f"Actual result: Sidebar is absent on the '{sidebar_item}' page")