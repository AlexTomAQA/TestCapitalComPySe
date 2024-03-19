import allure
import pytest

from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.Elements.TableTradingInstrumentsBuyButton import TableTradingInstrumentsBuyButton
from pages.Elements.TableTradingInstrumentsSellButton import TableTradingInstrumentsSellButton
from pages.Elements.testing_elements_locators import TableTradingInstrumentsLocators
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
            "01.05", "Markets > Menu item [Commodities]",
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

    @allure.step("Start test of button [Sell] in Widget 'Trading instrument'")
    @pytest.mark.test_002
    def test_002_sell_trading_instrument(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_sort):
        """
        Check: button [Sell] in Widget 'Trading instrument'
        Language: All License: All (except FCA) Role: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.05", "Markets > Menu item [Commodities]",
            ".00_002", "Testing button [Sell]")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.move_focus_to_markets_menu(d, cur_language, cur_country)
        cur_page_url = page_menu.sub_menu_commodities_move_focus_click(d, cur_language)

        test_element = TableTradingInstrumentsSellButton(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url, cur_sort)

    @allure.step("Start test of button [Buy] in Widget 'Trading instrument'")
    @pytest.mark.test_003
    def test_003_buy_trading_instrument(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_sort):
        """
        Check: button [Buy] in Widget 'Trading instrument'
        Language: All License: All (except FCA) Role: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.05", "Markets > Menu item [Commodities]",
            ".00_003", "Testing button [Buy]")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.move_focus_to_markets_menu(d, cur_language, cur_country)
        cur_page_url = page_menu.sub_menu_commodities_move_focus_click(d, cur_language)

        test_element = TableTradingInstrumentsBuyButton(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url, cur_sort)

    @allure.step("Start test of button [1. Create & verify your account] in Step trading block")
    @pytest.mark.test_004
    def test_004_block_step_trading_create_verify_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [1. Create & verify account]
        Language: All. License: All, except FCA. Role: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.05", "Markets > Menu item [Commodities]",
            ".00_004", "Testing button [1. Create your account] in Step trading block")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.move_focus_to_markets_menu(d, cur_language, cur_country)
        cur_page_url = page_menu.sub_menu_commodities_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, cur_page_url, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_page_url)

    @allure.step("Start pretest")
    def test_099_commodities_trading_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):

        global count

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.05", "Markets > Menu item [Commodities]",
            ".099", "Pretest for US_01.05.01")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)

        if count == 0:
            pytest.skip("The list of Live Commodities links is already created")

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        page_menu.move_focus_to_markets_menu(d, cur_language, cur_country)
        page_menu.sub_menu_commodities_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        file_name = "tests/US_01_Markets/US_01-05_Commodities/list_of_href.txt"
        list_items = d.find_elements(*TableTradingInstrumentsLocators.ITEM_TRADING_INSTRUMENT_LINK)
        Common().creating_file_of_hrefs("Commodities", list_items, file_name)

        count -= 1
