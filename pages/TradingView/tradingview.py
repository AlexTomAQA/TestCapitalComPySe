"""
-*- coding: utf-8 -*-
@Time    : 2024/04/02 16:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from pages.base_page import BasePage
from pages.common import Common
from pages.TradingView.tradingview_locators import TradingViewSiteLocators
from test_data.tradingview_site_data import data


class TradingView(BasePage):
    @allure.step("Checking that the TradingView site has opened")
    def should_be_tradingview_page(self, d):
        """Check if the page is open"""
        print(f"{datetime.now()}   Checking that the TradingView page has opened")
        if self.check_current_page_is_v2(data["SITE_URL"]):
            print(f"{datetime.now()}   TradingView page has opened")
            self.should_be_page_title_v3(data["PAGE_TITLE"])
            self.should_be_tradingview_site_app_title(data["APP_TITLE"])
            return True
        else:
            print(f"{datetime.now()}   TradingView site not opened")
            return False

    @allure.step("Checking that the TradingView site has expected app title")
    def should_be_tradingview_site_app_title(self, expected_app_title):
        """Check the app on the page has expected app title"""
        print(f"{datetime.now()}   Checking that the TradingView site has expected app title")
        current_app_title = self.get_text(0, *TradingViewSiteLocators.APP_TITLE)
        print(f"{datetime.now()}   => The app title of current page is '{current_app_title}'")

        # Check that the app title of current page meets the requirements
        Common().assert_true_false(
            expected_app_title in current_app_title,
            f"{datetime.now()}   Expected title '{expected_app_title}' "
            f"but got '{current_app_title}' on page: {self.driver.current_url}"
        )
