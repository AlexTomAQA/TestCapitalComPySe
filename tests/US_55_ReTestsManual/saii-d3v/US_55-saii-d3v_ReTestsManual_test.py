"""
-*- coding: utf-8 -*-
@Time    : 2024/06/19 18:00 GMT+5
@Author  : Sergey Aiidzhanov
"""

import pytest
import allure

from datetime import datetime

from pages.common import Common                                      # check FCA, check Auth
from pages.conditions import Conditions                              # accept cookies
from pages.base_page import BasePage
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55
from pages.BugsManual.bug_043 import SearchField
from pages.Signup_login.signup_login import SignupLogin
from pages.Elements.HeaderLoginButton import HeaderButtonLogin
from src.src import CapitalComPageSrc


@pytest.mark.us_55
class TestManualDetectedBugs:
    page_conditions = None

    @allure.step("Start retest manual TC_55!0043 The page is refreshed instead of opening the Login "
                 "form after clicking the [Log In] button on the Search page")
    @pytest.mark.parametrize('cur_country', ['au', 'ax', 'de'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "NoAuth"])
    @pytest.mark.test_043
    def test_043(self, worker_id, d, cur_language_3_rnd_from_14, cur_country, cur_role, cur_login, cur_password):
        """
         Check: The page is refreshed instead of opening the Login form after clicking the [Log In] button on the Search page
         Language: All.
         License: All, exclude FCA (GB country).
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_3_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "043",
            "The page is refreshed instead of opening the Login form after clicking the [Log In] button "
            "on the Search page"
        )

        page_conditions = Conditions(d, "")  # проверить без явного указания ссылки
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_3_rnd_from_14, cur_country, cur_role, cur_login, cur_password)

        Common().check_country_in_list_and_skip_if_present(cur_country, ['gb', 'ae'])

        search_field = SearchField(d, link, bid)
        search_field.open_search_page()

        pytest.skip("Autotest under construction")
