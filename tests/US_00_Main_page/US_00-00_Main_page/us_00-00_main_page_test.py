"""
-*- coding: utf-8 -*-
@Time    : 2024/02/25 08:50 GMT+3
@Author  : Artem Dashkov
"""

import pytest
import allure

from pages.common import Common
from tests.build_dynamic_arg import build_dynamic_arg_v4
from tests.ReTestsManual.pages.conditions_new import NewConditions
from src.src import CapitalComPageSrc
from pages.Elements.MainBannerSignUpButtonMainPage import MainBannerSignUpButtonMainPage
from pages.Elements.MainBannerTryDemoButtonMainPage import MainBannerTryDemoButtonMainPage


@pytest.mark.us_00_00
class TestMainPage:
    page_conditions = None

    @allure.step("Start test of button [Try demo] on Block 'Helping traders make better decisions'")
    @pytest.mark.test_101
    def test_101_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try Demo] on Block 'Helping traders make better decisions' Main Page
        Language: EN. License: FCA.
        """
        test_title = ("00.00", "Main Page",
                      "_101", "Testing button [Try Demo] on Block 'Helping traders make better decisions' Main Page")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role, *test_title)

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerTryDemoButtonMainPage(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Sign Up] on Block 'Helping traders make better decisions'")
    @pytest.mark.test_102
    def test_102_main_banner_sign_up_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Sign Up] on Block 'Helping traders make better decisions' Main Page
        Language: EN. License: FCA.
        """
        test_title = ("00.00", "Main Page",
                      "_102", "Testing button [Sign Up] on Block 'Helping traders make better decisions' Main Page")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role, *test_title)

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerSignUpButtonMainPage(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)
