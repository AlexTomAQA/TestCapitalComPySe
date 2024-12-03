"""
-*- coding: utf-8 -*-
@Time    : 2024/27/10 06:00
@Author  : poodchasova11
"""
import time

import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common

BUG_NUMBER = '408'
LINK_MARGIN_TRADIN_LOCATOR = (By.CSS_SELECTOR, "a[data-type='benefits_block_block_دليل_التداول_بالهامش_btn']")
HEADER_ACCORDION_LOCATOR = (By.CSS_SELECTOR, "div > details:nth-child(3) > summary")
LINK_SILVER_CFD_LOCATOR = (By.XPATH, "//a[contains(text(),'عقود الفروقات على الفضة')]")


class Bug408(BasePage):

    @allure.step(f"{datetime.now()}   Start Arrange: find and click link [Margin trading guide] "
                 f"find and click link [silver CFDs]")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1.1. Start Arrange: find and click link [Margin trading guide]")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        print(f"{datetime.now()}   Start check clickable link [Margin trading guide]\n")
        if not self.element_is_clickable(LINK_MARGIN_TRADIN_LOCATOR):
            msg = f"Link [Margin trading guide] don't clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Link [Margin trading guide] is clickable\n")

        print(f'{datetime.now()}   Start to click on link [Margin trading guide]')
        self.driver.find_element(*LINK_MARGIN_TRADIN_LOCATOR).click()
        print(f'{datetime.now()}   End to click link [Margin trading guide]')

        print(f"\n{datetime.now()}   1.2. Start Arrange: find and click header of accordion [What is the margin...]")
        # Check presenting the header of accordion
        if len(self.driver.find_elements(*HEADER_ACCORDION_LOCATOR)) == 0:
            msg = f"The header of accordion [What is the margin...] not present in DOM"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   The header of accordion [What is the margin...] present in DOM\n")

        # Scroll to the header of accordion [What is the margin...]
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*HEADER_ACCORDION_LOCATOR)[0]
        )

        # Check clickable header of accordion [What is the margin...]
        print(f"{datetime.now()}   Start to check clickable header of accordion [What is the margin...]\n")
        if not self.element_is_clickable(HEADER_ACCORDION_LOCATOR):
            msg = f"The header of accordion [What is the margin...] don't clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   The header of accordion [What is the margin...] is clickable\n")

        print(f"{datetime.now()}   Start to click header of accordion [What is the margin...]")
        self.driver.find_element(*HEADER_ACCORDION_LOCATOR).click()
        print(f"{datetime.now()}   End to click the header of accordion [What is the margin...]")
        time.sleep(1)

        print(f"\n{datetime.now()}   1.3. Start Arrange: find and click link [silver CFDs]")

        # Check presenting link [silver CFDs]
        if len(self.driver.find_elements(*LINK_SILVER_CFD_LOCATOR)) == 0:
            msg = f"The header of accordion [What is the margin...] don't have link [silver CFDs] in DOM"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   The header of accordion [What is the margin...]"
              f" have link [silver CFDs] in DOM\n")

        # Scroll to the link [silver CFDs]
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*LINK_SILVER_CFD_LOCATOR)[0]
        )

        # Check clickable LINK_SILVER_CFD_LOCATOR
        print(f"{datetime.now()}   Start to check clickable LINK_SILVER_CFD_LOCATOR\n")
        if not self.element_is_clickable(LINK_SILVER_CFD_LOCATOR):
            msg = f"LINK_SILVER_CFD_LOCATOR don't clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   LINK_SILVER_CFD_LOCATOR is clickable\n")

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):

        print(f"\n{datetime.now()}   2. Start Act. Click on the link [silver CFDs]")
        self.driver.find_element(*LINK_SILVER_CFD_LOCATOR).click()
        print(f"\n{datetime.now()}   Link [silver CFDs] is clicked\n")

    @allure.step(f"{datetime.now()}   3. Start Assert. Check [Silver Spot] page is opened in EN "
                 f"language after clicking the link [silver CFDs] on the opened page")
    def assert_(self, d):
        print(f"{datetime.now()}   3. Start Assert. Check [Silver Spot] page is opened in EN"
              f"language after clicking the link [silver CFDs] on the opened page")

        # Check presenting 'ar-ae' in url on the opened page
        print(f"{datetime.now()}   IS 'ar-ae' in url on the opened page?")

        if 'ar-ae' not in self.driver.current_url:
            msg = (f"Opened page have URL: {self.driver.current_url},"
                   f" and page opened in EN language")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        else:
            msg = f"Need to check content of opened page, url {self.driver.current_url}"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        return True
