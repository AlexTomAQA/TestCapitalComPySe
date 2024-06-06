"""
-*- coding: utf-8 -*-
@Time    : 2024/06/06 15:29
@Author  : podchasova11
"""
import pytest
import allure
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55

# from pages.common import Common
# from src.src import CapitalComPageSrc
# from pages.conditions_new import NewConditions


@pytest.mark.us_55
class TestManualDetectedBugs:
    page_conditions = None

    @allure.step("Start retest manual TC_55!00_027 Icon In Item 'Trade CFDs on margin' in block 'Why trade' is missing")
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.test_027
    def test_027(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: Icon In Item 'Trade CFDs on margin'
         Language: En. License: FCA.
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "027", "Icon In Item 'Trade CFDs on margin' in block 'Why trade' is missing"
        )

        pytest.skip("Autotest under construction")

        #
        # Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        # Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])
        #
        # page_conditions = NewConditions(d, "")
        # link = page_conditions.preconditions(
        #     d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #
        # test_element = IconInItemTradeCFDs(d, link, bid)
        # test_element.full_test(d, cur_language, cur_country, cur_role, link)


