import allure
import pytest

from pages.Elements import PageInstrumentWhyChooseBlockButtons
from pages.Elements.PageInstrumentNotificationButton import PageInstrumentNotificationButton
from pages.Elements.PromoMarketTradeNowButton import PromoMarketTradeNowButton
from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.Elements.TradingCalculatorStartTradingButton import TradingCalculatorStartTradingButton
from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.build_dynamic_arg import build_dynamic_arg_v4
from pages.Elements.PageInstrumentViewDetailedChartButton import PageInstrumentViewDetailedChartButton
from pages.Elements.PageInstrumentShortPositionGoToPlatformButton import PageInstrumentShortPositionGoToPlatformButton
from pages.Elements.TradeCFDAddToFavouriteButton import TradeCFDAddToFavoriteButton
from pages.Elements.PageInstrumentLongPositionGoToPlatformButton import PageInstrumentLongPositionGoToPlatformButton
from pages.Elements.TradeCFDBuyButton import TradeCFDBuyButton
from pages.Elements.TradeCFDSellButton import TradeCFDSellButton


def pytest_generate_tests(metafunc):
    file_name = "tests/US_01_Markets/US_01-03_Forex/list_of_href.txt"
    list_item_link = Common().generate_cur_item_link_parameter(file_name)
    metafunc.parametrize("cur_item_link", list_item_link, scope="class")


def check_cur_href(cur_item_link, list_href):
    if cur_item_link in list_href:
        return
    else:
        pytest.skip(f"This test case is not for page: '{cur_item_link}'")


@pytest.mark.us_01_03_01
class TestTradingInstrumentPage:
    page_conditions = None

    @allure.step("Start test_01.03.01_001 of button [Add to favorite] on trading instrument page'")
    @pytest.mark.test_001
    def test_001_page_trading_instrument_add_to_favourite_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Add to favourite]
        Language: All. License: All,except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.03", "Markets > Menu item [Forex]",
            ".01_001", "Testing button [Add to favourite] on trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = TradeCFDAddToFavoriteButton(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test_01.03.01_002 of button [View Detailed Chart] on trading instrument page'")
    @pytest.mark.test_002
    def test_002_page_trading_instrument_view_detailed_chart_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [View Detailed Chart] on trading instrument page
        Language: All. License: All (except FCA).
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.03", "Markets > Menu item [Forex]",
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
            "01.03", "Markets > Menu item [Forex]",
            ".01_003", "Testing button [Go to platform] long position on trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PageInstrumentLongPositionGoToPlatformButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi_v2(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test_01.03.01_004 of button [Go to platform] short position on trading instrument page'")
    @pytest.mark.test_004
    def test_004_page_trading_instrument_short_position_go_to_platform_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Go to platform] short position on trading instrument page
        Language: All. License: All (except FCA).
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.03", "Markets > Menu item [Forex]",
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
        Language: All. License: All,except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.03", "Markets > Menu item [Forex]",
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
            "01.03", "Markets > Menu item [Forex]",
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
            "01.03", "Markets > Menu item [Forex]",
            ".01_007", "Testing button [Notification] on trading instrument page")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PageInstrumentNotificationButton(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Try now] in Block 'Why choose Capital.com' on trading instrument page")
    @pytest.mark.test_008
    def test_008_page_trading_instrument_why_choose_block_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Try now] in Block 'Why choose Capital.com?' on trading
        instrument page
        Language: All. License: All, except FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.03", "Markets > Menu item [Forex]",
            ".01_008", "Testing button [Try now] in Block 'Why choose Capital.com?'on trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PageInstrumentWhyChooseBlockButtons.PageInstrumentWhyChooseBlockButton(d, cur_item_link, bid)
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
            "01.03", "Markets > Menu item [Forex]",
            ".01_009", "Testing button [Start Trading] in the 'Trading calculator' widget on trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = TradingCalculatorStartTradingButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Trade now] in block [People Also Watch] Widget 'PromoMarket' on trading "
                 "instrument page")
    @pytest.mark.test_010
    def test_010_page_trading_instrument_block_people_also_watch_widget_promomarket(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Trade now] in block [People Also Watch] Widget 'PromoMarket' on trading instrument page
        Language: All. License: All, except FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.03", "Markets > Menu item [Forex]",
            ".01_010", "Testing button [Trade now] in block [People Also Watch] "
                       "Widget 'PromoMarket' on trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PromoMarketTradeNowButton(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [1. Create & verify your account] in 'Step trading block' on trading instrument "
                 "page")
    @pytest.mark.test_011
    def test_011_page_trading_instrument_block_step_trading_create_and_verify_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [1. Create & verify account] in 'Step trading block' on trading instrument page
        Language: All. License: All, except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.03", "Markets > Menu item [Forex]",
            ".01_011", "Testing button [1. Create your account] in Step trading block on trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb", "ae"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)
