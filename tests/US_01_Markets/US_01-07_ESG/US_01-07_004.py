import allure
import pytest

from pages.Elements.TradeCFDBlockStartTradingNowButton import TradeCFDBlockStartTradingNowButton
from pages.common import Common
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from src.src import CapitalComPageSrc


@pytest.mark.us_01_07
class TestESG:
    page_conditions = None

    @allure.step("Start test_01.07_004 button '1. Create & verify your account'")
    @pytest.mark.test_004
    def test_004_create_verify_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [1. Create & verify account]
        Language: All. License: All,except FCA (GB country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.07", "Markets > Menu item [ESG]",
            "_004", "Testing button  [1. Create & verify your account]  on Block 'TSteps trading'")

        Common().check_country_in_list_and_skip_if_present(cur_country, ['gb'])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        cur_page_url = page_menu.open_esg_markets_menu(d, cur_language, cur_country, link)

        test_element = TradeCFDBlockStartTradingNowButton(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

