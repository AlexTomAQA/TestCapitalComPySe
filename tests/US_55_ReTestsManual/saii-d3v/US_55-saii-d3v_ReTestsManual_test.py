"""
-*- coding: utf-8 -*-
@Time    : 2024/06/19 18:00 GMT+5
@Author  : Sergey Aiidzhanov
"""

import time
from datetime import datetime

import pytest
import allure

from pages.common import Common
from pages.conditions import Conditions
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55
from pages.BugsManual.bug_043 import SearchField
from pages.BugsManual.bug_060 import ProfessionalAccountPage
from pages.Signup_login.signup_login import SignupLogin
from pages.Elements.HeaderLoginButton import HeaderButtonLogin
from src.src import CapitalComPageSrc


@pytest.mark.us_55
class TestManualDetectedBugs:
    page_conditions = None

    @allure.step("Start retest manual TC_55!0043 The page is refreshed instead of opening the Login "
                 "form after clicking the [Log In] button on the Search page")
    @pytest.mark.parametrize('cur_country', ['de', 'ua', 'au'])
    @pytest.mark.parametrize('cur_role', ['NoAuth', 'NoReg'])
    @pytest.mark.test_043
    def test_043(self, worker_id, d, cur_language_3_rnd_from_14, cur_country, cur_role,
                 cur_login, cur_password, random_search_string):
        """
         Check: The page is refreshed instead of opening the Login form after clicking the [Log In] button
                on the Search page
         Language: All.
         License: All, exclude FCA, SCA.
         Country: All, exclude GB, AE.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_3_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "043",
            "The page is refreshed instead of opening the Login form after clicking the [Log In] button "
            "on the Search page",
            False,
            False
        )

        Common().check_country_in_list_and_skip_if_present(cur_country, ['gb', 'ae'])

        page_conditions = Conditions(d)
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL, "", cur_language_3_rnd_from_14,
                                             cur_country, cur_role, cur_login, cur_password)

        # Arrange
        # refresh page to prevent "stale element exception" on 1st test if its in NoAuth role
        d.refresh()

        search_field = SearchField(d, link, bid)
        search_field.open_search_page(random_search_string)

        # Act
        login_btn = HeaderButtonLogin(d, link, bid)
        login_btn.element_click()

        # Assert
        time.sleep(1)
        print(f'\n{datetime.now()}   3. Assert')
        login_form = SignupLogin(d, link, bid)
        if login_form.should_be_login_form():
            Common().pytest_fail(f"Bug # 55!043   The Login form is NOT displayed")
        Common().save_current_screenshot(d, "AT_55!043 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        login_form.close_login_form()
        Common().browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step("Login form is opened instead of Sign up form after clicking the button [Apply] "
                 "in the Block 'Leverage Limits Professional Clients' on page 'Professional Account'")
    @pytest.mark.parametrize('cur_country', ['de'])
    @pytest.mark.parametrize('cur_role', ['NoReg'])
    @pytest.mark.test_060
    def test_060(self, worker_id, d, cur_language_3_rnd_from_14, cur_country, cur_role, cur_login, cur_password):
        """
         Check: Login form is opened instead of Sign up form after clicking the button [Apply]
                in the Block 'Leverage Limits Professional Clients' on page 'Professional Account'
         Language: All.
         License: CYSEC.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_3_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "060",
            "Login form is opened instead of Sign up form after clicking the button [Apply] "
            "in the Block 'Leverage Limits Professional Clients' on page 'Professional Account'"
        )

        # Bug is not reproduced in 'el' language
        Common().check_language_in_list_and_skip_if_present(cur_language_3_rnd_from_14, ['el'])

        page_conditions = Conditions(d)
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL, "", cur_language_3_rnd_from_14,
                                             cur_country, cur_role, cur_login, cur_password)

        # Arrange
        prof_acc_page = ProfessionalAccountPage(d, link, bid)
        prof_acc_page.arrange_(d, cur_language_3_rnd_from_14, cur_country)

        # Act
        prof_acc_page.click_the_apply_button()

        # Assert
        print(f'\n{datetime.now()}   3. Assert')
        signup_form = SignupLogin(d, link, bid)
        if signup_form.should_be_signup_form(cur_language_3_rnd_from_14):
            Common().pytest_fail("Bug # 55!060   The Signup form is NOT displayed")
        Common().save_current_screenshot(d, "AT_55!060 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        signup_form.close_signup_form()
        Common().browser_back_to_link(d, CapitalComPageSrc.URL)
