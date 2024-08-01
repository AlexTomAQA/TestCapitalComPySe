# import logging
# import re
import time

import allure
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from pages.common import Common

from pages.Menu.New.menu_new_locators import TradingMenuNew


class MainMenu(BasePage):
    # header
    SUB_MENU_LIST = (By.CSS_SELECTOR, '.menuGroup_dropdown__75ey5>div>a')
    MENU_LIST = (By.CSS_SELECTOR, '.menuGroup_item__jQrol')
    HEADER_LOGIN_BTN = (By.CSS_SELECTOR, '[data-type="btn_header_login"]')
    HEADER_SIGNUP_BTN = (By.CSS_SELECTOR, '[data-type="btn_header"]')
    HEADER_ACCOUNT_BTN = (By.CSS_SELECTOR, '.accountBtns_btnsPlace___6pn2 a')
    HEADER_ACCOUNT_BTN_OLD = (By.CSS_SELECTOR, '#wg_userarea')

    HEADER_LOGO = (By.CSS_SELECTOR, 'header .helpers_hideXs__vzgPk.logo_link__wVTFX')
    TP_LOGO = (By.CSS_SELECTOR, 'logo')
    TP_USER_MENU = (By.CSS_SELECTOR, 'em.arrow-down')
    TP_LOGOUT = (By.CSS_SELECTOR, '[data-qa="logout"]')
    HEADER_SEARCH = (By.CSS_SELECTOR, '[data-type="nav_search"]')

    # footer
    COOKIE_SETTING = (By.CSS_SELECTOR, '#onetrust-pc-btn-handler-custom')
    COOKIE_SETTING_TITLE = (By.CSS_SELECTOR, '#ot-pc-title')
    SCROLL_TO_TOP = (By.CSS_SELECTOR, '#scrollToTop')
    FOOTER_RISK_WARNING_BLOCK = (By.CSS_SELECTOR, 'footer .dark')
    FOOTER_RISK_WARNING_BLOCK_LINK = (By.CSS_SELECTOR, 'footer .dark a')

    # cookies_setting
    COOKIES_FRAME = (By.CSS_SELECTOR, '#onetrust-pc-sdk')
    STRICTLY_NECESSARY_COOKIES = (By.CSS_SELECTOR, '[aria-controls="ot-desc-id-C0001"]')
    COOKIES_DETAILS_1 = (By.CSS_SELECTOR, '[data-parent-id="C0001"]')
    COOKIES_lIST_1 = (By.CSS_SELECTOR, ".ot-sdk-column ul[style='display: block;'] li.ot-host-item")
    COOKIE_FILTER_CHBOX1 = (By.CSS_SELECTOR, "label[for='C0001-filter']")
    COOKIE_FILTER_CHBOX2 = (By.CSS_SELECTOR, "label[for='C0002-filter']")
    COOKIE_FILTER_CHBOX3 = (By.CSS_SELECTOR, "label[for='C0003-filter']")
    COOKIE_FILTER_CHBOX4 = (By.CSS_SELECTOR, "label[for='C0004-filter']")
    COOKIE_FILTER_APPLY = (By.CSS_SELECTOR, "#filter-apply-handler")
    COOKIE_FILTER = (By.CSS_SELECTOR, "#filter-btn-handler")
    COOKIE_CLEAR_FILTER = (By.CSS_SELECTOR, "#clear-filters-handler")

    # markets
    MENU_MARKETS = (By.CSS_SELECTOR, '[data-type="nav_id689"]')
    SUB_MENU_MARKETS_FOREX = (By.CSS_SELECTOR, '[data-type="nav_id690"]')
    SUB_MENU_MARKETS_INDICES = (By.CSS_SELECTOR, '[data-type="nav_id693"]')
    SUB_MENU_MARKETS_SHARES = (By.CSS_SELECTOR, '[data-type="nav_id694"]')
    SUB_MENU_MARKETS_COMMODITIES = (By.CSS_SELECTOR, '[data-type="nav_id701"]')
    SUB_MENU_MARKETS_ESG = (By.CSS_SELECTOR, '[data-type="nav_id738"]')
    SUB_MENU_MARKETS_SORT = (By.CSS_SELECTOR, '.dropdown_wrap__NQ42r')
    SUB_MENU_MARKETS_SORT_LIST = (By.CSS_SELECTOR, '.scroll_scroll__ueviH span')
    SUB_MENU_MARKETS_LIST = (By.CSS_SELECTOR, '[data-type="markets_list_deep"] a')

    # ways to trade
    MENU_WAYS_TO_TRADE = (By.CSS_SELECTOR, '[data-type="nav_id686"]')
    SUB_MENU_WAYS_TO_TRADE_1X = (By.CSS_SELECTOR, '[data-type="nav_id733"]')
    SUB_MENU_WAYS_TO_TRADE_PROFESSIONAL = (By.CSS_SELECTOR, '[data-type="nav_id752"]')
    SUB_MENU_WAYS_TO_TRADE_CFD_TRADING = (By.CSS_SELECTOR, '[data-type="nav_id734"]')
    SUB_MENU_WAYS_TO_TRADE_CFD_TRADING_CHART = (By.CSS_SELECTOR, '.main_chart__prq68')
    SUB_MENU_WAYS_TO_TRADE_CFD_TRADING_CHART_1M = (By.CSS_SELECTOR, 'button[name="M1"]')
    SUB_MENU_WAYS_TO_TRADE_CFD_TRADING_CHART_5M = (By.CSS_SELECTOR, 'button[name="M5"]')
    SUB_MENU_WAYS_TO_TRADE_CFD_TRADING_CHART_15M = (By.CSS_SELECTOR, 'button[name="M15"]')

    # trading platform
    MENU_TRADING_PLATFORM = (By.CSS_SELECTOR, '[data-type="nav_id688"]')
    SUB_MENU_TRADING_PLATFORM_WEB_PLATFORM = (By.CSS_SELECTOR, '[data-type="nav_id704"]')

    # Learn to trade
    MENU_LEARN_TO_TRADE = (By.CSS_SELECTOR, '[data-type="nav_id698"]')
    MENU_LEARN_TO_TRADE_BLOCKS_LINK_LIST = (By.CSS_SELECTOR, '[data-type="benefits_block"] .box_box__5Jmfa a')
    SUB_MENU_LEARN_TO_TRADING_STRATEGIES = (By.CSS_SELECTOR, '[data-type="nav_id697"]')

    # account
    MENU_ACCOUNT = (By.CSS_SELECTOR, '[class*="accountBtns"]>a')
    MENU_LOGIN = (By.CSS_SELECTOR, "[class='accountBtns_btnsPlace___6pn2'] [data-type='btn_header_login']")

    # Why Capital.com?
    MENU_WHY_CAPITAL = (By.CSS_SELECTOR, '[data-type="nav_id687"]')
    SUB_MENU_WHY_CAPITAL_CLIENT_FUNDS = (By.CSS_SELECTOR, '[data-type="nav_id706"]')

    @allure.step('Select "Why Capital.com?" menu, "Client funds" submenu')
    def open_way_capital_client_funds_sub_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Way_to_trade" menu, "Professional" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.main_menu_move_focus(d, cur_language, self.MENU_WHY_CAPITAL)
        self.sub_menu_move_focus_click(d, cur_language, self.SUB_MENU_WHY_CAPITAL_CLIENT_FUNDS)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Learn to trade" menu')
    def open_learn_to_trade_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Learn to trade" menu  =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.main_menu_move_focus(d, cur_language, self.MENU_LEARN_TO_TRADE)
        self.sub_menu_move_focus_click(d, cur_language, self.MENU_LEARN_TO_TRADE)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Learn to trade" menu "Trading strategies" sub-menu')
    def open_learn_to_trade_trading_strategies_sub_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Learn to trade" menu "Trading strategies" sub-menu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.main_menu_move_focus(d, cur_language, self.MENU_LEARN_TO_TRADE)
        self.sub_menu_move_focus_click(d, cur_language, self.SUB_MENU_LEARN_TO_TRADING_STRATEGIES)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

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

    @allure.step('Select "Trading platform" menu, Web platform sub-menu')
    def open_trading_platform_web_platform_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Trading platform" menu,  Web platform sub-menu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.main_menu_move_focus(d, cur_language, self.MENU_TRADING_PLATFORM)
        self.sub_menu_move_focus_click(d, cur_language, self.SUB_MENU_TRADING_PLATFORM_WEB_PLATFORM)

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

    @allure.step('Select "Way_to_trade" menu, "CFD trading" submenu')
    def open_waytotrade_cfd_trading_sub_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Way_to_trade" menu, "CFD trading submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.main_menu_move_focus(d, cur_language, self.MENU_WAYS_TO_TRADE)
        self.sub_menu_move_focus_click(d, cur_language, self.SUB_MENU_WAYS_TO_TRADE_CFD_TRADING)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Way_to_trade" menu, "1X" submenu')
    def open_waytotrade_1X_sub_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Way_to_trade" menu, "1X" =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.main_menu_move_focus(d, cur_language, self.MENU_WAYS_TO_TRADE)
        self.sub_menu_move_focus_click(d, cur_language, self.SUB_MENU_WAYS_TO_TRADE_1X)

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

    @allure.step('Select "Markets" menu')
    def open_markets_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Markets" menu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.main_menu_move_focus(d, cur_language, self.MENU_MARKETS)
        self.sub_menu_move_focus_click(d, cur_language, self.MENU_MARKETS)

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


