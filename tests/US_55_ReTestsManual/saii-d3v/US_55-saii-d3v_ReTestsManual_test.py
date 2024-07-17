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

from pages.BugsManual.bug_054 import CorporateAccountsPage
from pages.BugsManual.bug_076 import ProfessionalAccountPage
from pages.BugsManual.bug_085 import TradingGuidesPageDeTest
from pages.BugsManual.bug_158 import NewsAndAnalysisMenuSection
from pages.Elements.HeaderSearchField import SearchField
from pages.Signup_login.signup_login import SignupLogin
from pages.Elements.HeaderLoginButton import HeaderButtonLogin
from pages.Elements.Alert import Alert
from pages.Menu.menu import MenuSection
from pages.Trading_platform.trading_platform import TradingPlatform
from src.src import CapitalComPageSrc


@pytest.mark.us_55
class TestManualDetectedBugs:
    page_conditions = None

    @allure.step("Start retest manual TC_55!043 The page is refreshed instead of opening the Login "
                 "form after clicking the [Log In] button on the Search page")
    @pytest.mark.parametrize('cur_country', ['de', 'ua', 'au'])
    @pytest.mark.parametrize('cur_role', ['NoAuth', 'NoReg'])
    @pytest.mark.bug_053
    def test_053(self, worker_id, d, cur_language_qty_rnd_from_14, cur_country, cur_role,
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
            "053",
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
            Common().pytest_fail(f"Bug # 55!053   The Login form is NOT displayed")
        Common().save_current_screenshot(d, "AT_55!053 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        login_form.close_login_form()
        Common().browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step("Start retest manual TC_55!054 The Sign-up/Login form or the trading platform page "
                 "are not opened after clicking the [Try now] button on the 'Corporate Accounts' page")
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['au'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_054
    def test_054(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: The Sign-up/Login form or the trading platform page are not opened
                after clicking the [Try now] button on the 'Corporate Accounts' page
         Language: EN.
         License: ASIC.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "054",
            "The Sign-up/Login form or the trading platform page are not opened "
            "after clicking the [Try now] button on the 'Corporate Accounts' page"
        )

        # Arrange
        page_conditions = Conditions(d)
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL, "", cur_language,
                                             cur_country, cur_role, cur_login, cur_password)

        page_header_menu = MenuSection(d, link)
        corp_acc_page = CorporateAccountsPage(d, link, bid)
        signup_login = SignupLogin(d, link, bid)
        trading_platform = TradingPlatform(d, link, bid)

        page_header_menu.move_focus_to_products_and_services_menu(d, cur_language, cur_country)
        corp_acc_page.click_corp_acc_menu_item()

        # Act
        corp_acc_page.click_try_now_btn()

        # Assert
        match cur_role:
            case "NoReg":
                if not signup_login.should_be_login_form():
                    Common().pytest_fail("Bug # 55!054   The Login form is NOT displayed")
            case "NoAuth":
                if not signup_login.should_be_signup_form(cur_language):
                    Common().pytest_fail("Bug # 55!054   The Sign-up form is NOT displayed")
            case "Auth":
                if not trading_platform.should_be_trading_platform_page(d, link):
                    Common().pytest_fail("Bug # 55!054   The Trading platform page is NOT opened")
        Common().save_current_screenshot(d, "AT_55!054 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        signup_login.close_signup_form()
        Common().browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step("Start retest manual TC_55!076 Login form is opened instead of Sign-up form "
                 "after clicking the button [Apply] in the Block 'Leverage Limits Professional Clients' "
                 "on page 'Professional Account'")
    @pytest.mark.parametrize('cur_country', ['de'])
    @pytest.mark.parametrize('cur_role', ['NoReg'])
    @pytest.mark.bug_076
    def test_076(self, worker_id, d, cur_language_qty_rnd_from_14, cur_country, cur_role, cur_login, cur_password):
        """
         Check: Login form is opened instead of Sign-up form after clicking the button [Apply]
                in the Block 'Leverage Limits Professional Clients' on page 'Professional Account'
         Language: All, except EL.
         License: CYSEC.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_qty_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "076",
            "Login form is opened instead of Sign-up form after clicking the button [Apply] "
            "in the Block 'Leverage Limits Professional Clients' on page 'Professional Account'"
        )

        # Arrange
        # Bug is not reproduced in 'el' language
        Common().check_language_in_list_and_skip_if_present(cur_language_qty_rnd_from_14, ['el'])

        page_conditions = Conditions(d)
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL, "", cur_language_qty_rnd_from_14,
                                             cur_country, cur_role, cur_login, cur_password)

        page_header_menu = MenuSection(d, link)
        prof_acc_page = ProfessionalAccountPage(d, link, bid)

        page_header_menu.move_focus_to_products_and_services_menu(d, cur_language_qty_rnd_from_14, cur_country)
        prof_acc_page.click_the_professional_account_menu_item()

        # Act
        prof_acc_page.click_the_apply_button()

        # Assert
        print(f'\n{datetime.now()}   3. Assert')
        signup_form = SignupLogin(d, link, bid)
        if not signup_form.should_be_signup_form(cur_language_qty_rnd_from_14):
            Common().pytest_fail("Bug # 55!076   The Sign-up form is NOT displayed")
        Common().save_current_screenshot(d, "AT_55!076 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        signup_form.close_signup_form()
        Common().browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step("Start retest manual TC_55!085 The Trading Guides page is not opened "
                 "after clicking the link [Handelsleitfäden] (trading guides) "
                 "on the page [Demo-Konto] (Demo Account) in DE lang")
    @pytest.mark.parametrize('cur_language', ['de'])
    @pytest.mark.parametrize('cur_country', ['de', 'ua', 'au'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_085
    def test_085(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: The Trading Guides page is not opened after clicking the link [Handelsleitfäden] (trading guides)
         on the page [Demo-Konto] (Demo Account) in DE lang
         Language: DE.
         License: ASIC, CYSEC, SCB.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "085",
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
            Common().pytest_fail("Bug # 55!085 The Trading Guides page is NOT opened")
        Common().save_current_screenshot(d, "AT_55!085 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common().browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step(
        'Start retest manual TC_55!157 The modal window "Confirm Form Resubmission" is not opened '
        'after clicking the button [Back] on any article from search page.')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['de', 'ua', 'au'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_157
    def test_157(self, worker_id, d, cur_language, cur_country, cur_role,
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
            "157",
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
            Common().pytest_fail('Bug # 55!157 The modal window "Confirm Form Resubmission" is NOT opened')
        Common().save_current_screenshot(d, "AT_55!157 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        alert.accept_alert()
        Common().browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step(
        "Start retest manual TC_55!158 | Page '教育' (Education) is opened after click "
        "on menu section [新聞和分析] (News and analysis) in CN language")
    @pytest.mark.parametrize('cur_language', ['cn'])
    @pytest.mark.parametrize('cur_country', ['de', 'ua', 'au'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_158
    def test_158(self, worker_id, d, cur_language, cur_country, cur_role,
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
            "158",
            "Page '教育' (Education) is opened after click "
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
            Common().pytest_fail("Bug # 55!158 The News and Analysis page is NOT opened")
        Common().save_current_screenshot(d, "AT_55!158 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common().browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step("Start retest manual TC_55!160 The Search field in the header is not opened after performed search")
    @pytest.mark.parametrize('cur_country', ['de', 'ua', 'au'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_160
    def test_160(self, worker_id, d, cur_language_qty_rnd_from_14, cur_country, cur_role,
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
            "160",
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
            Common().pytest_fail("Bug # 55!160 The Search field in the header is NOT active")
        Common().save_current_screenshot(d, "AT_55!160 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common().browser_back_to_link(d, CapitalComPageSrc.URL)
