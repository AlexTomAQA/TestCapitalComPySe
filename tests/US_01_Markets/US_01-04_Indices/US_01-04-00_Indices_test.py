import allure
import pytest
from datetime import datetime

from pages.Elements.TradingInstrumentsBlockStartTradingNowButton import  \
    TradingInstrumentsBlockStartTradingNow
from pages.common import Common
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.Menu.menu import MenuSection
from pages.conditions import Conditions
from src.src import CapitalComPageSrc

count = 1


@pytest.fixture()
def cur_time():
    return str(datetime.now())


@pytest.mark.us_01_04_00
class TestIndices:
    page_conditions = None

    @allure.step("Start test_001 of button [Start Trading Now] on Block 'Trade Indices CFDs'")
    @pytest.mark.test_001
    def test_001_block_trade_indices_cfds_start_trading_now_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading Now]
        Language: All. License: All(except CFA).
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.04.00", "Market > Menu item [Trading Strategies Guides]",
            ".00_001", "Testing button [Start Trading Now] on Block 'Trade Indices CFDs'")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_markets_move_focus(d, cur_language, cur_country)
        cur_page_url = page_menu.sub_menu_indices_move_focus_click(d, cur_language)

        test_element = TradingInstrumentsBlockStartTradingNow(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)