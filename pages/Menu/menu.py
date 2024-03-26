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

from pages.base_page import BasePage
from pages.Menu.menu_locators import (
    Menu1101,
    MenuLanguageAndCountry,
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
    MenuUS01Indices, MenuUS0102MarketsShares, MenuUS0103MarketsForex, MenuUS0104Commodities
)
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

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    def open_education_shares_trading_menu(self, d, cur_language, cur_country, link):

        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()
        self.menu_education_move_focus(d, cur_language, cur_country)
        cur_menu_link = self.sub_menu_shares_trading_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        return cur_menu_link

    def open_education_commodities_trading_menu(self, d, cur_language, cur_country, link):

        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()
        self.menu_education_move_focus(d, cur_language, cur_country)
        cur_menu_link = self.sub_menu_commodities_trading_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        return cur_menu_link

    def open_education_indices_trading_menu(self, d, cur_language, cur_country, link):

        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()
        self.menu_education_move_focus(d, cur_language, cur_country)
        cur_menu_link = self.sub_menu_indices_trading_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        return cur_menu_link

    def open_education_cryptocurrency_trading_menu(self, d, cur_language, cur_country, link):

        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()
        self.menu_education_move_focus(d, cur_language, cur_country)
        cur_menu_link = self.sub_menu_cryptocurrency_trading_move_focus_click(d, cur_language)
        Common().move_pointer_to_capital_com_label(d)
        return cur_menu_link

    @allure.step(f"{datetime.now()}.   Click 'Language and Country' menu section.")
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

        # if not self.element_is_clickable(MenuLanguageAndCountry.MENU_LANGUAGE_AND_COUNTRY, 5):
        #     print(f"\n\n{datetime.now()}   => Language and Country menu not clickable")
        #     Common().pytest_fail("Language and Country menu not clickable")
        # print(f"\n\n{datetime.now()}   => Language and Country menu is clickable")
        #

        # menu = d.find_element(*MenuLanguageAndCountry.MENU_LANGUAGE_AND_COUNTRY)    # not Glossary
        time.sleep(0.5)
        ActionChains(d) \
            .move_to_element(d.find_element(*MenuLanguageAndCountry.MENU_LANGUAGE_AND_COUNTRY)) \
            .pause(0.5) \
            .perform()
        # del menu

        print(f"{datetime.now()}   => Focus is moved on Language and Country menu ")

    @allure.step(f"{datetime.now()}.   Move focus to 'Learn to trade' menu section.")
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
        print(f"{datetime.now()}   element = {element}")
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

    @allure.step(f"{datetime.now()}.   Focus moved to 'Education' menu")
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

    @allure.step(f"{datetime.now()}.   Focus moved to 'Markets' menu")
    def move_focus_to_markets_menu(self, d, test_language, test_country):
        markets_menu_locator = None
        if test_language == "" and test_country == "gb":
            markets_menu_locator = MenuUS01Markets.MENU_EN_GB_MARKETS   # новая верстка, FCA
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
                    markets_menu_locator = MenuUS01Markets.MENU_MARKETS_RU_BUTTON
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
        print(f"{datetime.now()}   element = {element}")
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

    @allure.step(f"{datetime.now()}.   Focus move to 'learning hub' menu item and click (US_11.01.01).")
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

    @allure.step(f"{datetime.now()}.   Focus move to 'Basics_of_trading' menu item and click (US_11.01.02).")
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

    @allure.step(f"{datetime.now()}.   Focus move to 'Glossary' menu item and click (US_11.01.07).")
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

    @allure.step(f"{datetime.now()}.   Click 'Forex trading' submenu.")
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

    @allure.step(f"{datetime.now()}.   Click 'Trading courses hyperlink.")
    def sub_menu_trading_courses_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_EN_ITEM_TRADING_COURSES)
            case "de":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_DE_ITEM_TRADING_COURSES)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_RU_ITEM_TRADING_COURSES)
            case "bg":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_BG_ITEM_TRADING_COURSES)
            case "cs":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_CS_ITEM_TRADING_COURSES)
            case "fr":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_FR_ITEM_TRADING_COURSES)
            case "ar":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_AR_ITEM_TRADING_COURSES)
            case "et":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ET_ITEM_TRADING_COURSES)
            case "da":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_DA_ITEM_TRADING_COURSES)
            case "el":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_EL_ITEM_TRADING_COURSES)
            case "es":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ES_ITEM_TRADING_COURSES)
            case "hr":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_HR_ITEM_TRADING_COURSES)
            case "it":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_IT_ITEM_TRADING_COURSES)
            case "lv":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_LV_ITEM_TRADING_COURSES)
            case "hu":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_HU_ITEM_TRADING_COURSES)
            case "nl":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_NL_ITEM_TRADING_COURSES)
            case "pl":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_PL_ITEM_TRADING_COURSES)
            case "pt":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_PT_ITEM_TRADING_COURSES)
            case "ro":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_RO_ITEM_TRADING_COURSES)
            case "sk":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_SK_ITEM_TRADING_COURSES)
            case "sl":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_SL_ITEM_TRADING_COURSES)
            case "fi":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_FI_ITEM_TRADING_COURSES)
            case "sv":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_SV_ITEM_TRADING_COURSES)
            case "vi":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_VI_ITEM_TRADING_COURSES)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ZH_ITEM_TRADING_COURSES)
            case "lt":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_LT_ITEM_TRADING_COURSES)
            case "cn":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_CN_ITEM_TRADING_COURSES)
            case "id":
                sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ID_ITEM_TRADING_COURSES)

        if len(sub_menu) == 0:
            pytest.skip(f"For '{test_language}' language [Trading courses] submenu item "
                        f"doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .pause(0.5) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Commodities trading' hyperlink.")
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

    @allure.step(f"{datetime.now()}.   Click 'Market guides hyperlink.")
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

    @allure.step(f"{datetime.now()}.   Click 'Cryptocurrency trading' hyperlink.")
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

    @allure.step(f"{datetime.now()}   Click 'CFD trading guide' hyperlink.")
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

    @allure.step(f"{datetime.now()}.   Click 'Spread betting guide' hyperlink.")
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

    @allure.step(f"{datetime.now()}   Set language")
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

    @allure.step(f"{datetime.now()}   Start Set country")
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

    @allure.step(f"{datetime.now()}.   Click 'ETF trading' hyperlink.")
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

    @allure.step(f"{datetime.now()}.   Click 'Trading Strategies Guide' hyperlink.")
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

    @allure.step(f"{datetime.now()}.   Click 'Day Trading' hyperlink.")
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

    @allure.step(f"{datetime.now()}.   Click 'Indices Trading' hyperlink.")
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
            # case _:
            #     sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_ALL_INDICES_TRADING)

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

    @allure.step(f"{datetime.now()}.   Click 'Investmate app' hyperlink.")
    def sub_menu_investmate_app_move_focus_click(self, d, test_language):
        sub_menu = None
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

    @allure.step(f"{datetime.now()}.   Click 'Trend Trading' menu item.")
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

    @allure.step(f"{datetime.now()}.   Click 'What is a margin?' hyperlink.")
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

    @allure.step(f"{datetime.now()}.   Click 'Trading Psychology Guide' hyperlink.")
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

    @allure.step(f"{datetime.now()}.   Click 'Position Trading' hyperlink.")
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

    @allure.step(f"{datetime.now()}.   Click 'Swing Trading' hyperlink.")
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

    @allure.step(f"{datetime.now()}.   Click 'Scalp Trading' hyperlink.")
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

    @allure.step(f"{datetime.now()}.   Click 'Shares trading' submenu.")
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

    @allure.step(f"{datetime.now()}.   Click 'Risk-management guide' menu item.")
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

    @allure.step(f"{datetime.now()}.   Click 'Risk-management guide' menu item.")
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

    @allure.step(f"{datetime.now()}.   Click 'Help' menu item.")
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

    @allure.step(f"{datetime.now()}.   Click 'Learn to trade' menu")
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

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Trading Strategies(FCA)' menu item.")
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

    @allure.step('Select "Learn to trade" menu, "Essentials of trading"')
    def open_learn_to_trade_essentials_of_trading_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Learn to trade" menu, "Essentials of trading" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_learn_to_trade_move_focus(d, cur_language, cur_country)
        self.sub_menu_essentials_of_of_trading_move_focus_click(d, cur_language)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Essentials of trading' submenu")
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
        print(f"\n\n{datetime.now()} => 'Essentials of trading' menu clicked")

        del sub_menu
        return d.current_url

    @allure.step('Select "Learn to trade" menu, "Market guides')
    def open_learn_to_trade_market_guides_new_menu(self, d, cur_language, cur_country, link):

        print(f'\n{datetime.now()}   START Open "Learn to trade" menu, "Market guides" submenu =>')
        print(f"\n{datetime.now()}   1. Cur URL = {d.current_url}")
        print(f"\n{datetime.now()}   2. Link = {link}")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.menu_learn_to_trade_move_focus(d, cur_language, cur_country)
        self.sub_menu_market_guides_new_move_focus_click(d, cur_language)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Market guides' menu item.")
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

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Forex' submenu.")
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

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Indices' submenu.")
    def sub_menu_indices_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS01Indices.SUB_MENU_EN_INDICES)
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

    @allure.step(f"{datetime.now()}. Move focus to 'Commodities' submenu and click.")
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

    @allure.step(f"{datetime.now()}. Click submenu 'Shares'.")
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
        return d.current_url
