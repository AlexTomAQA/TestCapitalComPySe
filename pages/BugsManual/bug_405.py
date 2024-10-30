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

BUG_NUMBER = '405'
LINK_PAGINATIONS_11_LOCATOR = (By.CSS_SELECTOR, " #alc > div.cardsNews_pagination__1p_3X > div > nav > a:nth-child(5)")
LINK_PAGE_BP_SHARE_LOCATOR = (By.XPATH, "//*[@id='alc']/div[1]/div[8]/div/a/b[contains(text(), 'BP share price')]")
LINK_RESEARCH_TEAM_LOCATOR = (By.XPATH, "//a[contains(text(), 'Research Team')]")
PAGE_RESEARCH_TEAM_LOCATOR = (By.XPATH, "//h1[contains(text(), 'Research Team')]")


class Bug_405(BasePage):

    @allure.step(f"{datetime.now()}   Start Arrange: find and click pagination item, "
                 f"find and click link page 'BP share price forecast...'")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1.1. Start Arrange: find and click link pagination item")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        print(f"{datetime.now()}   Start check clickable pagination item\n")
        if not self.element_is_clickable(LINK_PAGINATIONS_11_LOCATOR):
            msg = f"Link pagination item don't clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Link pagination item is clickable\n")

        print(f'{datetime.now()}   Start to click on link pagination item')
        self.driver.find_element(*LINK_PAGINATIONS_11_LOCATOR).click()
        print(f'{datetime.now()}   End to click pagination item')

        print(f"\n{datetime.now()}   1.2. Start Arrange: find and click link of the page 'BP share price forecast...'")
        # Check presenting link of the page 'BP share price forecast...'
        if len(self.driver.find_elements(*LINK_PAGE_BP_SHARE_LOCATOR)) == 0:
            msg = f"The page 'BP share price forecast...' not present in DOM"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   The page 'BP share price forecast...' present in DOM\n")

        # Scroll to the link of the page 'BP share price forecast...'
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*LINK_PAGE_BP_SHARE_LOCATOR)[0]
        )

        # Check clickable link of the page 'BP share price forecast...
        print(f"{datetime.now()}   Start to check clickable link of the page 'BP share price forecast...\n")
        if not self.element_is_clickable(LINK_PAGE_BP_SHARE_LOCATOR):
            msg = f"Link of the page 'BP share price forecast...' don't clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Link of the page 'BP share price forecast...' is clickable\n")

        print(f"{datetime.now()}   Start to click link of the page 'BP share price forecast...'")
        self.driver.find_element(*LINK_PAGE_BP_SHARE_LOCATOR).click()
        print(f"{datetime.now()}   End to click link of the page 'BP share price forecast...'")
        time.sleep(1)

        print(f"\n{datetime.now()}   1.3. Start Arrange: find and click link LINK_RESEARCH_TEAME_LOCATOR")

        # Check presenting link 'LINK_RESEARCH_TEAME_LOCATOR' on the page 'BP share price forecast...'
        if len(self.driver.find_elements(*LINK_RESEARCH_TEAM_LOCATOR)) == 0:
            msg = f"The page 'BP share price forecast...' don't have link LINK_RESEARCH_TEAME_LOCATOR in DOM"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Page 'BP share price forecast...' have link LINK_RESEARCH_TEAME_LOCATOR in DOM\n")

        # Scroll to the link LINK_RESEARCH_TEAME_LOCATOR
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*LINK_RESEARCH_TEAM_LOCATOR)[0]
        )

        # Check clickable LINK_RESEARCH_TEAME_LOCATOR
        print(f"{datetime.now()}   Start to check clickable LINK_RESEARCH_TEAME_LOCATOR\n")
        if not self.element_is_clickable(LINK_RESEARCH_TEAM_LOCATOR):
            msg = f"LINK_RESEARCH_TEAME_LOCATOR don't clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   LINK_RESEARCH_TEAME_LOCATOR is clickable\n")

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):

        print(f"\n{datetime.now()}   2. Start Act. Click on the link 'Capital.com Research Team'")
        self.driver.find_element(*LINK_RESEARCH_TEAM_LOCATOR).click()
        print(f"\n{datetime.now()}   Link 'Capital.com Research Team' is clicked\n")

    @allure.step(f"{datetime.now()}   3. Start Assert. Check message '404 not found' on the opened page")
    def assert_(self, d):
        print(f"{datetime.now()}   3. Start Assert. Check message '404 not found' on the opened page")

        # Check presenting 'analysis' in url on the opened page
        print(f"{datetime.now()}   IS 'analysis' in url on the opened page?")

        if 'analysis' not in self.driver.current_url:
            msg = f"Opened page have message '404 not found', url is: {self.driver.current_url}"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        else:
            msg = f"Need to check content of opened page, url is: {self.driver.current_url}"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        return True
