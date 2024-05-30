"""
-*- coding: utf-8 -*-
@Time    : 2024/05/18 18:00 GMT+3
@Author  : Artem Dashkov
"""

import allure
import pytest

# from pages.common import Common
from pages.Elements.WhyChooseBlockTryNowButtonInContent import WhyChooseBlockTryNowButtonInContent
from src.src import CapitalComPageSrc
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55
from pages.conditions import Conditions
from pages.Menu.menu import MenuSection


@pytest.mark.us_55
class TestManualDetected:
    page_conditions = None

    @allure.step("Start test of button [Try now] on the block 'Why choose Capital.com?'")
    @pytest.mark.parametrize('cur_language', ["", "ar", "de", "es", "fr", "it", "hu", "nl", "pl", "ru", "cn", "ro"])
    @pytest.mark.parametrize('cur_country', ['de', 'au', 'ae'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.test_012
    def test_012_try_now_button_on_why_choose_capital_com_block(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try now] on block Why choose Capital.com?
        Language: All.
        License: Not FCA
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "Bugs Manual Detect",
            ".00_012",
            "Testing button [Try now] on the block 'Why choose Capital.com?'",
            False, False
        )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_our_mobile_apps_submenu_products_and_services_menu(
            d, cur_language, cur_country, link
        )

        test_element = WhyChooseBlockTryNowButtonInContent(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)
