"""
-*- coding: utf-8 -*-
@Time    : 2023/01/27 10:00
@Author  : Alexander Tomelo
"""
import logging
# import re
import time
from datetime import datetime

import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.captcha import Captcha
from pages.Menu.menu_locators import (
    Menu1101,
    MenuLanguageAndCountry,
    MenuProductsAndServices,
    MenuProductsAndServicesOurMobileApps,
    MenuWhyCapitalCom,
    MenuUS11Education,
    MenuUS11LearningHub,
    MenuUS11TradingCourses,
    MenuUS11Glossary,
    MenuUS11MarketGuides,
    MenuUS11CommoditiesTrading,
    MenuUS11ForexTrading,
    MenuUS11CryptocurrencyTrading,
    MenuUS11CFDTradingGuide,
    MenuUS11SpreadBettingGuide,
    MenuUS11ETFTrading,
    MenuUS11TradingStrategiesGuide,
    MenuUS11DayTrading,
    MenuUS11IndicesTrading,
    MenuUS11InvestmateApp,
    MenuUS11TrendTrading,
    MenuUS11WhatIsMargin,
    MenuUS11TradingPsychologyGuide, MenuUS11PositionTrading, MenuUS11SwingTrading, MenuUS11ScalpTrading,
    MenuUS11SharesTrading, MenuUS11RiskManagement, MenuUS11TechnicalAnalysis, MenuUS11HELP, MenuUS11LearnToTrade,
    MenuUS11TradingStrategies, MenuUS11EssentialsOfTrading, MenuUS11MarketGuidesNew,
    MenuUS01Markets,
    MenuUS01Indices, MenuUS0102MarketsShares, MenuUS0103MarketsForex, MenuUS0104Commodities, MenuUS0101AllMarkets,
    MenuUS0106MarketsCryptocurrencies, MenuUS0107MarketsESG, MenuUS0109MarketsCFDCalculator, MenuUS55WaysToTrade,
    MenuUS02NewsAndAnalysis,
    MenuUS0201MarketAnalysis,
    MenuUS11MarketAnalysis, MenuProductsAndServicesDemoAccount
)

from pages.base_page import BasePage
from pages.common import Common

# from pages.common import bug_11_01_03_00

logger = logging.getLogger()


