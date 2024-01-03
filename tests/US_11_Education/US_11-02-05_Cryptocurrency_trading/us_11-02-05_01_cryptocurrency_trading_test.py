import pytest
import allure

from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.ButtonsSellBuyInContentBlock import ButtonsSellBuyInContentBlock
from pages.Elements.ButtonGetStartedOnStickyBar import GetStartedOnStickyBar
from pages.Elements.AssertClass import AssertClass



@allure.step("Start test of button [Sell] in content block")
def test_09_content_block_button_sell(
        self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
        prob_run_tc):
        """
        Check: Button [1. Sell] in content block
        Language: All. License: All.
        """
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.05", "Educations > Menu item [Cryptocurrency trading]",
                             "09", "Testing button [Sell] in content block")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if cur_country != 'gb':
            test_element = ButtonsSellBuyInContentBlock(d, cur_item_link)
            test_element.arrange_(cur_item_link, button='sell')

            test_element.element_click(cur_role)

            test_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(d, cur_item_link)
        else:
            pytest.skip("This test not for FCA licence.")

@allure.step("Start test of button [Buy] in content block")
def test_10_content_block_button_buy(
        self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
        prob_run_tc):
        """
        Check: Button [1. Buy] in content block
        Language: All. License: All.
        """
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.05", "Educations > Menu item [Cryptocurrency trading]",
                             "10", "Testing button [Sell] in content block")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if cur_country != 'gb':
            test_element = ButtonsSellBuyInContentBlock(d, cur_item_link)
            test_element.arrange_(cur_item_link, button='buy')

            test_element.element_click(cur_role)

            test_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(d, cur_item_link)
        else:
            pytest.skip("This test not for FCA licence.")


@allure.step("Start test of button [Get started] on Sticky bar")
def test_11_sticky_bar_button_get_started(
        self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
        prob_run_tc):
    """
    Check: Button [1. Get started] on Sticky bar
    Language: All. License: All.
    """
    build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                         "11.02.05", "Educations > Menu item [Cryptocurrency trading]",
                         "11", "Testing button [Get started] on Sticky bar")

    page_conditions = Conditions(d, "")
    page_conditions.preconditions(
        d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

    if cur_country != 'gb':
        test_element = GetStartedOnStickyBar(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)
    else:
        pytest.skip("This test not for FCA licence.")
