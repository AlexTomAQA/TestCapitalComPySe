import allure
import pytest

from pages.common import Common
from pages.Menu.menu import MenuSection
from pages.Elements.StepTradingBlock import BlockStepTrading
from tests.build_dynamic_arg import build_dynamic_arg_v4
from tests.ReTestsManual.pages.conditions_new import NewConditions
from src.src import CapitalComPageSrc


@pytest.mark.us_11_00_01
class TestEssentialsTrading:
    page_conditions = None

    @allure.step("Start test_11.00.01_05 button [1. Create your account] in block 'Ready to join a leading broker?'")
    @pytest.mark.test_05
    def test_05_create_your_account(
            self, worker_id, d, cur_role, cur_language, cur_country, cur_login, cur_password):
        """
        Check button [1. Create your account ] in block 'Ready to join a leading broker?'
        Language: En. License: FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.00.01", "Essentials of trading",
            ".00_05", "Testing button [1. Create your account] in block 'Ready to join a leading broker?'")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        link = menu.open_learn_to_trade_essentials_of_trading_menu(d, cur_language, cur_country, link)

        test_element = BlockStepTrading(d, link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, link)
