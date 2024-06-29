"""
-*- coding: utf-8 -*-
@Time    : 2024/02/22 23:44 GMT+3
@Author  : Dmitry Mudrik
"""
import allure
import pytest
from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.Elements.MainBannerButtonOpenAnAccount import MainBannerOpenAnAccount
from pages.Elements.MainBannerTryDemoAccountButton import MainBannerTryDemoAccount
from pages.Menu.menu import MenuSection
from pages.common import Common
from src.src import CapitalComPageSrc
from pages.conditions_new import NewConditions
from pages.build_dynamic_arg import build_dynamic_arg_v4


@pytest.mark.us_11_00_04
class TestTradingStrategies:
    page_conditions = None

    @allure.step('Test button [Create account] on Main banner')
    @pytest.mark.test_101
    def test_101_main_banner_create_account_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Create account] on Main banner
        Language: En.
        License: FCA (GB country), SCA (UAE country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.00.04", "Learn to trade > Menu item [Trading Strategies]",
            ".00_101", "Testing button [Create account] on the Main banner")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [""])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ["gb", "ae"])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country,
                                             cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_learn_to_trade_trading_strategies_new_menu(d, cur_language, cur_country, link)

        test_element = MainBannerOpenAnAccount(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step('Test button [Try demo account] on Main banner')
    @pytest.mark.test_102
    def test_102_main_banner_try_demo_account_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try demo account] on Main banner
        Language: En
        License: FCA (GB country), SCA (UAE country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.00.04", "Learn to trade > Menu item [Trading Strategies]",
            ".00_102", "Testing button [Try demo account] on the Main banner")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [""])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ["gb", "ae"])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country,
                                             cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_learn_to_trade_trading_strategies_new_menu(d, cur_language, cur_country, link)

        test_element = MainBannerTryDemoAccount(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step('Test button [1.Create your account] in block "Ready to join a leading broker?')
    @pytest.mark.test_103
    def test_103_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Create your account] in block "Ready to join a leading broker?"
        Language: En.
        License: FCA (GB country), SCA (UAE country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.00.04", "Learn to trade > Menu item [Trading Strategies]",
            ".00_103", "Testing button [1.Create your account] in block 'Ready to join a leading broker?'")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [""])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ["gb", "ae"])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country,
                                             cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        link = menu.open_learn_to_trade_trading_strategies_new_menu(d, cur_language, cur_country, link)

        test_element = BlockStepTrading(d, link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, link)
