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
from pages.Elements.WhyChooseBlockTryDemoButton import WhyChooseBlockTryDemoButton
from pages.Elements.WhyChooseBlockSignUpButton import WhyChooseBlockSignUpButton
from pages.Elements.ForLearnerTradersBlockTryDemoButton import ForLearnerTradersBlockTryDemoButton
from pages.Elements.ForLearnerTradersBlockSignUpButton import ForLearnerTradersBlockSignUpButton


@pytest.mark.us_00_00
class TestMainPage:
    page_conditions = None

    # @allure.step("Start test of button [Try demo] in Block 'Helping traders make better decisions'")
    # @pytest.mark.test_101
    # def test_101_main_banner_try_demo_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
    #     """
    #     Check: Button [Try Demo] in Block 'Helping traders make better decisions' Main Page
    #     Language: EN. License: FCA.
    #     """
    #     test_title = ("00", "Main Page",
    #                   ".00_101", "Testing button [Try Demo] in Block 'Helping traders make better decisions' Main Page")
    #
    #     bid = build_dynamic_arg_v4(
    #         d, worker_id, cur_language, cur_country, cur_role, *test_title)
    #
    #     Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
    #     Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])
    #
    #     page_conditions = NewConditions(d, "")
    #     main_page_link = page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     test_element = MainBannerTryDemoButtonMainPage(d, main_page_link, bid)
    #     test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)
    #
    # @allure.step("Start test of button [Sign Up] in Block 'Helping traders make better decisions'")
    # @pytest.mark.test_102
    # def test_102_main_banner_sign_up_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
    #     """
    #     Check: Button [Sign Up] in Block 'Helping traders make better decisions' Main Page
    #     Language: EN. License: FCA.
    #     """
    #     test_title = ("00", "Main Page",
    #                   ".00_102", "Testing button [Sign Up] in Block 'Helping traders make better decisions' Main Page")
    #
    #     bid = build_dynamic_arg_v4(
    #         d, worker_id, cur_language, cur_country, cur_role, *test_title)
    #
    #     Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
    #     Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])
    #
    #     page_conditions = NewConditions(d, "")
    #     main_page_link = page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     test_element = MainBannerSignUpButtonMainPage(d, main_page_link, bid)
    #     test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)
    #
    # @allure.step("Start test of button [Try demo] in Block 'Why choose Capital.com'")
    # @pytest.mark.test_103
    # def test_103_block_why_choose_try_demo_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
    #     """
    #     Check: Button [Try Demo] in Block 'Why choose Capital.com?' Main Page
    #     Language: EN. License: FCA.
    #     """
    #     test_title = ("00", "Main Page",
    #                   ".00_103", "Testing button [Try Demo] in Block 'Why choose Capital.com?' Main Page")
    #
    #     bid = build_dynamic_arg_v4(
    #         d, worker_id, cur_language, cur_country, cur_role, *test_title)
    #
    #     Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
    #     Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])
    #
    #     page_conditions = NewConditions(d, "")
    #     main_page_link = page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     test_element = WhyChooseBlockTryDemoButton(d, main_page_link, bid)
    #     test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)
    #
    # @allure.step("Start test of button [Sign Up] in Block 'Why choose Capital.com'")
    # @pytest.mark.test_104
    # def test_104_block_why_choose_sign_up_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
    #     """
    #     Check: Button [Sign Up] in Block 'Why choose Capital.com' Main Page
    #     Language: EN. License: FCA.
    #     """
    #     test_title = ("00", "Main Page",
    #                   ".00_104", "Testing button [Sign Up] in Block 'Why choose Capital.com' Main Page")
    #
    #     bid = build_dynamic_arg_v4(
    #         d, worker_id, cur_language, cur_country, cur_role, *test_title)
    #
    #     Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
    #     Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])
    #
    #     page_conditions = NewConditions(d, "")
    #     main_page_link = page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     test_element = WhyChooseBlockSignUpButton(d, main_page_link, bid)
    #     test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)
    #
    # @allure.step("Start test of button [Try demo] in Block 'For learner traders'")
    # @pytest.mark.test_107
    # def test_107_block_for_learner_traders_try_demo_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
    #     """
    #     Check: Button [Try Demo] in Block 'For learner traders' Main Page
    #     Language: EN. License: FCA.
    #     """
    #     test_title = ("00", "Main Page",
    #                   ".00_107", "Testing button [Try Demo] in Block 'For learner traders' Main Page")
    #
    #     bid = build_dynamic_arg_v4(
    #         d, worker_id, cur_language, cur_country, cur_role, *test_title)
    #
    #     Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
    #     Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])
    #
    #     page_conditions = NewConditions(d, "")
    #     main_page_link = page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     test_element = ForLearnerTradersBlockTryDemoButton(d, main_page_link, bid)
    #     test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Sign Up] in Block 'For learner traders'")
    @pytest.mark.test_108
    def test_108_block_for_learner_traders_sign_up_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Sign Up] in Block 'For learner traders' Main Page
        Language: EN. License: FCA.
        """
        test_title = ("00", "Main Page",
                      ".00_108", "Testing button [Sign Up] in Block 'For learner traders' Main Page")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role, *test_title)

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ForLearnerTradersBlockSignUpButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)