class MenuNew(BasePage):
    """Class for Menu on license SCA"""
    # @allure.step('Select "Trading" menu, "Web platform" submenu')
    # def open_trading_menu_web_platform_submenu(self, d, cur_language, cur_country, link):
    #
    #     print(f'\n{datetime.now()}   START Open "Trading" menu, "Web platform" submenu =>')
    #     print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
    #     print(f"\n{datetime.now()}   2. Link = {link}")
    #     if not self.current_page_is(link):
    #         self.link = link
    #         self.open_page()
    #
    #     self.move_focus_to_trading_menu(d, cur_language, cur_country)
    #     self.sub_menu_web_platform_move_focus_click(d, cur_language)
    #     Common().move_pointer_to_capital_com_label(d)
    #
    #     print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
    #     return d.current_url
    #

    @allure.step("Focus moved to 'Trading' menu")
    def move_focus_to_trading_menu(self, d, test_language, test_country):
        trading_menu_locator = TradingMenuNew.MENU_SCA_TRADING

        time.sleep(0.5)
        menu = d.find_elements(*trading_menu_locator)
        if len(menu) == 0:
            print(f"{datetime.now()}   => 'Trading' menu not present")
            Common().pytest_fail(f"Bug № ??? 'Trading' menu not present for '{test_language}' language")
        print(f"{datetime.now()}   => 'Trading' menu is present")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            menu[0]
        )

        element = self.element_is_visible(trading_menu_locator, 5)
        if not element:
            print(f"{datetime.now()}   => 'Trading' menu not visible")
            # Common().save_current_screenshot(d, "scr_qr")
            Common().pytest_fail("Problem. 'Trading' menu not visible")
        print(f"{datetime.now()}   => 'Trading' menu is visible")

        time.sleep(0.5)
        menu = d.find_elements(*trading_menu_locator)
        ActionChains(d) \
            .move_to_element(menu[0]) \
            .pause(0.5) \
            .perform()

        print(f"{datetime.now()}   => Focus moved to 'Trading' menu")
        del menu
        del element

    @allure.step("Focus move to 'Web platform' submenu item and click")
    def sub_menu_web_platform_move_focus_click(self, d, test_language):
        sub_menu = d.find_elements(*TradingMenuNew.SUB_MENU_SCA_WEB_PLATFORM)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"'Trading' Menu > 'Web platform' Submenu \" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => 'Web platform' sub-menu clicked")

        del sub_menu
        return d.current_url

