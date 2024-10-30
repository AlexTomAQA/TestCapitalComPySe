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
from pages.BugsManual.bug_322 import AssertTPI, TradingInstrumentsMarkets
from pages.BugsManual.bug_360 import IndicesItaly40
from pages.BugsManual.bug_371 import DiscoverCFDTtradingLink
from pages.BugsManual.bug_380 import SocialNetwork
from pages.BugsManual.bug_386 import ContactUs
from pages.BugsManual.bug_388 import TextIsNotLink
from pages.BugsManual.bug_399 import ValueItems
from pages.BugsManual.bug_401 import LinkIPO
from pages.Menu.New.from_markets_menu_open_cryptocurrencies import FromMarketsOpenCryptocurrencies
from pages.Menu.New.from_markets_menu_open_indices import MenuNewIndices
from pages.Menu.New.from_markets_menu_open_markets import MenuNewMarkets
from pages.Menu.New import from_trading_menu_open_mobile_apps, from_about_us_menu_open_why_capital, \
    from_about_us_menu_open_help, from_about_us_menu_open_client_vulnerability, from_trading_menu_open_web_platform, \
    from_markets_menu_open_shares
from pages.Menu.menu import MenuSection
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55
from pages.Elements.MyAccountButton import MyAccountButton
from pages.conditions_switch import conditions_switch


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

        link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MyAccountButton(d, link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, link)

    @allure.step("Start retest manual AT_55!00_048 of filters application in the 'Live shares prices' widget")
    @pytest.mark.parametrize('cur_country', ['ua'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_048
    def test_048(self, worker_id, d, cur_language_2_rnd_from_14, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Filters application in the 'Live shares prices' widget
        Language: All
        License: SCB
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_2_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "048", "Applied filters 'Region/Sectors' are not displayed after selecting an item from the "
                   "'Most traded' dropdown in the 'Live shares prices'  widget on the 'Shares' page"
            )

        link = conditions_switch(d, cur_language_2_rnd_from_14, cur_country, cur_role, cur_login, cur_password)
        menu = MenuSection(d, link)
        cur_item_link = menu.open_shares_market_menu(d, cur_language_2_rnd_from_14, cur_country, link)

        test_element = AppliedFilters(d, cur_item_link, bid)
        test_element.test_(d, cur_language_2_rnd_from_14, cur_country, cur_role, cur_item_link)

    @allure.step('Start retest manual AT_55!077a of the  presence of the "Crypto trading  guide" sidebar on '
                 '"Crypto vs stocks: What is the difference?" page')
    @pytest.mark.parametrize('cur_country', ['ua'])
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
        License: SCB
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "077a", 'Sidebar " Crypto trading  guide" is absent on pages "Bitcoin Gold" and "Crypto vs '
                    'stocks: What’s the difference?"'
        )

        link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_education_cryptocurrency_trading_menu(d, cur_language, cur_country, link)

        test_element = Sidebar(d, cur_item_link, bid)
        match cur_language:
            case "":
                test_element.sidebar_en(d, cur_item_link, sidebar_item)
        test_element.assert_a(sidebar_item)

    @allure.step('Start retest manual AT_55!077b of the presence of the "Crypto trading  guide" sidebar on '
                 '"Bitcoin Gold" page')
    @pytest.mark.parametrize('cur_country', ['ua'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.parametrize('sidebar_item', ['Bitcoin Gold'])
    @pytest.mark.bug_077b
    def test_077b(self, worker_id, d, cur_language_2_rnd_from_7, cur_country, cur_role, cur_login, cur_password,
                  sidebar_item):
        """
        Check: presence of the sidebar "Crypto Trading Guide" on the "Bitcoin Gold" page.
        Language: EN, DE, ZH, RU, ES,IT, PL
        License: SCB
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_2_rnd_from_7, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "077b", 'Sidebar " Crypto trading  guide" is absent on page "Bitcoin Gold"'
        )

        link = conditions_switch(d, cur_language_2_rnd_from_7, cur_country, cur_role, cur_login, cur_password)

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

        link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)

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

        link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = from_trading_menu_open_mobile_apps.MenuNew(d, link)
        cur_item_link = menu.from_trading_menu_open_mobile_apps(d, cur_language, cur_country, link)

        test_element = InvestmateAppPage(d, cur_item_link, bid)
        test_element.investmate_app_page(d, cur_item_link)
        test_element.assert_(d)

    @allure.step(
        'Start retest manual AT_55!322a that the Sign Up/Login/page of the corresponding trading instrument on '
        'the trading platform is opened after clicking [numeric values] in the Sell column.')
    @pytest.mark.parametrize('cur_language', ['', 'ar'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.parametrize('title_instrument', [''])
    @pytest.mark.bug_322a
    def test_322a(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, title_instrument):
        """
        Check: Clicking [numeric values] in the Sell column in Menu tittle Markets does not open the
                Sign-Up /Login form or page of the corresponding trading instrument on the trading platform using
                English or Arabic language.
        Language: EN, AR
        License: SCA
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "322a", 'The Sign Up/Login/page of the corresponding trading instrument on the trading platform'
                   ' is not opened after clicking [numeric values] in the Sell column'
        )

        match cur_language:
            case '':
                link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)
                menu = MenuNewMarkets(d, link)
                cur_item_link = menu.from_markets_menu_open_markets(d, cur_language, cur_country, link)
                test_element = TradingInstrumentsMarkets(d, cur_item_link, bid)
                test_element.trading_instruments(d, cur_item_link)
                test_element.click_button_sell(d)
                test_element = AssertTPI(d, cur_item_link, title_instrument)
                match cur_role:
                    case 'NoReg':
                        test_element.assert_signup(d)
                    case 'NoAuth':
                        test_element.assert_login(d)
                    case 'Auth':
                        test_element.assert_tpi(d, title_instrument)
            case 'ar':
                link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)
                menu = MenuNewMarkets(d, link)
                cur_item_link = menu.from_markets_menu_open_markets(d, cur_language, cur_country, link)
                test_element = TradingInstrumentsMarkets(d, cur_item_link, bid)
                test_element.trading_instruments(d, cur_item_link)
                test_element.click_button_sell(d)
                test_element = AssertTPI(d, cur_item_link, title_instrument)
                match cur_role:
                    case 'NoReg':
                        test_element.assert_signup(d)
                    case 'NoAuth':
                        test_element.assert_login(d)
                    case 'Auth':
                        test_element.assert_tpi(d, title_instrument)

    @allure.step(
        'Start retest manual AT_55!322b that the Sign Up/Login/page of the corresponding trading instrument on '
        'the trading platform is opened after clicking [numeric values] in the Buy column.')
    @pytest.mark.parametrize('cur_language', ['', 'ar'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.parametrize('title_instrument', [''])
    @pytest.mark.bug_322b
    def test_322b(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, title_instrument):
        """
        Check: Clicking [numeric values] in the Buy column in Menu tittle Markets does not open the
                Sign-Up /Login form or page of the corresponding trading instrument on the trading platform using
                English or Arabic language.
        Language: EN, AR
        License: SCA
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "322b", 'The Sign Up/Login/page of the corresponding trading instrument on the trading platform'
                   ' is not opened after clicking [numeric values] in the Buy column'
        )

        match cur_language:
            case '':
                link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)
                menu = MenuNewMarkets(d, link)
                cur_item_link = menu.from_markets_menu_open_markets(d, cur_language, cur_country, link)
                test_element = TradingInstrumentsMarkets(d, cur_item_link, bid)
                test_element.trading_instruments(d, cur_item_link)
                test_element.click_button_buy(d)
                test_element = AssertTPI(d, cur_item_link, title_instrument)
                match cur_role:
                    case 'NoReg':
                        test_element.assert_signup(d)
                    case 'NoAuth':
                        test_element.assert_login(d)
                    case 'Auth':
                        test_element.assert_tpi(d, title_instrument)
            case 'ar':
                link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)
                menu = MenuNewMarkets(d, link)
                cur_item_link = menu.from_markets_menu_open_markets(d, cur_language, cur_country, link)
                test_element = TradingInstrumentsMarkets(d, cur_item_link, bid)
                test_element.trading_instruments(d, cur_item_link)
                test_element.click_button_buy(d)
                test_element = AssertTPI(d, cur_item_link, title_instrument)
                match cur_role:
                    case 'NoReg':
                        test_element.assert_signup(d)
                    case 'NoAuth':
                        test_element.assert_login(d)
                    case 'Auth':
                        test_element.assert_tpi(d, title_instrument)

    @allure.step('Start retest manual AT_55!360 that the same license remains after clicking any of 5 links in the block'
        ' “Italy 40” on the page “Italy 40” when SCA license and EN language is selected')
    @pytest.mark.parametrize('cur_language', ['en'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_360
    def test_360(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Web pages with URLs of the FCA license are opened after clicking any of 5 links in the block “Italy 40”
            on the page “Italy 40” when SCA license and EN language is selected.
        Language: EN
        License: SCA
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "360", 'The same license, SCA (AE country), remains after clicking any of 5 links in the block'
                   ' “Italy 40”'
        )

        link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuNewIndices(d, link)
        cur_item_link = menu.from_markets_menu_open_indices(d, cur_language, cur_country, link)

        test_element = IndicesItaly40(d, cur_item_link, bid)
        test_element.arrange_v2(d, cur_item_link, link)
        test_element.element_click(d, link)
        test_element.assert_()

    @allure.step('Start retest manual AT_55!371a: the text of the link is “Discover CFD trading”')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['au'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_371a
    def test_371a(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: The text of the link is " ##AuUSPlink2## " in the block “Why choose Capital.com?” on the page
                “Why Capital.com?” when ASIC license is selected.
        Language: EN
        License: ASIC
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "371a", 'The text of the link is “Discover CFD trading”'
        )

        link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = from_about_us_menu_open_why_capital.MenuNew(d, link)
        cur_item_link = menu.from_about_us_menu_open_why_capital(d, cur_language, cur_country, link)

        test_element = DiscoverCFDTtradingLink(d, cur_item_link, bid)
        test_element.discover_cfd_trading_link(d, cur_item_link)
        test_element.element_pay_attention(d)
        test_element.assert_link(d)


    @allure.step('Start retest manual AT_55!371b: “CFD trading” page is opened')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['au'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_371b
    def test_371b(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: “CFD trading” page is not opened after clicking link in the tile "Fast account opening" in the block
                “Why choose Capital.com?” on the page “Why Capital.com?” when ASIC license is selected.
        Language: EN
        License: ASIC
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "371b", 'The text of the link is “Discover CFD trading”'
        )

        link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        menu = from_about_us_menu_open_why_capital.MenuNew(d, link)
        cur_item_link = menu.from_about_us_menu_open_why_capital(d, cur_language, cur_country, link)

        test_element = DiscoverCFDTtradingLink(d, cur_item_link, bid)
        test_element.discover_cfd_trading_link(d, cur_item_link)
        test_element.element_click(d)
        test_element.assert_page(d)


    @allure.step('Start retest manual AT_55!380: The relevant pages of "Social networks" are opened')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_380
    def test_380(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: TC_55!380 | The relevant pages of "Social networks" aren't opened after clicking the Social Network Icons
                when EN language and SCA license are selected.
        Language: EN
        License: SCA
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "380", 'The relevant pages of "Social networks" are opened”'
        )

        link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        menu = from_about_us_menu_open_help.MenuNew(d, link)
        cur_item_link = menu.from_about_us_menu_open_help(d, cur_language, cur_country, link)

        test_element = SocialNetwork(d, cur_item_link, bid)
        test_element.social_networks(d, cur_item_link, link)
        test_element.element_click(d)
        test_element.assert_page(d)


    @allure.step('Start retest manual AT_55!386: The "Contact us" page is opened')
    @pytest.mark.parametrize('cur_language', ['ar'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_386
    def test_386(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: TC_55!386 | Error message “Access denied Error 16 … This request was blocked by our security service …”
                is displayed after clicking the link “contact us in confidence” in the block “Your vulnerability risk”
                on the page “Client vulnerability” when AR language is selected (SCA license).
        Language: AR
        License: SCA
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "386", 'The "Contact us" page is opened'
        )

        link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        menu = from_about_us_menu_open_client_vulnerability.MenuNew(d, link)
        cur_item_link = menu.from_about_us_menu_open_client_vulnerability(d, cur_language, cur_country, link)

        test_element = ContactUs(d, cur_item_link, bid)
        test_element.contact_us_in_confidence(d, cur_item_link)
        test_element.element_click(d, link)
        test_element.assert_page(d)


    @allure.step('Start retest manual AT_55!388: The text "وقف الخسائر المتحركة" is not a link')
    @pytest.mark.parametrize('cur_language', ['ar'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_388
    def test_388(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: TC_55!388 | Menu section [Trading] > Menu item [Web platform] > Check the text “وقف الخسائر المتحركة” in the
                block “Risk-management tools”
        Language: AR
        License: SCA
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "388", 'The text "وقف الخسائر المتحركة" in the block [Risk-management tools] is a link when AR'
                   ' language is selected'
        )

        link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        menu = from_trading_menu_open_web_platform.MenuNew(d, link)
        cur_item_link = menu.from_trading_menu_open_web_platform(d, cur_language, cur_country, link)

        test_element = TextIsNotLink(d, cur_item_link, bid)
        test_element.text_is_not_link(d, cur_item_link)
        test_element.assert_text(d)


    @allure.step('Start retest manual AT_55!399a the value of the "Traders" item')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['au'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_399a
    def test_399a(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Main page > tab [Corporate] > block “Why Open a Corporate Account with Capital.com?”  > Pay attention to
                the value of the "Traders" item
        Language: EN
        License: ASIC
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "399a", 'The value of the "Traders" item is displayed  as “640K” in the block “Why Open a '
                   'Corporate Account with Capital.com?” on the page “Corporate Accounts with Capital.com” when ASIC '
                    'license is selected'
        )

        link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        test_element = ValueItems(d, link, bid)
        test_element.value_items(d, link)
        test_element.assert_value_traders(d)

    @allure.step('Start retest manual AT_55!399b the value of the "Active clients monthly" item')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['au'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_399b
    def test_399b(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Main page > tab [Corporate] > block “Why Open a Corporate Account with Capital.com?”  > Pay attention to
                the value of the "Active clients monthly" item
        Language: EN
        License: ASIC
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "399b", 'The value of the "Active clients monthly" item is displayed  as “640K” in the block '
                    '“Why Open a Corporate Account with Capital.com?” on the page “Corporate Accounts with Capital.com”'
                    ' when ASIC license is selected'
        )

        link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        test_element = ValueItems(d, link, bid)
        test_element.value_items(d, link)
        test_element.assert_value_active_clients_monthly(d)

    @allure.step('Start retest manual AT_55!401 The page with “404 error message” is displayed')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['ae', 'gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_401
    def test_401(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Menu section [Markets] > Menu item [Shares] > “Rivian Automotive, Inc.” page > Click the link “initial
                public offering (IPO)” in the  block “Rivian Automotive Inc. Company profile”
        Language: EN
        License: SCA, FCA
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "401", 'The page with “404 error message” is displayed after clicking the link “initial '
                    'public offering (IPO)” in the block “Rivian Automotive Inc. Company profile” on the page “Rivian '
                    'Automotive, Inc.” when SCA or FCA license is selected'
        )

        link = conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        menu = from_markets_menu_open_shares.MenuNewShares(d, link)
        cur_item_link = menu.from_markets_menu_open_shares(d, cur_language, cur_country, link)

        test_element = LinkIPO(d, cur_item_link, bid)
        test_element.link_ipo(d, cur_item_link, link)
        test_element.element_click(d, link)
        test_element.assert_url(d)
