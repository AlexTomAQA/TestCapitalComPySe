"""
-*- coding: utf-8 -*-
@Time    : 2024/05/06 22:00
@Author  : Kasilà
"""
import random

import pytest
import allure

from pages.BugsManual.bug_048 import AppliedFilters
from pages.BugsManual.bug_077 import Sidebar
from pages.BugsManual.bug_270 import LearnMoreAbout
from pages.BugsManual.bug_308 import InvestmateAppPage
from pages.BugsManual.bug_322 import TradingInstrumentSell
from pages.Menu.New.from_markets_menu_open_cryptocurrencies import FromMarketsOpenCryptocurrencies
from pages.Menu.New.from_markets_menu_open_markets import MenuNewMarkets
from pages.Menu.New.from_trading_menu_open_mobile_apps import MenuNew
from pages.Menu.menu import MenuSection
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55
from pages.Elements.MyAccountButton import MyAccountButton
from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.conditions_new import NewConditions


@pytest.mark.us_55
class TestManualDetectedBugs:
    page_conditions = None

    @allure.step("Start retest manual TC_55!009 of button [My account] in the Header")
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.bug_009
    def test_009(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: Button [My account] in the Header
         Language: En. License: FCA.
         Author: Kasila
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "009", "The 'My Account' menu is not displayed when click on the [My Account] button in the Header"
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MyAccountButton(d, link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, link)

    @allure.step("Start retest manual AT_55!00_048 of filters application in the 'Live shares prices' widget")
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'ua', 'au'], 1))
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_048
    def test_048(self, worker_id, d, cur_language_2_rnd_from_14, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Filters application in the 'Live shares prices' widget
        Language: All
        License: CYSEC, SCB, ASIC
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_2_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "048", "Applied filters 'Region/Sectors' are not displayed after selecting an item from the "
                   "'Most traded' dropdown in the 'Live shares prices'  widget on the 'Shares' page"
            )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_2_rnd_from_14, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_shares_market_menu(d, cur_language_2_rnd_from_14, cur_country, link)

        test_element = AppliedFilters(d, cur_item_link, bid)
        test_element.test_(d, cur_language_2_rnd_from_14, cur_country, cur_role, cur_item_link)

    @allure.step('Start retest manual AT_55!077a of the  presence of the "Crypto trading  guide" sidebar on '
                 '"Crypto vs stocks: What is the difference?" page')
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'ua', 'au'], 1))
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.parametrize('cur_language', [""])
    @pytest.mark.parametrize('sidebar_item', ['Crypto vs stocks: What’s the difference?'])
    @pytest.mark.bug_077a
    def test_077a(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
                  sidebar_item):
        """
        Check: presence of the sidebar "Crypto Trading Guide" on the "Cryptocurrencies vs. Stocks:
        What's the Difference?" page.
        Language: EN
        License: CYSEC, SCB, ASIC
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "077a", 'Sidebar " Crypto trading  guide" is absent on pages "Bitcoin Gold" and "Crypto vs '
                    'stocks: What’s the difference?"'
        )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_education_cryptocurrency_trading_menu(d, cur_language, cur_country, link)

        test_element = Sidebar(d, cur_item_link, bid)
        match cur_language:
            case "":
                test_element.sidebar_en(d, cur_item_link, sidebar_item)
        test_element.assert_a(sidebar_item)

    @allure.step('Start retest manual AT_55!077b of the presence of the "Crypto trading  guide" sidebar on '
                 '"Bitcoin Gold" page')
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'ua', 'au'], 1))
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.parametrize('sidebar_item', ['Bitcoin Gold'])
    @pytest.mark.bug_077b
    def test_077b(self, worker_id, d, cur_language_2_rnd_from_7, cur_country, cur_role, cur_login, cur_password,
                  sidebar_item):
        """
        Check: presence of the sidebar "Crypto Trading Guide" on the "Bitcoin Gold" page.
        Language: EN, DE, ZH, RU, ES,IT, PL
        License: CYSEC, SCB, ASIC
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_2_rnd_from_7, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "077b", 'Sidebar " Crypto trading  guide" is absent on page "Bitcoin Gold"'
        )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_2_rnd_from_7, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_education_cryptocurrency_trading_menu(d, cur_language_2_rnd_from_7, cur_country,
                                                                        link)

        test_element = Sidebar(d, cur_item_link, bid)
        match cur_language_2_rnd_from_7:
            case "" | "de" | "zh":
                test_element.sidebar_en_de_zh(d, cur_item_link, sidebar_item)
            case "ru" | "es" | "it" | "pl":
                test_element.sidebar_ru_es_it_pl(d, cur_item_link, sidebar_item)
        test_element.assert_b(sidebar_item)

    @allure.step('Start retest manual AT_55!270 that the page "what is cryptocurrency trading" is opened')
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_language', ['ar'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_270
    def test_270(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: The page "what is cryptocurrency trading" is not opened after clicking the link [Learn more about
            cryptocurrency trading] in the block "Why trade cryptocurrencies with Capital.com?" on the page
            "Cryptocurrencies" when SCA license is selected.
        Language: AR
        License: SCA
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "270", 'The page "what is cryptocurrency trading" is not opened'
        )

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_AR_AE, "", cur_language, cur_country, cur_role, cur_login,
            cur_password)

        menu = FromMarketsOpenCryptocurrencies(d, link)
        cur_item_link = menu.from_markets_menu_open_cryptocurrencies(d, cur_language, cur_country, link)

        test_element = LearnMoreAbout(d, cur_item_link, bid)
        test_element.learn_more_about(d, cur_item_link, link)
        test_element.assert_(d)

    @allure.step('Start retest manual AT_55!308 that the "Investmate" app page is opened on Google Play/App Store.')
    @pytest.mark.parametrize('cur_language', ['en'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_308
    def test_308(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: The page is refreshed after clicking the link “educational app Investmate” in the block “Investmate” on
            the page “Mobile apps” when EN language is selected (SCA license).
        Language: EN
        License: SCA
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "308", 'The "Investmate" app page is not opened on Google Play/App Store'
        )

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_EN_AE, "", cur_language, cur_country, cur_role, cur_login,
            cur_password)

        menu = MenuNew(d, link)
        cur_item_link = menu.from_trading_menu_open_mobile_apps(d, cur_language, cur_country, link)

        test_element = InvestmateAppPage(d, cur_item_link, bid)
        test_element.investmate_app_page(d, cur_item_link)
        test_element.assert_(d)

    @allure.step(
        'Start retest manual AT_55!322a that the Sign Up/Login/page of the corresponding trading instrument on '
        'the trading platform is opened.')
    @pytest.mark.parametrize('cur_language', ['', 'ar'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_322a
    def test_322a(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Clicking [numeric values] in the Sell/Buy column in Menu tittle Markets does not open the
                Sign-Up /Login form or page of the corresponding trading instrument on the trading platform using
                English or Arabic language.
        Language: EN, AR
        License: SCA
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "308", 'The Sign Up/Login/page of the corresponding trading instrument on the trading platform'
                   ' is not opened'
        )

        page_conditions = NewConditions(d, "")

        match cur_language:
            case '':
                link = page_conditions.preconditions(
                    d, CapitalComPageSrc.URL_NEW_EN_AE, "", cur_language, cur_country, cur_role, cur_login,
                    cur_password)
            case 'ar':
                link = page_conditions.preconditions(
                    d, CapitalComPageSrc.URL_NEW_AR_AE, "", cur_language, cur_country, cur_role, cur_login,
                    cur_password)

        menu = MenuNewMarkets(d, link)
        cur_item_link = menu.from_markets_menu_open_markets(d, cur_language, cur_country, link)

        test_element = TradingInstrumentSell(d, cur_item_link, bid)
        test_element.trading_instruments(d, cur_item_link)
        test_element.click_button_sell(d)
        match cur_role:
            case NoReg:
                test_element.assert_signup(d)
