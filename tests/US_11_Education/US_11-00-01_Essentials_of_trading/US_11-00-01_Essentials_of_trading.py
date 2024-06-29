import allure
import pytest

from pages.common import Common
from pages.Menu.menu import MenuSection
from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.Elements.ContentBlockCreateALiveAccountButton import ContentBlockCreateAliveAccountButton
from pages.Elements.ContentBlockCreateARiskFreeDemoAccountButton import ContentBlockCreateARiskFreeDemoAccountButton
from pages.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions_new import NewConditions
from src.src import CapitalComPageSrc


@pytest.mark.us_11_00_01
class TestEssentialsTrading:
    page_conditions = None

    @allure.step("Start test_11.00.01_101 button [Create a live account] in Unleveraged trading block")
    @pytest.mark.test_101
    def test_101_create_a_live_account_unleveraged_block(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: button [Create a live account] in Unleveraged trading block
        Language: En. License: FCA, SCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.00.01", "Learn to trade > Menu item [Essentials of trading]",
            ".00_101", "Testing button [Create a live account]")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [""])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb', "ae"])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_learn_to_trade_essentials_of_trading_menu(d, cur_language, cur_country, link)

        test_element = (ContentBlockCreateAliveAccountButton.ButtonALiveAccountUnleveragedTradingBlock
                        (d, cur_item_link, bid))
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test_11.00.01_102 button [Create a risk free demo account] in Unleveraged trading block")
    @pytest.mark.test_102
    def test_102_create_a_risk_free_demo_account_unleveraged_block(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: button [Create a risk-free demo account] in Unleveraged trading block
        Language: En. License: FCA, SCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.00.01", "Learn to trade > Menu item [Essentials of trading]",
            ".00_102", "Testing button [Create a risk free demo account]")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [""])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb', "ae"])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_learn_to_trade_essentials_of_trading_menu(d, cur_language, cur_country, link)

        test_element = (ContentBlockCreateARiskFreeDemoAccountButton.ButtonCreateARiskFreeDemoAccountUnleveragedBlock
                        (d, cur_item_link, bid))
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test_11.00.01_103 button [Create a live account]")
    @pytest.mark.test_103
    def test_103_create_a_live_account_how_to_get_started_with_trading_block(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check button [Create a live account]
        Language: En. License: FCA, SCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.00.01", "Learn to trade > Menu item [Essentials of trading]",
            ".00_103", "Testing button [Create a live account]")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [""])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb', "ae"])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_learn_to_trade_essentials_of_trading_menu(d, cur_language, cur_country, link)

        test_element = (ContentBlockCreateAliveAccountButton.ButtonCreateALiveAccountHowToGetStartedWithTradingBlock
                        (d, cur_item_link, bid))
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test_11.00.01_104 button [Create a risk free demo account] in How to get started trading block")
    @pytest.mark.test_104
    def test_104_create_a_risk_free_demo_account_how_to_get_started_trading_block(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: button [Create a risk-free demo account] in How to get started trading block
        Language: En. License: FCA, SCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.00.01", "Learn to trade > Menu item [Essentials of trading]",
            ".00_104", "Testing button [Create a risk-free demo account]")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [""])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb', "ae"])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_learn_to_trade_essentials_of_trading_menu(d, cur_language, cur_country, link)

        test_element = (ContentBlockCreateARiskFreeDemoAccountButton.
                        ButtonCreateARiskFreeDemoAccountHowToGetStartedTrading(d, cur_item_link, bid))
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test_11.00.01_105 button [1. Create your account] in block 'Ready to join a leading broker?'")
    @pytest.mark.test_105
    def test_05_create_your_account(
            self, worker_id, d, cur_role, cur_language, cur_country, cur_login, cur_password):
        """
        Check button [1. Create your account ] in block 'Ready to join a leading broker?'
        Language: En. License: FCA, SCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.00.01", "Learn to trade > Menu item [Essentials of trading]",
            ".00_105", "Testing button [1. Create your account] in block 'Ready to join a leading broker?'")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [""])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb', "ae"])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_learn_to_trade_essentials_of_trading_menu(d, cur_language, cur_country, link)

        test_element = BlockStepTrading(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)
