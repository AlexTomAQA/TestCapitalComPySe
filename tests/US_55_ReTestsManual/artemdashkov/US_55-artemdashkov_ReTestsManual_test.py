"""
-*- coding: utf-8 -*-
@Time    : 2024/05/18 18:00 GMT+3
@Author  : Artem Dashkov
"""

import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.common import Common
from datetime import datetime
from pages.Elements.ContentsBlockLearnMoreAboutUsLink import ContentsBlockLearnMoreAboutUsLink
from pages.Elements.TradePageAddToFavoriteButton import TradePageAddToFavoriteButton
from pages.Elements.WhyChooseBlockTryNowButtonInContent import WhyChooseBlockTryNowButtonInContent
from pages.Elements.PageInstrumentLongPositionGoToPlatformButton import PageInstrumentLongPositionGoToPlatformButton
from pages.Elements.PageInstrumentShortPositionGoToPlatformButton import PageInstrumentShortPositionGoToPlatformButton
from pages.Elements.EmailFieldSignUpForm import EmailFieldSignUpForm
from pages.BugsManual.bug_058 import WhatIsYourSentimentWidget
from pages.BugsManual.bug_077 import TradingCalculatorCFDCalculatorPage
from src.src import CapitalComPageSrc
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55
from pages.conditions import Conditions
from pages.Menu.menu import MenuSection
from pages.conditions_new import NewConditions


