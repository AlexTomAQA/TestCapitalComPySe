"""
-*- coding: utf-8 -*-
@Time    : 2023/07/17 07:00
@Author  : Alexander Tomelo
"""
from datetime import datetime

import pytest
import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Captcha(BasePage):

    CAPTCHA_API_KEY = "8729f4a5a40472cb058438731884ded9"
    LOCATOR = "div.g-recaptcha[data-sitekey]"

    @allure.step(f"{datetime.now()}   Start Checking Captcha")
    def fail_test_if_captcha_present_v2(self):
        captcha = self.driver.find_elements(By.CSS_SELECTOR, self.LOCATOR)
        if len(captcha) == 0:
            print(f"\n{datetime.now()}   Капчи нет. Идем дальше")
            return

        self.print_env()
        pytest.fail("reCaptcha V2")

    def fail_test_if_captcha_present_v3(self):
        captcha = self.driver.find_element(By.CSS_SELECTOR, ".spacer-bottom")
        if not captcha:
            print(f"\n{datetime.now()}   Капчи нет. Идем дальше")
            return

        captcha_page_url = self.driver.current_url
        print(f"{datetime.now()}   На странице {captcha_page_url} проявилась Captcha")
        pytest.fail("reCaptcha V3")


    def print_env(self):
        data_site_key = self.driver.find_elements(By.CSS_SELECTOR, self.LOCATOR)[0].get_property("data-sitekey")
        captcha_page_url = self.driver.current_url
        print(f"{datetime.now()}   На странице {captcha_page_url} проявилась Captcha")
        print(f"{datetime.now()}   SiteKey = {data_site_key}")
