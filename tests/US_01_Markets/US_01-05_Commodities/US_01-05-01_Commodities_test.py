import pytest
import allure

from pages.Elements.PageInstrumentLongPositionGoToPlatformButton import PageInstrumentLongPositionGoToPlatformButton
from pages.Elements.PageInstrumentNotificationButton import PageInstrumentNotificationButton
from pages.Elements.PageInstrumentShortPositionGoToPlatformButton import PageInstrumentShortPositionGoToPlatformButton
from pages.Elements.PageInstrumentViewDetailedChartButton import PageInstrumentViewDetailedChartButton
from pages.Elements.PromoMarketTradeNowButton import PromoMarketTradeNowButton
from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.Elements.TradeCFDAddToFavouriteButton import TradeCFDAddToFavoriteButton
from pages.Elements.TradeCFDBuyButton import TradeCFDBuyButton
from pages.Elements.TradeCFDSellButton import TradeCFDSellButton
from pages.Elements.TradingCalculatorStartTradingButton import TradingCalculatorStartTradingButton
# from pages.Menu.menu import MenuSection
from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.build_dynamic_arg import build_dynamic_arg_v4


def check_cur_href(cur_item_link, list_href):
    if cur_item_link in list_href:
        return
    else:
        pytest.skip(f"This test case is not for page: '{cur_item_link}'")


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    file_name = "tests/US_01_Markets/US_01-05_Commodities/list_of_href.txt"
    list_item_link = Common().generate_cur_item_link_parameter(file_name)
    metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_01_05_01
class TestCommodities:
    page_conditions = None

    @allure.step("Start test of button [Add to favourite] on 'Trade CFD' page")
    @pytest.mark.test_001
    def test_001_trade_cfd_page_add_to_favourite_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Add to favourite]
        Language: All. License: All,except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.05", "Markets > Menu item [Commodities]",
            ".01_001", "Testing button [Add to favourite] on 'Trade CFD' page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = TradeCFDAddToFavoriteButton(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [View Detailed Chart] on trading instrument page'")
    @pytest.mark.test_002
    def test_002_page_trading_instrument_view_detailed_chart_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [View Detailed Chart] on trading instrument page
        Language: All. License: All (except FCA).
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.05", "Markets > Menu item [Commodities]",
            ".01_002", "Testing button [View Detailed Chart] on trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PageInstrumentViewDetailedChartButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test button [Go to platform] on page instrument long position")
    @pytest.mark.test_003
    def test_003_page_trading_instrument_long_position_go_to_platform_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Go to platform] long position on trading instrument page
        Language: All. License: All,except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.05", "Markets > Menu item [Commodities]",
            ".01_003", "Testing button [Go to platform] long position on trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PageInstrumentLongPositionGoToPlatformButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi_v2(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Go to platform] on page instrument short position'")
    @pytest.mark.test_004
    def test_004_page_trading_instrument_short_position_go_to_platform_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Go to platform] short position on trading instrument page
        Language: All. License: All (except FCA).
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.05", "Markets > Menu item [Commodities]",
            ".01_004", "Testing button [Go to platform] short position on trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PageInstrumentShortPositionGoToPlatformButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Buy] on trading instrument page'")
    @pytest.mark.test_005
    def test_005_page_trading_instrument_buy_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Buy] on trading instrument page
        Language: All. License: All (except FCA).
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.05", "Markets > Menu item [Commodities]",
            ".01_005", "Testing button [Buy] on trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = TradeCFDBuyButton(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Sell] on trading instrument page'")
    @pytest.mark.test_006
    def test_006_page_trading_instrument_sell_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Sell] on trading instrument page
        Language: All. License: All,except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.05", "Markets > Menu item [Commodities]",
            ".01_006", "Testing button [Sell] on trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = TradeCFDSellButton(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Notification] on trading instrument page")
    @pytest.mark.test_007
    def test_007_page_instrument_notification_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Notification] on trading instrument page
        Language: All. License: All, except FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.05", "Markets > Menu item [Commodities]",
            ".01_007", "Testing button [Notification] on trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PageInstrumentNotificationButton(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Start Trading] in the 'Trading calculator' widget on trading instrument page ")
    @pytest.mark.test_009
    def test_009_page_trading_instrument_widget_trading_calculator_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Start Trading] in the 'Trading calculator' widget on trading instrument page
        Language: All. License: All,except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.05", "Markets > Menu item [Commodities]",
            ".01_009", "Testing button [Start Trading] in the 'Trading calculator' "
                       "widget on trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = TradingCalculatorStartTradingButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start testing the [Trade now] button in the widget Promo Market on the trading instrument page")
    @pytest.mark.test_010
    def test_010_page_instrument_widget_promo_market_trade_now_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Trade now] in the widget Promo Market on the trading instrument page
        Language: All. License: All,except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.05", "Markets > Menu item [Commodities]",
            ".01_010", "Testing button [Trade now] in the widget Promo Market "
                       "on the trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PromoMarketTradeNowButton(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [1. Create & verify your account] in Step trading block")
    @pytest.mark.test_011
    def test_011_block_step_trading_create_verify_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [1. Create & verify account]
        Language: All. License: All, except FCA. Role: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.05", "Markets > Menu item [Commodities]",
            ".01_011", "Testing button [1. Create your account] in Step trading block")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)
