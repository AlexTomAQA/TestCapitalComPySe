import allure
import pytest

from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.Elements.TableTradingInstrumentsBuyButton import TableTradingInstrumentsBuyButton
from pages.Elements.TableTradingInstrumentsSellButton import TableTradingInstrumentsSellButton
from pages.Elements.testing_elements_locators import SubPages
from pages.common import Common
from pages.build_dynamic_arg import build_dynamic_arg_v4
from pages.Menu.menu import MenuSection
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.TradeCFDBlockStartTradingNowButton import TradeCFDBlockStartTradingNowButton

count = 1


@pytest.mark.us_01_04_00
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
            "01.04", "Markets > Menu item [Indices]",
            ".00_001", "Testing button [Start Trading Now] on Block 'Trade Indices CFDs'")

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_country_in_list_and_skip_if_present(cur_country,["gb"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        cur_item_link = page_menu.open_indices_markets_menu(d, cur_language, cur_country, link)

        test_element = TradeCFDBlockStartTradingNowButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

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
            "01.04", "Markets > Menu item [Indices]",
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
            "01.04", "Markets > Menu item [Indices]",
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
            "01.04", "Markets > Menu item [Indices]",
            ".00_004", "Testing button [Create & verify your account] in block 'Steps trading'")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_indices_markets_menu(d, cur_language, cur_country, link)

        test_element = BlockStepTrading(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start pretest")
    def test_099_indices_trading_instrument_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        global count

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.04", "Markets > Menu item [Indices]",
            ".00_099", "Pretest for US_01.04-01")

        if count == 0:
            pytest.skip("The list of Indices links is already created")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.open_forex_markets_menu(d, cur_language, cur_country, link)

        file_name = "tests/US_01_Markets/US_01-04_Indices/list_of_href.txt"
        list_items = d.find_elements(*SubPages.SUB_PAGES_MARKETS_TABLE_INSTRUMENTS_LIST)

        Common().creating_file_of_hrefs("Indices trading instrument", list_items, file_name)

        count -= 1