class MenuSection(BasePage):
    """
    MenuSection class - класс работы с меню в хедере
    Аргументы при создании объекта:
        wd - driver
        main_page_link - страница, на которой расположено меню
        flag_set_menu - признак того, что нужное меню выбрано (установлено), необязательный аргумент. По умолчанию =
        False
    """

    def __init__(self, wd, main_page_link, flag_set_menu=False):
        self.flag_set_menu = flag_set_menu
        super().__init__(wd, main_page_link)

    # bug_11_01_03_00

    @allure.step('Select "Learn to trade" menu, "Risk-management guide')
    def open_learn_to_trade_risk_management_guide_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Education" menu, "Risk-management guide" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_learn_to_trade_move_focus(d, cur_language, cur_country)
        self.sub_menu_risk_management_guide_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        Common.flag_of_bug = False

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Learn to trade" menu, "Technical analysis" submenu')
    def open_learn_to_trade_technical_analysis_guide_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Education" menu, "Technical analysis" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_learn_to_trade_move_focus(d, cur_language, cur_country)
        self.sub_menu_technical_analysis_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        Common.flag_of_bug = False

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Learn to trade" menu, "Market analysis" submenu')
    def open_learn_to_trade_market_analysis_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Learn to trade" menu, "Market analysis" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_learn_to_trade_move_focus(d, cur_language, cur_country)
        self.sub_menu_market_analysis_move_focus_click(d, cur_language, cur_country)
        Common().move_pointer_to_capital_com_label(d)
        Common.flag_of_bug = False

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Learn to trade" menu, "Help" submenu')
    def open_learn_to_trade_help_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Learn to trade" menu, "Help" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_learn_to_trade_move_focus(d, cur_language, cur_country)
        self.sub_menu_help_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        Common.flag_of_bug = False

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select and click "Learn to trade" menu')
    def open_learn_to_trade_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Learn to trade" menu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_learn_to_trade_move_focus(d, cur_language, cur_country)
        self.sub_menu_learn_to_trade_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        Common.flag_of_bug = False

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Education" menu, "Spread betting guide" submenu')
    def open_education_spread_betting_guide_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Education" menu, "Spread betting guide" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_education_move_focus(d, cur_language, cur_country)
        self.sub_menu_spread_betting_guide_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        Common.flag_of_bug = False

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step(f'{datetime.now()}   Select "Education" menu, "CFD trading guide" submenu')
    def open_education_cfd_trading_menu(self, d, cur_language, cur_country, link):
        # self.bug_flag = bug_11_01_03_00

        print(f'\n{datetime.now()}   START Open "Education" menu, "CFD trading guide" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_education_move_focus(d, cur_language, cur_country)
        self.sub_menu_cfd_trading_guide_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        Common.flag_of_bug = False

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Education" menu, "Forex trading" submenu')
    def open_education_forex_trading_menu(self, d, cur_language, cur_country, link):

        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_education_move_focus(d, cur_language, cur_country)
        self.sub_menu_forex_trading_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        Common.flag_of_bug = False

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Education" menu, "Shares trading" submenu')
    def open_education_shares_trading_menu(self, d, cur_language, cur_country, link):

        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_education_move_focus(d, cur_language, cur_country)
        self.sub_menu_shares_trading_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        Common.flag_of_bug = False

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Education" menu, "Commodities trading" submenu')
    def open_education_commodities_trading_menu(self, d, cur_language, cur_country, link):

        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_education_move_focus(d, cur_language, cur_country)
        self.sub_menu_commodities_trading_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        Common.flag_of_bug = False

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Education" menu, "Indices trading" submenu')
    def open_education_indices_trading_menu(self, d, cur_language, cur_country, link):

        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_education_move_focus(d, cur_language, cur_country)
        self.sub_menu_indices_trading_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        Common.flag_of_bug = False

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Education" menu, "Cryptocurrency trading" submenu')
    def open_education_cryptocurrency_trading_menu(self, d, cur_language, cur_country, link):

        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_education_move_focus(d, cur_language, cur_country)
        self.sub_menu_cryptocurrency_trading_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        Common.flag_of_bug = False

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Education" menu, "Trading psychology guides" submenu')
    def open_education_trading_psychology_guides_menu(self, d, cur_language, cur_country, link):

        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_education_move_focus(d, cur_language, cur_country)
        self.sub_menu_trading_psychology_guide_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        Common.flag_of_bug = False

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Ways to trade" menu, "Professional" submenu')
    def open_ways_to_trade_professional_menu(self, d, cur_language, cur_country, link):
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_ways_to_trade_move_focus(d, cur_language, cur_country)
        self.sub_menu_professional_move_focus_click(d, cur_language, cur_country)
        Common().move_pointer_to_capital_com_label(d)
        Common.flag_of_bug = False

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step("Move focus to 'Ways to trade' menu section")
    def menu_ways_to_trade_move_focus(self, d, test_language, test_country):
        menu_locator = None
        if test_country == "gb" and test_language == "":
            menu_locator = MenuUS55WaysToTrade.MENU_WAYS_TO_TRADE

        time.sleep(0.5)
        menu = d.find_elements(*menu_locator)
        if len(menu) == 0:
            print(f"{datetime.now()}   => 'Ways to trade' menu not present")
            # allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
            Common().pytest_fail(f"Bug # ? 'Ways to trade' menu not present for '{test_language}' language")
        print(f"{datetime.now()}   => 'Ways to trade' menu is present")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            menu[0]
        )

        element = self.element_is_visible(menu_locator, 5)
        if not element:
            print(f"{datetime.now()}   => 'Ways to trade' menu not visible")
            Common().pytest_fail("Bug # ? 'Ways to trade' menu not visible")
        print(f"{datetime.now()}   => 'Ways to trade' menu is visible")

        time.sleep(0.5)
        menu = d.find_elements(*menu_locator)
        ActionChains(d) \
            .move_to_element(menu[0]) \
            .pause(0.5) \
            .perform()

        del menu
        del element
        print(f"{datetime.now()}   => Focus moved to 'Ways to trade' menu")

    @allure.step("Focus move to 'Professional' menu item and click")
    def sub_menu_professional_move_focus_click(self, d, test_language, test_country):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS55WaysToTrade.SUB_MENU_WAYS_TO_TRADE_PROFESSIONAL)

        if len(sub_menu) == 0:
            Common().pytest_fail(
                f"Bug # ??? For test language '{test_language}' "
                f"the page \"Ways to trade > Menu item [Professional]\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step("Open 'Language and Country' menu section.")
    def menu_language_and_country_move_focus(self, test_language):

        d = self.driver
        # menu = list()
        menu = d.find_elements(*MenuLanguageAndCountry.MENU_LANGUAGE_AND_COUNTRY)  # not Glossary
        if len(menu) == 0:
            print(f"{datetime.now()}   => Language and Country menu not present")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
            pytest.skip(f"For '{test_language}' language menu [Language & Country] not present")
        print(f"{datetime.now()}   => Language and Country menu is present")

        if not self.element_is_visible(MenuLanguageAndCountry.MENU_LANGUAGE_AND_COUNTRY, 5):
            print(f"{datetime.now()}   => Language and Country menu not visible")
            Common().pytest_fail("Language and Country menu not visible")
        print(f"{datetime.now()}   => Language and Country menu is visible")

        time.sleep(0.5)
        ActionChains(d) \
            .move_to_element(d.find_element(*MenuLanguageAndCountry.MENU_LANGUAGE_AND_COUNTRY)) \
            .pause(0.5) \
            .perform()
        # del menu

        print(f"{datetime.now()}   => Focus is moved on Language and Country menu ")

    @allure.step("Move focus to 'Learn to trade' menu section")
    def menu_learn_to_trade_move_focus(self, d, test_language, test_country):
        ed_menu_locator = None
        if test_country == "gb" and test_language == "":
            ed_menu_locator = MenuUS11Education.SUB_MENU_EN_GB_LEARN_TO_TRADE

        time.sleep(0.5)
        menu = d.find_elements(*ed_menu_locator)
        if len(menu) == 0:
            print(f"{datetime.now()}   => 'Learn to trade' menu not present")
            # allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
            Common().pytest_fail(f"Bug # ? 'Learn to trade' menu not present for '{test_language}' language")
        print(f"{datetime.now()}   => 'Learn to trade' menu is present")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            menu[0]
        )

        element = self.element_is_visible(ed_menu_locator, 5)
        if not element:
            print(f"{datetime.now()}   => 'Learn to trade' menu not visible")
            Common().pytest_fail("Bug # ? 'Learn to trade' menu not visible")
        print(f"{datetime.now()}   => 'Learn to trade' menu is visible")

        time.sleep(0.5)
        menu = d.find_elements(*ed_menu_locator)
        ActionChains(d) \
            .move_to_element(menu[0]) \
            .pause(0.5) \
            .perform()

        del menu
        del element
        print(f"{datetime.now()}   => Focus moved to 'Learn to trade' menu")

    @allure.step("Focus moved to 'Education' menu")
    def menu_education_move_focus(self, d, test_language, test_country):
        ed_menu_locator = None
        if test_language == "" and test_country == "gb":
            ed_menu_locator = MenuUS11Education.SUB_MENU_EN_GB_LEARN_TO_TRADE
        else:
            match test_language:
                case "":
                    ed_menu_locator = MenuUS11Education.SUB_MENU_EN_LEARN_TO_TRADE
                case "ar":
                    ed_menu_locator = MenuUS11Education.SUB_MENU_AR_LEARN_TO_TRADE
                case "de":
                    ed_menu_locator = MenuUS11Education.SUB_MENU_DE_LEARN_TO_TRADE
                case "el":
                    ed_menu_locator = MenuUS11Education.SUB_MENU_EL_LEARN_TO_TRADE
                case "es":
                    ed_menu_locator = MenuUS11Education.SUB_MENU_ES_LEARN_TO_TRADE
                case "fr":
                    ed_menu_locator = MenuUS11Education.SUB_MENU_FR_LEARN_TO_TRADE
                case "it":
                    ed_menu_locator = MenuUS11Education.SUB_MENU_IT_LEARN_TO_TRADE
                case "hu":
                    ed_menu_locator = MenuUS11Education.SUB_MENU_HU_LEARN_TO_TRADE
                case "nl":
                    ed_menu_locator = MenuUS11Education.SUB_MENU_NL_LEARN_TO_TRADE
                case "pl":
                    ed_menu_locator = MenuUS11Education.SUB_MENU_PL_LEARN_TO_TRADE
                case "ro":
                    ed_menu_locator = MenuUS11Education.SUB_MENU_RO_LEARN_TO_TRADE
                case "ru":
                    ed_menu_locator = MenuUS11Education.SUB_MENU_RU_LEARN_TO_TRADE
                case "zh":
                    ed_menu_locator = MenuUS11Education.SUB_MENU_ZH_LEARN_TO_TRADE
                case "cn":
                    ed_menu_locator = MenuUS11Education.SUB_MENU_CN_LEARN_TO_TRADE

        time.sleep(0.5)
        menu = d.find_elements(*ed_menu_locator)
        if len(menu) == 0:
            print(f"{datetime.now()}   => Education menu not present in DOM")
            # Common().save_current_screenshot(d, "scr_qr")
            Common().pytest_fail(f"Bug № ??? Education menu not present in DOM for '{test_language}' language")
        print(f"{datetime.now()}   => Education menu is present in DOM")

        element = self.element_visibility_of(menu[0], 5)
        if not element:
            print(f"{datetime.now()}   => Education menu not visible")
            Common().pytest_fail("Problem. Education menu not visible")
        print(f"{datetime.now()}   => Education menu is visible")

        time.sleep(0.5)
        menu = d.find_elements(*ed_menu_locator)
        ActionChains(d) \
            .move_to_element(menu[0]) \
            .pause(0.5) \
            .perform()

        print(f"{datetime.now()}   => Focus moved to Education menu")
        del menu
        del element

    @allure.step("Focus moved to 'Markets' menu")
    def move_focus_to_markets_menu(self, d, test_language, test_country):
        markets_menu_locator = None
        if test_language == "" and test_country == "gb":
            markets_menu_locator = MenuUS01Markets.MENU_EN_GB_MARKETS  # новая верстка, FCA
        else:
            match test_language:
                case "":
                    markets_menu_locator = MenuUS01Markets.MENU_MARKETS_EN_BUTTON
                case "ar":
                    markets_menu_locator = MenuUS01Markets.MENU_MARKETS_AR_BUTTON
                case "de":
                    markets_menu_locator = MenuUS01Markets.MENU_MARKETS_DE_BUTTON
                case "el":
                    markets_menu_locator = MenuUS01Markets.MENU_MARKETS_EL_BUTTON
                case "es":
                    markets_menu_locator = MenuUS01Markets.MENU_MARKETS_ES_BUTTON
                case "fr":
                    markets_menu_locator = MenuUS01Markets.MENU_MARKETS_FR_BUTTON
                case "it":
                    markets_menu_locator = MenuUS01Markets.MENU_MARKETS_IT_BUTTON
                case "hu":
                    markets_menu_locator = MenuUS01Markets.MENU_MARKETS_HU_BUTTON
                case "nl":
                    markets_menu_locator = MenuUS01Markets.MENU_MARKETS_NL_BUTTON
                case "pl":
                    markets_menu_locator = MenuUS01Markets.MENU_MARKETS_PL_BUTTON
                case "ro":
                    markets_menu_locator = MenuUS01Markets.MENU_MARKETS_RO_BUTTON
                case "ru":
                    markets_menu_locator = MenuUS01Markets.MENU_MARKETS_RU_BUTTON
                case "zh":
                    markets_menu_locator = MenuUS01Markets.MENU_MARKETS_ZH_BUTTON
                case "cn":
                    markets_menu_locator = MenuUS01Markets.MENU_MARKETS_CN_BUTTON

        time.sleep(0.5)
        menu = d.find_elements(*markets_menu_locator)
        if len(menu) == 0:
            print(f"{datetime.now()}   => 'Markets' menu not present")
            # Common().save_current_screenshot(d, "scr_qr")
            Common().pytest_fail(f"Bug № ??? 'Markets' menu not present for '{test_language}' language")
        print(f"{datetime.now()}   => 'Markets' menu is present")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            menu[0]
        )

        element = self.element_is_visible(markets_menu_locator, 5)
        if not element:
            print(f"{datetime.now()}   => 'Markets' menu not visible")
            # Common().save_current_screenshot(d, "scr_qr")
            Common().pytest_fail("Problem. 'Markets' menu not visible")
        print(f"{datetime.now()}   => 'Markets' menu is visible")

        time.sleep(0.5)
        menu = d.find_elements(*markets_menu_locator)
        ActionChains(d) \
            .move_to_element(menu[0]) \
            .pause(0.5) \
            .perform()

        print(f"{datetime.now()}   => Focus moved to 'Markets' menu")
        del menu
        del element

    @allure.step("Focus move to 'learning hub' menu item and click")
    def sub_menu_learning_hub_move_focus_click(self, d, test_language, test_country):
        sub_menu = None
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_EN_ITEM_LEARNING_HUB)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_AR_ITEM_LEARNING_HUB)
            case "de":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_DE_ITEM_LEARNING_HUB)
            case "el":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_EL_ITEM_LEARNING_HUB)
            case "es":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_ES_ITEM_LEARNING_HUB)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_FR_ITEM_LEARNING_HUB)
            case "it":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_IT_ITEM_LEARNING_HUB)
            case "hu":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_HU_ITEM_LEARNING_HUB)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_NL_ITEM_LEARNING_HUB)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_PL_ITEM_LEARNING_HUB)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_RO_ITEM_LEARNING_HUB)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_RU_ITEM_LEARNING_HUB)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_ZH_ITEM_LEARNING_HUB)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_CN_ITEM_LEARNING_HUB)

        if len(sub_menu) == 0:
            Common().save_current_screenshot(d, "SavePNG")
            Common().pytest_fail(
                f"Bug # ??? For language '{test_language}' \"Education > Learning hub\" submenu doesn't exist")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        del sub_menu
        return d.current_url

    @allure.step("Focus move to 'Basics_of_trading' menu item and click")
    def sub_menu_basics_of_trading_move_focus_click(self, d, test_language, test_country):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_EN_ITEM_BASICS_OF_TRADING)
            case "ar":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_AR_ITEM_BASICS_OF_TRADING)
            case "de":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_DE_ITEM_BASICS_OF_TRADING)
            case "el":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_EL_ITEM_BASICS_OF_TRADING)
            case "es":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_ES_ITEM_BASICS_OF_TRADING)
            case "fr":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_FR_ITEM_BASICS_OF_TRADING)
            case "it":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_IT_ITEM_BASICS_OF_TRADING)
            case "hu":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_HU_ITEM_BASICS_OF_TRADING)
            case "nl":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_NL_ITEM_BASICS_OF_TRADING)
            case "pl":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_PL_ITEM_BASICS_OF_TRADING)
            case "ro":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_RO_ITEM_BASICS_OF_TRADING)
            case "ru":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_RU_ITEM_BASICS_OF_TRADING)
            case "zh":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_ZH_ITEM_BASICS_OF_TRADING)
            case "cn":
                sub_menu = d.find_elements(*Menu1101.SUB_MENU_CN_ITEM_BASICS_OF_TRADING)

        if len(sub_menu) == 0:
            Common().pytest_fail(
                f"Bug # ??? For test language '{test_language}' "
                f"the page \"Education > Menu item [The basics of trading]\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step("Focus move to 'Glossary' menu item and click")
    def sub_menu_glossary_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_EN_GLOSSARY)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_AR_GLOSSARY)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_CN_GLOSSARY)
            case "de":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_DE_GLOSSARY)
            case "el":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_EL_GLOSSARY)
            case "es":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_ES_GLOSSARY)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_FR_GLOSSARY)
            case "hr":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_HR_GLOSSARY)
            case "hu":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_HU_GLOSSARY)
            case "it":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_IT_GLOSSARY)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_NL_GLOSSARY)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_PL_GLOSSARY)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_RO_GLOSSARY)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_RU_GLOSSARY)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_ZH_GLOSSARY)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Glossary of trading terms\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => Glossary sub-menu clicked")

        del sub_menu
        return d.current_url

    @allure.step("Move focus to 'Forex trading' submenu and click")
    def sub_menu_forex_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_EN_FOREX_TRADING)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_AR_FOREX_TRADING)
            case "de":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_DE_FOREX_TRADING)
            case "es":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_ES_FOREX_TRADING)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_FR_FOREX_TRADING)  # одна страница
            case "it":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_IT_FOREX_TRADING)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_RU_FOREX_TRADING)  # одна страница
            case "zh":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_ZH_FOREX_TRADING)  # одна страница
            case "cn":
                sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_CN_FOREX_TRADING)  # одна страница

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Forex Trading\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"{datetime.now()}   => Focus moved to Forex trading sub-menu and clicked")

        del sub_menu
        return d.current_url

    @allure.step("Focus move to 'Trading courses' submenu and click")
    def sub_menu_trading_courses_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_EN_ITEM_TRADING_COURSES)
            case "de":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_DE_ITEM_TRADING_COURSES)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_RU_ITEM_TRADING_COURSES)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_FR_ITEM_TRADING_COURSES)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_AR_ITEM_TRADING_COURSES)
            case "el":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_EL_ITEM_TRADING_COURSES)
            case "es":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ES_ITEM_TRADING_COURSES)
            case "it":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_IT_ITEM_TRADING_COURSES)
            case "hu":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_HU_ITEM_TRADING_COURSES)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_NL_ITEM_TRADING_COURSES)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_PL_ITEM_TRADING_COURSES)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_RO_ITEM_TRADING_COURSES)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ZH_ITEM_TRADING_COURSES)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_CN_ITEM_TRADING_COURSES)

        if len(sub_menu) == 0:
            pytest.skip(f"For '{test_language}' language [Trading courses] submenu item "
                        f"doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step("Focus move to 'Commodities trading' submenu and click")
    def sub_menu_commodities_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "ar":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_AR_COMMODITIES_TRADING)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_CN_COMMODITIES_TRADING)
            case "de":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_DE_COMMODITIES_TRADING)
            case "":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_EN_COMMODITIES_TRADING)
            case "es":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_ES_COMMODITIES_TRADING)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_FR_COMMODITIES_TRADING)
            case "it":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_IT_COMMODITIES_TRADING)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_NL_COMMODITIES_TRADING)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_PL_COMMODITIES_TRADING)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_RO_COMMODITIES_TRADING)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_RU_COMMODITIES_TRADING)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_ZH_COMMODITIES_TRADING)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Education > Commodities Trading\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step("Focus move to 'Market guides' submenu and click")
    def sub_menu_market_guides_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_EN_ITEM_MARKET_GUIDES)
            case "de":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_DE_ITEM_MARKET_GUIDES)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_RU_ITEM_MARKET_GUIDES)
            case "bg":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_BG_ITEM_MARKET_GUIDES)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_FR_ITEM_MARKET_GUIDES)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_AR_ITEM_MARKET_GUIDES)
            case "el":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_EL_ITEM_MARKET_GUIDES)
            case "es":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_ES_ITEM_MARKET_GUIDES)
            case "it":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_IT_ITEM_MARKET_GUIDES)
            case "hu":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_HU_ITEM_MARKET_GUIDES)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_NL_ITEM_MARKET_GUIDES)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_PL_ITEM_MARKET_GUIDES)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_RO_ITEM_MARKET_GUIDES)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_ZH_ITEM_MARKET_GUIDES)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_CN_ITEM_MARKET_GUIDES)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Education | Menu title [Market Guides]\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step("Focus move to 'Cryptocurrency trading' submenu and click")
    def sub_menu_cryptocurrency_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_EN_CRYPTOCURRENCY_TRADING)
            case "de":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_DE_CRYPTOCURRENCY_TRADING)
            case "es":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_ES_CRYPTOCURRENCY_TRADING)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_FR_CRYPTOCURRENCY_TRADING)
            case "it":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_IT_CRYPTOCURRENCY_TRADING)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_PL_CRYPTOCURRENCY_TRADING)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_RO_CRYPTOCURRENCY_TRADING)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_RU_CRYPTOCURRENCY_TRADING)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_ZH_CRYPTOCURRENCY_TRADING)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_CN_CRYPTOCURRENCY_TRADING)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education -> Cryptocurrency trading\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        print(f"{datetime.now()}   => Cryptocurrency trading submenu focus moved and clicked")

        return d.current_url

    @allure.step("Focus move to 'CFD trading guide' submenu and click")
    def sub_menu_cfd_trading_guide_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "de":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_DE_CFD_TRADING_GUIDE)
            # case "el": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_EL_CFD_TRADING_GUIDE)
            case "":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_EN_CFD_TRADING_GUIDE)
            case "es":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_ES_CFD_TRADING_GUIDE)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_FR_CFD_TRADING_GUIDE)
            case "it":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_IT_CFD_TRADING_GUIDE)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_NL_CFD_TRADING_GUIDE)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_PL_CFD_TRADING_GUIDE)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_RO_CFD_TRADING_GUIDE)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_RU_CFD_TRADING_GUIDE)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_ZH_CFD_TRADING_GUIDE)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Education->CFD trading guide\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        print(f"{datetime.now()}   => CFD trading guide submenu focus moved and clicked")

        return d.current_url

    @allure.step("Focus move to 'Spread betting guide' submenu and click")
    def sub_menu_spread_betting_guide_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11SpreadBettingGuide.SUB_MENU_EN_SPREAD_BETTING_GUIDE)
            case "es":
                sub_menu = d.find_elements(*MenuUS11SpreadBettingGuide.SUB_MENU_ES_SPREAD_BETTING_GUIDE)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11SpreadBettingGuide.SUB_MENU_CN_SPREAD_BETTING_GUIDE)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Education > Spread betting guide\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        print(f"{datetime.now()}   => Spread betting guide submenu focus moved and clicked")

        return d.current_url

    @allure.step("Set language")
    def set_language(self, cur_language):

        if cur_language == "":
            cur_language = "en"
        css_loc_lang = 'header a[data-type="nav_lang_' + cur_language + '"]'
        language_str_list = self.driver.find_elements(By.CSS_SELECTOR, css_loc_lang)
        if len(language_str_list) == 0:
            print(f"{datetime.now()}   => Cur url = {self.driver.current_url}")
            Common().pytest_fail(f"For test language '{cur_language}' problem № 2 with set language")

        print(f"{datetime.now()}   Move focus on {cur_language} item and click =>")
        ActionChains(self.driver) \
            .move_to_element(language_str_list[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        print(f"{datetime.now()}   => Focus moved on {cur_language} item and clicked")
        print(f"{datetime.now()}   => Cur url = {self.driver.current_url}")
        return self.driver.current_url

    @allure.step("Set country (licence)")
    def set_country(self, cur_country):

        elements = self.driver.find_elements(*MenuLanguageAndCountry.DROP_DOWN_LIST_COUNTRY)
        if len(elements) == 0:
            print(f"{datetime.now()}   => Cur url = {self.driver.current_url}")
            Common().pytest_fail(f"For test country '{cur_country}' problem № 1 with set country")

        ActionChains(self.driver) \
            .move_to_element(elements[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        css_sel_country = 'a[data-country="' + cur_country + '"]'
        country_str_list = self.driver.find_elements(By.CSS_SELECTOR, css_sel_country)
        if len(country_str_list) == 0:
            # time.sleep(10)
            Common().pytest_fail(f"Test country '{cur_country}' not present in country list")

        ActionChains(self.driver) \
            .move_to_element(country_str_list[0]) \
            .pause(0.5) \
            .click(country_str_list[0]) \
            .perform()

        print(f"{datetime.now()}   => Cur url = {self.driver.current_url}")
        return self.driver.current_url

    @allure.step("Focus move to 'ETF trading' submenu and click")
    def sub_menu_etf_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "ar":
                sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_AR_ETF_TRADING)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_CN_ETF_TRADING)
            case "de":
                sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_DE_ETF_TRADING)
            case "":
                sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_EN_ETF_TRADING)
            case "es":
                sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_ES_ETF_TRADING)
            case "it":
                sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_IT_ETF_TRADING)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_RU_ETF_TRADING)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Education->ETF trading\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step("Focus move to 'Trading Strategies Guide' submenu and click")
    def sub_menu_trading_strategies_guide_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_EN_TRADING_STRATEGIES_GUIDE)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_AR_TRADING_STRATEGIES_GUIDE)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_CN_TRADING_STRATEGIES_GUIDE)
            case "de":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_DE_TRADING_STRATEGIES_GUIDE)
            case "el":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_EL_TRADING_STRATEGIES_GUIDE)
            case "es":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_ES_TRADING_STRATEGIES_GUIDE)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_FR_TRADING_STRATEGIES_GUIDE)
            case "hu":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_HU_TRADING_STRATEGIES_GUIDE)
            case "it":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_IT_TRADING_STRATEGIES_GUIDE)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_NL_TRADING_STRATEGIES_GUIDE)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_PL_TRADING_STRATEGIES_GUIDE)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_RO_TRADING_STRATEGIES_GUIDE)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_RU_TRADING_STRATEGIES_GUIDE)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_ZH_TRADING_STRATEGIES_GUIDE)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Education->Trading Strategies Guide\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step("Focus move to 'Day Trading' submenu and click")
    def sub_menu_day_trading_move_focus_click(self, d, test_language):
        sub_menu = d.find_elements(*MenuUS11DayTrading.SUB_MENU_ALL_DAY_TRADING)

        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .pause(0.5) \
                .click() \
                .perform()
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Day Trading\" doesn't exist on production")
        return d.current_url

    @allure.step("Focus move to 'Indices Trading' submenu and click")
    def sub_menu_indices_trading_move_focus_click(self, d, test_language):
        sub_menu = None
        logger.info(f"Click 'Indices Trading' hyperlink in submenu")
        match test_language:
            case "ar":
                sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_AR_INDICES_TRADING)
            case "de":
                sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_DE_INDICES_TRADING)
            case "es":
                sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_ES_INDICES_TRADING)
            case "it":
                sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_IT_INDICES_TRADING)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_CN_INDICES_TRADING)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_ZH_INDICES_TRADING)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_RU_INDICES_TRADING)
            case _:
                sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_ALL_INDICES_TRADING)

        if len(sub_menu) > 0:
            logger.info(f"The menu item is found")
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .pause(0.5) \
                .click() \
                .perform()
            logger.info(f"Indices Trading menu click")
        else:
            logger.warning(f"For test language '{test_language}' "
                           f"the page \"Education->Indices Trading\" doesn't exist on production")
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Education->Indices Trading\" doesn't exist on production")
        return d.current_url

    @allure.step("Focus move to 'Investmate app' submenu and click")
    def sub_menu_investmate_app_move_focus_click(self, d, test_language):
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_ALL_INVESTMATE_APP)
            case "de":
                sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_DE_INVESTMATE_APP)
            case "es":
                sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_ES_INVESTMATE_APP)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_FR_INVESTMATE_APP)
            case "it":
                sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_IT_INVESTMATE_APP)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_NL_INVESTMATE_APP)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_PL_INVESTMATE_APP)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_CN_INVESTMATE_APP)
            case _:
                sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_ALL_INVESTMATE_APP)

        if sub_menu and len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .pause(0.5) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => 'Investmate App' menu click")
        else:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Education->Investmate app\" doesn't exist on production")
        return d.current_url

    @allure.step("Focus move to 'Trend Trading' submenu item and click")
    def sub_menu_trend_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS11TrendTrading.SUB_MENU_EN_ITEM_TREND_TRADING)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Education->Trend Trading\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => Trend trading menu item clicked")

        del sub_menu
        return d.current_url

    @allure.step("Focus move to 'What is a margin?' submenu item and click")
    def sub_menu_what_is_a_margin_move_focus_click(self, d, test_language):
        sub_menu = d.find_elements(*MenuUS11WhatIsMargin.SUB_MENU_ALL_WHAT_IS_A_MARGIN)
        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .pause(0.5) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => 'What is a margin?' menu click")
        else:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Education->What is a margin?\" doesn't exist on production")
        return d.current_url

    @allure.step("Focus move to 'Trading Psychology Guide' submenu item and click")
    def sub_menu_trading_psychology_guide_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_EN_TRADING_PSYCHOLOGY_GUIDE)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_AR_TRADING_PSYCHOLOGY_GUIDE)
            case "de":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_DE_TRADING_PSYCHOLOGY_GUIDE)
            case "el":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_EL_TRADING_PSYCHOLOGY_GUIDE)
            case "es":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_ES_TRADING_PSYCHOLOGY_GUIDE)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_FR_TRADING_PSYCHOLOGY_GUIDE)
            case "it":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_IT_TRADING_PSYCHOLOGY_GUIDE)
            case "hu":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_HU_TRADING_PSYCHOLOGY_GUIDE)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_NL_TRADING_PSYCHOLOGY_GUIDE)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_PL_TRADING_PSYCHOLOGY_GUIDE)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_RO_TRADING_PSYCHOLOGY_GUIDE)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_RU_TRADING_PSYCHOLOGY_GUIDE)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_ZH_TRADING_PSYCHOLOGY_GUIDE)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_CN_TRADING_PSYCHOLOGY_GUIDE)

        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .pause(0.5) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => Trading Psychology Guide menu click")
        else:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the submenu \"Education->Trading Psychology Guide\" doesn't exist")
        return d.current_url

    @allure.step("Focus move to 'Position Trading' submenu item and click")
    def sub_menu_position_trading_move_focus_click(self, d, test_language):
        sub_menu = d.find_elements(*MenuUS11PositionTrading.SUB_MENU_ALL_POSITION_TRADING)
        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .pause(0.5) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => 'Position Trading' menu click")
        else:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Education->Position Trading\" doesn't exist on production")
        return d.current_url

    @allure.step("Focus move to 'Swing Trading' submenu item and click")
    def sub_menu_swing_trading_move_focus_click(self, d, test_language):
        sub_menu = d.find_elements(*MenuUS11SwingTrading.SUB_MENU_ALL_SWING_TRADING)
        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .pause(0.5) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => 'Swing Trading' menu click")
        else:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Education->Swing Trading\" doesn't exist on production")
        return d.current_url

    @allure.step("Focus move to 'Scalp Trading' submenu item and click")
    def sub_menu_scalp_trading_move_focus_click(self, d, test_language):
        sub_menu = d.find_elements(*MenuUS11ScalpTrading.SUB_MENU_ALL_SCALP_TRADING)

        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .pause(0.5) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => 'Scalp Trading' menu click")
        else:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Education->Scalp Trading\" doesn't exist on production")
        return d.current_url

    @allure.step("Focus move to 'Shares trading' submenu item and click")
    def sub_menu_shares_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_EN_SHARES_TRADING)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_AR_SHARES_TRADING)
            case "de":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_DE_SHARES_TRADING)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_CN_SHARES_TRADING)
            case "cs":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_DE_SHARES_TRADING)
            case "es":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_ES_SHARES_TRADING)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_FR_SHARES_TRADING)
            case "it":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_IT_SHARES_TRADING)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_NL_SHARES_TRADING)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_PL_SHARES_TRADING)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_RO_SHARES_TRADING)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_RU_SHARES_TRADING)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11SharesTrading.SUB_MENU_ZH_SHARES_TRADING)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Education > Shared Trading\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => Shares trading sub-menu clicked")

        del sub_menu
        return d.current_url

    @allure.step("Focus move to 'Risk-management guide' submenu item and click")
    def sub_menu_risk_management_guide_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS11RiskManagement.SUB_MENU_EN_RISK_MANAGEMENT)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Learn to trade->Risk-management guide\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => Risk-management guide menu item clicked")

        del sub_menu
        return d.current_url

    @allure.step("Focus move to 'Technical analysis' submenu item and click")
    def sub_menu_technical_analysis_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS11TechnicalAnalysis.SUB_MENU_EN_TECHNICAL_ANALYSIS)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Learn to trade->Risk-management guide\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => Risk-management guide menu item clicked")

        del sub_menu
        return d.current_url

    @allure.step("Focus move to 'Help' submenu item and click")
    def sub_menu_help_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS11HELP.SUB_MENU_EN_HELP)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Learn to trade->Help\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => Help menu item clicked")

        del sub_menu
        return d.current_url

    @allure.step("Focus move to 'Learn to trade' menu and click")
    def sub_menu_learn_to_trade_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS11LearnToTrade.SUB_MENU_EN_LEARN_TO_TRADE)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Learn to trade\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => 'Learn to trade' menu clicked")

        del sub_menu
        return d.current_url

    @allure.step('Select "Learn to trade" menu, sub menu "Trading Strategies(FCA license)')
    def open_learn_to_trade_trading_strategies_new_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Learn to trade" menu, "Trading Strategies" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_learn_to_trade_move_focus(d, cur_language, cur_country)
        self.sub_menu_trading_strategies_new_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step("Focus move to 'Trading Strategies(FCA)' submenu item and click")
    def sub_menu_trading_strategies_new_move_focus_click(self, d, test_language):
        sub_menu = list()

        if test_language == "":
            sub_menu = d.find_elements(*MenuUS11TradingStrategies.SUB_MENU_EN_TRADING_STRATEGIES)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Learn to trade->Trading Strategies\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => Trading Strategies menu item clicked")

        del sub_menu
        return d.current_url

    @allure.step('Select "Why Capital.com?" menu, "Client funds" submenu')
    def open_why_capital_com_client_funds_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Why Capital.com?" menu, "Client funds" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_why_capital_com_move_focus(d, cur_language, cur_country)
        self.sub_menu_client_funds_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step("Move focus to 'Learn to trade' menu section")
    def menu_why_capital_com_move_focus(self, d, test_language, test_country):
        why_menu_locator = None
        if test_language == "" and test_country == "gb":
            why_menu_locator = MenuWhyCapitalCom.SUB_MENU_EN_GB_WHY_CAPITAL_COM

        time.sleep(0.5)
        menu = d.find_elements(*why_menu_locator)
        if len(menu) == 0:
            print(f"{datetime.now()}   => 'Why Capital.com?' menu not present")
            # allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
            Common().pytest_fail(f"Bug # ? 'Why Capital.com?' menu not present for '{test_language}' language")
        print(f"{datetime.now()}   => 'Why Capital.com?' menu is present")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            menu[0]
        )

        element = self.element_is_visible(why_menu_locator, 5)
        if not element:
            print(f"{datetime.now()}   => 'Why Capital.com?' menu not visible")
            Common().pytest_fail("Bug # ? 'Why Capital.com?' menu not visible")
        print(f"{datetime.now()}   => 'Why Capital.com?' menu is visible")

        time.sleep(0.5)
        menu = d.find_elements(*why_menu_locator)
        ActionChains(d) \
            .move_to_element(menu[0]) \
            .pause(0.5) \
            .perform()

        del menu
        del element
        print(f"{datetime.now()}   => Focus moved to 'Why Capital.com?' menu")

    @allure.step("Focus move to 'Client funds' submenu item and click")
    def sub_menu_client_funds_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuWhyCapitalCom.SUB_MENU_EN_ESSENTIALS_OF_TRADING)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Why Capital.com?->Client funds\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"{datetime.now()} => 'Client funds' menu clicked")

        del sub_menu
        return d.current_url

    @allure.step('Select "Learn to trade" menu, "Essentials of trading" submenu')
    def open_learn_to_trade_essentials_of_trading_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Learn to trade" menu, "Essentials of trading" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_learn_to_trade_move_focus(d, cur_language, cur_country)
        self.sub_menu_essentials_of_of_trading_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step("Focus move to 'Essentials of trading' submenu item and click")
    def sub_menu_essentials_of_of_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS11EssentialsOfTrading.SUB_MENU_EN_ESSENTIALS_OF_TRADING)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Learn to trade->Essentials of trading\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"{datetime.now()} => 'Essentials of trading' menu clicked")

        del sub_menu
        return d.current_url

    @allure.step('Select "Learn to trade" menu, "Market guides" submenu')
    def open_learn_to_trade_market_guides_new_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Learn to trade" menu, "Market guides" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_learn_to_trade_move_focus(d, cur_language, cur_country)
        self.sub_menu_market_guides_new_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step("Focus move to 'Market guides' submenu item and click")
    def sub_menu_market_guides_new_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS11MarketGuidesNew.SUB_MENU_MARKET_GUIDES_NEW)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Learn to trade->Market Guides\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()} => Market guides menu item clicked")

        del sub_menu
        return d.current_url

    @allure.step('Select "Markets" menu, "CFD Calculator" submenu')
    def open_markets_menu_cfd_calculator_submenu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Markets" menu, "CFD Calculator" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.move_focus_to_markets_menu(d, cur_language, cur_country)
        self.sub_menu_cfd_calculator_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step("Focus move to 'CFD Calculator' submenu item and click")
    def sub_menu_cfd_calculator_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS0109MarketsCFDCalculator.SUB_MENU_EN_CFDCALCULATOR)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Menu > CFD Calculator\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => 'CFD Calculator' sub-menu clicked")

        del sub_menu
        return d.current_url

    @allure.step('Select "Markets" menu, "Forex" submenu')
    def open_forex_markets_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Markets" menu, "Forex" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.move_focus_to_markets_menu(d, cur_language, cur_country)
        self.sub_menu_forex_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step("Focus move to 'Forex' submenu item and click")
    def sub_menu_forex_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS0103MarketsForex.SUB_MENU_EN_FOREX)
            case "ar":
                sub_menu = d.find_elements(*MenuUS0103MarketsForex.SUB_MENU_AR_FOREX)
            case "de":
                sub_menu = d.find_elements(*MenuUS0103MarketsForex.SUB_MENU_DE_FOREX)
            case "cn":
                sub_menu = d.find_elements(*MenuUS0103MarketsForex.SUB_MENU_CN_FOREX)
            case "es":
                sub_menu = d.find_elements(*MenuUS0103MarketsForex.SUB_MENU_ES_FOREX)
            case "fr":
                sub_menu = d.find_elements(*MenuUS0103MarketsForex.SUB_MENU_FR_FOREX)
            case "it":
                sub_menu = d.find_elements(*MenuUS0103MarketsForex.SUB_MENU_IT_FOREX)
            case "nl":
                sub_menu = d.find_elements(*MenuUS0103MarketsForex.SUB_MENU_NL_FOREX)
            case "pl":
                sub_menu = d.find_elements(*MenuUS0103MarketsForex.SUB_MENU_PL_FOREX)
            case "ro":
                sub_menu = d.find_elements(*MenuUS0103MarketsForex.SUB_MENU_RO_FOREX)
            case "ru":
                sub_menu = d.find_elements(*MenuUS0103MarketsForex.SUB_MENU_RU_FOREX)
            case "zh":
                sub_menu = d.find_elements(*MenuUS0103MarketsForex.SUB_MENU_ZH_FOREX)
            case "el":
                sub_menu = d.find_elements(*MenuUS0103MarketsForex.SUB_MENU_EL_FOREX)
            case "hu":
                sub_menu = d.find_elements(*MenuUS0103MarketsForex.SUB_MENU_HU_FOREX)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Menu > Forex\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => 'Forex' sub-menu clicked")

        del sub_menu
        return d.current_url

    @allure.step('Select "Markets" menu, "Indices" submenu')
    def open_indices_markets_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Markets" menu, "Indices" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.move_focus_to_markets_menu(d, cur_language, cur_country)
        self.sub_menu_indices_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Markets" menu, "Commodities" submenu')
    def open_commodities_markets_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Markets" menu, "Commodities" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.move_focus_to_markets_menu(d, cur_language, cur_country)
        self.sub_menu_commodities_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step("Focus move to 'Indices' submenu item and click")
    def sub_menu_indices_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS01Indices.SUB_MENU_EN_INDICES)
            case "ar":
                sub_menu = d.find_elements(*MenuUS01Indices.SUB_MENU_AR_INDICES)
            case "de":
                sub_menu = d.find_elements(*MenuUS01Indices.SUB_MENU_DE_INDICES)
            case "el":
                sub_menu = d.find_elements(*MenuUS01Indices.SUB_MENU_EL_INDICES)
            case "es":
                sub_menu = d.find_elements(*MenuUS01Indices.SUB_MENU_ES_INDICES)
            case "fr":
                sub_menu = d.find_elements(*MenuUS01Indices.SUB_MENU_FR_INDICES)
            case "it":
                sub_menu = d.find_elements(*MenuUS01Indices.SUB_MENU_IT_INDICES)
            case "hu":
                sub_menu = d.find_elements(*MenuUS01Indices.SUB_MENU_HU_INDICES)
            case "nl":
                sub_menu = d.find_elements(*MenuUS01Indices.SUB_MENU_NL_INDICES)
            case "pl":
                sub_menu = d.find_elements(*MenuUS01Indices.SUB_MENU_PL_INDICES)
            case "ro":
                sub_menu = d.find_elements(*MenuUS01Indices.SUB_MENU_RO_INDICES)
            case "ru":
                sub_menu = d.find_elements(*MenuUS01Indices.SUB_MENU_RU_INDICES)
            case "zh":
                sub_menu = d.find_elements(*MenuUS01Indices.SUB_MENU_ZH_INDICES)
            case "cn":
                sub_menu = d.find_elements(*MenuUS01Indices.SUB_MENU_CN_INDICES)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Markets->Indices\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => 'Indices' submenu clicked")

        del sub_menu
        return d.current_url

    @allure.step("Focus move to 'Commodities' submenu and click.")
    def sub_menu_commodities_move_focus_click(self, d, test_language):
        sub_menu = None
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS0104Commodities.SUB_MENU_EN_COMMODITIES_BUTTON)
            case "ar":
                sub_menu = d.find_elements(*MenuUS0104Commodities.SUB_MENU_AR_COMMODITIES_BUTTON)
            case "de":
                sub_menu = d.find_elements(*MenuUS0104Commodities.SUB_MENU_DE_COMMODITIES_BUTTON)
            case "el":
                sub_menu = d.find_elements(*MenuUS0104Commodities.SUB_MENU_EL_COMMODITIES_BUTTON)
            case "es":
                sub_menu = d.find_elements(*MenuUS0104Commodities.SUB_MENU_ES_COMMODITIES_BUTTON)
            case "fr":
                sub_menu = d.find_elements(*MenuUS0104Commodities.SUB_MENU_FR_COMMODITIES_BUTTON)
            case "it":
                sub_menu = d.find_elements(*MenuUS0104Commodities.SUB_MENU_IT_COMMODITIES_BUTTON)
            case "hu":
                sub_menu = d.find_elements(*MenuUS0104Commodities.SUB_MENU_HU_COMMODITIES_BUTTON)
            case "nl":
                sub_menu = d.find_elements(*MenuUS0104Commodities.SUB_MENU_NL_COMMODITIES_BUTTON)
            case "pl":
                sub_menu = d.find_elements(*MenuUS0104Commodities.SUB_MENU_PL_COMMODITIES_BUTTON)
            case "ro":
                sub_menu = d.find_elements(*MenuUS0104Commodities.SUB_MENU_RO_COMMODITIES_BUTTON)
            case "ru":
                sub_menu = d.find_elements(*MenuUS0104Commodities.SUB_MENU_RU_COMMODITIES_BUTTON)
            case "zh":
                sub_menu = d.find_elements(*MenuUS0104Commodities.SUB_MENU_ZH_COMMODITIES_BUTTON)
            case "cn":
                sub_menu = d.find_elements(*MenuUS0104Commodities.SUB_MENU_CN_COMMODITIES_BUTTON)

        if len(sub_menu) == 0:
            Common().pytest_fail(
                f"Bug # ??? For language '{test_language}' \"Markets > Commodities\" submenu doesn't exist")

        print(f"{datetime.now()}   => 'Markets > Commodities' submenu is present")

        ActionChains(d).move_to_element(sub_menu[0]).pause(0.5).click().pause(0.5).perform()

        del sub_menu

        return d.current_url

    @allure.step('Select "Markets" menu, "Shares" submenu click')
    def open_shares_market_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Markets" menu, "Shares" submenu =>')
        print(f"{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.move_focus_to_markets_menu(d, cur_language, cur_country)
        self.sub_menu_shares_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)

        print(f"{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step("Focus move to 'Shares' submenu item and click")
    def sub_menu_shares_move_focus_click(self, d, test_language):
        sub_menu = None
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS0102MarketsShares.SUB_MENU_EN_SHARES)
            case "ar":
                sub_menu = d.find_elements(*MenuUS0102MarketsShares.SUB_MENU_AR_SHARES)
            case "de":
                sub_menu = d.find_elements(*MenuUS0102MarketsShares.SUB_MENU_DE_SHARES)
            case "el":
                sub_menu = d.find_elements(*MenuUS0102MarketsShares.SUB_MENU_EL_SHARES)
            case "es":
                sub_menu = d.find_elements(*MenuUS0102MarketsShares.SUB_MENU_ES_SHARES)
            case "fr":
                sub_menu = d.find_elements(*MenuUS0102MarketsShares.SUB_MENU_FR_SHARES)
            case "it":
                sub_menu = d.find_elements(*MenuUS0102MarketsShares.SUB_MENU_IT_SHARES)
            case "hu":
                sub_menu = d.find_elements(*MenuUS0102MarketsShares.SUB_MENU_HU_SHARES)
            case "nl":
                sub_menu = d.find_elements(*MenuUS0102MarketsShares.SUB_MENU_NL_SHARES)
            case "pl":
                sub_menu = d.find_elements(*MenuUS0102MarketsShares.SUB_MENU_PL_SHARES)
            case "ro":
                sub_menu = d.find_elements(*MenuUS0102MarketsShares.SUB_MENU_RO_SHARES)
            case "ru":
                sub_menu = d.find_elements(*MenuUS0102MarketsShares.SUB_MENU_RU_SHARES)
            case "zh":
                sub_menu = d.find_elements(*MenuUS0102MarketsShares.SUB_MENU_ZH_SHARES)
            case "cn":
                sub_menu = d.find_elements(*MenuUS0102MarketsShares.SUB_MENU_CN_SHARES)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For language '{test_language}' \"Markets > Shares\" submenu doesn't exist")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .pause(0.5) \
            .perform()

        print(f"{datetime.now()}   => Focus moved to 'Shares' submenu and clicked")

        del sub_menu

    @allure.step('Select "Markets" menu, "ESG" submenu click')
    def open_esg_markets_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Markets" menu, "ESG" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.move_focus_to_markets_menu(d, cur_language, cur_country)
        self.sub_menu_esg_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step('Select "Markets" menu, "All Markets" submenu')
    def open_market_menu_all_markets_submenu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Markets" menu, "All Markets" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.move_focus_to_markets_menu(d, cur_language, cur_country)

        self.sub_menu_all_markets_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step(f"{datetime.now()}. Click submenu 'ESG'.")
    def sub_menu_esg_move_focus_click(self, d, test_language):
        sub_menu = None

        if test_language == "":
            sub_menu = d.find_elements(*MenuUS0107MarketsESG.SUB_MENU_EN_ESG)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For language '{test_language}' \"Markets > ESG\" submenu doesn't exist")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .pause(0.5) \
            .perform()

        print(f"{datetime.now()}   => Focus moved to 'ESG' submenu and clicked")

        del sub_menu
        return d.current_url

    @allure.step("Focus move to 'All Markets' submenu and click.")
    def sub_menu_all_markets_move_focus_click(self, d, test_language):
        sub_menu = None
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS0101AllMarkets.SUB_MENU_EN_ALLMARKETS_BUTTON)
            case "ar":
                sub_menu = d.find_elements(*MenuUS0101AllMarkets.SUB_MENU_AR_ALLMARKETS_BUTTON)
            case "de":
                sub_menu = d.find_elements(*MenuUS0101AllMarkets.SUB_MENU_DE_ALLMARKETS_BUTTON)
            case "el":
                sub_menu = d.find_elements(*MenuUS0101AllMarkets.SUB_MENU_EL_ALLMARKETS_BUTTON)
            case "es":
                sub_menu = d.find_elements(*MenuUS0101AllMarkets.SUB_MENU_ES_ALLMARKETS_BUTTON)
            case "fr":
                sub_menu = d.find_elements(*MenuUS0101AllMarkets.SUB_MENU_FR_ALLMARKETS_BUTTON)
            case "it":
                sub_menu = d.find_elements(*MenuUS0101AllMarkets.SUB_MENU_IT_ALLMARKETS_BUTTON)
            case "hu":
                sub_menu = d.find_elements(*MenuUS0101AllMarkets.SUB_MENU_HU_ALLMARKETS_BUTTON)
            case "nl":
                sub_menu = d.find_elements(*MenuUS0101AllMarkets.SUB_MENU_NL_ALLMARKETS_BUTTON)
            case "pl":
                sub_menu = d.find_elements(*MenuUS0101AllMarkets.SUB_MENU_PL_ALLMARKETS_BUTTON)
            case "ro":
                sub_menu = d.find_elements(*MenuUS0101AllMarkets.SUB_MENU_RO_ALLMARKETS_BUTTON)
            case "ru":
                sub_menu = d.find_elements(*MenuUS0101AllMarkets.SUB_MENU_RU_ALLMARKETS_BUTTON)
            case "zh":
                sub_menu = d.find_elements(*MenuUS0101AllMarkets.SUB_MENU_ZH_ALLMARKETS_BUTTON)
            case "cn":
                sub_menu = d.find_elements(*MenuUS0101AllMarkets.SUB_MENU_CN_ALLMARKETS_BUTTON)

        if len(sub_menu) == 0:
            Common().pytest_fail(
                f"Bug # ??? For language '{test_language}' \"Markets > All Markets\" submenu doesn't exist")

        print(f"{datetime.now()}   => 'Markets > All Markets' submenu is present")

        ActionChains(d).move_to_element(sub_menu[0]).pause(0.5).click().pause(0.5).perform()

        del sub_menu

        return d.current_url

    @allure.step('Select "Markets" menu, "Cryptocurrencies" submenu click')
    def open_cryptocurrencies_market_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Markets" menu, "Cryptocurrencies" submenu =>')
        print(f"{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.move_focus_to_markets_menu(d, cur_language, cur_country)
        self.sub_menu_cryptocurrencies_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)

        print(f"{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step("Focus move to 'Cryptocurrencies' submenu and click.")
    def sub_menu_cryptocurrencies_move_focus_click(self, d, test_language):
        sub_menu = None
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS0106MarketsCryptocurrencies.SUB_MENU_EN_CRYPTOCURRENCIES)
            case "ar":
                sub_menu = d.find_elements(*MenuUS0106MarketsCryptocurrencies.SUB_MENU_AR_CRYPTOCURRENCIES)
            case "de":
                sub_menu = d.find_elements(*MenuUS0106MarketsCryptocurrencies.SUB_MENU_DE_CRYPTOCURRENCIES)
            case "el":
                sub_menu = d.find_elements(*MenuUS0106MarketsCryptocurrencies.SUB_MENU_EL_CRYPTOCURRENCIES)
            case "es":
                sub_menu = d.find_elements(*MenuUS0106MarketsCryptocurrencies.SUB_MENU_ES_CRYPTOCURRENCIES)
            case "fr":
                sub_menu = d.find_elements(*MenuUS0106MarketsCryptocurrencies.SUB_MENU_FR_CRYPTOCURRENCIES)
            case "it":
                sub_menu = d.find_elements(*MenuUS0106MarketsCryptocurrencies.SUB_MENU_IT_CRYPTOCURRENCIES)
            case "hu":
                sub_menu = d.find_elements(*MenuUS0106MarketsCryptocurrencies.SUB_MENU_HU_CRYPTOCURRENCIES)
            case "nl":
                sub_menu = d.find_elements(*MenuUS0106MarketsCryptocurrencies.SUB_MENU_NL_CRYPTOCURRENCIES)
            case "pl":
                sub_menu = d.find_elements(*MenuUS0106MarketsCryptocurrencies.SUB_MENU_PL_CRYPTOCURRENCIES)
            case "ro":
                sub_menu = d.find_elements(*MenuUS0106MarketsCryptocurrencies.SUB_MENU_RO_CRYPTOCURRENCIES)
            case "ru":
                sub_menu = d.find_elements(*MenuUS0106MarketsCryptocurrencies.SUB_MENU_RU_CRYPTOCURRENCIES)
            case "zn":
                sub_menu = d.find_elements(*MenuUS0106MarketsCryptocurrencies.SUB_MENU_ZH_CRYPTOCURRENCIES)
            case "cn":
                sub_menu = d.find_elements(*MenuUS0106MarketsCryptocurrencies.SUB_MENU_CN_CRYPTOCURRENCIES)

        if len(sub_menu) == 0:
            Common().pytest_fail(
                f"Bug # ??? For language '{test_language}' \"Markets > Cryptocurrencies\" submenu doesn't exist")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .pause(0.5) \
            .perform()

        print(f"{datetime.now()}   => Focus moved to 'Cryptocurrencies' submenu and clicked")
        del sub_menu

    @allure.step('Select "News and Analysis" menu, "Market analysis"')
    def open_news_and_analysis_market_analysis_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "News and Analysis" menu, "Market analysis" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.move_focus_to_news_and_analysis_menu(d, cur_language, cur_country)
        self.sub_menu_market_analysis_move_focus_click(d, cur_language, cur_country)
        Common().move_pointer_to_capital_com_label(d)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step("Focus moved to 'News and Analysis' menu")
    def move_focus_to_news_and_analysis_menu(self, d, test_language, test_country):
        news_and_analysis_menu_locator = None
        match test_language:
            case "":
                news_and_analysis_menu_locator = MenuUS02NewsAndAnalysis.MENU_NEWS_AND_ANALYSIS_EN_BUTTON
            case "ar":
                news_and_analysis_menu_locator = MenuUS02NewsAndAnalysis.MENU_NEWS_AND_ANALYSIS_AR_BUTTON
            case "de":
                news_and_analysis_menu_locator = MenuUS02NewsAndAnalysis.MENU_NEWS_AND_ANALYSIS_DE_BUTTON
            case "el":
                news_and_analysis_menu_locator = MenuUS02NewsAndAnalysis.MENU_NEWS_AND_ANALYSIS_EL_BUTTON
            case "es":
                news_and_analysis_menu_locator = MenuUS02NewsAndAnalysis.MENU_NEWS_AND_ANALYSIS_ES_BUTTON
            case "fr":
                news_and_analysis_menu_locator = MenuUS02NewsAndAnalysis.MENU_NEWS_AND_ANALYSIS_FR_BUTTON
            case "it":
                news_and_analysis_menu_locator = MenuUS02NewsAndAnalysis.MENU_NEWS_AND_ANALYSIS_IT_BUTTON
            case "hu":
                news_and_analysis_menu_locator = MenuUS02NewsAndAnalysis.MENU_NEWS_AND_ANALYSIS_HU_BUTTON
            case "nl":
                news_and_analysis_menu_locator = MenuUS02NewsAndAnalysis.MENU_NEWS_AND_ANALYSIS_NL_BUTTON
            case "pl":
                news_and_analysis_menu_locator = MenuUS02NewsAndAnalysis.MENU_NEWS_AND_ANALYSIS_PL_BUTTON
            case "ro":
                news_and_analysis_menu_locator = MenuUS02NewsAndAnalysis.MENU_NEWS_AND_ANALYSIS_RO_BUTTON
            case "ru":
                news_and_analysis_menu_locator = MenuUS02NewsAndAnalysis.MENU_NEWS_AND_ANALYSIS_RU_BUTTON
            case "zh":
                news_and_analysis_menu_locator = MenuUS02NewsAndAnalysis.MENU_NEWS_AND_ANALYSIS_ZH_BUTTON
            case "cn":
                news_and_analysis_menu_locator = MenuUS02NewsAndAnalysis.MENU_NEWS_AND_ANALYSIS_CN_BUTTON

        time.sleep(0.5)
        menu = d.find_elements(*news_and_analysis_menu_locator)
        if len(menu) == 0:
            print(f"{datetime.now()}   => 'News and Analysis' menu not present")
            # Common().save_current_screenshot(d, "scr_qr")
            Common().pytest_fail(f"Bug № ??? 'News and Analysis' menu not present for '{test_language}' language")
        print(f"{datetime.now()}   => 'News and Analysis' menu is present")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            menu[0]
        )

        element = self.element_is_visible(news_and_analysis_menu_locator, 5)
        if not element:
            print(f"{datetime.now()}   => 'News and Analysis' menu not visible")
            # Common().save_current_screenshot(d, "scr_qr")
            Common().pytest_fail("Problem. 'News and Analysis' menu not visible")
        print(f"{datetime.now()}   => 'News and Analysis' menu is visible")

        time.sleep(0.5)
        menu = d.find_elements(*news_and_analysis_menu_locator)
        ActionChains(d) \
            .move_to_element(menu[0]) \
            .pause(0.5) \
            .perform()

        print(f"{datetime.now()}   => Focus moved to 'News and Analysis' menu")
        del menu
        del element

    @allure.step("Focus move to 'Market analysis' submenu item and click")
    def sub_menu_market_analysis_move_focus_click(self, d, test_language, test_country):
        sub_menu = None
        if test_country == "gb" and test_language == "":
            sub_menu = d.find_elements(*MenuUS11MarketAnalysis.SUB_MENU_MARKET_ANALYSIS_EN_GB)
        elif test_country == "ae" and test_language == "":
            sub_menu = d.find_elements(*MenuUS11MarketAnalysis.SUB_MENU_MARKET_ANALYSIS_EN_AE)
        else:
            sub_menu = d.find_elements(*MenuUS0201MarketAnalysis.SUB_MENU_EN_MARKET_ANALYSIS)

        if len(sub_menu) == 0:
            Common().pytest_fail(f"Bug # ??? For test language '{test_language}' "
                                 f"the page \"Menu > Market analysis\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()
        print(f"\n\n{datetime.now()}   => 'Market analysis' sub-menu clicked")

        del sub_menu
        return d.current_url

    @allure.step('Select "Products and services" menu, "Our Mobile Apps" submenu click')
    def open_our_mobile_apps_submenu_products_and_services_menu(self, d, cur_language, cur_country, link):
        print(f'\n{datetime.now()}   START Open "Products and services" menu, "Our Mobile Apps" submenu =>')
        print(f"{datetime.now()}   1. Cur URL: {d.current_url}")
        print(f"{datetime.now()}   2. New Link: {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        Captcha(d).fail_test_if_captcha_present_v2()
        self.move_focus_to_products_and_services_menu(d, cur_language, cur_country)
        self.sub_menu_our_mobile_apps_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)

        print(f"{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step("Focus moved to 'Products and services' menu")
    def move_focus_to_products_and_services_menu(self, d, test_language, test_country):
        products_and_services_menu_locator = None
        match test_language:
            case "":
                products_and_services_menu_locator = MenuProductsAndServices.MENU_PRODUCTS_AND_SERVICES_EN_BUTTON
            case "ar":
                products_and_services_menu_locator = MenuProductsAndServices.MENU_PRODUCTS_AND_SERVICES_AR_BUTTON
            case "de":
                products_and_services_menu_locator = MenuProductsAndServices.MENU_PRODUCTS_AND_SERVICES_DE_BUTTON
            case "el":
                products_and_services_menu_locator = MenuProductsAndServices.MENU_PRODUCTS_AND_SERVICES_EL_BUTTON
            case "es":
                products_and_services_menu_locator = MenuProductsAndServices.MENU_PRODUCTS_AND_SERVICES_ES_BUTTON
            case "fr":
                products_and_services_menu_locator = MenuProductsAndServices.MENU_PRODUCTS_AND_SERVICES_FR_BUTTON
            case "it":
                products_and_services_menu_locator = MenuProductsAndServices.MENU_PRODUCTS_AND_SERVICES_IT_BUTTON
            case "hu":
                products_and_services_menu_locator = MenuProductsAndServices.MENU_PRODUCTS_AND_SERVICES_HU_BUTTON
            case "nl":
                products_and_services_menu_locator = MenuProductsAndServices.MENU_PRODUCTS_AND_SERVICES_NL_BUTTON
            case "pl":
                products_and_services_menu_locator = MenuProductsAndServices.MENU_PRODUCTS_AND_SERVICES_PL_BUTTON
            case "ro":
                products_and_services_menu_locator = MenuProductsAndServices.MENU_PRODUCTS_AND_SERVICES_RO_BUTTON
            case "ru":
                products_and_services_menu_locator = MenuProductsAndServices.MENU_PRODUCTS_AND_SERVICES_RU_BUTTON
            case "zh":
                products_and_services_menu_locator = MenuProductsAndServices.MENU_PRODUCTS_AND_SERVICES_ZH_BUTTON
            case "cn":
                products_and_services_menu_locator = MenuProductsAndServices.MENU_PRODUCTS_AND_SERVICES_CN_BUTTON

        time.sleep(0.5)
        menu = d.find_elements(*products_and_services_menu_locator)
        if len(menu) == 0:
            print(f"{datetime.now()}   => 'Products and services' menu not present")
            Common().pytest_fail(f"Bug № ??? 'Products and services' menu not present for '{test_language}' language")
        print(f"{datetime.now()}   => 'Products and services' menu is present")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            menu[0]
        )

        element = self.element_is_visible(products_and_services_menu_locator, 5)
        if not element:
            print(f"{datetime.now()}   => 'Products and services' menu not visible")
            Common().pytest_fail("Problem. 'Products and services' menu not visible")
        print(f"{datetime.now()}   => 'Products and services' menu is visible")

        time.sleep(0.5)
        menu = d.find_elements(*products_and_services_menu_locator)
        ActionChains(d) \
            .move_to_element(menu[0]) \
            .pause(0.5) \
            .perform()

        print(f"{datetime.now()}   => Focus moved to 'Products and services' menu")
        del menu
        del element

    @allure.step("Focus move to 'Our Mobile Apps' submenu and click.")
    def sub_menu_our_mobile_apps_move_focus_click(self, d, test_language):
        sub_menu = None
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuProductsAndServicesOurMobileApps.SUB_MENU_EN_OUR_MOBILE_APPS)
            case "ar":
                sub_menu = d.find_elements(*MenuProductsAndServicesOurMobileApps.SUB_MENU_AR_OUR_MOBILE_APPS)
            case "de":
                sub_menu = d.find_elements(*MenuProductsAndServicesOurMobileApps.SUB_MENU_DE_OUR_MOBILE_APPS)
            case "es":
                sub_menu = d.find_elements(*MenuProductsAndServicesOurMobileApps.SUB_MENU_ES_OUR_MOBILE_APPS)
            case "fr":
                sub_menu = d.find_elements(*MenuProductsAndServicesOurMobileApps.SUB_MENU_FR_OUR_MOBILE_APPS)
            case "it":
                sub_menu = d.find_elements(*MenuProductsAndServicesOurMobileApps.SUB_MENU_IT_OUR_MOBILE_APPS)
            case "hu":
                sub_menu = d.find_elements(*MenuProductsAndServicesOurMobileApps.SUB_MENU_HU_OUR_MOBILE_APPS)
            case "nl":
                sub_menu = d.find_elements(*MenuProductsAndServicesOurMobileApps.SUB_MENU_NL_OUR_MOBILE_APPS)
            case "pl":
                sub_menu = d.find_elements(*MenuProductsAndServicesOurMobileApps.SUB_MENU_PL_OUR_MOBILE_APPS)
            case "ro":
                sub_menu = d.find_elements(*MenuProductsAndServicesOurMobileApps.SUB_MENU_RO_OUR_MOBILE_APPS)
            case "ru":
                sub_menu = d.find_elements(*MenuProductsAndServicesOurMobileApps.SUB_MENU_RU_OUR_MOBILE_APPS)
            case "cn":
                sub_menu = d.find_elements(*MenuProductsAndServicesOurMobileApps.SUB_MENU_CN_OUR_MOBILE_APPS)

        if len(sub_menu) == 0:
            Common().pytest_fail(
                f"Bug # ??? For language '{test_language}' "
                f"\"Products and services > Our Mobile Apps\" submenu doesn't exist")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .pause(0.5) \
            .perform()

        print(f"{datetime.now()}   => Focus moved to 'Our Mobile Apps' submenu and clicked")
        del sub_menu

    @allure.step("Focus move to 'Demo account' submenu and click.")
    def sub_menu_demo_account_move_focus_click(self, d, test_language):
        sub_menu = None
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuProductsAndServicesDemoAccount.SUB_MENU_EN_DEMO_ACCOUNT)
            case "ar":
                sub_menu = d.find_elements(*MenuProductsAndServicesDemoAccount.SUB_MENU_AR_DEMO_ACCOUNT)
            case "de":
                sub_menu = d.find_elements(*MenuProductsAndServicesDemoAccount.SUB_MENU_DE_DEMO_ACCOUNT)
            case "el":
                sub_menu = d.find_elements(*MenuProductsAndServicesDemoAccount.SUB_MENU_EL_DEMO_ACCOUNT)
            case "es":
                sub_menu = d.find_elements(*MenuProductsAndServicesDemoAccount.SUB_MENU_ES_DEMO_ACCOUNT)
            case "fr":
                sub_menu = d.find_elements(*MenuProductsAndServicesDemoAccount.SUB_MENU_FR_DEMO_ACCOUNT)
            case "it":
                sub_menu = d.find_elements(*MenuProductsAndServicesDemoAccount.SUB_MENU_IT_DEMO_ACCOUNT)
            case "hu":
                sub_menu = d.find_elements(*MenuProductsAndServicesDemoAccount.SUB_MENU_HU_DEMO_ACCOUNT)
            case "nl":
                sub_menu = d.find_elements(*MenuProductsAndServicesDemoAccount.SUB_MENU_NL_DEMO_ACCOUNT)
            case "pl":
                sub_menu = d.find_elements(*MenuProductsAndServicesDemoAccount.SUB_MENU_PL_DEMO_ACCOUNT)
            case "ro":
                sub_menu = d.find_elements(*MenuProductsAndServicesDemoAccount.SUB_MENU_RO_DEMO_ACCOUNT)
            case "ru":
                sub_menu = d.find_elements(*MenuProductsAndServicesDemoAccount.SUB_MENU_RU_DEMO_ACCOUNT)
            case "zh":
                sub_menu = d.find_elements(*MenuProductsAndServicesDemoAccount.SUB_MENU_ZH_DEMO_ACCOUNT)
            case "cn":
                sub_menu = d.find_elements(*MenuProductsAndServicesDemoAccount.SUB_MENU_CN_DEMO_ACCOUNT)

        if len(sub_menu) == 0:
            Common().pytest_fail(
                f"Bug # ??? For language '{test_language}' "
                f"\"Products and services > Demo account\" submenu doesn't exist")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .pause(0.5) \
            .perform()

        print(f"{datetime.now()}   => Focus moved to 'Demo account' submenu and clicked")
        del sub_menu
