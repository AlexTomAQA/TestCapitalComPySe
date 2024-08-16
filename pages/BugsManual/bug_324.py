"""
-*- coding: utf-8 -*-
@Time    : 2024/08/13 22:30
@Author  : Artem Dashkov
"""
import allure
import time
from datetime import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.common import Common

MENU_NAME = "[Trading]"
SUBMENU_NAME = "menu item [Demo]"
MENU_LOCATOR = (By.CSS_SELECTOR, 'span > a[data-type="nav_id798"]')
SUBMENU_LOCATOR = (By.CSS_SELECTOR, "div.grid_grid__2D3md > a[data-type='nav_id1029']")


class BUG_324(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: move focus menu section [Trading] to menu item [Demo]")
    def arrange(self, d, link):
        print(f"{datetime.now()}   1. Start Arrange: move focus menu section [Trading] to menu item [Demo]")
        print(f'\n{datetime.now()}   START move focus "{MENU_NAME}" menu, "{SUBMENU_NAME}" submenu =>')
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

    @allure.step(f"{datetime.now()}   2. Start Act.")
    def act(self, d):
        print(f"{datetime.now()}   2. Start Act.")
        sub_menu = d.find_elements(*SUBMENU_LOCATOR)

        if len(sub_menu) == 0:
            msg = (f"The page '{MENU_NAME}' Menu > '{SUBMENU_NAME}' Submenu doesn't exist in DOM")
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
        Common.save_current_screenshot(d, f"{SUBMENU_NAME}' sub-menu focused")

        del sub_menu

    @allure.step(f"{datetime.now()}   3. Start Assert.")
    def assert_(self, d):
        print(f"{datetime.now()}   3. Start Assert. Get text {SUBMENU_NAME}' sub-menu")

        text_menu_item = d.find_element(*SUBMENU_LOCATOR).text
        if text_menu_item == "":
            msg = "The text of the menu item [Demo] is not displayed"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 324: {msg}")

        print('The text of the menu item [Demo] is: ', text_menu_item)
        Common.save_current_screenshot(d, f"The text of the menu item [Demo] is displayed.")
        print(f"{datetime.now()} The text of the menu item [Demo] of the menu title [Trading tools]"
              f" in the menu section [Trading] is displayed in the header"
              f" when AR language is selected. Need to manually analyze text."
              f" Need to manually analyze text.")
        return True
