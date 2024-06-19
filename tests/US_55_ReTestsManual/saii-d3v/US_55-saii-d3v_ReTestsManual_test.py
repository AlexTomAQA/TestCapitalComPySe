"""
-*- coding: utf-8 -*-
@Time    : 2024/06/19 18:00 GMT+5
@Author  : Sergey Aiidzhanov
"""

import pytest
import allure

from pages.common import Common                                     # check FCA, check Auth
from pages.base_page import BasePage                                # accept cookies
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55
from pages.Elements.HeaderLoginButton import HeaderButtonLogin


@pytest.mark.us_55
class TestManualDetectedBugs:
    page_conditions = None

    @allure.step("Start retest manual TC_55!0043 The page is refreshed instead of opening the Login form after clicking the [Log In] button on the Search page")
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', [''])
    @pytest.mark.parametrize('cur_role', ["NoReg", "NoAuth"])
    @pytest.mark.test_043
    def test_043(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: The page is refreshed instead of opening the Login form after clicking the [Log In] button on the Search page
         Language: All.
         License: All, exclude FCA (GB country).
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "043",
            "The page is refreshed instead of opening the Login form after clicking the [Log In] button on the Search page"
        )

        pytest.skip("Autotest under construction")
