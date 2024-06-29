import allure
import pytest

from pages.Elements.MainBannerButtonOpenAnAccount import MainBannerOpenAnAccount
from pages.Elements.MainBannerTryDemoAccountButton import MainBannerTryDemoAccount
from pages.common import Common
from pages.Menu.menu import MenuSection
from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.conditions_new import NewConditions
from pages.build_dynamic_arg import build_dynamic_arg_v4
from src.src import CapitalComPageSrc


@pytest.mark.us_11_00_00
class TestLearnToTrade:
    page_conditions = None

    @allure.step("Start test_11.00.00_101 of button [Open an account] on Main banner")
    @pytest.mark.test_101
    def test_01_main_banner_open_an_account_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Open an account]
        Language: En. License: FCA, SCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.00.00", "Learn to trade",
            ".00_101", "Testing button [Open an account] on Main banner")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb', "ae"])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
             d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        link = menu.open_learn_to_trade_menu(d, cur_language, cur_country, link)

        test_element = MainBannerOpenAnAccount(d, link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, link)

    @allure.step("Start test_11.00.00_102 of button [Try demo account] on Main banner")
    @pytest.mark.test_102
    def test_02_main_banner_try_demo_account_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try demo account]
        Language: En. License: FCA, SCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.00.00", "Learn to trade",
            ".00_102", "Testing button [Try demo account] on Main banner")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb', "ae"])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        link = menu.open_learn_to_trade_menu(d, cur_language, cur_country, link)

        test_element = MainBannerTryDemoAccount(d, link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, link)

    @allure.step("Start test_11.00.00_103 button [1. Create your account] in block 'Ready to join a leading broker?'")
    @pytest.mark.test_103
    def test_03_create_your_account(
            self, worker_id, d, cur_role, cur_language, cur_country, cur_login, cur_password):
        """
        Check button [1. Create your account ] in block 'Ready to join a leading broker?'
        Language: En. License: FCA, SCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.00.00", "Learn to trade",
            ".00_103", "Testing button [1. Create your account] in block 'Ready to join a leading broker?'")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb', "ae"])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        link = menu.open_learn_to_trade_menu(d, cur_language, cur_country, link)

        test_element = BlockStepTrading(d, link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, link)
