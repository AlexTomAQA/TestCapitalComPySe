"""
-*- coding: utf-8 -*-
@Time    : 2025/01/30 19:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BUG_668(BasePage):

    TRY_DEMO_BUTTON = (By.CSS_SELECTOR, "[data-type='homepage_hero_banner_btn2_demo']")

    def __init__(self, driver, link, bid):
        super().__init__(driver, link, bid)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)

    @allure.step(f"{datetime.now()}   Click on [Try demo] button")
    def click_try_demo_button(self):
        # Check presenting, visibility button
        self.find_link_scroll_check_visibility_and_clickability(
            "Try demo", self.TRY_DEMO_BUTTON)
        # click_button
        print(f"{datetime.now()}   Start click [Try demo] button")
        self.driver.find_element(*self.TRY_DEMO_BUTTON).click()
        print(f"{datetime.now()}   End click [Try demo] button\n")
        Common().save_current_screenshot(self.driver, "After click on [Try demo] button")

    @allure.step(f"{datetime.now()}   Page changed successfully")
    def is_page_change_successfully(self):
        print(f"{datetime.now()}   Start find [Platform] in title of page")
        self.wait.until(EC.title_contains("Platform"))
        print(f"{datetime.now()}   End find [Platform] in title of page\n")
