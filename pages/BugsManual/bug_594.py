"""
-*- coding: utf-8 -*-
@Time    : 2024/07/12
@Author  : poodchasova11
"""

import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common

BUG_NUMBER = '594'
LINK_CFD = (By.CSS_SELECTOR, "div.banner_content__l6FZ6 > div > div.grid_grid__2D3md  a")


class Bug594(BasePage):

    @allure.step(f"{datetime.now()}   Start Arrange: find and click link [CFD] ")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1.1. Start Arrange: find and click link [CFD]")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting link [CFD]
        if len(self.driver.find_elements(*LINK_CFD)) == 0:
            msg = f"The  block [Capital.com mobile apps] don't have link [CFD] in DOM"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   The  block [Capital.com mobile apps]"
              f" have link [CFD] in DOM\n")

        # Scroll to the link [CFD]
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*LINK_CFD)[0]
        )

        # Check clickable LINK_CFD
        print(f"{datetime.now()}   Start check clickable LINK_CFD\n")
        if not self.element_is_clickable(LINK_CFD):
            msg = f"LINK [CFD] don't clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   LINK [CFD] is clickable\n")

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):

        print(f"\n{datetime.now()}   2. Start Act. Click on the link [CFD]")
        self.driver.find_element(*LINK_CFD).click()
        print(f"\n{datetime.now()}   Link [CFD] is clicked\n")

    @allure.step(f"{datetime.now()}   3. Start Assert. Check [CFD trading] page is opened in EN "
                 f"language after clicking the link [CFD] ")
    def assert_(self, d):
        print(f"{datetime.now()}   3. Start Assert. Check [CFD trading] page is opened in EN"
              f"language after clicking the link [CFD] ")

        # Check presenting 'fr-fr' in url on the opened page
        print(f"{datetime.now()}   IS 'fr-fr' in url on the opened page?")

        if 'fr-fr' not in self.driver.current_url:
            msg = (f"Opened page have URL: {self.driver.current_url},"
                   f" and page opened in EN language")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        else:
            msg = f"Need to check content of opened page, url {self.driver.current_url}"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        return True
