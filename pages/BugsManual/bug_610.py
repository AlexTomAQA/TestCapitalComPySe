"""
-*- coding: utf-8 -*-
@Time    : 2024/12/01 08:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common

LINK_RISK_MANAGEMENT_LOCATOR = (
    By.XPATH, "//div[@class='wrap_wrap__S_v0r white helpers_section__H1_eK'] //a[contains(text(), 'risk-management')]")
VULNERABILITY_NAME_OF_BLOCK = "Vulnerability: what to be aware of?"
VULNERABILITY_BLOCK_LOCATOR = (By.CSS_SELECTOR, "h1[data-id='part_0']")

class BUG_610(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find block 'Vulnerability: what to be aware of?'. ")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find block 'Vulnerability: what to be aware of?'. ")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.find_block_scroll_and_check_visibility(VULNERABILITY_NAME_OF_BLOCK, VULNERABILITY_BLOCK_LOCATOR)

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):

        # Start to check: is 'risk-management' link?
        self.find_link_scroll_check_visibility_and_clickability('risk-management', LINK_RISK_MANAGEMENT_LOCATOR)

        Common().click_link_and_print(
            d, 'risk-management', LINK_RISK_MANAGEMENT_LOCATOR
        )
        Common().save_current_screenshot(d, "Opened page after click link 'risk-management'")

    @allure.step(f"{datetime.now()}   3. Start Assert. Opened page")
    def assert_(self, d, link):

        current_url = d.current_url
        print(f"Link 'risk-management' is clickable. But need to analyze screenshot of current page: "
              f"{current_url}")
        self.driver.get(link)
        return True
