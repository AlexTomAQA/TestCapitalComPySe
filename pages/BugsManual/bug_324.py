"""
-*- coding: utf-8 -*-
@Time    : 2024/08/13 22:30
@Author  : Artem Dashkov
"""
import allure
import time
from datetime import datetime
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.common import Common
from pages.Signup_login.signup_login import SignupLogin

LINK_NAME = "[MT4 platforms] link"
LINK_LOCATOR = (By.XPATH, '//p//a[contains(text(), "MT4")]')
TRADINGVIEW_TITLE_LOCATOR = (By.XPATH, '//h1[contains(text(), "TradingView")]')
MT4_TITLE_LOCATOR = (By.XPATH, '//h1[contains(text(), "MetaTrader")]')

MENU_NAME = "[Trading]"
SUBMENU_NAME = "menu item [Demo]"
MENU_LOCATOR = (By.CSS_SELECTOR, 'span > a[data-type="nav_id824"]')
SUBMENU_LOCATOR = (By.CSS_SELECTOR, "div.grid_grid__2D3md > a[data-type='nav_id1029']")


class BUG_324(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange.")
    def arrange(self, d, cur_item_link):
        global LINK_LOCATOR
        print(f"{datetime.now()}   1. Start Arrange.")

        if not self.current_page_is(cur_item_link):
            print(f"{datetime.now()}   => current_url != cur_item_link")
            self.link = cur_item_link
            time.sleep(1)
            self.open_page()
        else:
            print(f"{datetime.now()}   => current_url == cur_item_link")


        # Check presenting [MT4 platforms] link
        print(f"{datetime.now()}   Check presenting {LINK_NAME}.")
        print(f"{datetime.now()}   IS {LINK_NAME} present on this page? =>")
        if len(self.driver.find_elements(*LINK_LOCATOR)) == 0:
            msg = f"{LINK_NAME} is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {LINK_NAME} present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*LINK_LOCATOR)[0]
        )

        # Check visible [MT4 platforms] link
        print(f"{datetime.now()}   IS {LINK_NAME} visible on this page? =>")
        if not self.element_is_visible(LINK_LOCATOR, 5):
            msg = f"{LINK_NAME} is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {LINK_NAME} is visible on this page!\n")

        # Check clickable [MT4 platforms] link
        print(f"{datetime.now()}   IS {LINK_NAME} clickable on this page? =>")
        if not self.element_is_clickable(LINK_LOCATOR, 5):
            msg = f"{LINK_NAME} is NOT clickable on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {LINK_NAME} is clickable on this page!\n")
        Common.save_current_screenshot(d, f"{LINK_NAME} is clickable on this page!")

    @allure.step(f"{datetime.now()}   2. Start Act.")
    def act(self, d):
        print(f"{datetime.now()}   2. Start Act.")

        # Start click [MT4 platforms] link
        print(f"{datetime.now()}   Start click on {LINK_NAME} =>")
        try:
            self.driver.find_element(*LINK_LOCATOR).click()
            print(f"{datetime.now()}   => {LINK_NAME} clicked!\n")

        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => {LINK_NAME} NOT CLICKED")

            print(f"{datetime.now()}   'Sign up' form or page is auto opened")

            page_ = SignupLogin(self.driver)
            if page_.close_signup_form():
                pass
            elif page_.close_login_form():
                pass
            elif page_.close_signup_page():
                pass
            else:
                page_.close_login_page()

            self.driver.find_element(*LINK_LOCATOR).click()
            time.sleep(1)
            print(f"{datetime.now()}   => {LINK_NAME} clicked!\n")

        Common.save_current_screenshot(d, f"{LINK_NAME} clicked!")

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d):
        print(f"{datetime.now()}   3. Start Assert.")

        # Check opened page
        print(f"{datetime.now()}   Check 'TradingView' page is opened instead 'MT4' page.")
        print(f"{datetime.now()}   IS 'TradingView' page is opened instead 'MT4' page? =>")
        print(f'{datetime.now()}   Current page is: {self.driver.current_url}')
        if len(self.driver.find_elements(*TRADINGVIEW_TITLE_LOCATOR)) != 0:
            msg = f"'TradingView' page is opened instead 'MT4' page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   Current page don't 'TradingView' title.")

        print(f"{datetime.now()}   Check opened page is 'MT4' page.")
        print(f"{datetime.now()}   IS opened page 'MT4' page.? =>")

        if len(self.driver.find_elements(*MT4_TITLE_LOCATOR)) == 0:
            msg = f"'MT4' page is not opened instead"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   Current page have 'MetaTrader' in title. Need to check content of page. "
              f"Current page url is: {self.driver.current_url}")

        Common.save_current_screenshot(d, f"Current page have 'MetaTrader' in title. "
                                          f"Need to check content of page.")
        return True

    @allure.step(f"{datetime.now()}   Start move focus menu section [Trading] move focus to menu item [Demo]")
    def from_trading_menu_focus_demo(self, d, link):
        print(f'\n{datetime.now()}   START Open "{MENU_NAME}" menu, "{SUBMENU_NAME}" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        time.sleep(0.5)
        menu = d.find_elements(*MENU_LOCATOR)
        if len(menu) == 0:
            print(f"{datetime.now()}   => '{MENU_NAME}' menu not present in DOM")
            Common().pytest_fail(
                f"'{MENU_NAME}' menu not present in DOM.")
        print(f"{datetime.now()}   => '{MENU_NAME}' menu is present")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            menu[0]
        )

        menu = self.element_is_visible(MENU_LOCATOR, 5)
        if not menu:
            print(f"{datetime.now()}   => '{MENU_NAME}' menu not visible")
            Common().save_current_screenshot(d, "menu_not_visible")
            Common().pytest_fail(f"Problem. '{MENU_NAME}' menu not visible")
        print(f"{datetime.now()}   => '{MENU_NAME}' menu is visible")

        time.sleep(0.5)
        menu = d.find_elements(*MENU_LOCATOR)
        ActionChains(d) \
            .move_to_element(menu[0]) \
            .pause(0.5) \
            .perform()

        print(f"{datetime.now()}   => Focus moved to '{MENU_NAME}' menu")
        del menu

        sub_menu = d.find_elements(*SUBMENU_LOCATOR)

        if len(sub_menu) == 0:
            msg = (f"The page \"{MENU_NAME}\" Menu > \"{SUBMENU_NAME}\" Submenu doesn't exist in DOM")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # ??? {msg}")

        sub_menu = self.element_is_visible(SUBMENU_LOCATOR, 5)
        if not sub_menu:
            print(f"{datetime.now()}   => '{SUBMENU_NAME}' submenu not visible")
            Common().save_current_screenshot(d, "submenu_not_visible")
            Common().pytest_fail(f"Problem. '{SUBMENU_NAME}' submenu not visible")
        print(f"{datetime.now()}   => '{SUBMENU_NAME}' submenu is visible")

        # time.sleep(0.5)
        sub_menu = d.find_elements(*SUBMENU_LOCATOR)
        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .perform()
        print(f"{datetime.now()}   => '{SUBMENU_NAME}' sub-menu focused")

        del sub_menu

