import pytest
import allure

from pages.common import Common
from pages.Menu.menu import MenuSection
from pages.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions_new import NewConditions
from src.src import CapitalComPageSrc
from pages.Elements.ContentBlockOpenAnAccountButton import ContentBlockOpenAnAccountButton
from pages.Elements.ContentBlockTryDemoAccountButton import ContentBlockTryDemoAccountButton
from pages.Elements.StepTradingBlock import BlockStepTrading


@pytest.mark.us_11_00_03
class TestMarketGuidesNew:
    page_conditions = None

    @allure.step("Start test_11.00.03_101 button [Open an account] in block 'Market guides'")
    @pytest.mark.test_101
    def test_101_open_an_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: button [Open an account] in block 'Market guides'
        Language: En. License: FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.00.03", "Learn to trade > Menu item [Market guides]",
            ".00_101", "Testing button [Open an account] in block 'Market guides'")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [""])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_learn_to_trade_market_guides_new_menu(d, cur_language, cur_country, link)

        test_element = ContentBlockOpenAnAccountButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test_11.00.03_102 button [Try demo account] in block 'Market guides'")
    @pytest.mark.test_102
    def test_102_try_demo_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check button [Try demo account] in block 'Market guides'
        Language: En. License: FCA, SCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.00.03", "Learn to trade > Menu item [Market guides]",
            ".00_102", "Testing button [Try demo account] in block 'Market guides'")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [""])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb', "ae"])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_learn_to_trade_market_guides_new_menu(d, cur_language, cur_country, link)

        test_element = ContentBlockTryDemoAccountButton(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test_11.00.03_103 button [1. Create your account] in block 'Ready to join a leading broker?'")
    @pytest.mark.test_103
    def test_103_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: button [1. Create your account] in block 'Ready to join a leading broker?'
        Language: En. License: FCA, SCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.00.03", "Learn to trade > Menu item [Market guides]",
            ".00_103", "Testing button [1. Create your account] in block 'Ready to join a leading broker?'")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [""])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb', "ae"])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_learn_to_trade_market_guides_new_menu(d, cur_language, cur_country, link)

        test_element = BlockStepTrading(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)
