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

from pages.BugsManual.bug_060 import ProfessionalAccountPage
from pages.BugsManual.bug_065 import TradingGuidesPageDeTest
from pages.BugsManual.bug_091 import NewsAndAnalysisMenuSection
from pages.Elements.HeaderSearchField import SearchField
from pages.Signup_login.signup_login import SignupLogin
from pages.Elements.HeaderLoginButton import HeaderButtonLogin
from pages.Elements.Alert import Alert
from pages.Menu.menu import MenuSection
from src.src import CapitalComPageSrc


@pytest.mark.us_55
class TestManualDetectedBugs:
    page_conditions = None

    @allure.step("Start retest manual TC_55!043 The page is refreshed instead of opening the Login "
                 "form after clicking the [Log In] button on the Search page")
    @pytest.mark.parametrize('cur_country', ['de', 'ua', 'au'])
    @pytest.mark.parametrize('cur_role', ['NoAuth', 'NoReg'])
    @pytest.mark.test_043
    def test_043(self, worker_id, d, cur_language_qty_rnd_from_14, cur_country, cur_role,
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
            d, worker_id, cur_language_qty_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "043",
            "The page is refreshed instead of opening the Login form after clicking the [Log In] button "
            "on the Search page",
            False,
            False
        )

        # Arrange
        Common().check_country_in_list_and_skip_if_present(cur_country, ['gb', 'ae'])

        page_conditions = Conditions(d)
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL, "", cur_language_qty_rnd_from_14,
                                             cur_country, cur_role, cur_login, cur_password)

        # refresh page to prevent "stale element exception" on 1st test if its in NoAuth role
        d.refresh()

        search_field = SearchField(d, link, bid)
        search_field.element_click()
        search_field.perform_search(random_search_string)

        # Act
        login_btn = HeaderButtonLogin(d, link, bid)
        login_btn.element_click()

        # Assert
        time.sleep(1)
        print(f'\n{datetime.now()}   3. Assert')
        login_form = SignupLogin(d, link, bid)
        if not login_form.should_be_login_form():
            Common().pytest_fail(f"Bug # 55!043   The Login form is NOT displayed")
        Common().save_current_screenshot(d, "AT_55!043 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        login_form.close_login_form()
        Common().browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step("Start retest manual TC_55!060 Login form is opened instead of Sign up form "
                 "after clicking the button [Apply] in the Block 'Leverage Limits Professional Clients' "
                 "on page 'Professional Account'")
    @pytest.mark.parametrize('cur_country', ['de'])
    @pytest.mark.parametrize('cur_role', ['NoReg'])
    @pytest.mark.test_060
    def test_060(self, worker_id, d, cur_language_qty_rnd_from_14, cur_country, cur_role, cur_login, cur_password):
        """
         Check: Login form is opened instead of Sign up form after clicking the button [Apply]
                in the Block 'Leverage Limits Professional Clients' on page 'Professional Account'
         Language: All, except EL.
         License: CYSEC.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_qty_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "060",
            "Login form is opened instead of Sign up form after clicking the button [Apply] "
            "in the Block 'Leverage Limits Professional Clients' on page 'Professional Account'"
        )

        # Arrange
        # Bug is not reproduced in 'el' language
        Common().check_language_in_list_and_skip_if_present(cur_language_qty_rnd_from_14, ['el'])

        page_conditions = Conditions(d)
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL, "", cur_language_qty_rnd_from_14,
                                             cur_country, cur_role, cur_login, cur_password)

        prof_acc_page = ProfessionalAccountPage(d, link, bid)
        prof_acc_page.arrange_(d, cur_language_qty_rnd_from_14, cur_country)

        # Act
        prof_acc_page.click_the_apply_button()

        # Assert
        print(f'\n{datetime.now()}   3. Assert')
        signup_form = SignupLogin(d, link, bid)
        if not signup_form.should_be_signup_form(cur_language_qty_rnd_from_14):
            Common().pytest_fail("Bug # 55!060   The Signup form is NOT displayed")
        Common().save_current_screenshot(d, "AT_55!060 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        signup_form.close_signup_form()
        Common().browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step("Start retest manual TC_55!065 The Trading Guides page is not opened "
                 "after clicking the link [Handelsleitfäden] (trading guides) "
                 "on the page [Demo-Konto] (Demo Account) in DE lang")
    @pytest.mark.parametrize('cur_language', ['de'])
    @pytest.mark.parametrize('cur_country', ['de', 'ua', 'au'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_065
    def test_065(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: The Trading Guides page is not opened after clicking the link [Handelsleitfäden] (trading guides)
         on the page [Demo-Konto] (Demo Account) in DE lang
         Language: CN.
         License: ASIC, CYSEC, SCB.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "065",
            "The Trading Guides page is not opened after clicking the link [Handelsleitfäden] (trading guides) "
            "on the page [Demo-Konto] (Demo Account) in DE lang"
        )

        # Arrange
        page_conditions = Conditions(d)
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL, "", cur_language,
                                             cur_country, cur_role, cur_login, cur_password)

        # refresh page to prevent "stale element exception" on 1st test if its in NoAuth role
        d.refresh()

        page_header_menu = MenuSection(d, link)
        trading_guides_page = TradingGuidesPageDeTest(d, link, bid)
        
        page_header_menu.move_focus_to_products_and_services_menu(d, cur_language, cur_country)
        trading_guides_page.click_demo_acc_menu_item()

        # Act
        trading_guides_page.click_trading_guides_link()

        # Assert
        if not trading_guides_page.should_be_trading_guides_page():
            Common().pytest_fail("Bug # 55!065 The Trading Guides page is NOT opened")
        Common().save_current_screenshot(d, "AT_55!065 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common().browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step(
        'Start retest manual TC_55!090 The modal window "Confirm Form Resubmission" is not opened '
        'after clicking the button [Back] on any article from search page.')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['de', 'ua', 'au'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.test_090
    def test_090(self, worker_id, d, cur_language, cur_country, cur_role,
                 cur_login, cur_password, random_search_string):
        """
         Check: The modal window "Confirm Form Resubmission" is not opened after clicking the button [Back]
         on any article from search page.
         Language: All.
         License: All, exclude FCA, SCA.
         Country: All, exclude GB, AE.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "090",
            'The modal window "Confirm Form Resubmission" is not opened after clicking the button [Back] '
            'on any article from search page.',
            False,
            False
        )

        # Arrange
        Common().check_country_in_list_and_skip_if_present(cur_country, ['gb', 'ae'])

        page_conditions = Conditions(d)
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL, "", cur_language,
                                             cur_country, cur_role, cur_login, cur_password)

        # refresh page to prevent "stale element exception" on 1st test if its in NoAuth role
        d.refresh()

        search_field = SearchField(d, link, bid)
        search_field.element_click()
        search_field.perform_search(random_search_string)

        # Act
        search_field.click_random_search_result_item()

        # Assert
        print(f'\n{datetime.now()}   Clicking the button [Back]')
        d.back()

        alert = Alert(d, link, bid)
        if not alert.should_be_alert():
            Common().pytest_fail('Bug # 55!090 The modal window "Confirm Form Resubmission" is NOT opened')
        Common().save_current_screenshot(d, "AT_55!090 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        alert.accept_alert()
        Common().browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step(
        "Start retest manual TC_55!091 | Page '教育' (Education) is opened after click "
        "on menu section [新聞和分析] (News and analysis) in CN language")
    @pytest.mark.parametrize('cur_language', ['cn'])
    @pytest.mark.parametrize('cur_country', ['de', 'ua', 'au'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.test_091
    def test_091(self, worker_id, d, cur_language, cur_country, cur_role,
                 cur_login, cur_password):
        """
         Check: Page '教育' (Education) is opened after click on menu section [新聞和分析] (News and analysis) in CN language.
         Language: CN.
         License: All, exclude FCA, SCA.
         Country: All, exclude GB, AE.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "091",
            "Start retest manual TC_55!091 | Page '教育' (Education) is opened after click "
            "on menu section [新聞和分析] (News and analysis) in CN language",
            False,
            False
        )

        # Arrange
        page_conditions = Conditions(d)
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL, "", cur_language,
                                             cur_country, cur_role, cur_login, cur_password)

        # refresh page to prevent "stale element exception" on 1st test if its in NoAuth role
        d.refresh()

        news_and_analysis_menu_section = NewsAndAnalysisMenuSection(d, link, bid)

        # Act
        news_and_analysis_menu_section.click_element()

        # Assert
        if not news_and_analysis_menu_section.should_be_news_and_analysis_page():
            Common().pytest_fail("Bug # 55!091 The News and Analysis page is NOT opened")
        Common().save_current_screenshot(d, "AT_55!091 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common().browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step("Start retest manual TC_55!093 The Search field in the header is not opened after performed search")
    @pytest.mark.parametrize('cur_country', ['de', 'ua', 'au'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.test_093
    def test_093(self, worker_id, d, cur_language_qty_rnd_from_14, cur_country, cur_role,
                 cur_login, cur_password, random_search_string):
        """
         Check: The Search field in the header is not opened after performed search
         Language: All.
         License: All, exclude FCA, SCA.
         Country: All, exclude GB, AE.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_qty_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "093",
            "The Search field in the header is not opened after performed search",
            False,
            False
        )

        # Arrange
        Common().check_country_in_list_and_skip_if_present(cur_country, ['gb', 'ae'])

        page_conditions = Conditions(d)
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL, "", cur_language_qty_rnd_from_14,
                                             cur_country, cur_role, cur_login, cur_password)

        # refresh page to prevent "stale element exception" on 1st test if its in NoAuth role
        d.refresh()

        search_field = SearchField(d, link, bid)
        search_field.element_click()
        search_field.perform_search(random_search_string)

        # Act
        search_field.element_click()

        # Assert
        time.sleep(1)

        if not search_field.should_be_active_search_field():
            Common().pytest_fail("Bug # 55!093 The Search field in the header is NOT active")
        Common().save_current_screenshot(d, "AT_55!093 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common().browser_back_to_link(d, CapitalComPageSrc.URL)