#    @allure.step('Select "Markets" menu, "Cryptocurrencies" submenu')
#    def open_markets_menu_cryptocurrencies_submenu(self, d, cur_language, cur_country, link):

#        print(f'\n{datetime.now()}   START Open "Markets" menu, "Cryptocurrencies" submenu =>')
#        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
#        print(f"\n{datetime.now()}   2. Link = {link}")
#        if not self.current_page_is(link):
#            self.link = link
#            self.open_page()

#        self.move_focus_to_markets_menu(d, cur_language)
#        self.sub_menu_cryptocurrencies_move_focus_click(d, cur_language)
#        Common().move_pointer_to_capital_com_label(d)

#        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
#        return d.current_url

#    @allure.step("Focus moved to 'Markets' menu")
#    def move_focus_to_markets_menu(self, d, test_language):
#        markets_menu_locator = MenuTrading.MENU_SCA_MARKETS

#        menu = self.driver.find_element(*markets_menu_locator)
#        if not menu:
#            print(f"{datetime.now()}   => 'Markets' menu not present")
#            Common().pytest_fail(f"Bug № ??? 'Markets' menu not present for '{test_language}' language")
#        print(f"{datetime.now()}   => 'Markets' menu is present")

#        self.driver.execute_script(
#            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
#            menu
#        )

#        menu = self.driver.find_element(*markets_menu_locator)
#        ActionChains(d) \
#            .move_to_element(menu) \
#            .pause(0.5) \
#            .perform()

#        print(f"{datetime.now()}   => Focus moved to 'Markets' menu")

#    @allure.step("Focus move to 'Cryptocurrencies' submenu item and click")
#    def sub_menu_cryptocurrencies_move_focus_click(self, d, test_language):
#        sub_menu = self.driver.find_element(*MenuTrading.SUB_MENU_SCA_CRYPTOCURRENCIES)

#        if not sub_menu:
#            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
#                                 f"the page \"'Markets' Menu > 'Cryptocurrencies' Submenu \" doesn't exist on production")

#        ActionChains(d) \
#            .move_to_element(sub_menu) \
#            .pause(0.5) \
#            .click() \
#            .perform()
#        print(f"\n\n{datetime.now()}   => 'Cryptocurrencies' sub-menu clicked")

#        return d.current_url
