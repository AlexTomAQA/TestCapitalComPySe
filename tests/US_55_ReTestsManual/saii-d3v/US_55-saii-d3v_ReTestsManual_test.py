"""
-*- coding: utf-8 -*-
@Time    : 2024/06/19 18:00 GMT+5
@Author  : Sergey Aiidzhanov
"""

import pytest
import allure
import time

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

    @allure.step("Start retest manual TC_55!0043 The page is refreshed instead of opening the Login form after clicking the [Log In] button on the Search page")
    @pytest.mark.parametrize('cur_country', ['au', 'ax', 'de'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "NoAuth"])
    @pytest.mark.test_043
    def test_043(self, worker_id, d, cur_language_3_rnd_from_14, cur_country, cur_role, cur_login, cur_password):
        """
         Check: The page is refreshed instead of opening the Login form after clicking the [Log In] button on the Search page
         Language: All.
         License: All, exclude FCA.
         Country: All, exclude GB, AE
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_3_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "043",
            "The page is refreshed instead of opening the Login form after clicking the [Log In] button on the Search page"
        )

        page_conditions = Conditions(d)
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_3_rnd_from_14, cur_country, cur_role, cur_login, cur_password)

        Common().check_country_in_list_and_skip_if_present(cur_country, ['gb', 'ae'])
        # refresh page to prevent "stale element exception" on NoAuth role + au country
        d.refresh()

        search_field = SearchField(d, link, bid)
        search_field.open_search_page()

        login_btn = HeaderButtonLogin(d, link, bid)
        login_btn.element_click()

        login_form = SignupLogin(d, link, bid)
        # time.sleep(1)
        assert login_form.should_be_login_form()


        # pytest.skip("Autotest under construction")
