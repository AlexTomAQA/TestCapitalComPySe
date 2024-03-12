import allure
import pytest

from pages.common import Common
from pages.Menu.menu import MenuSection
from pages.Elements.TableTradingInstrumentsBuyButton import TableTradingInstrumentsBuyButton
from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from src.src import CapitalComPageSrc


@pytest.mark.us_01_03
class TestForex:
    page_conditions = None

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

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_forex_markets_menu(d, cur_language, cur_country, link)

        test_element = TableTradingInstrumentsBuyButton(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link, cur_sort)
