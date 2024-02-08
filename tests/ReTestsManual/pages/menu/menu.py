# import logging
# import re
import time

import allure
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from pages.base_page import BasePage


class MainMenu(BasePage):

    SUB_MENU_LIST = (By.CSS_SELECTOR, '.menuGroup_dropdown__75ey5>div>a')
    MENU_LIST = (By.CSS_SELECTOR, '.menuGroup_item__jQrol')
    HEADER_LOGIN_BTN = (By.CSS_SELECTOR, '[data-type="btn_header_login"]')
    HEADER_SIGNUP_BTN = (By.CSS_SELECTOR, '[data-type="btn_header"]')
    HEADER_ACCOUNT_BTN = (By.CSS_SELECTOR, '.accountBtns_btnsPlace___6pn2 a')

    # markets
    MENU_MARKETS = (By.CSS_SELECTOR, '[data-type="nav_id689"]')
    SUB_MENU_MARKETS_FOREX = (By.CSS_SELECTOR, '[data-type="nav_id690"]')
    SUB_MENU_MARKETS_INDICES = (By.CSS_SELECTOR, '[data-type="nav_id693"]')
    SUB_MENU_MARKETS_SHARES = (By.CSS_SELECTOR, '[data-type="nav_id694"]')
    SUB_MENU_MARKETS_COMMODITIES = (By.CSS_SELECTOR, '[data-type="nav_id701"]')
    SUB_MENU_MARKETS_ESG = (By.CSS_SELECTOR, '[data-type="nav_id738"]')
    # ways to trade
    MENU_WAYS_TO_TRADE = (By.CSS_SELECTOR, '[data-type="nav_id686"]')
    SUB_MENU_WAYS_TO_TRADE_PROFESSIONAL = (By.CSS_SELECTOR, '[data-type="nav_id752"]')
    # trading platform
    MENU_TRADING_PLATFORM = (By.CSS_SELECTOR, '[data-type="nav_id688"]')
    # account
    MENU_ACCOUNT = (By.CSS_SELECTOR, '[class*="accountBtns"]>a')
    MENU_LOGIN = (By.CSS_SELECTOR, '[data-type="btn_header_login"]')

    @allure.step('Select "Trading platform" menu')
    def open_trading_platform_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Trading platform" menu  =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.main_menu_move_focus(d, cur_language, self.MENU_TRADING_PLATFORM)
        self.sub_menu_move_focus_click(d, cur_language, self.MENU_TRADING_PLATFORM)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Way_to_trade" menu, "Professional" submenu')
    def open_waytotrade_professional_sub_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Way_to_trade" menu, "Professional" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.main_menu_move_focus(d, cur_language, self.MENU_WAYS_TO_TRADE)
        self.sub_menu_move_focus_click(d, cur_language, self.SUB_MENU_WAYS_TO_TRADE_PROFESSIONAL)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Markets" menu, "Forex" submenu')
    def open_markets_forex_sub_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Markets" menu, "Forex" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.main_menu_move_focus(d, cur_language, self.MENU_MARKETS)
        self.sub_menu_move_focus_click(d, cur_language, self.SUB_MENU_MARKETS_FOREX)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Markets" menu, "Indices" submenu')
    def open_markets_indices_sub_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Markets" menu, "Indices" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.main_menu_move_focus(d, cur_language, self.MENU_MARKETS)
        self.sub_menu_move_focus_click(d, cur_language, self.SUB_MENU_MARKETS_INDICES)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Markets" menu, "Shares" submenu')
    def open_markets_shares_sub_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Markets" menu, "Shares" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.main_menu_move_focus(d, cur_language, self.MENU_MARKETS)
        self.sub_menu_move_focus_click(d, cur_language, self.SUB_MENU_MARKETS_SHARES)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Markets" menu, "Commodities" submenu')
    def open_markets_commodities_sub_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Markets" menu, "Commodities" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.main_menu_move_focus(d, cur_language, self.MENU_MARKETS)
        self.sub_menu_move_focus_click(d, cur_language, self.SUB_MENU_MARKETS_COMMODITIES)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Markets" menu, "ESG" submenu')
    def open_markets_esg_sub_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Markets" menu, "ESG" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.main_menu_move_focus(d, cur_language, self.MENU_MARKETS)
        self.sub_menu_move_focus_click(d, cur_language, self.SUB_MENU_MARKETS_ESG)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Markets' menu section.")
    def main_menu_move_focus(self, d, test_language, main_menu_locator):

        menu = d.find_elements(*main_menu_locator)
        if len(menu) == 0:
            print(f"{datetime.now()}   => Main Menu not present")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
            pytest.skip(f"Main menu not present for '{test_language}' language")
        print(f"{datetime.now()}   => Main menu is present")

        if not self.element_is_visible(main_menu_locator, 5):
            print(f"{datetime.now()}   => Main menu not visible")
            pytest.fail("Main menu not visible")
        print(f"{datetime.now()}   => Main menu is visible")

        time.sleep(0.5)
        menu = d.find_elements(*main_menu_locator)  # not Glossary
        ActionChains(d) \
            .move_to_element(menu[0]) \
            .pause(0.5) \
            .perform()

        del menu
        print(f"{datetime.now()}   => Markets menu focus moved")

    @allure.step(f"{datetime.now()}.   Focus move to 'Markets [Forex]' menu item and click (US_11.01.02).")
    def sub_menu_move_focus_click(self, d, test_language, sub_menu_locator):

        sub_menu = d.find_elements(*sub_menu_locator)
        if len(sub_menu) == 0:
            pytest.skip(f"Sub menu not present for '{test_language}' language")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    def open_menu_sub_menu(self, d, test_language, menu_elem, sub_menu_elem):
        # print(f"{datetime.now()}.   Focus move to menu item and click sub-menu.")
        ActionChains(d) \
            .move_to_element(menu_elem) \
            .pause(0.5) \
            .move_to_element(sub_menu_elem) \
            .pause(1) \
            .click() \
            .perform()
