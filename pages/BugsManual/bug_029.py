"""
-*- coding: utf-8 -*-
@Time    : 2024/07/05 15:29
@Author  : podchasova11
"""

from datetime import datetime

import allure

from pages.Elements.testing_elements_locators import WebTradingPlatformPageLocators
from pages.base_page import BasePage
from test_data.page_web_trading_platform_data import page_data

PAGE_WEB_TRADING_PLATFORM_URL = "https://capital.com/online-trading-platform"
PAGE_TITLE = "The Capital.com web trading platform | Capital.com"


class WebTradingPlatformPage(BasePage):

    global PAGE_WEB_TRADING_PLATFORM_URL
    global PAGE_TITLE

    # def __init__(self, browser, link, bid):
    #     self.button_platform_overview = None
    #
    #     super().__init__(browser, link, bid)

    @allure.step("Checking that the Page 'Web trading platform' opened")
    def should_be_web_trading_platform_page(self, d, current_page):
        """Check that the page web trading platform has opened"""
        print(f"{datetime.now()}   Checking that the Page 'Web trading platform' has opened =>")
        if not self.current_page_is(current_page):
            self.link = current_page
            self.open_page()
        web_platform_url = page_data["PAGE_WEB_TRADING_PLATFORM_URL"]
        if self.current_page_url_contain_the(web_platform_url):
            print(f"{datetime.now()}   => Page 'Web trading platform' has opened ")
            self.should_be_page_title_v3(page_data["PAGE_TITLE"])
            self.should_be_web_trading_platform_breadcrumbs()
        else:
            print(f"{datetime.now()}   => Page 'Web trading platform' not opened")

        assert False, ("Bug#029."
                       "Expected result:The Desktop Trading page is opened"
                       "\n"
                       "Actual result: The Home page is opened")

    @allure.step("Checking that breadcrumbs present on the Page 'Web trading platform'")
    def should_be_web_trading_platform_breadcrumbs(self, d):
        """Checking that breadcrumbs present on the Page 'Web trading platform'"""
        print(f"{datetime.now()}   Checking that breadcrumbs present on the Page 'Web trading platform' =>")
        if not self.element_is_visible(WebTradingPlatformPageLocators.BREADCRUMBS_DESKTOP_TRADING, 3):
            print(f"{datetime.now()}   => The breadcrumbs on Page 'Web trading platform' not visible")
