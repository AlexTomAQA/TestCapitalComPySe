import allure
import pytest

from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.Elements.PageInstrumentViewDetailedChartButton import PageInstrumentViewDetailedChartButton


def pytest_generate_tests(metafunc):

    file_name = "tests/US_01_Markets/US_01-03_Forex/list_of_href.text"
    list_item_link = Common().generate_cur_item_link_parameter(file_name)
    metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_01_03_01
class TestTradingInstrumentPage:
    page_conditions = None

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

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        cur_item_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PageInstrumentViewDetailedChartButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)
