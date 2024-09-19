"""
-*- coding: utf-8 -*-
@Time    : 2024/09/18 20:45
@Author  : Sergey Aiidzhanov
"""
import allure
from datetime import datetime

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.common import Common
from src.src import CapitalComPageSrc
from pages.base_page import BasePage
from pages.Menu.menu import MenuSection
from pages.captcha import Captcha
from pages.Header.header import Header
from pages.Signup_login.signup_login import SignupLogin
from pages.Elements.HeaderLoginButton import HeaderButtonLogin
from pages.My_account.my_account import MyAccount
from pages.Trading_platform.Topbar.topbar import TopBar
from pages.Trading_platform.trading_platform import TradingPlatform
from pages.Signup_login.signup_login_locators import NewLoginFormLocators, LoginFormLocators
from pages.Menu.New.menu_new import MainMenu

flag_cookies = False
# url_language = "?"
# url_country = "?"
# host = 'https://capital.com/en-gb'
test_link = "?"
prev_role = "?"
prev_language = "?"
prev_country = "?"
url_after_prev_preconditions_new = "?"
url_after_preconditions = "?"


def conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password):

    if cur_country in ['de', 'ua']:
        cond = Conditions(d)
        return cond.preconditions(d, CapitalComPageSrc.URL, '', cur_language, cur_country, cur_role,
                                  cur_login, cur_password)

    if cur_country in ['ae', 'au', 'gb']:
        cond = NewConditions(d)
        return cond.preconditions(d, CapitalComPageSrc.URL_NEW, '', cur_language, cur_country, cur_role,
                                  cur_login, cur_password)


