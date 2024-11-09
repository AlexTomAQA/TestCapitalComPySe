"""
-*- coding: utf-8 -*-
@Time    : 2024/11/09 18:20
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common

BLOCK_DEDICATED_HELP_LOCATOR = (By.XPATH,
                    "//h3[@class='heading_h3__nTE01 heading_noMargins__P5e_q'] [contains(text(), '24/7')]")
LINK_SUPPORT_LOCATOR = (By.XPATH,
                    "(//div[@class='box_box__5Jmfa box_mdLg__ppwI5 lg4 dark'])[1] //a")

NAME_OF_BLOCK = "Dedicated help, 24/7"

SEARCH_FIELD_LOCATOR = (By.CSS_SELECTOR, "[data-type='markets_list_search']")
SEARCH_FIELD_NAME = "Search field"
SEARCHING_TEXT = "CHF"
CHF_JPY_LOCATOR = (
    By.XPATH, "//strong[@class='helpers_stringEllipsed__ylDvq'][contains(text(), 'CHF/JPY')]"
)
INDICES_LOCATOR = (By.XPATH, "//a[@class='link-tool']")
MESSAGE_404_LOCATOR = (By.XPATH, '//p[text()="404"]')
EXPECTED_PAGE = 'https://capital.com/en-gb/markets/indices'

class BUG_455(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find search field, "
                 f"write 'CHF', "
                 f"Click link [CHF/JPY], "
                 f"find link [indices]. ")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find block search field. ")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting, visibility block 'For learner traders'
        self.find_block_scroll_and_check_visibility(SEARCH_FIELD_NAME, SEARCH_FIELD_LOCATOR)

        # Click on search field
        search_field = self.driver.find_element(*SEARCH_FIELD_LOCATOR)
        search_field.click()
        print(f"{datetime.now()}   '{SEARCH_FIELD_NAME}' is clicked\n")

        if not self.element_is_clickable(CHF_JPY_LOCATOR):
            msg = f"Link 'CHF/JPY' don't clickable."
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"{msg}")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*CHF_JPY_LOCATOR)
        )
        self.driver.find_element(CHF_JPY_LOCATOR).click()

        self.find_link_scroll_check_visibility_and_clickability('indices', INDICES_LOCATOR)

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):

        Common().click_link_and_print(
            d, 'indices', INDICES_LOCATOR
        )
        Common().save_current_screenshot(d, "Opened page after click link 'indices'")

    @allure.step(f"{datetime.now()}   3. Start Assert. Opened page")
    def assert_(self, d, link):

        print(f"{datetime.now()}   3. Start Assert.")

        # Check opened page
        print(f"{datetime.now()}   Check page with '404 error' message is displayed instead 'Indices' page.")
        print(f"{datetime.now()}   IS page with '404 error' message is displayed instead 'Indices' page.? =>")
        print(f'{datetime.now()}   Current page is: {self.driver.current_url}')
        if self.driver.find_elements(*MESSAGE_404_LOCATOR):
            msg = f"Page with '404 error' message is displayed instead 'Indices' page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   Current page don't have '404 error' message.")

        print(f"{datetime.now()}   Check opened page is 'Indices' page.")
        print(f"{datetime.now()}   IS opened page 'Indices' page.? =>")
        if not self.current_page_url_contain_the(EXPECTED_PAGE):
            msg = (f"Instead 'Indices' page and page with '404 error' message opened other page. "
                   f"Expected_page is '{EXPECTED_PAGE}', "
                   f"current page is '{self.driver.current_url}'")
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)

        print(f"{datetime.now()}   => Opened expected page 'Indices'!\n")
        Common.save_current_screenshot(d, f"Opened expected page 'Indices'!")
        return True
