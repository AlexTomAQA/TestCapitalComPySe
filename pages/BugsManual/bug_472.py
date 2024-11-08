"""
-*- coding: utf-8 -*-
@Time    : 2024/11/01
@Author  : podchasova11
"""
from datetime import datetime

import allure
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common

BUG_NUMBER = '472'
LINK_OFFICES_IN_FOUR_COUNTRY_LOCATOR = (
    By.CSS_SELECTOR, " div.path_mainContent__TIwFt  div:nth-child(8) div > span > p > a")


class Bug472(BasePage):

    @allure.step(f"{datetime.now()}   Start Arrange: find and click "
                 f" link [مكاتبنا الموزّعة على أربع قارات] ('Offices in four continents')"
                 f" in block [مكاتبنا العالمية] ('Our global offices')")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1.1. Start Arrange: find and click link [مكاتبنا الموزّعة على أربع قارات]\n"
              f"('Offices in four continents')\n")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting link on the page
        if len(self.driver.find_elements(*LINK_OFFICES_IN_FOUR_COUNTRY_LOCATOR)) == 0:
            msg = f"Link [مكاتبنا الموزّعة على أربع قارات]('Offices in four continents') don't present in DOM"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}  Link 'مكاتبنا الموزّعة على أربع قارات'('Offices in four continents') present in DOM\n")

        # Scroll to the link of the page
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*LINK_OFFICES_IN_FOUR_COUNTRY_LOCATOR)[0]
        )

        # Check clickable the link ('Offices in four continents')
        print(f"{datetime.now()}   Start to check clickable link 'مكاتبنا الموزّعة على أربع قارات'\n"
              f"('Offices in four continents')\n")
        if not self.element_is_clickable(LINK_OFFICES_IN_FOUR_COUNTRY_LOCATOR):
            msg = f"Link 'مكاتبنا الموزّعة على أربع قارات'('Offices in four continents') don't clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Link 'مكاتبنا الموزّعة على أربع قارات'('Offices in four continents') is clickable\n")

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):

        print(f"\n{datetime.now()}   2. Start Act. Click on the link 'مكاتبنا الموزّعة على أربع قارات'\n"
              f"('Offices in four continents')\n")
        self.driver.find_element(*LINK_OFFICES_IN_FOUR_COUNTRY_LOCATOR).click()
        time.sleep(1)
        print(f"\n{datetime.now()}   Link 'مكاتبنا الموزّعة على أربع قارات'\n"
              f"('Offices in four continents') is clicked\n")

    @allure.step(f"{datetime.now()}   3. Start Assert. Check message 'Access denied Error 16' on the opened page")
    def assert_(self, d):
        print(f"{datetime.now()}   3. Start Assert. Check message 'Access denied Error 16' on the opened page")

        # Check presenting 'ar-ae/about-us/our-offices' in url on the opened page
        print(f"{datetime.now()}   IS 'ar-ae/about-us/our-offices' in url on the opened page?")

        if 'ar-ae/about-us/our-offices' not in self.driver.current_url:
            msg = f"Opened page have message 'Access denied Error 16', url is: {self.driver.current_url}"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        else:
            msg = f"Need to check content of opened page, url is: {self.driver.current_url}"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        return True
