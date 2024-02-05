import logging
# import re
import time

import allure
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from pages.base_page import BasePage

MENU_MARKETS = (By.CSS_SELECTOR, '[data-type="nav_id689"]')
SUB_MENU_MARKETS_FOREX = (By.CSS_SELECTOR, '[data-type="nav_id690"')


class MenuSection(BasePage):

    @allure.step('Select "Markets" menu, "Forex" submenu')
    def open_markets_forex_sub_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Markets" menu, "Forex" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.main_menu_move_focus(d, cur_language, MENU_MARKETS)
        self.sub_menu_move_focus_click(d, cur_language, SUB_MENU_MARKETS_FOREX)

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
