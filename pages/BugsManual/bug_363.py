"""
-*- coding: utf-8 -*-
@Time    : 2024/10/11
@Author  : podchasova11
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from selenium.webdriver.common.action_chains import ActionChains

LINK_COUNTRY_FOOTER_LOCATOR = (
    By.CSS_SELECTOR, 'div:nth-child(1) > span.localization_btn__9zIyt.js-analyticsClick')
FIELD_COUNTRY_IN_REGIONAL_SETTINGS = (
    By.CSS_SELECTOR, 'div.modal_overlay__f_YlZ div:nth-child(1) > div > div.select_field__SLoS0')
SEARCH_COUNTRY_LOCATOR = (By.CSS_SELECTOR, '#search-country')  # class="search_wrap__lj8qW"
HONK_KONG_LOCATOR = (By.CSS_SELECTOR, 'button[data-type="nav_country_hong_kong"]')
HONK_KONG_TAIWAN_LOCATOR = (By.CSS_SELECTOR, '[data-type="nav_country_honk_kong_&_taiwan"]')


class Bug363(BasePage):

    def __init__(self, browser, link, bid):
        self.button_locator = None

        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}   1. Start Arrange: open dropdown [Regional settings]")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: open dropdown [Regional settings]")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting link country to open dropdown [Regional settings]
        print(f"{datetime.now()}   Start to check link country to open dropdown [Regional settings] "
              f"in DOM on the Main page\n")
        if len(d.find_elements(*LINK_COUNTRY_FOOTER_LOCATOR)) == 0:
            msg = "The main page don't have link country to open dropdown in DOM"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 363 {msg}")
        print(f"{datetime.now()}   The main page have link country to open dropdown in DOM\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*LINK_COUNTRY_FOOTER_LOCATOR)
        )

        d.find_element(*LINK_COUNTRY_FOOTER_LOCATOR).click()
        print(f"\n{datetime.now()}   Link country to open dropdown [Regional settings] clicked\n")

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def check_present_honk_kong_taiwan_locator(self, d):

        print(f"\n{datetime.now()}   2. Start Act. Select 'Search' input field and enter value 'Honk'")

        # Check field country in Regional settings
        print(f"{datetime.now()}   Start check field country in Regional settings")
        if len(d.find_elements(*FIELD_COUNTRY_IN_REGIONAL_SETTINGS)) == 0:
            msg = f"Field country in Regional settings isn't in DOM"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 363 {msg}")
        print(f"{datetime.now()}   Field country in Regional settings is in DOM\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*FIELD_COUNTRY_IN_REGIONAL_SETTINGS)
        )

        ActionChains(self.driver) \
            .click(d.find_element(*FIELD_COUNTRY_IN_REGIONAL_SETTINGS)) \
            .pause(1) \
            .click(d.find_element(*SEARCH_COUNTRY_LOCATOR)) \
            .pause(1) \
            .send_keys("Hon") \
            .pause(1) \
            .perform()

    @allure.step(f"{datetime.now()}   3. Start Assert. Start to check presenting HONK_KONG_TAIWAN_LOCATOR in DOM")
    def assert_(self, d, cur_language, cur_country):
        print(f"{datetime.now()}   3. Start Assert. Start to check presenting HONK_KONG_TAIWAN_LOCATOR in DOM")

        # Check presenting HONK_KONG_TAIWAN_LOCATOR in DOM
        print(f"{datetime.now()}   Start to check presenting HONK_KONG_TAIWAN_LOCATOR in DOM")
        elements = self.driver.find_elements(*HONK_KONG_TAIWAN_LOCATOR)
        if len(elements) == 0:
            msg = "The page don't have HONK_KONG_TAIWAN_LOCATOR in DOM"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 363 {msg}")
            Common.save_current_screenshot(d, f"Field don't have HONK_KONG_TAIWAN_LOCATOR in DOM")
        print(f"{datetime.now()}   HONK_KONG_TAIWAN_LOCATOR present in DOM\n")
        return True
