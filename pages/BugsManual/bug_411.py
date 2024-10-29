"""
-*- coding: utf-8 -*-
@Time    : 2024/10/27 22:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from src.src import CapitalComPageSrc

LINK_GO_CFD_TRADING_GUIDE_LOCATOR = (By.CSS_SELECTOR,
                                     '[data-type="benefits_block_block_go_cfd_trading_guide_btn"]')
LINK_INDICES_LOCATOR = (By.CSS_SELECTOR,
                "h2 ~ p ~ p a[href='http://https://capital.com/en-gb/markets/indices']")


MESSAGE_404_LOCATOR = (By.XPATH, "//p[@class='textCenter title404'][contains(text(), '404')]")
MARKETS_LOCATOR = (By.XPATH, "//div[@class='breadcrumbs_breadcrumbs__UgZeo'] //span[contains(text(), 'Markets')]")

class BUG_411(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find and click link 'Go CFD trading guide'. "
                 f"Find link 'indices'.")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find and click link 'Go CFD trading guide'. "
              f"Find link 'indices'.")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting, visibility and clickability link 'Go CFD trading guide'
        self.find_link_scroll_check_visibility_and_clickability(
            'Go CFD trading guide', LINK_GO_CFD_TRADING_GUIDE_LOCATOR
        )
        # Click link 'Go CFD trading guide'
        Common().click_link_and_print(
            d, 'Go CFD trading guide', LINK_GO_CFD_TRADING_GUIDE_LOCATOR
        )

        # Check presenting, visibility and clickability link 'indices'
        self.find_link_scroll_check_visibility_and_clickability(
             'indices', LINK_GO_CFD_TRADING_GUIDE_LOCATOR
        )


    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):

        # Click link 'indices'
        Common().click_link_and_print(
            d, 'indices', LINK_GO_CFD_TRADING_GUIDE_LOCATOR
        )

    @allure.step(f"{datetime.now()}   3. Start Assert. Opened page")
    def assert_(self, d):
        print(f"{datetime.now()}   3. Start Assert. Opened page")

        # # Check presenting message '404 not found' on the opened page
        # print(f"{datetime.now()}   IS message '404 not found' on the opened page?")
        # if len(d.find_elements(*MESSAGE_404_LOCATOR)) != 0:
        #     print(f"{datetime.now()}   Opened page have message '404 not found' in the DOM")
        #
        #     self.driver.execute_script(
        #         'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
        #         self.driver.find_element(*MESSAGE_404_LOCATOR)
        #     )
        #
        #     # Check visibility message '404 not found' on the opened page
        #     print(f"{datetime.now()}   IS message '404 not found' on the opened page?")
        #     if self.element_is_visible(MESSAGE_404_LOCATOR):
        #         msg = (f"Message '404 not found' is visible on the opened page")
        #         print(f"{datetime.now()}   => {msg}")
        #         Common().pytest_fail(f"Bug # 370 {msg}")
        #
        # print(f"{datetime.now()}   Opened page don't have message '404 not found', but need to check content of page.")
        #
        # # Check presenting 'Markets' in breadcrumbs
        # print(f"{datetime.now()}   Check that opened page is 'Markets': is 'Markets' presenting in breadcrumbs?")
        # if len(d.find_elements(*MARKETS_LOCATOR)) == 0:
        #     msg = f"Opened page don't have presenting 'Markets' in breadcrumbs in DOM"
        #     print(f"{datetime.now()}   => {msg}")
        #     Common().pytest_fail(f"Bug # 370 {msg}")
        # print(f"{datetime.now()}   The opened page have presenting 'Markets' in breadcrumbs in DOM\n")
        #
        # self.driver.execute_script(
        #     'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
        #     self.driver.find_element(*MARKETS_LOCATOR)
        #     )
        #
        # # Check visible 'Markets' in breadcrumbs
        # print(f"{datetime.now()}   Check that opened page is 'Markets': is 'Markets' visible in breadcrumbs?")
        # if not self.element_is_visible(MARKETS_LOCATOR):
        #     msg = f"Opened page don't have visible 'Markets' in breadcrumbs"
        #     print(f"{datetime.now()}   => {msg}")
        #     Common().pytest_fail(f"Bug # 370 {msg}")
        # print(f"{datetime.now()}   The opened page have visible 'Markets' in breadcrumbs\n")
        #
        # Common.save_current_screenshot(d, f"Opened page have visible 'Markets' in breadcrumbs")
        # self.driver.get(CapitalComPageSrc.URL_NEW_EN_AU)
        # return True
