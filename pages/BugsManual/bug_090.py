"""
-*- coding: utf-8 -*-
@Time    : 2024/07/10 11:00
@Author  : podchasova11
"""

from datetime import datetime

import time
import allure
from selenium.webdriver.common.by import By

from pages.Elements.AssertClass import AssertClass
from pages.base_page import BasePage
from pages.common import Common
from src.src import DemoTradingAccount
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# "div.wrap > main > section.gridRTab.gLg > div > a.btn.btn"


CREATE_A_RISK_FREE_DEMO_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "div.wrap > main div > a[data-type='content_img_7_btn']")


class CreateARiskFreeDemoAccountButton(BasePage):

    global CREATE_A_RISK_FREE_DEMO_ACCOUNT_BUTTON

    def __init__(self, browser, link, bid):
        super().__init__(browser, link, bid)

    def full_test(self, d, cur_role, link):
        self.arrange(d)
        self.element_click()
    #   self.assert()

        print(f"\n{datetime.now()}   3. Start Assert_v0 ")
        test_element = AssertClass(d, self.bid)
        match cur_role:
            case "Auth":
                test_element.assert_trading_platform_demo_v1(d, link)

    @allure.step(f"{datetime.now()}  1. Start Arrange_v0 ")
    def arrange(self, link):
        print(f"\n{datetime.now()}   1. Start Arrange_v0 ")

        if not self.current_page_is(link):
            self.link = DemoTradingAccount.URL
            self.open_page()
            time.sleep(3)

        print(f"{datetime.now()}   Is CREATE_A_RISK_FREE_DEMO_ACCOUNT_BUTTON present on the page? =>")
        button = self.driver.find_elements(*CREATE_A_RISK_FREE_DEMO_ACCOUNT_BUTTON)
        if len(button) == 0:
            print(f"{datetime.now()}   => CREATE_A_RISK_FREE_DEMO_ACCOUNT_BUTTON is not present on the page")
            Common().pytest_fail("CREATE_A_RISK_FREE_DEMO_ACCOUNT_BUTTON is not present on the page")
        print(f"{datetime.now()}   => CREATE_A_RISK_FREE_DEMO_ACCOUNT_BUTTON is present on the page")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button[0]
        )

        print(f"{datetime.now()}   Is CREATE_A_RISK_FREE_DEMO_ACCOUNT_BUTTON clickable?  =>")
        time_out = 3
        if not self.element_is_clickable(button[0], time_out):
            print(f"{datetime.now()}   => CREATE_A_RISK_FREE_DEMO_ACCOUNT_BUTTON is not clickable after {time_out} sec")
            Common.pytest_fail("Bug ? CREATE_A_RISK_FREE_DEMO_ACCOUNT_BUTTON is not clickable")
        print(f"{datetime.now()}   => CREATE_A_RISK_FREE_DEMO_ACCOUNT_BUTTON is clickable")

    @allure.step(f"{datetime.now()}  2. Start Act_v0 ")
    def element_click(self):
        print(f"{datetime.now()}   2. Start Act_v0 ")
        print(f"{datetime.now()}   Start to click CREATE_A_RISK_FREE_DEMO_ACCOUNT_BUTTON =>")

        button = self.driver.find_elements(*CREATE_A_RISK_FREE_DEMO_ACCOUNT_BUTTON)
        button[0].click()

        WebDriverWait(self.driver, 10).until(
            EC.url_changes(self.driver.current_url)
        )

        print(f"{datetime.now()}   => CREATE_A_RISK_FREE_DEMO_ACCOUNT_BUTTON is clicked")




