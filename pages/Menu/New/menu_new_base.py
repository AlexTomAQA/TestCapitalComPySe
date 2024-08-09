"""
-*- coding: utf-8 -*-
@Time    : 2024/07/30
@Author  : Alexander Tomelo
"""
import time
from datetime import datetime

# from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from pages.common import Common


class MenuBase(BasePage):

    def move_focus_menu_pause_move_focus_to_submenu_and_click(
            self, d, cur_language, cur_country, link, menu_name, menu_locator, submenu_name, submenu_locator):

        print(f'\n{datetime.now()}   START Open "{menu_name}" menu, "{submenu_name}" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        #     @allure.step("Focus moved to {menu_name} menu")
        time.sleep(0.5)
        menu = d.find_elements(*menu_locator)
        if len(menu) == 0:
            print(f"{datetime.now()}   => '{menu_name}' menu not present in DOM")
            Common().pytest_fail(
                f"Bug № ??? "
                f"'{menu_name}' menu not present in DOM for '{cur_country}' country '{cur_language}' language")
        print(f"{datetime.now()}   => '{menu_name}' menu is present")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            menu[0]
        )

        menu = self.element_is_visible(menu_locator, 5)
        if not menu:
            print(f"{datetime.now()}   => '{menu_name}' menu not visible")
            Common().save_current_screenshot(d, "menu_not_visible")
            Common().pytest_fail(f"Problem. '{menu_name}' menu not visible")
        print(f"{datetime.now()}   => '{menu_name}' menu is visible")

        time.sleep(0.5)
        menu = d.find_elements(*menu_locator)
        ActionChains(d) \
            .move_to_element(menu[0]) \
            .pause(0.5) \
            .perform()

        print(f"{datetime.now()}   => Focus moved to '{menu_name}' menu")
        del menu

        # @allure.step("Focus move to 'submenu_name' submenu item and click")
        sub_menu = d.find_elements(*submenu_locator)

        if len(sub_menu) == 0:
            msg = (f"For '{cur_country}' country '{cur_language}' language "
                   f"the page \"{menu_name}\" Menu > \"{submenu_name}\" Submenu doesn't exist in DOM")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # ??? {msg}")

        sub_menu = self.element_is_visible(submenu_locator, 5)
        if not sub_menu:
            print(f"{datetime.now()}   => '{submenu_name}' submenu not visible")
            Common().save_current_screenshot(d, "submenu_not_visible")
            Common().pytest_fail(f"Problem. '{submenu_name}' submenu not visible")
        print(f"{datetime.now()}   => '{submenu_name}' submenu is visible")

        # time.sleep(0.5)
        sub_menu = d.find_elements(*submenu_locator)
        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"{datetime.now()}   => '{submenu_name}' sub-menu clicked")

        del sub_menu

        Common.flag_of_bug = False
        Common().move_pointer_to_capital_com_label(d)
        print(f"{datetime.now()}   3. Cur URL = {d.current_url}")

        return d.current_url
