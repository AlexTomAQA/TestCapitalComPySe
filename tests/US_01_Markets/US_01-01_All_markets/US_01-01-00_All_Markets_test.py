import allure
import pytest

from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.Menu.menu import MenuSection
from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v4


@pytest.mark.us_01_01
class TestAllMarkets:
    page_conditions = None

    @allure.step("Start test of button [1. Create & verify your account] in Step trading block")
    @pytest.mark.test_003
    def test_003_block_step_trading_create_verify_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [1. Create & verify account]
        Language: All. License: All, except FCA. Role: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.01", "Markets > Menu item [All Markets]",
            ".00_003", "Testing button [1. Create your account] in Step trading block")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        cur_page_url = page_menu.open_all_markets_menu(d, cur_language, cur_country, link)

        test_element = BlockStepTrading(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)
