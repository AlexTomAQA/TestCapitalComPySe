"""
-*- coding: utf-8 -*-
@Time    : 2024/02/25 08:50 GMT+3
@Author  : Artem Dashkov
"""

import allure
import pytest

from pages.common import Common
from pages.Elements.ForLearnerTradersBlockTryDemoButton import ForLearnerTradersBlockTryDemoButton
from pages.Elements.ForLearnerTradersBlockSignUpButton import ForLearnerTradersBlockSignUpButton
from pages.Elements.MainBannerSignUpButtonMainPage import MainBannerSignUpButtonMainPage
from pages.Elements.MainBannerTryDemoButtonMainPage import MainBannerTryDemoButtonMainPage
from pages.Elements.OurMarketsTableBuyButton import BuyButtonOurMarketsTable
from pages.Elements.OurMarketsTableSellButton import SellButtonOurMarketsTable
from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.Elements.TradingCalculatorStartTradingButton import TradingCalculatorStartTradingButton
from pages.Elements.TradingInstrumentTradeButton import TradingInstrumentTradeButton
from pages.Elements.WhyChooseBlockTryDemoButton import WhyChooseBlockTryDemoButton
from pages.Elements.WhyChooseBlockSignUpButton import WhyChooseBlockSignUpButton
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v4
from tests.ReTestsManual.pages.conditions_new import NewConditions
from pages.conditions import Conditions
from pages.Elements.ContentPageStartTradingButton import ContentStartTrading


