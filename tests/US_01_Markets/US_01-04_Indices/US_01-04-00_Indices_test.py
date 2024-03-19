import allure
import pytest

from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.Elements.TableTradingInstrumentsBuyButton import TableTradingInstrumentsBuyButton
from pages.Elements.TableTradingInstrumentsSellButton import TableTradingInstrumentsSellButton
from pages.common import Common
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.Menu.menu import MenuSection
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.TradeCFDBlockStartTradingNowButton import TradeCFDBlockStartTradingNowButton


@pytest.mark.us_01_04
class TestIndices:
    page_conditions = None

    @allure.step("Start test of button [Start Trading Now] on Block 'Trade Indices CFDs'")
    @pytest.mark.test_001
    def test_001_block_trade_indices_cfds_start_trading_now_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading Now]
        Language: All. License: All,except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.04", "Market > Menu item [Indices]",
            ".00_001", "Testing button [Start Trading Now] on Block 'Trade Indices CFDs'")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_country_in_list_and_skip_if_present(cur_country,["gb"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.move_focus_to_markets_menu(d, cur_language, cur_country)
        cur_page_url = page_menu.sub_menu_indices_move_focus_click(d, cur_language)

        test_element = TradeCFDBlockStartTradingNowButton(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test of button [Sell] on table Widget 'Trading instrument'")
    @pytest.mark.test_002
    def test_002_widget_trading_instrument_sell_button(
                self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_sort):
        """
        Check: Button [Sell]
        Language: All. License: All,except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.04", "Market > Menu item [Indices]",
            ".00_002", "Testing button [Sell] on table Widget 'Trading instrument'")

        Common().check_country_in_list_and_skip_if_present(cur_country,["gb"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        cur_item_link = page_menu.open_indices_markets_menu(d, cur_language, cur_country, link)

        test_element = TableTradingInstrumentsSellButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link, cur_sort)

    @allure.step("Start test of button [Buy] on table Widget 'Trading instrument'")
    @pytest.mark.test_003
    def test_003_widget_trading_instrument_buy_button(
                self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_sort):
        """
        Check: Button [Buy]
        Language: All. License: All,except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.04", "Market > Menu item [Indices]",
            ".00_003", "Testing button [Buy] on table Widget 'Trading instrument'")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        cur_item_link = page_menu.open_indices_markets_menu(d, cur_language, cur_country, link)

        test_element = TableTradingInstrumentsBuyButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link, cur_sort)

    @allure.step("Start test of button [Create & verify your account] in block 'Steps trading'")
    @pytest.mark.test_004
    def test_004_create_and_verify_your_account_button(
            self, worker_id, d, cur_role, cur_language, cur_country, cur_login, cur_password):
        """
        Check button [Create & verify your account] in block 'Steps trading'
        Language: All. License: All,except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.0", "Markets > Menu item [Indices]",
            ".00_004", "Testing button [Create & verify your account] in block 'Steps trading'")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_indices_markets_menu(d, cur_language, cur_country, link)

        test_element = BlockStepTrading(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

