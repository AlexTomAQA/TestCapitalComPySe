import allure
import pytest

from pages.common import Common
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.Menu.menu import MenuSection
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.TradeCFDBlockStartTradingNowButton import TradeCFDBlockStartTradingNowButton

count = 1


@pytest.mark.us_01_05
class TestCommodities:
    page_conditions = None

    @allure.step("Start test of button [Start Trading Now] on Block 'Trade Commodities CFDs'")
    @pytest.mark.test_001
    def test_001_block_trade_commodities_cfds_start_trading_now_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading Now]
        Language: All. License: All,except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.05", "Market > Menu item [Commodities]",
            ".00_001", "Testing button [Start Trading Now] on Block 'Trade Commodities CFDs'")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.move_focus_to_markets_menu(d, cur_language, cur_country)
        cur_page_url = page_menu.sub_menu_commodities_move_focus_click(d, cur_language)

        test_element = TradeCFDBlockStartTradingNowButton(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)
