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

import conf
from src.src import CapitalComPageSrc
from pages.base_page import BasePage
from pages.Menu.menu import MenuSection
from pages.captcha import Captcha
from pages.Header.header import Header
from pages.Signup_login.signup_login import SignupLogin
from pages.Elements.HeaderLoginButton import HeaderButtonLogin
from pages.My_account.my_account import MyAccount
from pages.Capital.Trading_platform.Topbar.topbar import TopBar
from pages.Signup_login.signup_login_locators import (
    # SignupFormLocators,
    LoginFormLocators,
)

flag_cookies = False
url_language = "?"
url_country = "?"
# host = CapitalComPageSrc.URL
prev_country = "?"
prev_language = "?"
prev_role = "?"
test_link = "?"


class Conditions(BasePage):
    """This class used as a base class for other page classes that represent specific pages on a website"""

    debug = False

    @allure.step(f"{datetime.now()}   Set preconditions")
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
        # global host
        global test_link
        global prev_role
        global prev_language
        global prev_country

        print(f"\n\n{datetime.now()}   START PRECONDITIONS =>\n")
        if test_link == "?":
            self.link = host
            self.open_page()
        # if url == "":
        #     self.link = host
        #     self.open_page()
        print(f"\n{datetime.now()}   => Windows size - {d.get_window_size()}")
        # print(f"\n{datetime.now()}   Set windows position at (320, 180) =>")
        # d.set_window_position(320, 180)
        print(f"{datetime.now()}   Set windows position at (0, 0) =>")
        d.set_window_position(0, 0)
        print(f"{datetime.now()}   Set resolution 1280 * 800 =>")
        d.set_window_size(1280, 800)
        print(f"{datetime.now()}   => Windows size is set to {d.get_window_size()}")

        Captcha(d).fail_test_if_captcha_present_v2()

        # Настраиваем в соответствии с параметром "Роль"
        print(f"\n{datetime.now()}   Работа с куками")
        if cur_role != prev_role:
            print(f"{datetime.now()}   => Prev. role - '{prev_role}'")
            print(f"{datetime.now()}   => Current testing role - '{cur_role}'")
            print(f"{datetime.now()}   All cookies must be delete =>")

            test_link = host
            self.link = test_link
            self.open_page()
            if conf.DEBUG:
                print(f"{datetime.now()} Debug:   test_link = {test_link}")
            d.delete_all_cookies()
            print(f"\n{datetime.now()}   => All cookies are deleted")
            # print(d.get_cookies(), "")
            self.open_page()
            self.button_accept_all_cookies_click()
            prev_country = "?"
            prev_language = "?"

        # устанавливаем Страну, если не соответствует предыдущей
        # Captcha(d).fail_test_if_captcha_present_v2()
        print(f"\n{datetime.now()}   => Prev. country - '{prev_country}'")
        if cur_country != prev_country:
            print(f"{datetime.now()}   Set '{cur_country}' country =>")
            # page_menu = MenuSection(d, host)
            page_menu = MenuSection(d, self.driver.current_url)
            page_menu.menu_language_and_country_move_focus(cur_language)
            page_menu.set_country(cur_country)
            del page_menu
            prev_country = cur_country
            # prev_language = "?"
        print(f"{datetime.now()}   => Country set to '{cur_country}'")

        # устанавливаем Язык, если не соответствует предыдущему
        # Captcha(d).fail_test_if_captcha_present_v2()
        language_prev, language_cur = prev_language, cur_language
        if language_prev == "":
            language_prev = "en"
        print(f"\n{datetime.now()}   => Prev. language - '{language_prev}'")
        if language_cur == "":
            language_cur = "en"
        if cur_language != prev_language:
            print(f"{datetime.now()}   Set '{language_cur}' language =>")
            # page_menu = MenuSection(d, host)
            page_menu = MenuSection(d, self.driver.current_url)
            page_menu.menu_language_and_country_move_focus(cur_language)
            page_menu.set_language(cur_language)
            del page_menu
            prev_language = cur_language
        print(f"{datetime.now()}   => Language is set to '{language_cur}'")

        # Продолжаем настройки в соответствии с параметром "Роль"
        print(f"\n{datetime.now()}   => Prev. role - '{prev_role}'")
        if cur_role != prev_role:
            match cur_role:
                case "NoAuth":
                    self.to_do_authorisation(d, self.driver.current_url, cur_login, cur_password)
                    self.to_do_de_authorisation(d, self.driver.current_url)
                    # self.to_do_authorisation(d, host, cur_login, cur_password)
                    # self.to_do_de_authorisation(d, host)
                case "Auth":
                    self.to_do_authorisation(d, self.driver.current_url, cur_login, cur_password)
                    # self.to_do_authorisation(d, host, cur_login, cur_password)

            prev_role = cur_role
        print(f"{datetime.now()}   => The '{cur_role}' role is set")

        test_link = self.driver.current_url
        print(f"\n{datetime.now()}   => THE END PRECONDITIONS")

        return test_link

    # авторизация пользователя
    @allure.step(f"{datetime.now()}   Start Authorisation")
    # @profile(precision=3)
    def to_do_authorisation(self, d, link, login, password):
        """Authorisation"""
        print(f"" f"{datetime.now()}   Start Autorization")
        # Setup wait for later

        assert login != "", "Авторизация невозможна. Не указан e-mail"
        assert password != "", "Авторизация невозможна. Не указан пароль"
        # нажать в хедере на кнопку "Log in"
        if not HeaderButtonLogin(d, link).element_click():
            pytest.fail("Bug! 'Login' button is not clicked")

        if SignupLogin(d, link).should_be_login_form():
            print(f"{datetime.now()}   => 'Login' form is opened")
        elif SignupLogin(d, link).should_be_login_page():
            print(f"{datetime.now()}   => 'Login' page is opened")
        elif SignupLogin(d, link).should_be_trading_platform_login_form():
            print(f"{datetime.now()}   => 'Login' form is opened on Trading platform")
        else:
            pytest.fail("Problem with Authorisation")

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

        # Wait for the new tab to finish loading content
        timeout = 30
        print(f"{datetime.now()}   Set timeout = {timeout}")
        wait = WebDriverWait(d, timeout)
        wait.until(EC.title_is("Trading Platform | Capital.com"))
        print(f"{datetime.now()}   -> Page with 'Trading Platform | Capital.com' title opened")

        platform_url = "https://capital.com/trading/platform/"
        top_bar = TopBar(d, platform_url)

        if top_bar.trading_platform_logo_is_present():
            print(f'{datetime.now()}   -> "Capital.com" logo is present on trading platform page')
        else:
            print(f'{datetime.now()}   -> "Capital.com" logo mission')
        del top_bar
        d.back()

    @allure.step(f"{datetime.now()}   Start DeAuthorisation")
    def to_do_de_authorisation(self, d, link):
        """DeAuthorisation"""
        print(f"{datetime.now()}   Start DeAuthorisation")

        assert Header(d, link).header_button_my_account_click(), "Button 'My account' missing"
        assert MyAccount(d, link).my_account_button_logout_click(), "Button 'Logout' missing"

    @allure.step("Start Checking that Main Page is opened")
    def arrange_0(self):
        """
        Checking Main Page is opened
        """
        base_link = CapitalComPageSrc.URL
        print(f"{datetime.now()}   0. Arrange_0")
        if not self.current_page_is(base_link):
            self.link = base_link
            self.open_page()
