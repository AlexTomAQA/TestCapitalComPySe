"""
-*- coding: utf-8 -*-
@Time    : 2024/09/17 22:20
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from src.src import CapitalComPageSrc

LINK_LOCATOR = (By.CSS_SELECTOR, '[data-type="tiles_w_img_link4_signup"]')
LINK_NAME = '"Discover what you can trade"'

MESSAGE_404_LOCATOR = (By.XPATH, "//p[@class='textCenter title404'][contains(text(), '404')]")

class BUG_370(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find link '{LINK_NAME}'")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find link '{LINK_NAME}'")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting link on the page
        if len(d.find_elements(*LINK_LOCATOR)) == 0:
            msg = (f"The page 'Why Capital.com?' don't have link {LINK_NAME} in DOM")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 370 {msg}")
        print(f"{datetime.now()}   The page 'Why Capital.com?' have link {LINK_NAME} in DOM\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*LINK_LOCATOR)
        )

        # Check visibility link on the page
        print(f"{datetime.now()}   Start to check visibility link {LINK_NAME} on the page 'Why Capital.com?'\n")
        if not self.element_is_visible(LINK_LOCATOR):
            msg = f"Link {LINK_NAME} don't visible on the page 'Why Capital.com?'"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 370 {msg}")
        print(f"{datetime.now()}   Link {LINK_NAME} visible on the page 'Why Capital.com?'\n")

        # Check clickability link on the page
        print(f"{datetime.now()}   Start to check clickability link {LINK_NAME} on the page 'Why Capital.com?'\n")
        if not self.element_is_clickable(LINK_LOCATOR):
            msg = f"Link {LINK_NAME} don't clickable on the page 'Why Capital.com?'"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 370 {msg}")
        print(f"{datetime.now()}   Link {LINK_NAME} clickable on the page 'Why Capital.com?'\n")

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):

        print(f"\n{datetime.now()}   2. Start Act. Click on the link {LINK_NAME}")

        d.find_element(*LINK_LOCATOR).click()
        print(f"\n{datetime.now()}   Link {LINK_NAME} is clicked\n")

    @allure.step(f"{datetime.now()}   3. Start Assert. Check message '404 not found' on the opened page")
    def assert_(self, d):
        print(f"{datetime.now()}   3. Start Assert. Check message '404 not found' on the opened page")

        # Check presenting message '404 not found' on the opened page
        print(f"{datetime.now()}   IS message '404 not found' on the opened page?")
        if len(d.find_elements(*MESSAGE_404_LOCATOR)) != 0:
            print(f"{datetime.now()}   Opened page have message '404 not found' in the DOM")

            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                self.driver.find_element(*MESSAGE_404_LOCATOR)
            )

            # Check visibility message '404 not found' on the opened page
            print(f"{datetime.now()}   IS message '404 not found' on the opened page?")
            if self.element_is_visible(MESSAGE_404_LOCATOR):
                print('========1111========')
                msg = (f"Message '404 not found' is visible on the opened page")
                print(f"{datetime.now()}   => {msg}")
                Common().pytest_fail(f"Bug # 370 {msg}")

        print(f"{datetime.now()}   Opened page don't have message '404 not found', but need to check content of page.")
        Common.save_current_screenshot(d, f"Opened page don't have message '404 not found'")
        self.driver.get(CapitalComPageSrc.URL_NEW_EN_AU)
        return True