@pytest.mark.us_00_00
class TestMainPage:
    page_conditions = None

    @allure.step("Start test of button [Try demo] in Block 'Helping traders make better decisions'")
    @pytest.mark.test_101
    def test_101_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try Demo] in Block 'Helping traders make better decisions' Main Page
        Language: EN. License: FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_101", "Testing button [Try Demo] in Block 'Helping traders make better decisions' Main Page",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerTryDemoButtonMainPage(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Sign Up] in Block 'Helping traders make better decisions'")
    @pytest.mark.test_102
    def test_102_main_banner_sign_up_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Sign Up] in Block 'Helping traders make better decisions' Main Page
        Language: EN. License: FCA.
        """
        # test_title = ("00", "Main Page",
        #               ".00_102", "Testing button [Sign Up] in Block 'Helping traders make better decisions' Main Page")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_102", "Testing button [Sign Up] in Block 'Helping traders make better decisions' Main Page",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerSignUpButtonMainPage(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Try demo] in Block 'Why choose Capital.com'")
    @pytest.mark.test_103
    def test_103_why_choose_block_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try Demo] in Block 'Why choose Capital.com?' Main Page
        Language: EN. License: FCA.
        """
        # test_title = ("00", "Main Page",
        #               ".00_103", "Testing button [Try Demo] in Block 'Why choose Capital.com?' Main Page")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_103", "Testing button [Try Demo] in Block 'Why choose Capital.com?' Main Page",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = WhyChooseBlockTryDemoButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Sign Up] in Block 'Why choose Capital.com'")
    @pytest.mark.test_104
    def test_104_why_choose_block_sign_up_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Sign Up] in Block 'Why choose Capital.com' Main Page
        Language: EN. License: FCA.
        """
        # test_title = ("00", "Main Page",
        #               ".00_104", "Testing button [Sign Up] in Block 'Why choose Capital.com' Main Page")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_104", "Testing button [Sign Up] in Block 'Why choose Capital.com' Main Page",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = WhyChooseBlockSignUpButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Sell] in Block 'Our markets'")
    @pytest.mark.test_105
    def test_105_our_markets_block_sell_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_market, instrument):
        """
        Check: Button [Sell] in Block 'Our markets' Main Page
        Language: EN. License: FCA.
        """
        # test_title = ("00", "Main Page",
        #               ".00_105",
        #               f"Testing button [Sell] in Block 'Our markets' {market} market, {instrument} instrument")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_105",
            f"Testing button [Sell] in Block 'Our markets' '{cur_market}' market, '{instrument}' instrument",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])
        Common().check_market_in_list_and_skip_if_present(cur_market, ['Cryptocurrencies'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = SellButtonOurMarketsTable(d, main_page_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, main_page_link, cur_market, instrument)

    @allure.step("Start test of button [Buy] in Block 'Our markets'")
    @pytest.mark.test_106
    def test_106_our_markets_block_buy_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_market, instrument):
        """
        Check: Button [Buy] in Block 'Our markets' Main Page
        Language: EN. License: FCA.
        """
        # test_title = ("00", "Main Page",
        #               ".00_106",
        #               f"Testing button [Buy] in Block 'Our markets' {market} market, {instrument} instrument")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_106",
            f"Testing button [Buy] in Block 'Our markets' '{cur_market}' market, '{instrument}' instrument",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])
        Common().check_market_in_list_and_skip_if_present(cur_market, ['Cryptocurrencies'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BuyButtonOurMarketsTable(d, main_page_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, main_page_link, cur_market, instrument)

    @allure.step("Start test of button [Try demo] in Block 'For learner traders'")
    @pytest.mark.test_107
    def test_107_for_learner_traders_block_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try Demo] in Block 'For learner traders' Main Page
        Language: EN. License: FCA.
        """
        # test_title = ("00", "Main Page",
        #               ".00_107", "Testing button [Try Demo] in Block 'For learner traders' Main Page")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_107", "Testing button [Try Demo] in Block 'For learner traders' Main Page",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ForLearnerTradersBlockTryDemoButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Sign Up] in Block 'For learner traders'")
    @pytest.mark.test_108
    def test_108_for_learner_traders_block_sign_up_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Sign Up] in Block 'For learner traders' Main Page
        Language: EN. License: FCA.
        """
        # test_title = ("00", "Main Page",
        #               ".00_108", "Testing button [Sign Up] in Block 'For learner traders' Main Page")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_108", "Testing button [Sign Up] in Block 'For learner traders' Main Page",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ForLearnerTradersBlockSignUpButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [1. Create your account] in Block 'Ready to join a leading broker?'")
    @pytest.mark.test_109
    def test_109_create_your_account_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [1. Create your account] in Block 'Ready to join a leading broker?' Main Page
        Language: EN. License: FCA.
        """
        # test_title = ("00", "Main Page",
        #               ".00_109", "Testing button [1. Create your account] in Block 'Ready to join a leading broker?' "
        #                          "Main Page")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_109", "Testing button [1. Create your account] in Block 'Ready to join a leading broker?' Main Page",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Trade] in Widget 'Trading instrument'")
    @pytest.mark.test_001
    def test_001_trading_instrument_widget_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_market):
        """
        Check: Button [Trade] in Widget 'Trading instrument' Main Page
        Language: ALL. License: Not FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_001", "Start test of button [Trade] in Widget 'Trading instrument'",
            False, False
        )

        Common().check_country_in_list_and_skip_if_not_present(
            cur_country,
            ['de', 'au', 'ae']
        )

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = TradingInstrumentTradeButton(d, main_page_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, main_page_link, cur_market)

    @allure.step("Start test of button [Start trading] in 'The Capital.com trading experience' block")
    @pytest.mark.test_002
    def test_002_start_trading_in_trading_experience_block_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start trading] in 'The Capital.com trading experience' block
        Language: ALL. License: Not FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_002", "Start test of button [Start trading] in 'The Capital.com trading experience' block",
            False, False
        )

        Common().check_country_in_list_and_skip_if_not_present(
            cur_country,
            ['de', 'au', 'ae']
        )

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ContentStartTrading(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Start Trading] in Widget 'Trading calculator'")
    @pytest.mark.test_015
    def test_015_create_your_account_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading] in Widget 'Trading calculator' Main Page
        Language: EN. License: FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_015", "Testing button [Start Trading] in Widget 'Trading calculator' Main Page",
            False, False
        )

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language,
            ['ar', 'de', 'el', 'es', 'fr', 'it', 'hu', 'pl', 'cn', 'ro', 'ru', 'zh']
        )
        Common().check_country_in_list_and_skip_if_not_present(
            cur_country,
            ['de', 'au', 'ae']
        )

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = TradingCalculatorStartTradingButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)
