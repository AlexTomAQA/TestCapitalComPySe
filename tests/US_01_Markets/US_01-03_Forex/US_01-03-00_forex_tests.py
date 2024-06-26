import allure
import pytest

from pages.Elements.TableTradingInstrumentItem import TableTradingInstrumentsItem
from pages.common import Common
from pages.Menu.menu import MenuSection
from pages.Elements.TableTradingInstrumentsBuyButton import TableTradingInstrumentsBuyButton
from pages.Elements.TradeCFDBlockStartTradingNowButton import TradeCFDBlockStartTradingNowButton
from pages.Elements.TableTradingInstrumentsSellButton import TableTradingInstrumentsSellButton
from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.Elements.testing_elements_locators import SubPages
from pages.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from src.src import CapitalComPageSrc

count = 1


@pytest.mark.us_01_03_00
class TestForex:
    page_conditions = None

    @allure.step("Start test_01.03_001 of button [Start Trading Now] in Block 'Trade Forex CFDs'")
    @pytest.mark.test_001
    def test_001_block_trade_forex_cfds_start_trading_now_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading Now] in Block 'Trade Forex CFDs'
        Language: All. License: All (except FCA).
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.03", "Markets > Menu item [Forex]",
            ".00_001", "Testing button [Start Trading Now] in Block 'Trade Forex CFDs'")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        cur_page_url = page_menu.open_forex_markets_menu(d, cur_language, cur_country, link)

        test_element = TradeCFDBlockStartTradingNowButton(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test_01.03_002 button [Sell] in Widget 'Trading instrument'")
    @pytest.mark.test_002
    def test_002_sell_trading_instrument(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_sort):
        """
        Check: button [Sell] in Widget 'Trading instrument'
        Language: All License: All (except FCA) Role: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.03", "Markets > Menu item [Forex]",
            ".00_002", "Testing button [Sell]")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_forex_markets_menu(d, cur_language, cur_country, link)

        test_element = TableTradingInstrumentsSellButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link, cur_sort)

    @allure.step("Start test_01.03_003 button [Buy] in Widget 'Trading instrument'")
    @pytest.mark.test_003
    def test_003_buy_trading_instrument(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_sort):
        """
        Check: button [Buy] in Widget 'Trading instrument'
        Language: All License: All (except FCA) Role: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.03", "Markets > Menu item [Forex]",
            ".00_003", "Testing button [Buy]")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_forex_markets_menu(d, cur_language, cur_country, link)

        test_element = TableTradingInstrumentsBuyButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link, cur_sort)

    @allure.step("Start test_01.03_004 button [Create & verify your account] in block" 
                 "'Still looking for a broker/platform you can trust?'")
    @pytest.mark.test_004
    def test_004_create_and_verify_your_account(
            self, worker_id, d, cur_role, cur_language, cur_country, cur_login, cur_password):
        """
        Check button [Create & verify your account] in block 'Still looking for a broker/platform you can trust?'
        Language: All. License: All (except FCA).
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.03", "Markets > Menu item [Forex]",
            ".00_004", "Testing button [Create & verify your account]")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_forex_markets_menu(d, cur_language, cur_country, link)

        test_element = BlockStepTrading(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test_01.03_005 open Trading instrument page")
    @pytest.mark.test_005
    def test_005_trading_instrument(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: open Trading instrument page
        Language: All License: All (except FCA)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.03", "Markets > Menu item [Forex]",
            ".00_005", "open Trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_forex_markets_menu(d, cur_language, cur_country, link)

        test_element = TableTradingInstrumentsItem(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start pretest")
    def test_099_forex_trading_instrument_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        global count

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.03", "Markets > Menu item [Forex]",
            ".00_099", "Pretest for US_01.03_01")

        if count == 0:
            pytest.skip("Так надо")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.open_forex_markets_menu(d, cur_language, cur_country, link)

        file_name = "tests/US_01_Markets/US_01-03_Forex/list_of_href.txt"
        list_items = d.find_elements(*SubPages.SUB_PAGES_MARKETS_FOREX_LIST)

        Common().creating_file_of_hrefs("Forex trading instrument", list_items, file_name, 1)

        count -= 1
