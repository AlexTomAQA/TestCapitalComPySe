"""
-*- coding: utf-8 -*-
@Time    : 2023/04/14 11:00
@Author  : Alexander Tomelo
"""

from datetime import datetime

import allure
# from selenium import webdriver
# import pytest

from pages.Capital.Trading_platform.Topbar.topbar import TopBar
from pages.base_page import BasePage
from pages.common import Common
# from pages.common import flag_of_bug
from test_data.trading_platform_data import data as tp_data
from pages.Capital.Trading_platform.trading_platform_locators import (
    TradingPlatformSignupFormLocators as TPSignupFormLocators,
    TradingInstruments,
    MenuSideBar
)
from pages.Capital.Trading_platform.trading_platform_locators import TopBarLocators
from pages.Capital.Trading_platform.trading_platform_locators import ChartingLocators
from test_data.trading_platform_data import data
from tests.ReTestsAuto.ReTest_table_fill import retest_table_fill


class TradingPlatform(BasePage):

    @allure.step("Select Chart menu")
    def select_menu_charts(self):
        element = self.element_is_visible(MenuSideBar.MENU_CHARTS, 3)
        element.click()
        print(f"{datetime.now()}   => Charts menu of Trading platform is opened")

    @allure.step("Button 'Close all' click")
    def button_close_all_ti_click(self):
        element = self.element_is_visible(TradingInstruments.BUTTON_CLOSE_ALL, 3)
        element.click()
        print(f"{datetime.now()}   => Button Close all Trading instruments clicked")

    @allure.step("Checking that the trading platform page has opened")
    def should_be_trading_platform_page(self, d, link):
        """Check if the page is open"""
        print(f"{datetime.now()}   Checking that the trading platform page has opened")
        if self.current_page_url_contain_the(link):
            page_ = TopBar(d, link)
            if page_.trading_platform_logo_is_present():
                d.back()
                del page_
                assert True
            else:
                # d.back()
                del page_
                assert False, 'Page with title "Trading Platform | Capital.com" not loaded'
        else:
            assert False, f'Loaded page with not {link} url. Current url is {self.driver.current_url}'

    @allure.step("Checking that the trading platform page has opened - ver 2")
    def should_be_trading_platform_page_v2(self, d, test_link, demo=False):
        """Check if the trading platform page is open"""
        print(f"{datetime.now()}   Checking that the trading platform page has opened =>")
        platform_url = data["PLATFORM_DEMO_URL"] if demo else data["PLATFORM_URL/"]
        # print(platform_url)
        # print(self.wait_for_change_url(platform_url, 120))
        if self.wait_for_target_url(platform_url, 10):
            print(f"{datetime.now()}   => Opened page with {self.driver.current_url} url. Expected: {platform_url} ")
            self.should_be_page_title_v2(data["PAGE_TITLE"])
            self.should_be_platform_logo()
            self.should_be_corresponding_trading_instrument()
            self.open_page()
            assert True, 'Trading platform with title "Trading Platform | Capital.com" opened'
        else:
            print(f"{datetime.now()}   => Loaded page {self.driver.current_url} with not {platform_url} url")
            cur_url = self.driver.current_url
            self.open_page()
            assert False, f"Loaded page with {cur_url} url, but expected {platform_url}"

    @allure.step("Checking that the trading platform page has opened - ver 3")
    def should_be_trading_platform_page_v3(self, demo=False):
        """Check if the trading platform page is open"""
        print(f"{datetime.now()}   Checking that the trading platform page has opened (v3) =>")
        platform_url = data["PLATFORM_URL"]
        if self.current_page_url_contain_the(platform_url):
            print(f"{datetime.now()}   => Opened page with {self.driver.current_url} url. Expected: {platform_url} ")
            self.should_be_page_title_v2(data["PAGE_TITLE"])
            self.should_be_platform_logo()
            if demo:
                self.should_be_platform_demo_mode()
            else:
                self.should_be_platform_live_mode()
            self.open_page()
        else:
            print(f"{datetime.now()}   => Loaded page {self.driver.current_url} with not {platform_url} url")
            # self.link = self.driver.current_url
            # self.open_page()
            assert False, "Bug! The trading platform page is not opened"

    @allure.step("Checking that the trading platform page has opened - ver 4")
    def should_be_trading_platform_page_v4(self, d, test_link, tpd, tpi, trade_instrument):
        """
        Check if the trading platform page for the corresponding trade instrument is opened
        Args:
            d: Webdriver
            test_link: Link in the list of 3 random items and start page of the sidebar
            tpd: open Trade platform in Demo mode (True). Live mode (False)
            tpi: open Trade platform for corresponding trade instrument (False)
            trade_instrument: corresponding trade instrument (False)
        """
        print(f"{datetime.now()}   Checking that the trading platform page has opened (v4) =>")
        platform_url = data["PLATFORM_URL/"]
        cur_url = self.driver.current_url
        if self.wait_for_target_url(platform_url, 10):
            print(f"{datetime.now()}   Checking way # 1 => ")
            self.should_be_page_title_v2(data["PAGE_TITLE"])
            self.should_be_platform_logo()
            print(f"\n{datetime.now()}   tpd = {tpd}")
            if tpd:
                self.should_be_platform_demo_mode(d, test_link)
                print(f"{datetime.now()}   => The page with {self.driver.current_url} url was opened in DEMO mode")
            else:
                self.should_be_platform_live_mode(d, test_link)
                print(f"{datetime.now()}   => The page with {self.driver.current_url} url was opened in lIVE mode")

            if tpi:
                print(f"\n{datetime.now()}   Check that opened page with {self.driver.current_url} url\n"
                      f"with selected corresponding trading instrument '{trade_instrument}' =>")
                self.should_be_corresponding_trading_instrument(test_link, trade_instrument)

            # assert True, 'Trading platform with title "Trading Platform | Capital.com" opened'
            msg = 'Trading platform with title "Trading Platform | Capital.com" opened'
            Common.browser_back_to_link_and_test_pass(d, test_link, msg)
        else:
            print(f"{datetime.now()}   Checking way # 2 =>")
            self.should_be_page_title_v2(data["PAGE_TITLE"])
            self.should_be_platform_logo()
            print(f"{datetime.now()}   tpd = {tpd}")
            if tpd:
                print(f"{datetime.now()}   => Loaded page {self.driver.current_url} with not {platform_url} url")
                # проверка бага для ретеста

                print(f'\nBug: {self.bid}')
                retest_table_fill(d, self.bid, '09', self.link)

                # assert False, (f"Bug # 9. Loaded page with {cur_url} url, but expected the Trading platform in"
                #                f"Demo mode(timeout=15c)")
                Common.flag_of_bug = True
                msg = (f"Bug # 9. Loaded page with {cur_url} url, "
                       f"but expected the Trading platform in Demo mode (timeout=15c)")
                assert False, msg
                # Common().browser_back_to_link_and_test_fail(self.driver, test_link, msg)
            else:
                print(f"{datetime.now()}   => Loaded page {cur_url} with not {platform_url} url")
                # проверка бага для ретеста

                print(f'\nBug: {self.bid}')
                retest_table_fill(d, self.bid, '10', self.link)

                # assert False, (f"Bug # 10. Loaded page with {cur_url} url, but expected the Trading platform in"
                #                f"Live mode(timeout=15c)")
                Common.flag_of_bug = True
                msg = (f"Bug # 10. Loaded page with {cur_url} url, "
                       f"but expected the Trading platform in Live mode (timeout=15c)")
                assert False, msg
                # Common().browser_back_to_link_and_test_fail(self.driver, test_link, msg)

    @allure.step("Check if the Logo element is present on the page")
    def should_be_platform_logo(self):
        """Check that the Capital.com Logo is present"""
        """Check if the app title"""
        print(f"\n{datetime.now()}   Checking that the Trading platform LOGO is present on the page =>")
        # assert self.element_is_visible(TopBarLocators.LOGO, 30), \
        if not self.element_is_visible(TopBarLocators.LOGO, 15):
            msg = "Trading platform LOGO is not present on the page"
            Common().assert_true_false(False, msg)

        print(f"{datetime.now()}   => Trading platform 'capital*com' logo is present on the current page")

    @allure.step("Check if the trading platform opened in DEMO mode")
    def should_be_platform_demo_mode(self, d, test_link):
        """Check that Trading platform opened in Demo mode"""

        print(f"{datetime.now()}   Checking that the Trading platform opened in DEMO mode =>")
        if not self.element_is_visible(TopBarLocators.MODE_DEMO, 15):
            # проверка бага для ретеста
            print(f'\nBug: {self.bid}')
            retest_table_fill(d, self.bid, '11', self.link)
            msg = "Bug # 11. Trading platform is opened in not DEMO mode"
            Common().assert_true_false(False, msg)
            # Common().browser_back_to_link_and_test_fail(self.driver, test_link, msg)

    @allure.step("Check if the trading platform opened in LIVE mode")
    def should_be_platform_live_mode(self, d, test_link):
        """Check that Trading platform opened in Live mode"""

        print(f"{datetime.now()}   Checking that the Trading platform opened in LIVE mode =>")
        if not self.element_is_visible(TopBarLocators.MODE_LIVE, 15):
            # проверка бага для ретеста
            print(f'\nBug: {self.bid}')
            retest_table_fill(d, self.bid, '12', self.link)
            msg = "Bug # 12. Trading platform is opened in not LIVE mode"
            Common().assert_true_false(False, msg)
            # Common().browser_back_to_link_and_test_fail(self.driver, test_link, msg)

    @allure.step("Check that form [Sign Up] is opened on the Trading Platform page")
    # @profile(precision=3)
    def should_be_signup_form_on_the_trading_platform(self, d):
        """
        Check there are an elements to on 'Sign up' page on the Trading Platform
        """
        print(f"{datetime.now()}   Start method Check that [Sign up] page opened =>")

        if self.current_page_url_contain_the(tp_data["SIGNUP_URL"]):
            print(f"{datetime.now()}   'Sign up' page opened on the Trading Platform")
            print(f"{datetime.now()}   SIGNUP_FRAME =>")
            # assert self.element_is_visible(TPSignupFormLocators.SIGNUP_FRAME, 30), \
            assert self.element_is_visible(TPSignupFormLocators.SIGNUP_FRAME, 15), \
                f"{datetime.now()}   The layout of the 'SignUp' page has not visible"

            print(f"{datetime.now()}   INPUT_EMAIL =>")
            assert self.element_is_visible(TPSignupFormLocators.USERNAME), \
                f"{datetime.now()}   Problem with 'Username (email)' field"

            print(f"{datetime.now()}   INPUT_PASS =>")
            assert self.element_is_visible(TPSignupFormLocators.PASSWORD), \
                f"{datetime.now()}   Problem with 'Password' field"

            print(f"{datetime.now()}   BUTTON_CONTINUE =>")
            assert self.element_is_visible(TPSignupFormLocators.BUTTON_CONTINUE), \
                f"{datetime.now()}   Problem with 'Continue' button"
            # self.open_page()
        else:
            # self.open_page()
            print("'SignUp' page on the Trading Platform is not opened")
            assert False

    @allure.step("Check that form [Login] is opened on the Trading Platform page")
    # @profile(precision=3)
    def should_be_login_form_on_the_trading_platform(self):
        """
        Check there are an elements to on 'Log in' page on the Trading Platform
        """
        print(f"{datetime.now()}   Start method Check that [Log in] page opened on the Trading Platform =>")
        print(self.driver.current_url)
        if self.current_page_url_contain_the(tp_data["LOGIN_URL"]):
            print(f"{datetime.now()}   => 'Log in' page opened on the Trading Platform")

            print(f"{datetime.now()}   LOGIN_FRAME =>")
            # assert self.element_is_visible(TPSignupFormLocators.LOGIN_FRAME, 30), \
            assert self.element_is_visible(TPSignupFormLocators.LOGIN_FRAME, 15), \
                f"{datetime.now()}   The layout of the 'Login' page has changed"

            print(f"{datetime.now()}   INPUT_EMAIL =>")
            assert self.element_is_visible(TPSignupFormLocators.USERNAME), \
                f"{datetime.now()}   Problem with 'Username (email)' field"

            print(f"{datetime.now()}   INPUT_PASS =>")
            assert self.element_is_visible(TPSignupFormLocators.PASSWORD), \
                f"{datetime.now()}   Problem with 'Password' field"

            print(f"{datetime.now()}   BUTTON_CONTINUE =>")
            assert self.element_is_visible(TPSignupFormLocators.BUTTON_CONTINUE), \
                f"{datetime.now()}   Problem with 'Continue' button"
            self.open_page()
        elif self.current_page_url_contain_the(tp_data["SIGNUP_URL"]):
            print(f"{datetime.now()}   => 'Sign up' page opened on the Trading Platform")
            print(f"{datetime.now()}   SIGNUP_FRAME =>")
            if self.element_is_visible(TPSignupFormLocators.SIGNUP_FRAME):
                print(f"{datetime.now()}   => SIGNUP_FRAME is visible")
            else:
                print(f"{datetime.now()}   => SIGNUP_FRAME is not visible")
            print(f"{datetime.now()}   => 'Login' page on the Trading Platform is not opened")

            # new bug re-test checking =====
            print(f'\nBug: {self.bid}')
            retest_table_fill(self.driver, self.bid, '13', self.link)
            # ==============================
            assert False, "Bug # 13. 'Sign up' form opened on the Trading Platform instead of 'Login' form"
        else:
            # self.open_page()
            print(f"{datetime.now()}   => 'Login' page on the Trading Platform is not opened")
            assert False, "Problem! 'Login' page on the Trading Platform is not opened"

    @allure.step("Check the corresponding trading instrument")
    def should_be_corresponding_trading_instrument(self, test_link, trade_instrument):
        """
        Check Trading platform is opened for corresponding trade instrument
        """

        # cur_url = self.driver.current_url
        print(f"\n{datetime.now()}   trade_instrument = '{trade_instrument}'")
        # trade_instrument_name = trade_instrument.split(" ")[0]
        # print(f"{datetime.now()}   => trade_instrument_name = '{trade_instrument_name}'")

        # проверяем, что открыта трейдинговая платформа на вкладке [Charts]
        print(f"\n{datetime.now()}   Check that Trading Platform is opened in Chart mode")
        menu_chart = self.elements_are_present(*ChartingLocators.MENU_CHART)
        if len(menu_chart) == 0:
            print(f"{datetime.now()}   => Trading Platform opened, but not Chart mode")
            print(f'\nBug: {self.bid}')
            retest_table_fill(self.driver, self.bid, '14', self.link)
            msg = "Bug # 14. Trading platform opened, but not Chart mode"
            Common().assert_true_false(False, msg)
        print(f"{datetime.now()}   => Trading Platform opened in Chart mode")

        # определяем, какие вкладки открыты и избегаем ошибки пустого списка
        print(f"\n{datetime.now()}   "
              f"Check that Top Charts List of Trading Platform not empty =>")
        top_chart_trade_list = self.elements_are_located(TradingInstruments.LIST_TRADE_INSTRUMENTS, 3)
        if len(top_chart_trade_list) == 0:
            print(f"{datetime.now()}   => Trading Platform opened in Chart mode, but Top Charts List is empty")
            print(f'\nBug: {self.bid}')
            retest_table_fill(self.driver, self.bid, '15', self.link)
            msg = ("Bug # 15. Trading platform was opened, "
                   "but does no contain any trade instrument in the Top Charts List")
            Common().assert_true_false(False, msg)
            # Common().browser_back_to_link_and_test_fail(self.driver, test_link, msg)

        # проверяем, есть ли в списке вкладка запрашиваемого торгового инструмента
        print(f"\n{datetime.now()}   Check that Top Charts List contain selected trade instrument =>")
        print(f"\n{datetime.now()}   Top Charts List contain {len(top_chart_trade_list)} trade instruments")
        print(f"\n{datetime.now()}   Top Charts List contain following trade instruments:")
        present = False
        for element in top_chart_trade_list:
            # print(f"'{element.text}'", " ", "")
            print(f"'{element.text}'")
            if trade_instrument in element.text:
                print(f"{datetime.now()}   => Trade instrument '{trade_instrument}' is present in the Top Charts List")
                present = True
                break

        if not present:
            # new bug re-test checking =====
            print(f'\nBug: {self.bid}')
            retest_table_fill(self.driver, self.bid, '16', self.link)
            msg = f"Bug # 16. Trade instrument '{trade_instrument}' is not present in the Top Charts List"
            Common().assert_true_false(False, msg)

        print(f"{datetime.now()}   => Trade instrument '{trade_instrument}' is present in the Top Charts List")

        # проверяем, что есть выбранный торговый инструмент и он отображен (виден) в списке инструментов
        selected_trade_instrument = self.element_is_visible(TradingInstruments.SELECTED_TRADE_INSTRUMENT)
        if not selected_trade_instrument:
            # new bug re-test checking =====
            print(f'\nBug: {self.bid}')
            retest_table_fill(self.driver, self.bid, '17', self.link)
            msg = (f"Bug # 17. SeTrade instrument '{trade_instrument}' is the Top Charts List, "
                   f"but not visible and not selected")
            Common().assert_true_false(False, msg)
            # Common().browser_back_to_link_and_test_fail(self.driver, test_link, msg)
        print(f"{datetime.now()}   => The Top Charts List contain selected and visible Trade instrument"
              f"visible")

        # проверяем, что запрашиваемый торговый инструмент выбран
        if trade_instrument not in selected_trade_instrument.text:
            # new bug re-test checking =====
            print(f"{datetime.now()}   => Trade instrument '{trade_instrument}' is present in the Top Charts "
                  f"List, visible, but not selected")
            print(f'\nBug: {self.bid}')
            retest_table_fill(self.driver, self.bid, '18', self.link)
            msg = (f"Bug # 18. Trade instrument '{trade_instrument}' is on the Top Charts List, visible, "
                   f"but Not selected")
            Common().assert_true_false(False, msg)
            # Common().browser_back_to_link_and_test_fail(self.driver, test_link, msg)

        print(f"{datetime.now()}   => Trade instrument '{trade_instrument}' is present in the Top Charts List, "
              f"visible and selected")
