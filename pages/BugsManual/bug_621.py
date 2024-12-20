"""
-*- coding: utf-8 -*-
@Time    : 2024/12/20 23:30
@Author  : Artem Dashkov
"""
import allure
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from src.src import CapitalComPageSrc

RISK_MANAGEMENT_TOOLS_BLOCK_LOCATOR = (
    By.XPATH,
    "(//div [@class='grid_grid__2D3md grid_md__Udd_J grid_gSmLg__B_vHD grid_center__cwyYf grid_fit__9qW_j'])[6]"
)
# RISK_MANAGEMENT_TOOLS_BLOCK_LOCATOR = (
#     By.CSS_SELECTOR,
#     "[data-type='banner_in_body_block'] [class='grid_grid__2D3md grid_gMdLg__9Xp_H'] >.grid_grid__2D3md:nth-child(6)"
# )

TRAILING_STOP_LOSS_LINK_LOCATOR = (By.CSS_SELECTOR, "a[href*='capitalcysec.zendesk.com']")
HELP_CENTER_NO_LONGER_EXISTS_LOCATOR = (By.XPATH, "//h1[contains(text(), 'Oops, this help center no longer exists')]")

class BUG_621(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find 'Risk-management tools' block, "
                 f"find link [Trailing stop loss].")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find 'Risk-management tools' block.")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting, visibility block
        self.find_block_scroll_and_check_visibility("Risk-management tools",
                                                    RISK_MANAGEMENT_TOOLS_BLOCK_LOCATOR)

        # Check presenting, visibility and clickability link
        self.find_link_scroll_check_visibility_and_clickability("Trailing stop loss",
                                                                TRAILING_STOP_LOSS_LINK_LOCATOR)

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):
        print(f"{datetime.now()}   2. Start Act.")
        # Click link
        tabs_before_click = self.driver.window_handles
        Common().click_link_and_print(d, 'Trailing stop loss', TRAILING_STOP_LOSS_LINK_LOCATOR)
        tabs_after_click = self.driver.window_handles
        if len(tabs_after_click) > len(tabs_before_click):
            self.driver.switch_to.window(tabs_after_click[-1])
        time.sleep(5)
        Common().save_current_screenshot(d, "Opened page after click link 'Trailing stop loss'")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d, link):

        print(f"{datetime.now()}   3. Start Assert.")

        # Check opened page
        print(f'{datetime.now()}   Current page is: {self.driver.current_url}')
        if len(self.driver.find_elements(*HELP_CENTER_NO_LONGER_EXISTS_LOCATOR)) != 0:
            msg = f"Help center no longer exists"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   Current page don't have message 'Oops, this help center no longer exists', "
              f"need to analyze page screen.")

        self.driver.get(CapitalComPageSrc.URL_NEW_AR_AE)
        return True