@pytest.mark.us_55
class TestManualDetected:
    page_conditions = None

    @pytest.mark.parametrize('cur_country', ['de', 'au', 'ua'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.test_011a
    @allure.step("Start test of button [Add to favourite] on the 'Trading Instrument Page'")
    def test_011a_add_to_favourite_button_on_trading_instrument_page(
            self, worker_id, d, cur_language_3_rnd_from_14, cur_country, cur_role,
            cur_login, cur_password, cur_market_2_rnd_from_5):
        """
        Check: The trading platform is opened, not the page of the corresponding trading instrument on the trading platform
        Language: All.
        License: Not FCA
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_3_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "011a",
            "Testing button [Add to favourite] on the 'Trading Instrument Page'",
            False, False
        )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_3_rnd_from_14, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = None
        match cur_market_2_rnd_from_5:
            case "Shares":
                cur_item_link = menu.open_shares_market_menu(d, cur_language_3_rnd_from_14, cur_country, link)
            case "Forex":
                cur_item_link = menu.open_forex_markets_menu(d, cur_language_3_rnd_from_14, cur_country, link)
            case "Indices":
                cur_item_link = menu.open_indices_markets_menu(d, cur_language_3_rnd_from_14, cur_country, link)
            case "Commodities":
                cur_item_link = menu.open_commodities_markets_menu(d, cur_language_3_rnd_from_14, cur_country, link)
            case "Cryptocurrencies":
                cur_item_link = menu.open_cryptocurrencies_market_menu(d, cur_language_3_rnd_from_14, cur_country, link)

        test_element = TradePageAddToFavoriteButton(d, cur_item_link, bid)
        test_element.full_test(
            d, cur_language_3_rnd_from_14, cur_country, cur_role, cur_item_link, cur_market_2_rnd_from_5)

    @allure.step("Start test of button [Go to platform] on tooltip 'Long position overnight fee'")
    @pytest.mark.parametrize('cur_country', ['de', 'au', 'ua'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.test_011b
    def test_011b_add_to_favourite_button_on_tooltip_long_position_overnight_fee(
            self, worker_id, d, cur_language_3_rnd_from_14, cur_country, cur_role,
            cur_login, cur_password, cur_market_2_rnd_from_5):
        """
        Check: The trading platform is opened, not the page of the corresponding trading instrument on the trading platform
        Language: All.
        License: Not FCA
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_3_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "011b",
            "Testing button [Go to platform] on tooltip 'Long position overnight fee'",
            False, False
        )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_3_rnd_from_14, cur_country, cur_role, cur_login, cur_password)

        cur_item_link = None
        menu = MenuSection(d, link)
        match cur_market_2_rnd_from_5:
            case "Shares":
                cur_item_link = menu.open_shares_market_menu(d, cur_language_3_rnd_from_14, cur_country, link)
            case "Forex":
                cur_item_link = menu.open_forex_markets_menu(d, cur_language_3_rnd_from_14, cur_country, link)
            case "Indices":
                cur_item_link = menu.open_indices_markets_menu(d, cur_language_3_rnd_from_14, cur_country, link)
            case "Commodities":
                cur_item_link = menu.open_commodities_markets_menu(d, cur_language_3_rnd_from_14, cur_country, link)
            case "Cryptocurrencies":
                cur_item_link = menu.open_cryptocurrencies_market_menu(d, cur_language_3_rnd_from_14, cur_country, link)

        test_element = TradePageAddToFavoriteButton(d, cur_item_link, bid)
        test_element.arrange_1(d, cur_item_link, cur_market_2_rnd_from_5)

        cur_item_link = d.current_url
        test_element = PageInstrumentLongPositionGoToPlatformButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi_v2(d, cur_language_3_rnd_from_14, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Go to platform] on tooltip 'Short position overnight fee'")
    @pytest.mark.parametrize('cur_country', ['de', 'au', 'ua'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.test_011c
    def test_011c_add_to_favourite_button_on_tooltip_short_position_overnight_fee(
            self, worker_id, d, cur_language_3_rnd_from_14, cur_country, cur_role,
            cur_login, cur_password, cur_market_2_rnd_from_5):
        """
        Check:  The trading platform is opened, not the page of the corresponding trading instrument
                on the trading platform
        Language: All.
        License: Not FCA
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_3_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "011c",
            "Testing button [Go to platform] on tooltip 'Short position overnight fee'",
            False, False
        )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_3_rnd_from_14, cur_country, cur_role, cur_login, cur_password)

        cur_item_link = None
        menu = MenuSection(d, link)
        match cur_market_2_rnd_from_5:
            case "Shares":
                cur_item_link = menu.open_shares_market_menu(d, cur_language_3_rnd_from_14, cur_country, link)
            case "Forex":
                cur_item_link = menu.open_forex_markets_menu(d, cur_language_3_rnd_from_14, cur_country, link)
            case "Indices":
                cur_item_link = menu.open_indices_markets_menu(d, cur_language_3_rnd_from_14, cur_country, link)
            case "Commodities":
                cur_item_link = menu.open_commodities_markets_menu(d, cur_language_3_rnd_from_14, cur_country, link)
            case "Cryptocurrencies":
                cur_item_link = menu.open_cryptocurrencies_market_menu(d, cur_language_3_rnd_from_14, cur_country, link)

        test_element = TradePageAddToFavoriteButton(d, cur_item_link, bid)
        test_element.arrange_1(d, cur_item_link, cur_market_2_rnd_from_5)

        cur_item_link = d.current_url
        test_element = PageInstrumentShortPositionGoToPlatformButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language_3_rnd_from_14, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Try now] on the block 'Why choose Capital.com?'")
    @pytest.mark.parametrize('cur_country', ['de', 'au', 'ua'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.test_012
    def test_012_try_now_button_on_why_choose_capital_com_block(
            self, worker_id, d, cur_language_3_rnd_from_12, cur_country, cur_role, cur_login, cur_password):
        """
        Check:  Sign up/log in/forms or the transition to the trading platform are
                not opened after clicking the [Try now] button in "Why choose
                Capital.com?.." Block in the menu item [Our Mobile Apps]
        Language: All.
        License: Not FCA
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_3_rnd_from_12, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "012",
            "Testing button [Try now] on the block 'Why choose Capital.com?'",
            False, False
        )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_3_rnd_from_12, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_our_mobile_apps_submenu_products_and_services_menu(
            d, cur_language_3_rnd_from_12, cur_country, link
        )

        test_element = WhyChooseBlockTryNowButtonInContent(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language_3_rnd_from_12, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of link [Learn more about us] on the block 'Contents'")
    @pytest.mark.parametrize('cur_language', [""])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.test_024
    def test_024_learn_more_about_us_link_on_contents_block(
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
            "024",
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
    @pytest.mark.parametrize('cur_country', ['de', 'au', 'ua'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "NoAuth"])
    @pytest.mark.parametrize('invalid_login', ['КИРИЛЛИЦА_без_пробелов@gmail.com', 'LATIN with space@gmail.com'])
    @pytest.mark.parametrize('valid_password', ['VALID_password44!VALID_password44!VALID_password44!'])
    @pytest.mark.test_036a
    def test_036a_email_field_sign_up_form(
            self, worker_id, d, cur_language_3_rnd_from_14, cur_country, cur_role,
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
            d, worker_id, cur_language_3_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "036a",
            "Testing field [email] in Sign up form",
            False, False
        )

        d.refresh()
        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_3_rnd_from_14, cur_country, cur_role, cur_login, cur_password)

        test_element = EmailFieldSignUpForm(d, cur_item_link, bid)
        test_element.full_test(
            d, cur_language_3_rnd_from_14, cur_country, cur_role, cur_item_link, invalid_login, valid_password)

    @allure.step("Start test of voted function in 'What is your sentiment...' block")
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['de', 'au', 'ua'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.test_058
    def test_058_voted_function_in_sentiment_block(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: voted function in 'What is your sentiment...' block
        Language: All.
        License/Country: All
        Role: NoReg, NoAuth, Auth
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "058",
            "Testing voted function in 'What is your sentiment...' block",
            False, False
        )
        # pytest.skip("Промежуточная версия!")
        # Arrange
        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        menu_link = page_menu.open_news_and_analysis_market_analysis_menu(d, cur_language, cur_country, cur_item_link)
        test_element = WhatIsYourSentimentWidget(d, menu_link, bid)
        test_element.arrange(d, menu_link)

        # Act
        d.back()
        print(f"{datetime.now()}   Returned to article list page, current url is: {d.current_url}")
        # WebDriverWait(d, 30, poll_frequency=1).until(EC.url_changes(menu_link))
        test_element.act(d)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test of 'Trading calculator' widget in menu [CFD calculator]")
    @pytest.mark.parametrize('cur_language', ['en'])
    @pytest.mark.parametrize('cur_country', ['de', 'au', 'ua'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.parametrize('calc_instrument_1', ["EUR/USD", "GBP/USD", "Natural Gas", "US Tech 100", "NVIDIA Corp",
                                                   "Gold", "Germany 40"])
    @pytest.mark.parametrize('calc_instrument_2', ["EUR/USD", "GBP/USD", "Natural Gas", "US Tech 100", "NVIDIA Corp",
                                                   "Gold", "Germany 40"])
    @pytest.mark.test_077
    def test_077_trading_calculator_collapse_after_setting_duration(
            self, worker_id, d, cur_language, cur_country, cur_role,
            cur_login, cur_password, calc_instrument_1, calc_instrument_2):
        """
        Check: The trading calculator is collapsed in the menu section [Markets] --> [CFD calculator]
        after setting the maximum duration on the Prof/Loss element and changing the asset
        Language: En.
        Country: CYSEC, ASIC, SCB
        Role: NoReg, Auth, NoAuth,
        Calc_instrument_1: ["EUR/USD", "GBP/USD", "Natural Gas", "US Tech 100", "NVIDIA Corp",
                                                   "Gold", "Germany 40"],
        Calc_instrument_2: ["EUR/USD", "GBP/USD", "Natural Gas", "US Tech 100", "NVIDIA Corp",
                                                   "Gold", "Germany 40"]
        Author: Artem Dashkov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "077",
            "Testing 'Trading calculator' widget in menu [CFD calculator]",
            False, False
        )
        pytest.skip("Промежуточная версия")
        if calc_instrument_1 == calc_instrument_2:
            pytest.skip("calc_instrument_1 = calc_instrument_2")

        # Arrange
        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, cur_item_link)
        cur_item_link = page_menu.open_markets_menu_cfd_calculator_submenu(d, cur_language, cur_country, cur_item_link)

        test_element = TradingCalculatorCFDCalculatorPage(d, cur_item_link, bid)
        test_element.arrange(d, cur_language, cur_country, cur_role, cur_item_link, calc_instrument_1, calc_instrument_2)