class NewConditions(BasePage):
    """This class used as a base class for other page classes that represent specific pages on a website"""

    debug = False

    @allure.step("   Set New preconditions")
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
        # global url_language
        # global url_country
        # global host
        global test_link
        global url_after_prev_preconditions_new
        global prev_role
        global prev_language
        global prev_country

        print(f"\n\n{datetime.now()}   START NEW PRECONDITIONS =>")
        print(f"\n{datetime.now()}   => URL after prev. preconditions - {url_after_prev_preconditions_new}")
        print(f"{datetime.now()}   => flag_of_bug - {Common.flag_of_bug}")
        print(f"{datetime.now()}   => Current URL - {self.driver.current_url}")

        if self.driver.current_url != url_after_prev_preconditions_new:
            if url_after_prev_preconditions_new == "?":
                url_after_prev_preconditions_new = host
            self.link = url_after_prev_preconditions_new
            self.open_page()

        print(f"\n{datetime.now()}   => Windows size: {d.get_window_size()}")
        print(f"\n{datetime.now()}   Set windows position at (0, 0) =>")
        d.set_window_position(0, 0)
        print(f"\n{datetime.now()}   Set resolution 1920 * 1080 =>")
        d.set_window_size(1920, 1080)
        print(f"\n{datetime.now()}   => Resolution set {d.get_window_size()}")

        # Captcha(d).fail_test_if_captcha_present_v2()

        # Настраиваем в соответствии с параметром "Роль"
        print(f"\n{datetime.now()}   Работа с куками =>")
        if cur_role != prev_role:
            print(f"{datetime.now()}   Prev. role - '{prev_role}'")
            print(f"{datetime.now()}   Current testing role - '{cur_role}'")
            print(f"\n{datetime.now()}   All cookies must be delete =>")
            d.delete_all_cookies()
            print(f"{datetime.now()}   => All cookies are deleted")
            url_after_prev_preconditions_new = host
            self.link = url_after_prev_preconditions_new
            self.open_page()
            self.button_accept_all_cookies_click()
        else:
            print(f"\n{datetime.now()}   => не требуется")

        # Продолжаем настройки в соответствии с параметром "Роль"
        print(f"\n{datetime.now()}   Prev. role - '{prev_role}'")
        print(f"{datetime.now()}   Cur. role - '{cur_role}'")
        # if cur_role != prev_role or Common.flag_of_bug:
        if cur_role != prev_role:
            match cur_role:
                case "Auth":
                    self.to_do_authorisation_new(d, host, cur_login, cur_password, cur_role)
                case "NoAuth":
                    self.to_do_authorisation_new(d, host, cur_login, cur_password, cur_role)
                    self.to_do_de_authorisation_new(d, host)
                case "NoReg":
                    pass
                case _:
                    msg = f"Stop! Указанная роль '{cur_role}' не обрабатывается. Stop running"
                    print(f'{datetime.now()}   {msg}')
                    pytest.fail(msg)

            prev_role = cur_role
        print(f"\n{datetime.now()}   => The '{cur_role}' role is set")

        # # устанавливаем Страну, если не соответствует предыдущей
        # Captcha(d).fail_test_if_captcha_present_v2()
        # print(f"\n{datetime.now()}   Prev country: {prev_country}")
        # if cur_country != prev_country:
        #     print(f"{datetime.now()}   Set '{cur_country}' country =>")
        #     # page_menu = MenuSection(d, self.driver.current_url)
        #     # page_menu.menu_language_and_country_move_focus(cur_language)
        #     # page_menu.set_country(cur_country)
        #     # del page_menu
        #     prev_country = cur_country
        # print(f"{datetime.now()}   => Current country: {cur_country}")
        #
        # # устанавливаем Язык, если не соответствует предыдущему
        # Captcha(d).fail_test_if_captcha_present_v2()
        # language_prev, language_cur = prev_language, cur_language
        # if language_prev == "":
        #     language_prev = "en"
        # print(f"{datetime.now()}   Prev. language: '{language_prev}'")
        # if language_cur == "":
        #     language_cur = "en"
        # print(f"{datetime.now()}   Cur. language - '{language_cur}'")
        # if cur_language != prev_language:
        #     print(f"{datetime.now()}   Set '{language_cur}' language =>")
        #     # page_menu = MenuSection(d, self.driver.current_url)
        #     # page_menu.menu_language_and_country_move_focus(cur_language)
        #     # page_menu.set_language(cur_language)
        #     # del page_menu
        #     prev_language = cur_language
        # print(f"{datetime.now()}   => Language is set to '{language_cur}'")

        # устанавливаем параметры Язык и Страну, если хоть один из их не соответствует предыдущему значению
        # Captcha(d).fail_test_if_captcha_present_v2()
        language_prev, language_cur = prev_language, cur_language
        if language_prev == "":
            language_prev = "en"
        if language_cur == "":
            language_cur = "en"

        print(f"\n{datetime.now()}   Prev. language: {language_prev}")
        print(f"{datetime.now()}   Cur. language - '{language_cur}'")
        print(f"\n{datetime.now()}   Prev. country: {prev_country}")
        print(f"\n{datetime.now()}   Cur. country: {cur_country}")
        if cur_country != prev_country or language_cur != language_prev:
            print(f"{datetime.now()}   Set '{language_cur}' language and '{cur_country}' country =>")
            self.set_language_country_new(d, language_cur, cur_country)
            print(f"{datetime.now()}   => Language is set to '{language_cur}'")
            print(f"{datetime.now()}   => Country is set to '{cur_country}'")
        else:
            print(f"{datetime.now()}   => Language and country without change")

        print(f"{datetime.now()}   => Current URL - {self.driver.current_url}")

        url_after_preconditions_new = self.driver.current_url
        print(f"\n{datetime.now()}   => Current URL - {url_after_preconditions_new}")
        print(f"\n{datetime.now()}   => THE END PRECONDITIONS")

        return url_after_preconditions_new

    # авторизация пользователя
    @allure.step(f"{datetime.now()}   Start Authorisation")
    # @profile(precision=3)
    def to_do_authorisation_new(self, d, link, login, password, cur_role):
        """Authorisation"""
        print(f"\n" f"{datetime.now()}   Start Autorization")

        # Setup wait for later
        menu = MainMenu(d, link)
        assert login != "", "Авторизация невозможна. Не указан e-mail"
        assert password != "", "Авторизация невозможна. Не указан пароль"

        # нажать в хедере на кнопку "Log in"
        try:
            menu.element_is_clickable(menu.MENU_LOGIN).click()
        except:
            pytest.fail("Bug! 'Login' button is not clicked")

        print(f"{datetime.now()}   => 'Login' form is opened")

        # User's name is passed to the text element on the login page
        try:
            menu.send_keys(login, *NewLoginFormLocators.LOGIN_INPUT_EMAIL)
        except:
            pytest.fail(f'{datetime.now()}   => "login" is not inputted')

        # Password is passed to the text element on the login page
        try:
            menu.send_keys(password, *NewLoginFormLocators.LOGIN_INPUT_PASSWORD)
        except:
            pytest.fail(f'{datetime.now()}   => "password" is not inputted')

        print(f'{datetime.now()}   => "login" and "password" are inputted')

        print(f"{datetime.now()}   Click [Continue] button on [Login] form =>")
        menu.click_button(*NewLoginFormLocators.LOGIN_CONTINUE)
        print(f"{datetime.now()}   => [Continue] button on [Login] form is clicked")

        # Wait for the new tab to finish loading content
        timeout = 30
        print(f"{datetime.now()}   Set timeout = {timeout}")
        wait = WebDriverWait(d, timeout)
        wait.until(EC.title_is("Trading Platform | Capital.com"))
        print(f"{datetime.now()}   => Page with 'Trading Platform | Capital.com' title opened")

        platform_url = "https://capital.com/trading/platform/"
        trading_platform = TradingPlatform(d, platform_url)

        # if top_bar.trading_platform_logo_is_present():
        trading_platform.should_be_platform_logo()

        if cur_role == "Auth":
            d.back()

    @allure.step(f"{datetime.now()}   Start DeAuthorisation")
    def to_do_de_authorisation_new(self, d, link):
        """DeAuthorisation"""
        print(f"\n" f"{datetime.now()}   Start DeAuthorisation")

        top_bar = TopBar(d, link)
        if not top_bar.trading_platform_top_bar_account_info_menu_logout():
            msg = "De authorisation failed"
            print(f"{datetime.now()}   => {msg}")
            pytest.fail(f"Bug!   {msg}")
        # Header(d, link).check_visible_login_button_in_header_on_capital_com_new_page()
        print(f"{datetime.now()}   => Logout is OK")

        return True

    # def to_do_de_authorisation_new(self, d, link):
    #     """DeAuthorisation"""
        # print(f"\n" f"{datetime.now()}   Start DeAuthorisation")
        # menu = MainMenu(d, link)
        # if not Header(d, link).header_button_my_account_click():
        #     msg = "Button 'My account' missing"
        #     print(f"{datetime.now()}   {msg}")
        # if not Header(d.link).check_opened_my_account_panel():
        #     # Header(d.link).
        #     pass

        # print(f"{datetime.now()}   => 'My account' panel opened")
        #
        # assert MyAccount(d, link).my_account_button_logout_click(), "Button 'Logout' missing"

    @allure.step(f"{datetime.now()}   Set language and country")
    def set_language_country_new(self, d, cur_language, cur_country):
        # устанавливаем Язык и Страну
        # if cur_language == "":
        #     cur_language = "en"
        print(f'{datetime.now()}   Set "{cur_language}" language and "{cur_country}" country =>')

        host = 'https://capital.com/'
        # Captcha(d).fail_test_if_captcha_present_v2()

        match cur_language:
            case "en": host += "en-"
            case "ar": host += "ar-"
            case _:
                msg = f"Stop! Указанный язык '{cur_language}' не обрабатывается. Stop running"
                print(f'{datetime.now()}   {msg}')
                pytest.fail(msg)
        match cur_country:
            case "gb": host += "gb"
            case "ae": host += "ae"
            case _:
                msg = f"Stop! Указанная страна '{cur_country}' не обрабатывается. Stop running"
                print(f'{datetime.now()}   {msg}')
                pytest.fail(msg)

        self.driver = d
        self.link = host
        self.open_page()

        # page_menu = MenuSection(d, host)
        # page_menu.menu_language_and_country_move_focus(cur_language)
        # page_menu.set_country(cur_country)
        # del page_menu

    @allure.step("Start Checking that Main Page is opened")
    def arrange_0(self):
        """
        Checking Main Page is opened
        """
        base_link = CapitalComPageSrc.URL
        print(f"\n{datetime.now()}   0. Arrange_0")
        if not self.current_page_is(base_link):
            self.link = base_link
            self.open_page()


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
