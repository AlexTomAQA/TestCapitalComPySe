"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import allure
from datetime import datetime

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import conf
# from pages.common import flag_of_bug
from pages.common import Common
from src.src import CapitalComPageSrc
from pages.base_page import BasePage
from pages.Menu.menu import MenuSection
from pages.captcha import Captcha
from pages.Header.header import Header
from pages.Signup_login.signup_login import SignupLogin
from pages.Elements.HeaderLoginButton import HeaderButtonLogin
from pages.My_account.my_account import MyAccount
# from pages.Capital.Trading_platform.Topbar.topbar import TopBar
from pages.Trading_platform.trading_platform import TradingPlatform
from pages.Signup_login.signup_login_locators import (
    # SignupFormLocators,
    LoginFormLocators,
)

flag_cookies = False
url_language = "?"
url_country = "?"
prev_country = "?"
prev_language = "?"
prev_role = "?"
url_after_preconditions = "?"


class Conditions(BasePage):
    """This class used as a base class for other page classes that represent specific pages on a website"""

    debug = False

    @allure.step("Preconditions")
    def preconditions(
        self,
        d,
        host,
        end_point,
        cur_language,
        cur_country,
        cur_role,
        cur_login,
        cur_password,
    ):
        """
        Method Preconditions
        """
        global url_language
        global url_country
        global url_after_preconditions
        global prev_role
        global prev_language
        global prev_country

        print(f"\n{datetime.now()}   START PRECONDITIONS =>")
        print(f"\n{datetime.now()}   => URL after prev. preconditions - {url_after_preconditions}")
        print(f"{datetime.now()}   => flag_of_bug - {Common.flag_of_bug}")
        print(f"{datetime.now()}   => Current URL - {self.driver.current_url}")

        if url_after_preconditions == "?":
            url_after_preconditions = host

        if self.driver.current_url != url_after_preconditions:
            self.link = url_after_preconditions
            self.open_page()

        print(f"\n{datetime.now()}   => Windows size: {d.get_window_size()}")
        print(f"{datetime.now()}   Set windows position at (0, 0) =>")
        d.set_window_position(0, 0)
        # print(f"{datetime.now()}   Set resolution 1280 * 800 =>")
        # d.set_window_size(1280, 800)
        print(f"{datetime.now()}   Set resolution 1920 * 1080 =>")
        d.set_window_size(1920, 1080)
        print(f"{datetime.now()}   => Windows size is set to {d.get_window_size()}")

        answer = Captcha(d).fail_test_if_captcha_present_v2()

        # Настраиваем в соответствии с параметром "Роль"
        print(f"\n{datetime.now()}   Работа с куками =>")
        # if cur_role != prev_role or Common.flag_of_bug:
        if cur_role != prev_role:
            print(f"{datetime.now()}   Prev. role - '{prev_role}'")
            print(f"{datetime.now()}   Current testing role - '{cur_role}'")
            print(f"\n{datetime.now()}   All cookies must be delete =>")

            d.delete_all_cookies()
            print(f"{datetime.now()}   => All cookies are deleted")
            url_after_preconditions = host
            self.link = url_after_preconditions
            self.open_page()
            self.button_accept_all_cookies_click()
            prev_country = "?"
            prev_language = "?"
        else:
            print(f"\n{datetime.now()}   => не требуется")

        # устанавливаем Страну, если не соответствует предыдущей
        Captcha(d).fail_test_if_captcha_present_v2()
        print(f"\n{datetime.now()}   Prev. country - '{prev_country}'")
        print(f"{datetime.now()}   Cur. country - '{cur_country}'")
        # if cur_country != prev_country or Common.flag_of_bug:
        if cur_country != prev_country:
            print(f"{datetime.now()}   Set '{cur_country}' country =>")
            page_menu = MenuSection(d, self.driver.current_url)
            page_menu.menu_language_and_country_move_focus(cur_language)
            page_menu.set_country(cur_country)
            del page_menu
            prev_country = cur_country
            # prev_language = "?"
        print(f"{datetime.now()}   => Country set to '{cur_country}'")

        # устанавливаем Язык, если не соответствует предыдущему
        Captcha(d).fail_test_if_captcha_present_v2()
        language_prev, language_cur = prev_language, cur_language
        if language_prev == "":
            language_prev = "en"
        print(f"\n{datetime.now()}   Prev. language - '{language_prev}'")
        if language_cur == "":
            language_cur = "en"
        print(f"{datetime.now()}   Cur. language - '{language_cur}'")
        # if cur_language != prev_language or Common.flag_of_bug:
        if cur_language != prev_language:
            print(f"{datetime.now()}   Set '{language_cur}' language =>")
            page_menu = MenuSection(d, self.driver.current_url)
            page_menu.menu_language_and_country_move_focus(cur_language)
            page_menu.set_language(cur_language)
            del page_menu
            prev_language = cur_language
        print(f"{datetime.now()}   => Language is set to '{language_cur}'")

        # Продолжаем настройки в соответствии с параметром "Роль"
        Captcha(d).fail_test_if_captcha_present_v2()
        print(f"\n{datetime.now()}   Prev. role - '{prev_role}'")
        print(f"{datetime.now()}   Cur. role - '{cur_role}'")
        # if cur_role != prev_role or Common.flag_of_bug:
        if cur_role != prev_role:
            match cur_role:
                case "NoAuth":
                    self.to_do_authorization(d, self.driver.current_url, cur_language, cur_login, cur_password)
                    self.to_do_de_authorization(d, self.driver.current_url)
                case "Auth":
                    self.to_do_authorization(d, self.driver.current_url, cur_language, cur_login, cur_password)

            prev_role = cur_role
        print(f"{datetime.now()}   => The '{cur_role}' role is set")

        url_after_preconditions = self.driver.current_url
        print(f"\n{datetime.now()}   => Current URL - {url_after_preconditions}")
        print(f"\n{datetime.now()}   => THE END PRECONDITIONS")

        return url_after_preconditions

    # авторизация пользователя
    # @profile(precision=3)
    @allure.step("Authorization")
    def to_do_authorization(self, d, link, cur_language, login, password):
        """Authorisation"""

        print(f"" f"{datetime.now()}   Start Autorization")
        # Setup wait for later
        print(f"\n{datetime.now()}   => Current URL - {self.driver.current_url}")

        assert login != "", "Авторизация невозможна. Не указан e-mail"
        assert password != "", "Авторизация невозможна. Не указан пароль"
        # нажать в хедере на кнопку "Log in"
        if not HeaderButtonLogin(d, link).element_click():
            pytest.fail("Bug! 'Login' button is not clicked")

        if SignupLogin(d, link).should_be_login_form():
            print(f"{datetime.now()}   => 'Login' form is opened")
        elif SignupLogin(d, link).should_be_login_page():
            print(f"{datetime.now()}   => 'Login' page is opened")
        elif SignupLogin(d, link).should_be_trading_platform_login_form(cur_language):
            print(f"{datetime.now()}   => 'Login' form is opened on Trading platform")
        else:
            msg = "Problem with Authorisation"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # ???   {msg}")

        # User's name is passed to the text element on the login page
        if not self.send_keys(login, *LoginFormLocators.LOGIN_INPUT_EMAIL):
            pytest.fail(f'{datetime.now()}   => "login" is not inputted')

        # Password is passed to the text element on the login page
        if not self.send_keys(password, *LoginFormLocators.LOGIN_INPUT_PASSWORD):
            pytest.fail(f'{datetime.now()}   => "password" is not inputted')

        print(f'{datetime.now()}   => "login" and "password" are inputted')

        print(f"{datetime.now()}   Click [Continue] button on [Login] form =>")
        self.click_button(*LoginFormLocators.LOGIN_CONTINUE)
        print(f"{datetime.now()}   => [Continue] button on [Login] form is clicked")

        print(f"\n{datetime.now()}   1. Checking that the Page opened with 'Trading Platform | Capital.com' title")
        # Wait for the new tab to finish loading content
        timeout = 30
        print(f"{datetime.now()}   Set timeout = {timeout}")
        print(f"{datetime.now()}   Wait Trading platform page with 'Trading Platform | Capital.com' title open =>")
        wait = WebDriverWait(d, timeout)
        wait.until(EC.title_is("Trading Platform | Capital.com"))
        print(f"{datetime.now()}   => Trading platform page with 'Trading Platform | Capital.com' title opened")

        platform_url = "https://capital.com/trading/platform/"
        trading_platform = TradingPlatform(d, platform_url)

        # if top_bar.trading_platform_logo_is_present():
        trading_platform.should_be_platform_logo()

        # self.clear_charts_list(d)
        Common().browser_back_to_link(d, link)
        print(f"\n{datetime.now()}   => Current URL - {self.driver.current_url}")

    # def clear_charts_list(self, wd):
    #     allure.step(f"{datetime.now()}   Start Clear Chart list if trading instruments")
    #
    #     ti_page = TradingPlatform(wd)
    #     ti_page.select_menu_charts()
    #     ti_page.button_close_all_ti_click()
    #
    @allure.step(f"{datetime.now()}   DeAuthorisation")
    def to_do_de_authorization(self, d, link):
        """DeAuthorisation"""

        print(f"{datetime.now()}   Start DeAuthorisation")
        print(f"\n{datetime.now()}   => Current URL - {self.driver.current_url}")

        if not Header(d, link).header_button_my_account_click():
            msg = "Button 'My account' missing"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # ???   {msg}")

        if not MyAccount(d, link).my_account_button_logout_click():
            msg = "Button 'Logout' missing"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # ???   {msg}")

        print(f"\n{datetime.now()}   => Current URL - {self.driver.current_url}")

    def arrange_0(self):
        """
        Checking Main Page is opened
        """
        allure.step("Checking that Main Page is opened")

        base_link = CapitalComPageSrc.URL
        print(f"{datetime.now()}   0. Arrange_0")
        if not self.current_page_is(base_link):
            self.link = base_link
            self.open_page()
