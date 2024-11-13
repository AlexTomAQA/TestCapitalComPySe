"""
-*- coding: utf-8 -*-
@Date    : 18/10/2024
@Author  : Alexey Kurochkin
"""

import time
from datetime import datetime
import random

import pytest
import allure

from pages.BugsManual.bug_467 import Bug467
from pages.common import Common
from pages.conditions_v2 import apply_preconditions_to_link
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55


from pages.BugsManual.bug_272 import Bug272

from pages.Elements.HeaderSearchField import SearchField
from pages.Signup_login.signup_login import SignupLogin
from pages.Elements.HeaderLoginButton import HeaderButtonLogin
from pages.Elements.Alert import Alert
from pages.Menu.menu import MenuSection
from src.src import CapitalComPageSrc

@pytest.mark.us_55
class TestManualDetectedBugs:
    page_conditions = None

    @allure.step(
        # 'Start retest manual TC_55!467 | Sign up form is opened instead of Login '
        # 'on the page "Charges and fees" after clicking the button [Start trading now]')
        'Start retest manual TC_55!467 | ???')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['au'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_467
    def test_467(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         # Check: ????

         Language: EN
         License: ASIC
         Author: Aleksei Kurochkin
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "467",
            # 'Sign up form is opened instead of Login '
            # 'on the page "Charges and fees" after clicking the button [Start trading now]',
            "???",
            False,
            False
            #     new layout ????
        )

        # Arrange
        link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        test_el = Bug467(d, link, bid)
        test_el.open_risk_management_page(d, cur_language, cur_country, link)

        time.sleep(5)
        # Act
        test_el.click_start_trading_btn()

        # Assert
        signup_login = SignupLogin(d, link, bid)
        if not signup_login.should_be_new_login_form():
            Common.pytest_fail('Bug # 55!414 The Login form is not opened')
        Common.save_current_screenshot(d, "AT_55!414 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        signup_login.close_new_login_form()
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW)

