"""
-*- coding: utf-8 -*-
@Time    : 2024/11/06 13:40
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


LINK_GO_CFD_TRADING_GUIDE_LOCATOR = (By.CSS_SELECTOR,
                                     '[data-type="benefits_block_block_go_cfd_trading_guide_btn"]')
LINK_INDICES_LOCATOR = (By.CSS_SELECTOR,
                "h2 ~ p ~ p a[href='http://https://capital.com/en-gb/markets/indices']")
EXPECTED_URL_INDICES = "https://capital.com/en-gb/markets/indices"

class BUG_431(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find block 'For learner traders'. ")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find block 'For learner traders'. ")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting, visibility block 'For learner traders'
        if len(self.driver.find_elements(*BLOCK_DEDICATED_HELP_LOCATOR)) == 0:
            msg = (f"Page don't have block '{NAME_OF_BLOCK}' in DOM")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"{msg}")
        print(f"{datetime.now()}   Page have block '{NAME_OF_BLOCK}' in DOM\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*BLOCK_DEDICATED_HELP_LOCATOR)
        )
        print(f"{datetime.now()}   Scrolled to block '{NAME_OF_BLOCK}'")

        # Check visibility block on the page
        print(f"{datetime.now()}   Start to check visibility block '{NAME_OF_BLOCK}'.'")
        if not self.element_is_visible(BLOCK_DEDICATED_HELP_LOCATOR):
            msg = f"Block '{NAME_OF_BLOCK}' don't visible."
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"{msg}")
        print(f"{datetime.now()}   Block {NAME_OF_BLOCK} visible.\n")
        Common().save_current_screenshot(d, "Check visibility block 'Dedicated help' on the page")

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):

        # Start to check: is 'support' link?
        self.find_link_scroll_check_visibility_and_clickability('support', LINK_SUPPORT_LOCATOR)

        Common().click_link_and_print(
            d, 'support', LINK_SUPPORT_LOCATOR
        )
        Common().save_current_screenshot(d, "Opened page after click link 'support'")

    @allure.step(f"{datetime.now()}   3. Start Assert. Opened page")
    def assert_(self, d, link):

        current_url = d.current_url
        print(f"Link 'Support' is clickable. But need to analyze screenshot of current page: "
              f"{current_url}")
        self.driver.get(link)
        return True
