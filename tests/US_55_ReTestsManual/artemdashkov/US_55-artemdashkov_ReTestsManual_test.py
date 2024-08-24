"""
-*- coding: utf-8 -*-
@Time    : 2024/05/18 18:00 GMT+3
@Author  : Artem Dashkov
"""

import allure
import pytest
import random
from datetime import datetime
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
from src.src import CapitalComPageSrc
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55
from pages.conditions import Conditions
from pages.Menu.menu import MenuSection
from pages.Menu.New import (from_trading_menu_open_web_platform,
                            from_pricing_menu_open_how_capital_com_makes_money,
                            from_trading_menu_open_platforms,
                            from_markets_menu_open_forex)
from pages.conditions_new import NewConditions


@pytest.mark.us_55
class TestManualDetected:
    page_conditions = None

    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.bug_016a
    @allure.step("Start test of button [Add to favourite] on the 'Trading Instrument Page'")
    def test_016a_add_to_favourite_button_on_trading_instrument_page(
            self, worker_id, d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, cur_role,
            cur_login, cur_password, cur_market_1_rnd_from_5):
        """
        Check:  The trading platform is opened, not the page
                of the corresponding trading instrument on the trading platform
        Language: All.
        License: Not FCA
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "016a",
            "The trading platform is opened, "
            "not the page of the corresponding trading instrument on the trading platform",
            False, False
        )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_2_rnd_from_14,
            cur_country_1_rnd_from_3, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = None
        match cur_market_1_rnd_from_5:
            case "Shares":
                cur_item_link = menu.open_shares_market_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, link)
            case "Forex":
                cur_item_link = menu.open_forex_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, link)
            case "Indices":
                cur_item_link = menu.open_indices_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, link)
            case "Commodities":
                cur_item_link = menu.open_commodities_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, link)
            case "Cryptocurrencies":
                cur_item_link = menu.open_cryptocurrencies_market_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, link)

        test_element = TradePageAddToFavoriteButton(d, cur_item_link, bid)
        test_element.full_test(
            d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, cur_role, cur_item_link, cur_market_1_rnd_from_5)

    @allure.step("Start test of button [Go to platform] on tooltip 'Long position overnight fee'")
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.bug_016b
    def test_016b_add_to_favourite_button_on_tooltip_long_position_overnight_fee(
            self, worker_id, d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, cur_role,
            cur_login, cur_password, cur_market_1_rnd_from_5):
        """
        Check:  The trading platform is opened, not the page
                of the corresponding trading instrument on the trading platform
        Language: All.
        License: Not FCA
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "016b",
            "The trading platform is opened, "
            "not the page of the corresponding trading instrument on the trading platform",
            False, False
        )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_2_rnd_from_14,
            cur_country_1_rnd_from_3, cur_role, cur_login, cur_password)

        cur_item_link = None
        menu = MenuSection(d, link)
        match cur_market_1_rnd_from_5:
            case "Shares":
                cur_item_link = menu.open_shares_market_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, link)
            case "Forex":
                cur_item_link = menu.open_forex_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, link)
            case "Indices":
                cur_item_link = menu.open_indices_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, link)
            case "Commodities":
                cur_item_link = menu.open_commodities_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, link)
            case "Cryptocurrencies":
                cur_item_link = menu.open_cryptocurrencies_market_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, link)

        test_element = TradePageAddToFavoriteButton(d, cur_item_link, bid)
        test_element.arrange_1(d, cur_item_link, cur_market_1_rnd_from_5)

        cur_item_link = d.current_url
        test_element = PageInstrumentLongPositionGoToPlatformButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi_v2(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, cur_role, cur_item_link)

    @allure.step("Start test of button [Go to platform] on tooltip 'Short position overnight fee'")
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.bug_016c
    def test_016c_add_to_favourite_button_on_tooltip_short_position_overnight_fee(
            self, worker_id, d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, cur_role,
            cur_login, cur_password, cur_market_1_rnd_from_5):
        """
        Check:  The trading platform is opened, not the page of the corresponding trading instrument
                on the trading platform
        Language: All.
        License: Not FCA
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "016c",
            "The trading platform is opened, "
            "not the page of the corresponding trading instrument on the trading platform",
            False, False
        )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_2_rnd_from_14,
            cur_country_1_rnd_from_3, cur_role, cur_login, cur_password)

        cur_item_link = None
        menu = MenuSection(d, link)
        match cur_market_1_rnd_from_5:
            case "Shares":
                cur_item_link = menu.open_shares_market_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, link)
            case "Forex":
                cur_item_link = menu.open_forex_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, link)
            case "Indices":
                cur_item_link = menu.open_indices_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, link)
            case "Commodities":
                cur_item_link = menu.open_commodities_markets_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, link)
            case "Cryptocurrencies":
                cur_item_link = menu.open_cryptocurrencies_market_menu(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, link)

        test_element = TradePageAddToFavoriteButton(d, cur_item_link, bid)
        test_element.arrange_1(d, cur_item_link, cur_market_1_rnd_from_5)

        cur_item_link = d.current_url
        test_element = PageInstrumentShortPositionGoToPlatformButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, cur_role, cur_item_link)

    @allure.step("Start test of button [Try now] on the block 'Why choose Capital.com?'")
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_017
    def test_017_try_now_button_on_why_choose_capital_com_block(
            self, worker_id, d, cur_language_2_rnd_from_12, cur_country_1_rnd_from_3, cur_role, cur_login, cur_password):
        """
        Check:  Sign up/log in/forms or the transition to the trading platform are
                not opened after clicking the [Try now] button in "Why choose
                Capital.com?.." Block in the menu item [Our Mobile Apps]
        Language: All.
        License: Not FCA
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_2_rnd_from_12, cur_country_1_rnd_from_3, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "017",
            "Sign up/log in/forms or the transition to the trading platform are not opened "
            "after clicking the [Try now] button in 'Why choose Capital.com?..' Block "
            "in the menu item [Our Mobile Apps]",
            False, False
        )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_2_rnd_from_12,
            cur_country_1_rnd_from_3, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_our_mobile_apps_submenu_products_and_services_menu(
            d, cur_language_2_rnd_from_12, cur_country_1_rnd_from_3, link
        )

        test_element = WhyChooseBlockTryNowButtonInContent(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language_2_rnd_from_12, cur_country_1_rnd_from_3, cur_role, cur_item_link)

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

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

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
            self, worker_id, d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, cur_role,
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
            d, worker_id, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "045a",
            "Testing field [email] in Sign up form",
            False, False
        )

        d.refresh()
        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_2_rnd_from_14,
            cur_country_1_rnd_from_3, cur_role, cur_login, cur_password)

        test_element = EmailFieldSignUpForm(d, cur_item_link, bid)
        test_element.full_test(
            d, cur_language_2_rnd_from_14, cur_country_1_rnd_from_3, cur_role,
            cur_item_link, invalid_login, valid_password)

    @allure.step("Start test of voted function in 'What is your sentiment...' block")
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_074
    def test_074_voted_function_in_sentiment_block(
            self, worker_id, d, cur_language, cur_country_1_rnd_from_3, cur_role, cur_login, cur_password):
        """
        Check:  Not possible to vote for another trading instrument
                in the block "What is your sentiment..."  if on another page voted for another instrument
        Language: All.
        License/Country: All
        Role: NoReg, NoAuth, Auth
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country_1_rnd_from_3, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "074",
            "Not possible to vote for another trading instrument "
            "in the block 'What is your sentiment...' if on another page voted for another instrument",
            False, False
        )

        # Arrange
        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country_1_rnd_from_3,
            cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        menu_link = page_menu.open_news_and_analysis_market_analysis_menu(
            d, cur_language, cur_country_1_rnd_from_3, cur_item_link)
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
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_104
    def test_104_trading_calculator_collapse_after_setting_duration(
            self, worker_id, d, cur_language, cur_country_1_rnd_from_3, cur_role,
            cur_login, cur_password, calc_1_and_calc_2):
        """
        Check: The trading calculator is collapsed in the menu section [Markets] --> [CFD calculator]
        after setting the maximum duration on the Prof/Loss element and changing the asset
        Language: En.
        Country: CYSEC, ASIC, SCB
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
            d, worker_id, cur_language, cur_country_1_rnd_from_3, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "104",
            "Testing 'Trading calculator' widget in menu [CFD calculator]",
            False, False
        )

        # Arrange
        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country_1_rnd_from_3,
            cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        cur_item_link = page_menu.open_markets_menu_cfd_calculator_submenu(
            d, cur_language, cur_country_1_rnd_from_3, cur_item_link)

        test_element = TradingCalculatorCFDCalculatorPage(d, cur_item_link, bid)
        test_element.arrange(d)

        # Act
        test_element.act(d, calc_1_and_calc_2)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test of the link [Go to all cryptocurrencies] in menu [Cryptocurrency trading]")
    @pytest.mark.parametrize('cur_language', random.sample(["ro", "it", "pl", "cn"], 2), )
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_129
    def test_129_link_go_to_all_cryptocurrencies_does_not_open_cfd_page(
            self, worker_id, d, cur_language, cur_country_1_rnd_from_3, cur_role,
            cur_login, cur_password):
        """
        Check:  The Main page is opened instead of the Cryptocurrencies page on the page
                "Cryptocurrency trading" after clicking the button [Go to all cryptocurrencies]
                when RO, IT, PL or CN language is selected
        Language: RO, IT, PL, CN.
        Country: CYSEC, ASIC, SCB
        Role: NoReg, Auth, NoAuth,
        Author: Artem Dashkov
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country_1_rnd_from_3, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "129",
            "Testing button [Go to all cryptocurrencies] in menu [Cryptocurrency trading]",
            False, False
        )

        # Arrange
        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country_1_rnd_from_3,
            cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        cur_item_link = page_menu.open_education_cryptocurrency_trading_menu(
            d, cur_language, cur_country_1_rnd_from_3, cur_item_link)

        test_element = BUG_129(d, cur_item_link, bid)
        test_element.arrange(d, cur_language)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test of the link [Go to all cryptocurrencies] "
                 "in menu [Cryptocurrency trading] for Germany language")
    @pytest.mark.parametrize('cur_language', ["de"])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_130
    def test_130_link_go_to_all_cryptocurrencies_does_not_open_cfd_page(
            self, worker_id, d, cur_language, cur_country_1_rnd_from_3, cur_role,
            cur_login, cur_password):
        """
        Check:  "Alle Kryptowährungen" (Go to all cryptocurrencies) is not implemented as a link
                when the German language is selected in the block "Why trade cryptocurrency with Capital.com"
        Language: DE.
        Country: CYSEC, ASIC, SCB
        Role: NoReg, Auth, NoAuth,
        Author: Artem Dashkov
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country_1_rnd_from_3, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "130",
            "Testing link [Go to all cryptocurrencies] in menu [Cryptocurrency trading]",
            False, False
        )

        # Arrange
        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country_1_rnd_from_3,
            cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        cur_item_link = page_menu.open_education_cryptocurrency_trading_menu(
            d, cur_language, cur_country_1_rnd_from_3, cur_item_link)

        test_element = BUG_129(d, cur_item_link, bid)
        test_element.arrange(d, cur_language)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test of the link [Browse all markets] in menu [Charges & fees]")
    @pytest.mark.parametrize('cur_language', random.sample(["de", "es", "it", "ru", "cn", "zh",
                                                            "fr", "pl", "ro", "nl", "el", "hu"], 2),)
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_149
    def test_149_link_browse_all_markets_does_not_open_markets_page_on_parameters_language(
            self, worker_id, d, cur_language, cur_country_1_rnd_from_3, cur_role,
            cur_login, cur_password):
        """
        Check:  After clicking the link "Browse all markets"
                on page "Charges & fees" in not EN language
                always open EN-language version of page "Markets"
        Language: All, except EN (AND AR)
        Country: CYSEC, ASIC, SCB
        Role: NoReg, Auth, NoAuth
        Author: Artem Dashkov
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country_1_rnd_from_3, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "149",
            "Testing link [Browse all markets] in menu [Charges & fees]",
            False, False
        )

        # Arrange
        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country_1_rnd_from_3,
            cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        cur_item_link = page_menu.open_charges_and_fees_submenu_products_and_services_menu(
            d, cur_language, cur_country_1_rnd_from_3, cur_item_link)

        test_element = BUG_149(d, cur_item_link, bid)
        test_element.arrange(d, cur_language)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d, cur_language)

    @allure.step("Start test of the link [demo account] in the 'Main page'")
    @pytest.mark.parametrize('cur_language', random.sample(["hu", "ru"],1))
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_151
    def test_151_link_demo_account_does_not_open_demo_account_page_on_parameters_language(
            self, worker_id, d, cur_language, cur_country_1_rnd_from_3, cur_role,
            cur_login, cur_password):
        """
        Check:  The [demo account] page is opened in EN language instead corresponding language,
                when clicked [demo account] link on the "Main page" for HU or RU language is selected
        Language: HU, RU
        Country: CYSEC, ASIC, SCB
        Role: NoReg, Auth, NoAuth
        Author: Artem Dashkov
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country_1_rnd_from_3, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "151",
            "Testing link [demo account] on the 'Main page'",
            False, False
        )
        # Arrange
        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country_1_rnd_from_3,
            cur_role, cur_login, cur_password)

        test_element = BUG_151(d, cur_item_link, bid)
        test_element.arrange(d, cur_language, cur_item_link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d, cur_language)

    @allure.step("Start test of the Search field [How can we help?] in menu [Help & Support]")
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_171
    def test_171_search_field_does_not_search_in_help_and_support_menu(
            self, worker_id, d, cur_language_and_query, cur_country_1_rnd_from_3, cur_role,
            cur_login, cur_password):
        """
        Check:  The search field [How can we help?] on the menu title [Help & Support]
                of the section menu "More" isn't searched when any language is selected
        Language: All (except ar).
        Country: CYSEC, ASIC, SCB
        Role: NoReg, Auth, NoAuth,
        Search_query: cur_search_query_2_rnd_from_10
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_and_query[0], cur_country_1_rnd_from_3, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "171",
            "Testing Search field [How can we help?] in menu [Help & Support]",
            False, False
        )

        # Arrange
        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_and_query[0],
            cur_country_1_rnd_from_3, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        cur_item_link = page_menu.open_more_menu_help_and_support_submenu(
            d, cur_language_and_query[0], cur_country_1_rnd_from_3, cur_item_link)

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
        page_conditions = NewConditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_AR_AE, "", cur_language, cur_country,
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
        page_conditions = NewConditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_AR_AE, "", cur_language, cur_country,
            cur_role, cur_login, cur_password)

        page_menu = from_trading_menu_open_platforms.MenuNew(d, cur_item_link)
        cur_item_link = page_menu.from_trading_menu_open_trading_platforms(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_265(d, cur_item_link, bid)
        test_element.arrange(d, cur_language, cur_item_link)

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
        page_conditions = NewConditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_AR_AE, "", cur_language, cur_country,
            cur_role, cur_login, cur_password)

        page_menu = from_trading_menu_open_web_platform.MenuNew(d, cur_item_link)
        cur_item_link = page_menu.from_trading_menu_open_web_platform(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_300(d, cur_item_link, bid)
        test_element.arrange(d, cur_language, cur_item_link)

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
        page_conditions = NewConditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_EN_AE, "", cur_language, cur_country,
            cur_role, cur_login, cur_password)

        page_menu = from_markets_menu_open_forex.MenuNewForex(d, cur_item_link)
        cur_item_link = page_menu.from_markets_menu_open_forex(
            d, cur_language, cur_country, cur_item_link)

        test_element = BUG_312(d, cur_item_link, bid)
        test_element.arrange(d, cur_item_link)

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
        page_conditions = NewConditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_EN_AE, "", cur_language, cur_country,
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
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_334
    def test_334_sidebar_title_shares_trading_guide_is_not_displayed(
            self, worker_id, d, cur_language, cur_country_1_rnd_from_3, cur_role, cur_login, cur_password):
        """
        Check:  The sidebar title [Shares trading guide] is not displayed
                when selected any sidebar item in the sidebar "Shares trading guide"
        Language: All (except EL, HU).
        License/Country: ASIC, CYSEC, SCB
        Role: NoReg, NoAuth, Auth
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country_1_rnd_from_3, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "334",
            "The sidebar title [Shares trading guide] is not displayed"
            " when selected any sidebar item in the sidebar [Shares trading guide]",
            False, False
        )
        pytest.skip("Промежуточная версия: add test_334 and test class")
        # Arrange
        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country_1_rnd_from_3,
            cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        menu_link = page_menu.open_education_shares_trading_menu(
            d, cur_language, cur_country_1_rnd_from_3, cur_item_link)

        test_element = BUG_334(d, menu_link, bid)
        test_element.arrange(d, menu_link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d)
