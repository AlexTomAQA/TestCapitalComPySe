"""
-*- coding: utf-8 -*-
@Time    : 2024/09/05 20:20
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from pages.Menu.menu import MenuSection
from selenium.webdriver.common.action_chains import ActionChains
from pages.Menu.menu_locators import MenuLanguageAndCountry

LINK_COUNTRY_FOOTER_LOCATOR = (By.XPATH, '(//span[@class="localization_btn__9zIyt"])[1]')
FIELD_COUNTRY_IN_REGIONAL_SETTINGS = (By.XPATH, '(//div[@class="select_selected__8wH_E select_gI__pn40f"])[1]')

HONK_KONG_TAIWAN_LOCATOR = (By.CSS_SELECTOR, '[data-type="nav_country_honk_kong_&_taiwan"]')
APPLY_IN_REGIONAL_SETTINGS_LOCATOR = (By.CSS_SELECTOR, '.grid_gXs__xir6K  button.button_primary__raeTg')
REGIONAL_SETTINGS_FRAME_LOCATOR = (By.CSS_SELECTOR, '.box_box__5Jmfa.box_xl__ox1gr.modal_modal__Y9d1p')

COUNTRY_IN_DROP_DOWN_LIST = (By.ID, 'selectedCountryName')

DROPDOWN_REGIONAL_SETTINGS = (By.CSS_SELECTOR, '.main_chart__prq68')
COMMODITIES_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[name='Commodities']")
SHARES_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[name='Shares']")

class BUG_362(BasePage):

    def __init__(self, browser, link, bid):
        self.button_locator = None

        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}   1. Start Arrange: open dropdown [Regional settings]")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: open dropdown [Regional settings]")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting link country to open dropdown [Regional settings]
        print(f"{datetime.now()}   Start to check link country to open dropdown [Regional settings] "
              f"in DOM on the Main page\n")
        if len(d.find_elements(*LINK_COUNTRY_FOOTER_LOCATOR)) == 0:
            msg = "The main page don't have link country to open dropdown [Regional settings] in DOM"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 362 {msg}")
        print(f"{datetime.now()}   The main page have link country to open dropdown [Regional settings] in DOM\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*LINK_COUNTRY_FOOTER_LOCATOR)
        )

        # Check visibility link country to open dropdown [Regional settings]
        print(f"{datetime.now()}   Start to check visibility link country to open dropdown [Regional settings]\n")
        if not self.element_is_visible(LINK_COUNTRY_FOOTER_LOCATOR):
            msg = ("Link country to open dropdown [Regional settings] don't visible on the main page")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 362 {msg}")
        print(f"{datetime.now()}   Link country to open dropdown [Regional settings] visible "
              f"on the main page\n")

        # Check clickable link
        print(f"{datetime.now()}   Is link country to open dropdown [Regional settings] clickable?")
        if not self.element_is_clickable(LINK_COUNTRY_FOOTER_LOCATOR):
            msg = "Link country to open dropdown [Regional settings] is not clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 362 {msg}")
        print(f"{datetime.now()}   Link country to open dropdown [Regional settings] is clickable\n")

        d.find_element(*LINK_COUNTRY_FOOTER_LOCATOR).click()
        print(f"\n{datetime.now()}   Link country to open dropdown [Regional settings] clicked\n")

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):

        print(f"\n{datetime.now()}   2. Start Act. Select 'Honk Kong & Taiwan' and click button [Apply]")

        # Check field country in Regional settings
        print(f"{datetime.now()}   Start check field country in Regional settings")
        if len(d.find_elements(*FIELD_COUNTRY_IN_REGIONAL_SETTINGS)) == 0:
            msg = f"Field country in Regional settings isn't in DOM"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 362 {msg}")
        print(f"{datetime.now()}   Field country in Regional settings is in DOM\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*FIELD_COUNTRY_IN_REGIONAL_SETTINGS)
        )

        ActionChains(self.driver) \
            .click(d.find_element(*FIELD_COUNTRY_IN_REGIONAL_SETTINGS)) \
            .pause(1) \
            .scroll_to_element(d.find_element(*HONK_KONG_TAIWAN_LOCATOR)) \
            .pause(1) \
            .move_to_element(d.find_element(*HONK_KONG_TAIWAN_LOCATOR)) \
            .pause(1) \
            .click() \
            .pause(1) \
            .perform()

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*APPLY_IN_REGIONAL_SETTINGS_LOCATOR)
        )

        d.find_element(*APPLY_IN_REGIONAL_SETTINGS_LOCATOR).click()
        print(f"\n{datetime.now()}   [Apply] button clicked\n")

    @allure.step(f"{datetime.now()}   3. Start Assert. Find widget in the block 'Our spread betting markets'")
    def assert_(self, d, cur_language, cur_country):
        print(f"{datetime.now()}   3. Start Assert. Find widget in the block 'Our spread betting markets'")

        page_menu = MenuSection(d, self.driver.current_url)
        page_menu.menu_language_and_country_move_focus(cur_language)

        elements = self.driver.find_elements(*MenuLanguageAndCountry.DROP_DOWN_LIST_COUNTRY)
        if len(elements) == 0:
            print(f"{datetime.now()}   => Cur url = {self.driver.current_url}")
            Common().pytest_fail(f"For test country '{cur_country}' problem № 1 with set country")
        ActionChains(self.driver) \
            .move_to_element(elements[0]) \
            .pause(0.5) \
            .perform()

        Common.save_current_screenshot(d, f"Select country in DROP_DOWN_LIST")

        select_country = self.driver.find_element(*COUNTRY_IN_DROP_DOWN_LIST).text
        print(f"{datetime.now()}   Displayed country is: {select_country}")
        if select_country == "Select Country":
            msg = (f"Selected country in Dropdown list [Country & Language] not displayed "
                   f"when selecting Honk Kong & Taiwan in the dropdown [Regional settings]."
                   f"Displayed country is: {select_country}")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 362: {msg}")
        elif "Kong & Taiwan" not in select_country:
            msg = (f"Selected country in Dropdown list [Country & Language] displayed "
                   f"but does not match chosen Honk Kong & Taiwan in the dropdown [Regional settings]. "
                   f"Displayed country is: {select_country}")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # 362: {msg}")

        print(f"{datetime.now()}   Selected country in Dropdown list [Country & Language] displayed"
              f"and have Kong & Taiwan, but need to analyze displayed country."
              f"Displayed country is: {select_country}")
        return True
