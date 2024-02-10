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
from pages.My_account.my_account import MyAccount
from pages.Capital.Trading_platform.Topbar.topbar import TopBar
from pages.Signup_login.signup_login_locators import NewLoginFormLocators
from tests.ReTestsManual.pages.menu.menu import MainMenu

flag_cookies = False
url_language = "?"
url_country = "?"
# host = 'https://capital.com/en-gb'
test_link = "?"
prev_role = "?"
prev_language = "?"
prev_country = "?"


class NewConditions(BasePage):
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

        print(f"\n{datetime.now()}   {d.get_window_size()}")
        print(f"\n{datetime.now()}   Set windows position at (0, 0) =>")
        d.set_window_position(0, 0)
        print(f"\n{datetime.now()}   Set resolution 1280 * 720 =>")
        d.set_window_size(1280, 720)
        print(f"\n{datetime.now()}   => Resolution seted {d.get_window_size()}")

        Captcha(d).fail_test_if_captcha_present_v2()

        # Настраиваем в соответствии с параметром "Роль"
        print(f"\n{datetime.now()}   Prev. Role: {prev_role}")
        if cur_role != prev_role:
            print(f"\n{datetime.now()}   Run preconditions: set {cur_role} Role =>")

            test_link = host
            self.link = test_link
            self.open_page()
            if conf.DEBUG:
                print(f"\n{datetime.now()} Debug:   test_link = {test_link}")
            d.delete_all_cookies()
            print(f"\n{datetime.now()}   => All cookies are deleted")
            # print(d.get_cookies(), "")
            self.open_page()

            self.button_accept_all_cookies_click()

            match cur_role:
                case "NoAuth":
                    self.to_do_authorisation(d, host, cur_login, cur_password, cur_role)
                    menu = MainMenu(d, host)
                    if menu.element_is_visible(menu.HEADER_LOGIN_BTN):
                        self.set_new_country(d, cur_language, cur_country)
                        self.to_do_authorisation(d, host, cur_login, cur_password, cur_role)
                case "Auth":
                    self.to_do_authorisation(d, host, cur_login, cur_password, cur_role)

            prev_role = cur_role
            prev_language = "?"
            prev_country = "?"

        print(f"\n{datetime.now()}   Current role: {cur_role}")

        # устанавливаем Язык, если не соответствует предыдущему
        # Captcha(d).fail_test_if_captcha_present_v2()
        # language_prev, language_cur = prev_language, cur_language
        # if language_prev == "":
        #     language_prev = "en"
        # print(f"\n{datetime.now()}   Prev language: {language_prev}")
        # if language_cur == "":
        #     language_cur = "en"
        # if cur_language != prev_language:
        #     print(f"\n{datetime.now()}   Run preconditions: set {language_cur} language =>")
        #
        #     page_menu = MenuSection(d, host)
        #     page_menu.menu_language_and_country_move_focus(cur_language)
        #     page_menu.set_language(cur_language)
        #     test_link = self.driver.current_url
        #     del page_menu
        #     prev_language = cur_language
        #
        print(f"\n{datetime.now()}   => Current language: {url_language}")

        # устанавливаем Страну, если не соответствует предыдущей
        Captcha(d).fail_test_if_captcha_present_v2()

        # print(f"\n{datetime.now()}   Prev country: {prev_country}")
        # if cur_country != prev_country:
        #     print(f'{datetime.now()}   Run preconditions: set "{cur_country}" country =>')
        #
        #     page_menu = MenuSection(d, host)
        #     page_menu.menu_language_and_country_move_focus(cur_language)
        #     page_menu.set_country(cur_country)
        #     del page_menu
        #
        #     prev_country = cur_country
        print(f"{datetime.now()}   => Current country: {cur_country}")

        print(f"\n{datetime.now()}   => THE END PRECONDITIONS")

        return test_link

    # авторизация пользователя
    @allure.step(f"{datetime.now()}   Start Authorisation")
    # @profile(precision=3)
    def to_do_authorisation(self, d, link, login, password, cur_role):
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
        print(f"{datetime.now()}   -> Page with 'Trading Platform | Capital.com' title opened")

        platform_url = "https://capital.com/trading/platform/"
        top_bar = TopBar(d, platform_url)

        if top_bar.trading_platform_logo_is_present():
            print(f'{datetime.now()}   -> "Capital.com" logo is present on trading platform page')
        else:
            print(f'{datetime.now()}   -> "Capital.com" logo mission')
        del top_bar
        if cur_role == "NoAuth":
            print(f"\n" f"{datetime.now()}   Start DeAuthorisation")
            menu.element_is_clickable(menu.TP_USER_MENU).click()
            menu.element_is_clickable(menu.TP_LOGOUT).click()
        else:
            d.back()
        del menu

    def set_new_country(self, d, cur_language, cur_country):
        host = 'https://capital.com/'
        # устанавливаем Страну
        Captcha(d).fail_test_if_captcha_present_v2()

        page_menu = MenuSection(d, host)
        page_menu.menu_language_and_country_move_focus(cur_language)
        page_menu.set_country(cur_country)
        del page_menu

    @allure.step(f"{datetime.now()}   Start DeAuthorisation")
    def to_do_de_authorisation(self, d, link):
        """DeAuthorisation"""
        print(f"\n" f"{datetime.now()}   Start DeAuthorisation")
        menu = MainMenu(d, link)
        assert Header(d, link).header_button_my_account_click(), "Button 'My account' missing"
        assert MyAccount(d, link).my_account_button_logout_click(), "Button 'Logout' missing"

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
