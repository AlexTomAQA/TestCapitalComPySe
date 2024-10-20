"""
-*- coding: utf-8 -*-
@Time    : 2024/05/18 18:00 GMT+3
@Author  : Artem Dashkov
"""

import allure
import pytest
import random
from datetime import datetime
from pages.common import Common
from pages.BugsManual.bug_031 import ContentsBlockLearnMoreAboutUsLink
from pages.Elements.TradePageAddToFavoriteButton import TradePageAddToFavoriteButton
from pages.BugsManual.bug_017 import WhyChooseBlockTryNowButtonInContent
from pages.Elements.PageInstrumentLongPositionGoToPlatformButton import PageInstrumentLongPositionGoToPlatformButton
from pages.Elements.PageInstrumentShortPositionGoToPlatformButton import PageInstrumentShortPositionGoToPlatformButton
from pages.BugsManual.bug_045a import EmailFieldSignUpForm
from pages.BugsManual.bug_074 import WhatIsYourSentimentWidget
from pages.BugsManual.bug_104 import TradingCalculatorCFDCalculatorPage
from pages.BugsManual.bug_171 import BUG_171
from pages.BugsManual.bug_129 import BUG_129
from pages.BugsManual.bug_149 import BUG_149
from pages.BugsManual.bug_151 import BUG_151
from pages.BugsManual.bug_257 import BUG_257
from pages.BugsManual.bug_265 import BUG_265
from pages.BugsManual.bug_300 import BUG_300
from pages.BugsManual.bug_312 import BUG_312
from pages.BugsManual.bug_324 import BUG_324
from pages.BugsManual.bug_334 import BUG_334
from pages.BugsManual.bug_357 import BUG_357
from pages.BugsManual.bug_362 import BUG_362
from pages.BugsManual.bug_370 import BUG_370
from pages.BugsManual.bug_377 import BUG_377
from pages.BugsManual.bug_383 import BUG_383
from pages.BugsManual.bug_406 import BUG_406
from pages.BugsManual.bug_407 import BUG_407
from src.src import CapitalComPageSrc
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55
from pages.conditions import Conditions
from pages.conditions_v2 import apply_preconditions_to_link
from pages.Menu.menu import MenuSection
from pages.Menu.New import (from_trading_menu_open_web_platform,
                            from_pricing_menu_open_how_capital_com_makes_money,
                            from_trading_menu_open_all_platforms,
                            from_markets_menu_open_commodities,
                            from_markets_menu_open_forex,
                            from_markets_menu_open_market_analysis,
                            from_trading_menu_open_spread_betting,
                            from_about_us_menu_open_why_capital)
from pages.conditions_new import NewConditions
from pages.conditions_new_v1 import NewConditions_v1


