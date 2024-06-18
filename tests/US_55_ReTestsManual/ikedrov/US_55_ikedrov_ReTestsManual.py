"""
-*- coding: utf-8 -*-
@Time    : 2024/06/16 19:00 GMT+3
@Author  : Ivan Kedrov
"""

import allure
import pytest

from pages.Elements.GooglePlayButtonCFDTradinAppBlock import GooglePlayButtonOnCFDTradingAppBlock
from pages.Menu.menu import MenuSection
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55
from pages.conditions import Conditions
from src.src import CapitalComPageSrc


@pytest.mark.us_55
class TestManualDetected:
    page_conditions = None

    @allure.step("Start test of button [Google Play] on the block 'CFD trading app'")
    @pytest.mark.parametrize('cur_country', ['de', 'au', 'ae'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.test_022
    def test_022_google_play_button_on_cfd_trading_app_block(
            self, worker_id, d, cur_language_3_rnd_from_12, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Google Play] on the block CFD Trading app
        Language: All.
        License: Not FCA

        Author  : Ivan Kedrov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_3_rnd_from_12, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "022",
            "Testing button [Google Play] on the block 'CFD trading app'",
            False, False
        )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_3_rnd_from_12, cur_country, cur_role, cur_login,
            cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_our_mobile_apps_submenu_products_and_services_menu(
            d, cur_language_3_rnd_from_12, cur_country, link)

        test_element = GooglePlayButtonOnCFDTradingAppBlock(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language_3_rnd_from_12, cur_country, cur_role, cur_item_link)

    # pytest.skip('Under construction')
