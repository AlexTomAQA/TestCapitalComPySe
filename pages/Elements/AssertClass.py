"""
-*- coding: utf-8 -*-
@Time    : 2023/03/28 09:00
@Author  : Alexander Tomelo
"""

# import pytest
from datetime import datetime

import allure
from selenium.webdriver.common.by import By

from pages.Capital.trading_instrument_page import PageTradingInstrument
from pages.common import Common
from pages.AppStore.app_store import AppStore
from pages.Capital.Trading_platform.trading_platform import TradingPlatform
from pages.GooglePlay.google_play import GooglePlay
from pages.TradingView.tradingview import TradingView
from pages.base_page import BasePage
from pages.Signup_login.signup_login import SignupLogin
from pages.ReTests.ReTest_table_fill import retest_table_fill


class AssertClass(BasePage):
    page_signup_login = None
    page_trading = None
    page_app_store = None
    page_google_play = None
    page_tradingview = None
    platform_url = ""
    page_trading_instrument = None

    # def __init__(self, *args):
    #     super().__init__(*args)
    #     self.is_captcha()

    @allure.step('Checking that "Signup" opened (old layout)')
    def assert_signup(self, d, cur_language, cur_link):
        """Method Assert Signup"""

        print(f"\n{datetime.now()}   3. Assert_Signup_v0")
        self.page_signup_login = SignupLogin(d, cur_link)
        if self.page_signup_login.should_be_signup_form(cur_language):
            self.page_signup_login.close_signup_form()
        elif self.page_signup_login.should_be_new_signup_form(cur_language):
            self.page_signup_login.close_new_signup_form()
        elif self.page_signup_login.should_be_signup_page(cur_language):
            self.page_signup_login.close_signup_page()
        elif self.page_signup_login.should_be_trading_platform_signup_form(cur_language):
            self.page_signup_login.close_trading_platform_signup_form()
        else:
            del self.page_signup_login
            print(f'\nBug: {self.bid}')
            retest_table_fill(d, self.bid, '04', self.link)
            Common().assert_true_false(False, "Bug # 04. Unknown situation instead 'Sign Up' form opened")
            # pytest.fail("Bug # 04. Unknown situation instead 'Sign Up' form opened")

        Common().assert_true_false(True, "")
        # del self.page_signup_login

    @allure.step('Checking that "Signup Pause" opened (new layout)')
    def assert_signup_pause(self, d, cur_language, cur_link):
        """Method Assert Signup Pause"""

        print(f"\n{datetime.now()}   3. Assert_SignUp_Pause_v0")
        self.page_signup_login = SignupLogin(d, cur_link)
        if self.page_signup_login.should_be_signup_pause_form(cur_language):
            self.page_signup_login.close_signup_pause_form()
        else:
            print(f'\nBug: {self.bid}')
            retest_table_fill(d, self.bid, '04', self.link)
            Common().assert_true_false(False, "Bug # 04. Unknown situation instead 'Sign Up' form opened")

    @allure.step('Checking that "Login" form or page opened')
    def assert_login(self, d, cur_language, cur_link):
        """Method Assert Login form or page"""
        print(f"\n{datetime.now()}   3. Assert_Login_v0")
        self.page_signup_login = SignupLogin(d, cur_link)
        if self.page_signup_login.should_be_login_form():
            self.page_signup_login.close_login_form()
            del self.page_signup_login
        elif self.page_signup_login.should_be_new_login_form():
            self.page_signup_login.close_new_login_form()
            del self.page_signup_login
        elif self.page_signup_login.should_be_login_page():
            self.page_signup_login.close_login_page()
            del self.page_signup_login
        elif self.page_signup_login.should_be_trading_platform_login_form(cur_language):
            self.page_signup_login.close_trading_platform_login_form()
            del self.page_signup_login
        elif self.page_signup_login.should_be_signup_form(cur_language):
            del self.page_signup_login
            print(f'\nBug: {self.bid}')
            retest_table_fill(d, self.bid, '05', self.link)
            Common().assert_true_false(False,
                                       "Bug # 05. Opened a 'Sign up' form instead of a 'Login'")
            # pytest.fail("Bug # 05. Opened a 'Sign up' form instead of a 'Login'", False)
        elif self.page_signup_login.should_be_new_signup_form(cur_language):
            del self.page_signup_login
            print(f'\nBug: {self.bid}')
            retest_table_fill(d, self.bid, '05', self.link)
            Common().assert_true_false(False,
                                       "Bug # 05. Opened a new 'Sign up' form instead of a 'Login'")
            # pytest.fail("Bug # 05. Opened a 'Sign up' form instead of a 'Login'", False)
        elif self.page_signup_login.should_be_signup_page(cur_language):
            del self.page_signup_login
            print(f'\nBug: {self.bid}')
            retest_table_fill(self.driver, self.bid, '06', self.link)
            Common().assert_true_false(False,
                                       "Bug # 06. Opened a 'Sign up' page instead of a 'Login'")
            # pytest.fail("Bug # 06. Opened a 'Sign up' page instead of a 'Login'", False)
        elif self.page_signup_login.should_be_trading_platform_signup_form(cur_language):
            del self.page_signup_login
            print(f'\nBug: {self.bid}')
            retest_table_fill(d, self.bid, '07', self.link)
            Common().assert_true_false(False,
                                       "Bug # 07. Opened a 'Sign up' form on trading platform instead of a 'Login'")
            # pytest.fail("Bug # 07. Opened a 'Sign up' form on trading platform instead of a 'Login'", False)
        else:
            del self.page_signup_login
            print(f'\nBug: {self.bid}')
            retest_table_fill(d, self.bid, '08', self.link)
            Common().assert_true_false(False,
                                       "Bug # 08. Unknown situation instead 'Login' form opened")
            # pytest.fail("Bug # 08. Unknown situation instead 'Login' form opened", False)

        Common().assert_true_false(True, "")

    @allure.step('Checking that "Trading platform" page opened')
    def assert_trading_platform(self, d):
        print(f"\n{datetime.now()}   3. Assert_v0")
        # time.sleep(1)
        self.platform_url = "https://capital.com/trading/platform/"
        # self.platform_url = "https://capital.com/trading/platform"
        self.page_trading = TradingPlatform(d)
        # self.page_trading.should_be_trading_platform_page_v2(d, self.platform_url)
        self.page_trading.should_be_trading_platform_page_v3()
        del self.page_trading

    @allure.step('Checking that "Trading platform" page opened - ver 2')
    def assert_trading_platform_v2(self, d, cur_link, demo=False):
        print(f"\n{datetime.now()}   3. Assert_v2")
        self.page_trading = TradingPlatform(d, cur_link)
        self.page_trading.should_be_trading_platform_page_v2(d, cur_link, demo)

    @allure.step('Checking that "Trading platform" page opened - ver 3')
    def assert_trading_platform_v3(self, d, cur_link, demo=False):
        print(f"\n{datetime.now()}   3. Assert_v3")
        self.page_trading = TradingPlatform(d, cur_link)
        self.page_trading.should_be_trading_platform_page_v3(demo)

    @allure.step('Checking that "Trading platform" page opened - ver 4')
    def assert_trading_platform_v4(self, d, cur_link, tpd=False, tpi=False, trade_instrument=""):
        """
        Check if the trading platform page for the corresponding trade instrument is opened
        Args:
            d: Webdriver
            cur_link: Link in the list of 3 random items and start page of the sidebar
            "Shares trading" is selected (Param)
            tpd: open Trade platform in Demo mode (False), else open Trade platform
            tpi: open Trade platform for corresponding trade instrument (False)
            trade_instrument: corresponding trade instrument (False)
        """

        print(f"\n{datetime.now()}   3. Assert_Trading_Platform_v4")
        self.page_trading = TradingPlatform(d, cur_link, self.bid)
        print(f"\n{datetime.now()}   ")
        self.page_trading.should_be_trading_platform_page_v4(d, cur_link, tpd, tpi, trade_instrument)

    @allure.step('Checking that "Trading platform" page opened and the element is selected')
    def assert_trading_platform_with_selected_element(self, d, cur_link, tab="", trade_instrument=""):
        """
        Check if the trading platform page for the corresponding trade instrument is opened
        Args:
            d: Webdriver
            cur_link: Link in the list of 3 random items and start page of the sidebar
            "Shares trading" is selected (Param)
            tab: open Trade platform for corresponding trade instrument tab (False)
            trade_instrument: corresponding trade instrument (False)
        """

        print(f"\n{datetime.now()}   3. Assert element is selected")
        self.page_trading = TradingPlatform(d, cur_link, self.bid)
        self.page_trading.should_be_trading_platform_page_with_selected_element(d, cur_link, tab, trade_instrument)

    @allure.step('Checking that "Trading platform" page opened in demo mode')
    def assert_trading_platform_demo(self, d):
        print(f"\n{datetime.now()}   3. Assert_v0")
        self.platform_url = "https://capital.com/trading/platform/?mode=demo"
        self.page_trading = TradingPlatform(d)
        self.page_trading.should_be_trading_platform_page(d, self.platform_url)
        del self.page_trading

    @allure.step('Checking that "App Store" page opened')
    def assert_app_store(self, d, cur_link):
        print(f"\n{datetime.now()}   3. Assert_v0")
        self.page_app_store = AppStore(d, cur_link, self.bid)
        self.page_app_store.should_be_app_store_page(cur_link)

    @allure.step('Checking that "App Store Investmate" page opened')
    def assert_app_store_investmate(self):
        print(f"\n{datetime.now()}   3. Assert_v0")
        self.page_app_store = AppStore(self.driver, self.link, self.bid)
        self.page_app_store.should_be_app_store_investmane_page()

    @allure.step('Checking that "Google Play" page opened')
    def assert_google_play(self, d, cur_link):
        print(f"\n{datetime.now()}   3. Assert_v0")
        self.page_google_play = GooglePlay(d, cur_link, self.bid)
        self.page_google_play.should_be_google_play_page(cur_link)

    @allure.step('Checking that "Sign Up" form on the Trading Platform page opened')
    def assert_signup_form_on_the_trading_platform(self, d):
        print(f"\n{datetime.now()}   3. Assert_v0")
        self.page_trading = TradingPlatform(d, self.link, self.bid)
        self.page_trading.should_be_signup_form_on_the_trading_platform(d)

    @allure.step('Checking that "Login" form on the Trading Platform page opened')
    def assert_login_form_on_the_trading_platform(self, d):
        print(f"\n{datetime.now()}   3. Assert_v0")
        self.page_trading = TradingPlatform(d, self.link, self.bid)
        self.page_trading.should_be_login_form_on_the_trading_platform()

    @allure.step('Checking the Site TradingView is opened')
    def assert_site_tradingview(self, d):
        print(f"\n{datetime.now()}   3. Assert_v0")
        self.page_tradingview = TradingView(d)
        self.page_tradingview.should_be_tradingview_page(d)

        tabs = self.driver.window_handles
        if len(tabs) == 2:
            self.driver.close()
            self.driver.switch_to.window(tabs[0])

    @allure.step(
        'Checking that "Page of trading instrument" on capital.com with corresponding instrument is opened')
    def assert_page_trading_instrument(self, d, language, cur_link, title_instrument):
        print(f"\n{datetime.now()}   3. Assert_v0")
        self.page_trading_instrument = PageTradingInstrument(d, cur_link, self.bid)
        self.page_trading_instrument.should_be_trading_instrument_page(title_instrument)

    @allure.step('Checking that the "My account" menu is opened')
    def assert_my_account_menu(self, d):
        print(f"\n{datetime.now()}   3. Assert_v0")
        account_btn_link = d.current_url
        if account_btn_link == "https://capital.com/trading/platform/":
            assert False, \
                ('Bug#005. '
                 'Expected result: Menu "My account" is displayed'
                 '\n'
                 'Actual result: The trading platform page is opened')
        else:
            print(f"{datetime.now()}   =>This does not mean that there is no bug")

    @allure.step('Checking that Home page is not opened when click [Platform overview] button')
    def assert_that_trading_page_is_opened(self, d):
        print(f"\n{datetime.now()}   3. Assert_v0")
        platform_overview_btn_link = d.current_url
        if platform_overview_btn_link == "https://capital.com/":
            assert False, \
                ('Bug#029. '
                 'Expected result:The Desktop Trading page is opened '
                 '\n'
                 'Actual result: The Home page is opened ')

    @allure.step('Checking that applied filters "Region/Sectors" are displayed')
    def assert_filters(self, d, cur_link, selected_filters_text_list):
        print(f"\n{datetime.now()}   3. Assert_v0")

        filters_labels = self.driver.find_element(By.CSS_SELECTOR, '#flt_labels')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            filters_labels
        )

        actual_filters_locator = (By.CSS_SELECTOR, '#flt_labels > span > span.text-ellipsis')
        time_out = 5

        actual_filters_list = self.elements_are_located(actual_filters_locator, time_out)
        actual_filters_text_list = [element.text for element in actual_filters_list]

        if actual_filters_text_list != selected_filters_text_list:
            assert False, \
                ('Bug#039. '
                 f'Expected result: applied filters "Region/Sectors" are displayed {selected_filters_text_list}'
                 '\n'
                 'Actual result: applied filters "Region/Sectors" are not displayed after selecting an item from '
                 f'the "Most traded" dropdown {actual_filters_text_list}')
        else:
            print(f"{datetime.now()}   Applied filters {selected_filters_text_list} are displayed")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