@pytest.mark.us_55
class TestManualDetected:
    page_conditions = None

    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.bug_016a
    @allure.step("Start test of button [Add to favourite] on the 'Trading Instrument Page'")
    def test_016a_add_to_favourite_button_on_trading_instrument_page(
            self, worker_id, d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, cur_role,
            cur_login, cur_password, cur_market_1_rnd_from_5):
        """
        Check:  The trading platform is opened, not the page
                of the corresponding trading instrument on the trading platform
        Language: All.
        License: Not FCA
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "016a",
            "The trading platform is opened, "
            "not the page of the corresponding trading instrument on the trading platform",
            False, False
        )

        link = apply_preconditions_to_link(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2,
                                           cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = None
        match cur_market_1_rnd_from_5:
            case "Shares":
                cur_item_link = menu.open_shares_market_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, link)
            case "Forex":
                cur_item_link = menu.open_forex_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, link)
            case "Indices":
                cur_item_link = menu.open_indices_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, link)
            case "Commodities":
                cur_item_link = menu.open_commodities_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, link)
            case "Cryptocurrencies":
                cur_item_link = menu.open_cryptocurrencies_market_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, link)

        test_element = TradePageAddToFavoriteButton(d, cur_item_link, bid)
        test_element.full_test(
            d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, cur_role, cur_item_link, cur_market_1_rnd_from_5)

    @allure.step("Start test of button [Go to platform] on tooltip 'Long position overnight fee'")
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.bug_016b
    def test_016b_add_to_favourite_button_on_tooltip_long_position_overnight_fee(
            self, worker_id, d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, cur_role,
            cur_login, cur_password, cur_market_1_rnd_from_5):
        """
        Check:  The trading platform is opened, not the page
                of the corresponding trading instrument on the trading platform
        Language: All.
        License: Not FCA
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "016b",
            "The trading platform is opened, "
            "not the page of the corresponding trading instrument on the trading platform",
            False, False
        )

        link = apply_preconditions_to_link(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2,
                                           cur_role, cur_login, cur_password)

        cur_item_link = None
        menu = MenuSection(d, link)
        match cur_market_1_rnd_from_5:
            case "Shares":
                cur_item_link = menu.open_shares_market_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, link)
            case "Forex":
                cur_item_link = menu.open_forex_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, link)
            case "Indices":
                cur_item_link = menu.open_indices_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, link)
            case "Commodities":
                cur_item_link = menu.open_commodities_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, link)
            case "Cryptocurrencies":
                cur_item_link = menu.open_cryptocurrencies_market_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, link)

        test_element = TradePageAddToFavoriteButton(d, cur_item_link, bid)
        test_element.arrange_1(d, cur_item_link, cur_market_1_rnd_from_5)

        cur_item_link = d.current_url
        test_element = PageInstrumentLongPositionGoToPlatformButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi_v2(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, cur_role, cur_item_link)

    @allure.step("Start test of button [Go to platform] on tooltip 'Short position overnight fee'")
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.bug_016c
    def test_016c_add_to_favourite_button_on_tooltip_short_position_overnight_fee(
            self, worker_id, d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, cur_role,
            cur_login, cur_password, cur_market_1_rnd_from_5):
        """
        Check:  The trading platform is opened, not the page of the corresponding trading instrument
                on the trading platform
        Language: All.
        License: Not FCA
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "016c",
            "The trading platform is opened, "
            "not the page of the corresponding trading instrument on the trading platform",
            False, False
        )

        link = apply_preconditions_to_link(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2,
                                           cur_role, cur_login, cur_password)

        cur_item_link = None
        menu = MenuSection(d, link)
        match cur_market_1_rnd_from_5:
            case "Shares":
                cur_item_link = menu.open_shares_market_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, link)
            case "Forex":
                cur_item_link = menu.open_forex_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, link)
            case "Indices":
                cur_item_link = menu.open_indices_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, link)
            case "Commodities":
                cur_item_link = menu.open_commodities_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, link)
            case "Cryptocurrencies":
                cur_item_link = menu.open_cryptocurrencies_market_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, link)

        test_element = TradePageAddToFavoriteButton(d, cur_item_link, bid)
        test_element.arrange_1(d, cur_item_link, cur_market_1_rnd_from_5)

        cur_item_link = d.current_url
        test_element = PageInstrumentShortPositionGoToPlatformButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, cur_role, cur_item_link)

    @allure.step("Start test of button [Try now] on the block 'Why choose Capital.com?'")
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_017
    def test_017_try_now_button_on_why_choose_capital_com_block(
            self, worker_id, d, cur_language_2_rnd_from_12, cur_country_1_rnd_from_2, cur_role, cur_login, cur_password):
        """
        Check:  Sign up/log in/forms or the transition to the trading platform are
                not opened after clicking the [Try now] button in "Why choose
                Capital.com?.." Block in the menu item [Our Mobile Apps]
        Language: All.
        License: Not FCA
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_2_rnd_from_12, cur_country_1_rnd_from_2, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "017",
            "Sign up/log in/forms or the transition to the trading platform are not opened "
            "after clicking the [Try now] button in 'Why choose Capital.com?..' Block "
            "in the menu item [Our Mobile Apps]",
            False, False
        )

        link = apply_preconditions_to_link(d, cur_language_2_rnd_from_12, cur_country_1_rnd_from_2,
                                           cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_our_mobile_apps_submenu_products_and_services_menu(
            d, cur_language_2_rnd_from_12, cur_country_1_rnd_from_2, link
        )

        test_element = WhyChooseBlockTryNowButtonInContent(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language_2_rnd_from_12, cur_country_1_rnd_from_2, cur_role, cur_item_link)

    @allure.step("Start test of link [Learn more about us] on the block 'Contents'")
    @pytest.mark.parametrize('cur_language', [""])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_031
    def test_031_learn_more_about_us_link_on_contents_block(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check:  [Learn more about us] anchor doesn't navigate to the "Learn more about us"
                section on the "Client funds" page when clicking on it.
        Language: En.
        License: FCA
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "031",
            "Testing link [Learn more about us] on the block 'Contents'",
            False, True
        )

        link = apply_preconditions_to_link(d, cur_language, cur_country,
                                           cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_why_capital_com_client_funds_menu(
            d, cur_language, cur_country, link
        )

        test_element = ContentsBlockLearnMoreAboutUsLink(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of field [email] in Sign up form")
    @pytest.mark.parametrize('cur_role', ["NoReg", "NoAuth"])
    @pytest.mark.parametrize('invalid_login', ['КИРИЛЛИЦА_без_пробелов@gmail.com', 'LATIN with space@gmail.com'])
    @pytest.mark.parametrize('valid_password', ['VALID_password44!VALID_password44!VALID_password44!'])
    @pytest.mark.bug_045a
    def test_045a_email_field_sign_up_form(
            self, worker_id, d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, cur_role,
            cur_login, cur_password, invalid_login, valid_password):
        """
        Check: Field [email] in Sign up form
        Language: All.
        License/Country: de/CYSEC, au/ASIC,
        Role: NoReg, NoAuth,
        Login: ['КИРИЛЛИЦА_без_пробелов@gmail.com', 'LATIN with space@gmail.com'],
        Password: ['VALID_password44!']
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "045a",
            "Testing field [email] in Sign up form",
            False, False
        )

        d.refresh()

        link = apply_preconditions_to_link(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2,
                                           cur_role, cur_login, cur_password)

        test_element = EmailFieldSignUpForm(d, link, bid)
        test_element.full_test(
            d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_2, cur_role,
            link, invalid_login, valid_password)

    @allure.step("Start test of voted function in 'What is your sentiment...' block")
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_074
    def test_074_voted_function_in_sentiment_block(
            self, worker_id, d, cur_language, cur_country_1_rnd_from_2, cur_role, cur_login, cur_password):
        """
        Check:  Not possible to vote for another trading instrument
                in the block "What is your sentiment..."  if on another page voted for another instrument
        Language: All.
        License/Country: All
        Role: NoReg, NoAuth, Auth
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country_1_rnd_from_2, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "074",
            "Not possible to vote for another trading instrument "
            "in the block 'What is your sentiment...' if on another page voted for another instrument",
            False, False
        )

        # Arrange
        link = apply_preconditions_to_link(d, cur_language, cur_country_1_rnd_from_2,
                                           cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        menu_link = page_menu.open_news_and_analysis_market_analysis_menu(
            d, cur_language, cur_country_1_rnd_from_2, link)
        test_element = WhatIsYourSentimentWidget(d, menu_link, bid)
        test_element.arrange(d, menu_link)

        # Act
        d.back()
        print(f"{datetime.now()}   Returned to article list page, current url is: {d.current_url}")
        test_element.act(d)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test of 'Trading calculator' widget in menu [CFD calculator]")
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', random.sample(["de", "ua"], 1), )
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_104
    def test_104_trading_calculator_collapse_after_setting_duration(
            self, worker_id, d, cur_language, cur_country, cur_role,
            cur_login, cur_password, calc_1_and_calc_2):
        """
        Check: The trading calculator is collapsed in the menu section [Markets] --> [CFD calculator]
        after setting the maximum duration on the Prof/Loss element and changing the asset
        Language: En.
        Country: CYSEC, SCB
        Role: NoReg, Auth, NoAuth,
        calc_1_and_calc_2:  ("GBP/USD", "EUR/USD"),
                            ("EUR/USD", "GBP/USD"),
                            ("Gold", "Natural Gas"),
                            ("Natural Gas", "Gold"),
                            ("Germany 40", "US Tech 100"),
                            ("US Tech 100", "Germany 40")
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "104",
            "Testing 'Trading calculator' widget in menu [CFD calculator]",
            False, False
        )

        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                           cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        link = page_menu.open_markets_menu_cfd_calculator_submenu(
            d, cur_language, cur_country, cur_item_link)

        test_element = TradingCalculatorCFDCalculatorPage(d, link, bid)
        test_element.arrange(d)

        # Act
        test_element.act(d, calc_1_and_calc_2)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test of the link [Go to all cryptocurrencies] in menu [Cryptocurrency trading]")
    @pytest.mark.parametrize('cur_language', random.sample(["ro", "it", "pl", "cn"], 2), )
    @pytest.mark.parametrize('cur_country', random.sample(["de", "ua"], 1), )
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_129
    def test_129_link_go_to_all_cryptocurrencies_does_not_open_cfd_page(
            self, worker_id, d, cur_language, cur_country, cur_role,
            cur_login, cur_password):
        """
        Check:  The Main page is opened instead of the Cryptocurrencies page on the page
                "Cryptocurrency trading" after clicking the button [Go to all cryptocurrencies]
                when RO, IT, PL or CN language is selected
        Language: RO, IT, PL, CN.
        Country: CYSEC, SCB
        Role: NoReg, Auth, NoAuth,
        Author: Artem Dashkov
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "129",
            "Testing button [Go to all cryptocurrencies] in menu [Cryptocurrency trading]",
            False, False
        )

        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                           cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        cur_item_link = page_menu.open_education_cryptocurrency_trading_menu(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_129(d, cur_item_link, bid)
        test_element.arrange(d, cur_language)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test of the link [Go to all cryptocurrencies] "
                 "in menu [Cryptocurrency trading] for Germany language")
    @pytest.mark.parametrize('cur_language', ["de"])
    @pytest.mark.parametrize('cur_country', random.sample(["de", "ua"], 1), )
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_130
    def test_130_link_go_to_all_cryptocurrencies_does_not_open_cfd_page(
            self, worker_id, d, cur_language, cur_country, cur_role,
            cur_login, cur_password):
        """
        Check:  "Alle Kryptowährungen" (Go to all cryptocurrencies) is not implemented as a link
                when the German language is selected in the block "Why trade cryptocurrency with Capital.com"
        Language: DE.
        Country: CYSEC, SCB
        Role: NoReg, Auth, NoAuth,
        Author: Artem Dashkov
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "130",
            "Testing link [Go to all cryptocurrencies] in menu [Cryptocurrency trading]",
            False, False
        )

        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                           cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        cur_item_link = page_menu.open_education_cryptocurrency_trading_menu(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_129(d, cur_item_link, bid)
        test_element.arrange(d, cur_language)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test of the link [Browse all markets] in menu [Charges & fees]")
    @pytest.mark.parametrize('cur_language', random.sample(["de", "es", "it", "ru", "cn", "zh",
                                                            "fr", "pl", "ro", "nl", "el", "hu"], 2),)
    @pytest.mark.parametrize('cur_country', random.sample(["de", "ua"], 1), )
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_149
    def test_149_link_browse_all_markets_does_not_open_markets_page_on_parameters_language(
            self, worker_id, d, cur_language, cur_country, cur_role,
            cur_login, cur_password):
        """
        Check:  After clicking the link "Browse all markets"
                on page "Charges & fees" in not EN language
                always open EN-language version of page "Markets"
        Language: All, except EN (AND AR)
        Country: CYSEC, SCB
        Role: NoReg, Auth, NoAuth
        Author: Artem Dashkov
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "149",
            "Testing link [Browse all markets] in menu [Charges & fees]",
            False, False
        )

        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                           cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        cur_item_link = page_menu.open_charges_and_fees_submenu_products_and_services_menu(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_149(d, cur_item_link, bid)
        test_element.arrange(d, cur_language)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d, cur_language)

    @allure.step("Start test of the link [demo account] in the 'Main page'")
    @pytest.mark.parametrize('cur_language', random.sample(["hu", "ru"],1))
    @pytest.mark.parametrize('cur_country', random.sample(["de", "ua"], 1), )
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_151
    def test_151_link_demo_account_does_not_open_demo_account_page_on_parameters_language(
            self, worker_id, d, cur_language, cur_country, cur_role,
            cur_login, cur_password):
        """
        Check:  The [demo account] page is opened in EN language instead corresponding language,
                when clicked [demo account] link on the "Main page" for HU or RU language is selected
        Language: HU, RU
        Country: CYSEC, SCB
        Role: NoReg, Auth, NoAuth
        Author: Artem Dashkov
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "151",
            "Testing link [demo account] on the 'Main page'",
            False, False
        )
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                           cur_role, cur_login, cur_password)

        test_element = BUG_151(d, cur_item_link, bid)
        test_element.arrange(d, cur_language, cur_item_link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d, cur_language)

    @allure.step("Start test of the Search field [How can we help?] in menu [Help & Support]")
    @pytest.mark.parametrize('cur_country', random.sample(["de", "ua"], 1), )
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_171
    def test_171_search_field_does_not_search_in_help_and_support_menu(
            self, worker_id, d, cur_language_and_query, cur_country, cur_role,
            cur_login, cur_password):
        """
        Check:  The search field [How can we help?] on the menu title [Help & Support]
                of the section menu "More" isn't searched when any language is selected
        Language: All (except ar).
        Country: CYSEC, SCB
        Role: NoReg, Auth, NoAuth,
        Search_query: cur_search_query_2_rnd_from_10
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_and_query[0], cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "171",
            "Testing Search field [How can we help?] in menu [Help & Support]",
            False, False
        )

        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language_and_query[0], cur_country,
                                    cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        cur_item_link = page_menu.open_more_menu_help_and_support_submenu(
            d, cur_language_and_query[0], cur_country, cur_item_link)

        test_element = BUG_171(d, cur_item_link, bid)
        test_element.arrange(d)

        # Act
        test_element.act(d, cur_language_and_query[1])

        # Assert
        test_element.assert_(d, cur_item_link)

    @allure.step("Start test of the [How we manage your money] link on the 'How Capital.com makes money' page")
    @pytest.mark.parametrize('cur_language', ["ar"])
    @pytest.mark.parametrize('cur_country', ["ae"])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_257
    def test_257_link_how_we_manage_your_money_does_not_open_client_funds_page_on_parameters_language(
            self, worker_id, d, cur_language, cur_country, cur_role,
            cur_login, cur_password):
        """
        Check:  The "Charges and fees" page is opened instead "Client funds" page,
                when clicked [How we manage your money] link in "You might also be interested in..." block
                on the "How Capital.com makes money" page for AR language is selected.
        Language: AR
        Country: SCA
        Role: NoReg, Auth, NoAuth
        Author: Artem Dashkov
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "257",
            "Testing link [How we manage your money] in 'You might also be interested in...' block "
            "on the 'How Capital.com makes money' page",
            False, False
        )
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                           cur_role, cur_login, cur_password)

        page_menu = from_pricing_menu_open_how_capital_com_makes_money.MenuNew(d, cur_item_link)
        cur_item_link = page_menu.from_pricing_menu_open_how_capital_com_makes_money(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_257(d, cur_item_link, bid)
        test_element.arrange(d, cur_language, cur_item_link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d, cur_language)

    @allure.step("Start test of the [Open an account] button on the 'Trading platforms' page")
    @pytest.mark.parametrize('cur_language', ["ar"])
    @pytest.mark.parametrize('cur_country', ["ae"])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_265
    def test_265_button_open_an_account_does_not_open_contact_us_page_on_parameters_language(
            self, worker_id, d, cur_language, cur_country, cur_role,
            cur_login, cur_password):
        """
        Check:  The page with "404 error" message is displayed instead "Contact us" page,
                when clicked the button [Open an account] in the block "We’re here to help"
                on the page "Trading platforms" for AR language is selected
        Language: AR
        Country: SCA
        Role: NoReg, Auth, NoAuth
        Author: Artem Dashkov
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "265",
            "Testing button [Open an account] in 'We’re here to help' block "
            "on the 'Trading platforms' page",
            False, False
        )
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                           cur_role, cur_login, cur_password)

        page_menu = from_trading_menu_open_all_platforms.MenuNew(d, cur_item_link)
        link = page_menu.from_trading_menu_open_all_platforms(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_265(d, link, bid)
        test_element.arrange(d, cur_language, link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d, cur_language)

    @allure.step("Start test of the [Explore features] button in the 'Web platform' page")
    @pytest.mark.parametrize('cur_language', ["ar"])
    @pytest.mark.parametrize('cur_country', ["ae"])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_300
    def test_300_button_explore_features_does_not_open_trading_view_page_on_parameters_language(
            self, worker_id, d, cur_language, cur_country, cur_role,
            cur_login, cur_password):
        """
        Check:  The "TradingView" page is opened in EN language instead AR language,
                when clicked [Explore features] button on the "Web platform" page for AR language is selected
        Language: AR
        Country: SCA
        Role: NoReg, Auth, NoAuth
        Author: Artem Dashkov
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "300",
            "Testing button [Explore features] on the 'Web platform' page",
        )
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                           cur_role, cur_login, cur_password)

        page_menu = from_trading_menu_open_web_platform.MenuNew(d, cur_item_link)
        link = page_menu.from_trading_menu_open_web_platform(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_300(d, link, bid)
        test_element.arrange(d, cur_language, link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d, cur_language)

    @allure.step("Start test of the [MT4 platforms] link on the 'Forex' page")
    @pytest.mark.parametrize('cur_language', [""])
    @pytest.mark.parametrize('cur_country', ["ae"])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_312
    def test_312_link_mt4_platforms_does_not_open_mt4_page_on_parameters_language(
            self, worker_id, d, cur_language, cur_country, cur_role,
            cur_login, cur_password):
        """
        Check:  The "TradingView" page is opened instead "MT4" page,
                when clicked the link [MT4 platforms] in the block "Forex trading"
                on the page "Forex" for EN language is selected
        Language: EN
        Country: SCA
        Role: NoReg, Auth, NoAuth
        Author: Artem Dashkov
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "312",
            "Testing link [MT4 platforms] in 'Forex trading' block "
            "on the 'Forex' page",
            False, False
        )
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                           cur_role, cur_login, cur_password)

        page_menu = from_markets_menu_open_forex.MenuNewForex(d, cur_item_link)
        link = page_menu.from_markets_menu_open_forex(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_312(d, link, bid)
        test_element.arrange(d, link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test of the menu item [Demo] in the menu section [Trading]")
    @pytest.mark.parametrize('cur_language', ["ar"])
    @pytest.mark.parametrize('cur_country', ["ae"])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_324
    def test_324_menu_item_demo_is_not_displayed_in_the_header(
            self, worker_id, d, cur_language, cur_country, cur_role,
            cur_login, cur_password):
        """
        Check:  The text of the menu item [Demo] of the menu title [Trading tools]
                in the menu section [Trading] is not displayed in the header when AR language is selected
        Language: AR
        Country: SCA
        Role: NoReg, Auth, NoAuth
        Author: Artem Dashkov
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "324",
            "The text of the menu item [Demo] of the menu title [Trading tools] "
            "in the menu section [Trading] is not displayed in the header when AR language is selected",
            False, False
        )
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                           cur_role, cur_login, cur_password)

        test_element = BUG_324(d, cur_item_link, bid)
        test_element.arrange(d, cur_item_link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test of the sidebar title 'Shares trading guide'")
    @pytest.mark.parametrize('cur_language', random.sample(["", "ar", "de", "es", "it", "ru", "cn",
                                                            "zh", "fr", "pl", "ro", "nl"], 2),)
    @pytest.mark.parametrize('cur_country', random.sample(["de", "ua"], 1), )
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_334
    def test_334_sidebar_title_shares_trading_guide_is_not_displayed(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check:  The sidebar title [Shares trading guide] is not displayed
                when selected any sidebar item in the sidebar "Shares trading guide"
        Language: All (except EL, HU).
        License/Country: CYSEC, SCB
        Role: NoReg, NoAuth, Auth
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "334",
            "The sidebar title [Shares trading guide] is not displayed"
            " when selected any sidebar item in the sidebar [Shares trading guide]",
            False, False
        )
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                           cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        menu_link = page_menu.open_education_shares_trading_menu(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_334(d, menu_link, bid)
        test_element.arrange(d, menu_link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test of check widget in the block 'Our spread betting markets'")
    @pytest.mark.parametrize('cur_language', [""])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.parametrize('cur_tool', ["Commodities", "Shares"])
    @pytest.mark.bug_357
    def test_357_widget_in_the_block_our_spread_betting_markets_is_not_displayed(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_tool):
        """
        Check:  The widget of the block "Our spread betting markets" is absent
                when click on the button [Commodities] or [Shares] on the page "Spread betting"
        Language: EN
        License/Country: FCA
        Role: NoReg, NoAuth, Auth
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "357",
            "Menu section [Trading] > Menu item [Spread betting] > "
            "The widget of the block 'Our spread betting markets' > Click on the button [Commodities]",
            False, True
        )
        # pytest.skip("Промежуточная версия")
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                           cur_role, cur_login, cur_password)

        page_menu = from_trading_menu_open_spread_betting.MenuNewSpreadBetting(d, cur_item_link)
        link = page_menu.from_trading_menu_open_spread_betting(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_357(d, link, bid)
        test_element.arrange(d, link)

        # Act
        test_element.act(d, cur_tool)

        # Assert
        test_element.assert_(d, cur_tool)

    @allure.step("Start test of check selected country in Dropdown [Country & Language]")
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_362
    def test_362_selected_country_in_dropdown_country_and_language_is_not_displayed(
            self, worker_id, d, cur_language_country_for_fca_and_sca, cur_role, cur_login, cur_password):
        """
        Check:  Click to the dropdown [Regional settings] > Click to the dropdown [Countries] >
                Scroll down to the "Honk Kong & Taiwan" > Select "Honk Kong & Taiwan" > Click the button [Apply]
                > Check country in Dropdown [Country & Language]
        Language: EN - FCA, SCA; AR - SCA
        License/Country: FCA, SCA
        Role: NoReg, NoAuth, Auth
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_country_for_fca_and_sca[0],
            cur_language_country_for_fca_and_sca[1], cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "362",
            "Click to the dropdown [Regional settings] > Click to the dropdown [Countries] > "
            "Scroll down to the 'Honk Kong & Taiwan' > Select 'Honk Kong & Taiwan' > Click the button [Apply]",
            False, True
        )
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language_country_for_fca_and_sca[0],
                                                    cur_language_country_for_fca_and_sca[1],
                                                    cur_role, cur_login, cur_password)

        test_element = BUG_362(d, cur_item_link, bid)
        test_element.arrange(d, cur_item_link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d, cur_language_country_for_fca_and_sca[0], cur_language_country_for_fca_and_sca[1])

    @allure.step("Start test of link 'Discover what you can trade' in block 'Why choose Capital.com?'")
    @pytest.mark.parametrize('cur_language', [""])
    @pytest.mark.parametrize('cur_country', ['au'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_370
    def test_370_link_in_the_block_why_choose_capital_com_does_not_open_page(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check:  Menu section [About us] > Menu item [Why Capital.com?] >
                Find block 'Why choose Capital.com?' > Click the link 'Discover what you can trade'
        Language: EN
        License/Country: ASIC
        Role: NoReg, NoAuth, Auth
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "370",
            "Menu section [About us] > Menu item [Why Capital.com?] > "
            "Find block 'Why choose Capital.com?' > Click the link 'Discover what you can trade'",
            False, True
        )
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                                    cur_role, cur_login, cur_password)

        page_menu = from_about_us_menu_open_why_capital.MenuNew(d, cur_item_link)
        link = page_menu.from_about_us_menu_open_why_capital(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_370(d, link, bid)
        test_element.arrange(d, link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test of link 'Capital.com' in block 'Capital.com is an execution-only brokerage platform…'")
    @pytest.mark.parametrize('cur_language', [""])
    @pytest.mark.parametrize('cur_country', ['au'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_377
    def test_377_link_in_the_block_capital_com_is_an_execution_only_brokerage_platform_does_not_open_page(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check:  Menu section [Markets] > Menu item [Market analysis] >
                Find articles and click article link > Click the link 'Capital.com'
                in block 'Capital.com is an execution-only brokerage platform…'
        Language: EN
        License/Country: ASIC
        Role: NoReg, NoAuth, Auth
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "377",
            "Menu section [Markets] > Menu item [Market analysis] > "
            "Find articles and click article link > Click the link 'Capital.com'"
            "in block 'Capital.com is an execution-only brokerage platform…'",
            False, True
        )
        # pytest.skip("Промежуточная версия")
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                                    cur_role, cur_login, cur_password)

        page_menu = from_markets_menu_open_market_analysis.MenuNew(d, cur_item_link)
        link = page_menu.from_markets_menu_open_market_analysis(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_377(d, link, bid)
        test_element.arrange(d, link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test of link 'Daniela Hathorn' on page 'ECB Preview…'")
    @pytest.mark.parametrize('cur_language', [""])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_383
    def test_383_link_daniela_hathorn_on_the_page_ecb_preview_does_not_open(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check:  Menu section [Markets] > Menu item [Market analysis] >
                Find and click article link “ECB Preview: Higher CPI expected to keep Lagarde on a hawkish path” >
                Click the link 'Daniela Hathorn'
        Language: EN
        License/Country: SCA
        Role: NoReg, NoAuth, Auth
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "383",
            "Menu section [Markets] > Menu item [Market analysis] > "
            "Find and click article link 'ECB Preview: Higher CPI expected to keep Lagarde on a hawkish path' > "
            "Click the link 'Daniela Hathorn'",
            False, True
        )
        # pytest.skip("Промежуточная версия")
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                                    cur_role, cur_login, cur_password)

        page_menu = from_markets_menu_open_market_analysis.MenuNew(d, cur_item_link)
        link = page_menu.from_markets_menu_open_market_analysis(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_383(d, link, bid)
        test_element.arrange(d, link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test of links 'CFDs' and 'ETFs' on page 'What is commodity trading'")
    @pytest.mark.parametrize('cur_language', [""])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.parametrize('type_of_markets', ["CFDs", "ETFs"])
    @pytest.mark.bug_406
    def test_406_link_cfds_and_etfs_on_page_what_is_commodity_trading_open_on_other_license(
            self, worker_id, d, cur_language, cur_country, cur_role, type_of_markets, cur_login, cur_password):
        """
        Check:  Menu section [Markets] >
                Menu item [Commodities] >
                Scroll down to the block “Why trade commodities with Capital.com?” >
                Click the link “Learn more about commodities trading” >
                Scroll down to the text block “Frequently asked questions” >
                Сlick the header of the accordion “How do you trade commodities?” >
                Click the links “CFDs” / ”exchange traded funds”
        Language: EN
        License/Country: SCA
        Role: NoReg, NoAuth, Auth
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "406",
            "Menu section [Markets] > Menu item [Commodities] >"
            "Scroll down to the block 'Why trade commodities with Capital.com?' >"
            "Click the link 'Learn more about commodities trading' >"
            "Scroll down to the text block 'Frequently asked questions' >"
            "Сlick the header of the accordion 'How do you trade commodities?' >"
            "Click the links 'CFDs' or 'exchange traded funds'",
            False, True
        )
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                                    cur_role, cur_login, cur_password)

        page_menu = from_markets_menu_open_commodities.MenuNew(d, cur_item_link)
        link = page_menu.from_markets_menu_open_commodities(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_406(d, link, bid)
        test_element.arrange(d, link, type_of_markets)

        # Act
        test_element.act(d, type_of_markets)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test authors of articles on the 'Daniela Hathorn' page")
    @pytest.mark.parametrize('cur_language', [""])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_407
    def test_407_articles_all_authors_present_on_the_daniela_hathorn_page(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check:  Menu section [Markets] > Menu item [Market analysis] >
                Find and click article of 'Daniela Hathorn' author >
                Click the link 'Daniela Hathorn' >
                Click any article on the 'Daniela Hathorn' page
        Language: EN
        License/Country: SCA
        Role: NoReg, NoAuth, Auth
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "407",
            "Menu section [Markets] > Menu item [Market analysis] > "
            "Find and click article of 'Daniela Hathorn' author > "
            "Click the link 'Daniela Hathorn' > "
            "Click any article on the 'Daniela Hathorn' page",
            False, True
        )
        pytest.skip("Промежуточная версия")
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                                    cur_role, cur_login, cur_password)

        page_menu = from_markets_menu_open_market_analysis.MenuNew(d, cur_item_link)
        link = page_menu.from_markets_menu_open_market_analysis(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_407(d, link, bid)
        test_element.arrange(d, link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d)
