import pytest
import allure

from pages.Elements.TradeCFDAddToFavouriteButton import TradeCFDAddToFavoriteButton
from pages.Menu.menu import MenuSection
from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v4

count = 1


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    file_name = "tests/US_01_Markets/US_01-05_Commodities/list_of_href.txt"
    list_item_link = Common().generate_cur_item_link_parameter(file_name)
    metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_01_05
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

        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # page_menu = MenuSection(d, link)
        # page_menu.move_focus_to_markets_menu(d, cur_language, cur_country)
        # cur_page_url = page_menu.sub_menu_commodities_move_focus_click(d, cur_language)

        test_element = TradeCFDAddToFavoriteButton(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)
