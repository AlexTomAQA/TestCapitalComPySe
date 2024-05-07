"""
-*- coding: utf-8 -*-
@Time    : 2024/05/06 22:00
@Author  : Alexander Tomelo
"""
# from datetime import datetime
import pytest
import allure
# from pages.common import Common
# from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v4
# from pages.conditions import Conditions
# from pages.Elements.StepTradingBlock import BlockStepTrading
# from pages.Elements.AssertClass import AssertClass
# from src.src import CapitalComPageSrc
# from pages.Education.Glossary_locators import (
#     FinancialDictionary,
# )


@pytest.mark.us_55
class TestManualDetected:

    @allure.step("Start test of ???")
    @pytest.mark.test_01
    def test_501(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        # """
        # Check: Button [1. Create your account] in block [Steps trading]
        # Language: All. License: All.
        # """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTest Manual Detected > Menu item [Glossary of trading terms]",
            ".00_01", "Testing button [1. Create your account] in block [Steps trading]")
        pytest.skip("Autotest under construction")

        #
        # Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        # Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        # if cur_language not in ["", "de", "el", "es", "fr", "it", "hu", "nl", "pl", "ro", "ru", "zh"]:
        #     pytest.skip(f"This test-case is not for {cur_language} language")
        #
        # page_conditions = Conditions(d, "")
        # link = page_conditions.preconditions(
        #     d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #
        # page_menu = MenuSection(d, link)
        # page_menu.menu_education_move_focus(d, cur_language, cur_country)
        # link = page_menu.sub_menu_glossary_move_focus_click(d, cur_language)
        #
        # test_element = BlockStepTrading(d, link)
        # test_element.arrange_(d, link)
        #
        # test_element.element_click()
        #
        # test_element = AssertClass(d, link, bid)
        # match cur_role:
        #     case "NoReg" | "NoAuth":
        #         test_element.assert_signup(d, cur_language, link)
        #     case "Auth":
        #         test_element.assert_trading_platform_v4(d, link)
        #
        # del test_element
        # del page_menu
