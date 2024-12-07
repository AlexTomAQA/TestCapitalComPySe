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
from src.src import CapitalComPageSrc

LINK_RISK_MANAGEMENT_LOCATOR = (
    By.XPATH, "//div[@class='wrap_wrap__S_v0r white helpers_section__H1_eK'] //a[contains(text(), 'risk-management')]")
VULNERABILITY_NAME_OF_BLOCK = "Vulnerability: what to be aware of?"
VULNERABILITY_BLOCK_LOCATOR = (By.CSS_SELECTOR, "h1[data-id='part_0']")

STILL_LOOKING_FOR_HELP_BLOCK_LOCATOR = (By.XPATH, "(//div[@class='wrap_wrap__S_v0r white helpers_section__H1_eK'])[2]")
LINKS_DICT_LOCATOR = {
    "+97145768641": (By.XPATH, "//p[contains(text(), '97145768614')]"),
    "support@capital.com": (By.XPATH, "//p[contains(text(), 'support@capital.com')]")
}


class BUG_610(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find block 'Still looking for help? Get in touch'.")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find block 'Still looking for help? Get in touch'.")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.find_block_scroll_and_check_visibility("Still looking for help? Get in touch",
                                                    STILL_LOOKING_FOR_HELP_BLOCK_LOCATOR)

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d, name_link_for_check):

        # Start to check: is link?
        self.find_link_scroll_check_visibility_and_clickability(name_link_for_check,
                                                                LINKS_DICT_LOCATOR[name_link_for_check])

        Common().click_link_and_print(
            d, name_link_for_check, LINKS_DICT_LOCATOR[name_link_for_check]
        )
        Common().save_current_screenshot(d, f"Opened page after click link: '{name_link_for_check}'")

    @allure.step(f"{datetime.now()}   3. Start Assert. Opened page")
    def assert_(self, d, link, name_link_for_check):

        current_url = self.driver.current_url
        if current_url == link:
            msg = f"Link '{name_link_for_check}' is not active."
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"{msg}")
        print(f"Link '{name_link_for_check}' is clickable. But need to analyze screenshot of current page: "
              f"{current_url}")
        self.driver.get(CapitalComPageSrc.URL_NEW_AR_AE)
        return True
