import allure
import pytest

from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.Elements.TableTradingInstrumentItem import TableTradingInstrumentsItem
from pages.Elements.TableTradingInstrumentItiemAllMarkets import TableTradingInstrumentsItemAllMarkets
from pages.Elements.TableTradingInstrumentsBuyButtonAllMarkets import TableTradingInstrumentsBuyButtonAllMarkets
from pages.Elements.TableTradingInstrumentsSellButtonAllMarkets import TableTradingInstrumentsSellButtonAllMarkets
from pages.Elements.testing_elements_locators import TableTradingInstrumentsLocators
from pages.Menu.menu import MenuSection
from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.build_dynamic_arg import build_dynamic_arg_v4

count = 1


@pytest.mark.us_01_01_00
class TestAllMarkets:
    page_conditions = None

    # @allure.step("Start test of button [Sell] in Widget 'Trading instrument'")
    # @pytest.mark.test_001
    # def test_001_sell_trading_instrument(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_market,
    #         cur_sort_all_markets):
    #     """
    #     Check: button [Sell] in Widget 'Trading instrument'
    #     Language: All License: All (except FCA) Role: All.
    #     """
    #     bid = build_dynamic_arg_v4(
    #         d, worker_id, cur_language, cur_country, cur_role,
    #         "01.01", "Markets > Menu item [All markets]",
    #         ".00_001", "Testing button [Sell]")
    #
    #     Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
    #     Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
    #
    #     page_conditions = Conditions(d, "")
    #     link = page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     page_menu = MenuSection(d, link)
    #     cur_page_url = page_menu.open_market_menu_all_markets_submenu(d, cur_language, cur_country, link)
    #
    #     test_element = TableTradingInstrumentsSellButtonAllMarkets(d, cur_page_url, bid)
    #     test_element.full_test_with_tpi(
    #         d, cur_language, cur_country, cur_role, cur_page_url, cur_market, cur_sort_all_markets)

    # @allure.step("Start test of button [Buy] in Widget 'Trading instrument'")
    # @pytest.mark.test_002
    # def test_002_buy_trading_instrument(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_market,
    #         cur_sort_all_markets):
    #     """
    #     Check: button [Buy] in Widget 'Trading instrument'
    #     Language: All License: All (except FCA) Role: All.
    #     """
    #     bid = build_dynamic_arg_v4(
    #         d, worker_id, cur_language, cur_country, cur_role,
    #         "01.01", "Markets > Menu item [All markets]",
    #         ".00_002", "Testing button [Buy]")
    #
    #     Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
    #     Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
    #
    #     page_conditions = Conditions(d, "")
    #     link = page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     page_menu = MenuSection(d, link)
    #     cur_page_url = page_menu.open_market_menu_all_markets_submenu(d, cur_language, cur_country, link)
    #
    #     test_element = TableTradingInstrumentsBuyButtonAllMarkets(d, cur_page_url, bid)
    #     test_element.full_test_with_tpi(
    #         d, cur_language, cur_country, cur_role, cur_page_url, cur_market, cur_sort_all_markets)

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
            "01.01", "Markets > Menu item [All markets]",
            ".00_003", "Testing button [1. Create your account] in Step trading block")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        cur_page_url = page_menu.open_market_menu_all_markets_submenu(d, cur_language, cur_country, link)

        test_element = BlockStepTrading(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start test open Trading instrument page")
    @pytest.mark.test_004
    def test_004_trading_instrument(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_market):
        """
        Check: open Trading instrument page
        Language: All License: All (except FCA)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.01", "Markets > Menu item [All markets]",
            ".00_004", "open Trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_market_menu_all_markets_submenu(d, cur_language, cur_country, link)

        test_element = TableTradingInstrumentsItemAllMarkets(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link, cur_market)

    @allure.step("Start pretest")
    def test_099_all_markets_trading_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        global count

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.01", "Markets > Menu item [All markets]",
            ".00_099", "Pretest for US_01.01.01")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        if count == 0:
            pytest.skip("The list of Live All markets links is already created")

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        page_menu.open_market_menu_all_markets_submenu(d, cur_language, cur_country, main_page_link)

        # Записываем ссылки в файл
        file_name = "tests/US_01_Markets/US_01-01_All_markets/list_of_href.txt"
        list_items = d.find_elements(*TableTradingInstrumentsLocators.ITEM_TRADING_INSTRUMENT_LINK)
        Common().creating_file_of_hrefs("All markets", list_items, file_name)

        count -= 1
