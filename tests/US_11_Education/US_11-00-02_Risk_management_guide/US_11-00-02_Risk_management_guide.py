import allure
import pytest

from pages.common import Common
from pages.Menu.menu import MenuSection
from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.conditions_new import NewConditions
from pages.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from src.src import CapitalComPageSrc


@pytest.mark.us_11_00_02
class TestLearningHub:
    page_conditions = None

    @allure.step("Start test_11.00.02_01 button '1. Create your account' in the block [Steps trading].")
    @pytest.mark.test_101
    def test_101_create_your_account(
            self, worker_id, d, cur_role, cur_language, cur_country, cur_login, cur_password):
        """
        Check: Header -> button [Log In]
        Language: En. License: FCA, SCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.00.02", "Learn to trade > Menu Item [Risk-management guide]",
            ".00_101", "Testing button [1. Create your account] in block [Steps trading]")

        list_languages = ['']
        list_countries = ['gb', "ae"]
        Common().check_language_in_list_and_skip_if_not_present(cur_language, list_languages)
        Common().check_country_in_list_and_skip_if_not_present(cur_country, list_countries)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        link = menu.open_learn_to_trade_risk_management_guide_menu(d, cur_language, cur_country, link)

        test_element = BlockStepTrading(d, link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, link)
