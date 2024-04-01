"""
-*- coding: utf-8 -*-
@Time    : 2024/03/24 22:57 GMT+3
@Author  : Dmitry Mudrik
"""
import allure
import pytest

from pages.Elements.PageInstrumentLongPositionGoToPlatformButton import PageInstrumentLongPositionGoToPlatformButton
from pages.Elements.PageInstrumentShortPositionGoToPlatformButton import PageInstrumentShortPositionGoToPlatformButton
from pages.Elements.PageInstrumentViewDetailedChartButton import PageInstrumentViewDetailedChartButton
from pages.Elements.TradeCFDAddToFavouriteButton import TradeCFDAddToFavoriteButton
from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v4


def pytest_generate_tests(metafunc):
    file_name = "tests/US_01_Markets/US_01-02_Shares/list_of_href.txt"
    list_item_link = Common().generate_cur_item_link_parameter(file_name)
    metafunc.parametrize("cur_item_link", list_item_link, scope="class")


def check_cur_href(cur_item_link, list_href):
    if cur_item_link in list_href:
        return
    else:
        pytest.skip(f"This test case is not for page: '{cur_item_link}'")


@pytest.mark.us_01_02
class TestSharesItemPage:
    page_conditions = None

    @allure.step("Start testing the [Add to favourite] button on the trading instrument page")
    @pytest.mark.test_001
    def test_001_page_instrument_add_to_favourite_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Add to favourite] on trading instrument page
        Language: All. License: All,except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.02", "Markets > Menu item [Shares]",
            ".01_001", "Testing button [Add to favourite] on the trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, "[gb]")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = TradeCFDAddToFavoriteButton(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start testing the [View detailed chart] button on the trading instrument page")
    @pytest.mark.test_002
    def test_002_page_instrument_view_detailed_chart_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [View detailed chart] on trading instrument page
        Language: All. License: All,except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.02", "Markets > Menu item [Shares]",
            ".01_002", "Testing button [View detailed chart] on the trading instrument page")

        Common().check_country_in_list_and_skip_if_present(cur_country, "[gb]")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PageInstrumentViewDetailedChartButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start testing the [Go to platform] button on the trading instrument page long position")
    @pytest.mark.test_003
    def test_003_page_instrument_long_position_go_to_platform_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Go to platform] on trading instrument page long position
        Language: All. License: All,except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.02", "Markets > Menu item [Shares]",
            ".01_003", "Testing button [Go to platform] on trading instrument page long position")

        Common().check_country_in_list_and_skip_if_present(cur_country, "[gb]")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PageInstrumentLongPositionGoToPlatformButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi_v2(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start testing the [Go to platform] button on the trading instrument page short position")
    @pytest.mark.test_004
    def test_004_page_instrument_short_position_go_to_platform_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Go to platform] on trading instrument page short position
        Language: All. License: All,except FCA.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "01.02", "Markets > Menu item [Shares]",
            ".01_004", "Testing button [Go to platform] on trading instrument page short position")

        Common().check_country_in_list_and_skip_if_present(cur_country, "[gb]")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PageInstrumentShortPositionGoToPlatformButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)
