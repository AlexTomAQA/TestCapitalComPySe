"""
-*- coding: utf-8 -*-
@Time    : 2024/06/19 18:00 GMT+5
@Author  : Sergey Aiidzhanov
"""

import time
from datetime import datetime
import random

import pytest
import allure

from pages.common import Common
from pages.conditions import Conditions
from pages.conditions_new import NewConditions
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55

from pages.BugsManual.bug_052 import CommoditiesPageOpenCheck
from pages.BugsManual.bug_054 import CorporateAccountsPage
from pages.BugsManual.bug_076 import ProfessionalAccountPage
from pages.BugsManual.bug_085 import TradingGuidesPageDeTest
from pages.BugsManual.bug_158 import NewsAndAnalysisMenuSection
from pages.BugsManual.bugs_272_273 import LearnToTradePage
from pages.BugsManual.bug_288 import Bug288
from pages.BugsManual.bug_299 import CheckLoginFacebookModal
from pages.BugsManual.bug_305 import Bug305
from pages.BugsManual.bug_307 import Bug307
from pages.BugsManual.bug_327 import Bug327
from pages.BugsManual.bug_330 import Bug330
from pages.BugsManual.bug_332 import Bug332
from pages.BugsManual.bug_335 import Bug335
from pages.BugsManual.bug_359 import Bug359
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

    @allure.step("Start retest manual TC_55!052 The main page in EN language is opened "
                 "after click on the link [Go to all commodities] on the 'Commodities trading' page "
                 "when AR, IT, NL, PL, RO, CN language is selected")
    @pytest.mark.parametrize('cur_language', random.sample(['ar', 'it', 'nl', 'pl', 'ro', 'cn'], 2))
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'ua', 'au'], 1))
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_052
    def test_052(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: The main page in EN language is opened after click on the link [Go to all commodities]
                on the "Commodities trading" page when AR, IT, NL, PL, RO, CN language is selected
         Language: AR, IT, NL, PL, RO, CN.
         License: ASIC, CYSEC, SCB.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "052",
            "The main page in EN language is opened after click on the link [Go to all commodities] "
            "on the 'Commodities trading' page when AR, IT, NL, PL, RO, CN language is selected"
        )

        # Arrange
        page_conditions = Conditions(d)
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL, "", cur_language,
                                             cur_country, cur_role, cur_login, cur_password)

        page_header_menu = MenuSection(d, link)
        test_el = CommoditiesPageOpenCheck(d, link, bid)

        page_header_menu.open_education_commodities_trading_menu(d, cur_language, cur_country, link)

        # Act
        test_el.click_go_to_all_commodities_link()

        # Assert
        if not test_el.should_not_be_main_page():
            Common.pytest_fail("Bug # 55!052   The Commodities page is NOT opened")
        Common.save_current_screenshot(d, "AT_55!052 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step("Start retest manual TC_55!043 The page is refreshed instead of opening the Login "
                 "form after clicking the [Log In] button on the Search page")
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'ua', 'au'], 1))
    @pytest.mark.parametrize('cur_role', ['NoAuth', 'NoReg'])
    @pytest.mark.bug_053
    def test_053(self, worker_id, d, cur_language_qty_rnd_from_14, cur_country, cur_role,
                 cur_login, cur_password, random_search_string):
        """
         Check: The page is refreshed instead of opening the Login form after clicking the [Log In] button
                on the Search page
         Language: All.
         License: ASIC, CYSEC, SCB.
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
            Common.pytest_fail(f"Bug # 55!053   The Login form is NOT displayed")
        Common.save_current_screenshot(d, "AT_55!053 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        login_form.close_login_form()
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

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
                    Common.pytest_fail("Bug # 55!054   The Login form is NOT displayed")
            case "NoAuth":
                if not signup_login.should_be_signup_form(cur_language):
                    Common.pytest_fail("Bug # 55!054   The Sign-up form is NOT displayed")
            case "Auth":
                if not trading_platform.should_be_trading_platform_page(d, link):
                    Common.pytest_fail("Bug # 55!054   The Trading platform page is NOT opened")
        Common.save_current_screenshot(d, "AT_55!054 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        signup_login.close_signup_form()
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

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
        Common.check_language_in_list_and_skip_if_present(cur_language_qty_rnd_from_14, ['el'])

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
            Common.pytest_fail("Bug # 55!076   The Sign-up form is NOT displayed")
        Common.save_current_screenshot(d, "AT_55!076 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        signup_form.close_signup_form()
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step("Start retest manual TC_55!085 The Trading Guides page is not opened "
                 "after clicking the link [Handelsleitfäden] (trading guides) "
                 "on the page [Demo-Konto] (Demo Account) in DE lang")
    @pytest.mark.parametrize('cur_language', ['de'])
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'ua', 'au'], 1))
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
            Common.pytest_fail("Bug # 55!085 The Trading Guides page is NOT opened")
        Common.save_current_screenshot(d, "AT_55!085 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step(
        'Start retest manual TC_55!157 The modal window "Confirm Form Resubmission" is not opened '
        'after clicking the button [Back] on any article from search page.')
    @pytest.mark.parametrize('cur_language', [''])  # temporary use only EN, because of bug #55!292
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'ua', 'au'], 1))
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_157
    def test_157(self, worker_id, d, cur_language, cur_country, cur_role,
                 cur_login, cur_password, random_search_string):
        """
         Check: The modal window "Confirm Form Resubmission" is not opened after clicking the button [Back]
         on any article from search page.
         Language: All.
         License: ASIC, CYSEC, SCB.
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
            Common.pytest_fail('Bug # 55!157 The modal window "Confirm Form Resubmission" is NOT opened')
        Common.save_current_screenshot(d, "AT_55!157 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        alert.accept_alert()
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step(
        "Start retest manual TC_55!158 | Page '教育' (Education) is opened after click "
        "on menu section [新聞和分析] (News and analysis) in CN language")
    @pytest.mark.parametrize('cur_language', ['cn'])
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'ua', 'au'], 1))
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_158
    def test_158(self, worker_id, d, cur_language, cur_country, cur_role,
                 cur_login, cur_password):
        """
         Check: Page '教育' (Education) is opened after click on menu section [新聞和分析] (News and analysis) in CN language.
         Language: CN.
         License: ASIC, CYSEC, SCB.
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
            Common.pytest_fail("Bug # 55!158 The News and Analysis page is NOT opened")
        Common.save_current_screenshot(d, "AT_55!158 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step("Start retest manual TC_55!160 The Search field in the header is not opened after performed search")
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'ua', 'au'], 1))
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_160
    def test_160(self, worker_id, d, cur_language_qty_rnd_from_14, cur_country, cur_role,
                 cur_login, cur_password, random_search_string):
        """
         Check: The Search field in the header is not opened after performed search
         Language: All.
         License: ASIC, CYSEC, SCB.
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
            Common.pytest_fail("Bug # 55!160 The Search field in the header is NOT active")
        Common.save_current_screenshot(d, "AT_55!160 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step(
        'Start retest manual TC_55!272 | The page with “404 error” message is displayed '
        'after clicking the link [تعلّم التداول] (Learn to trade) '
        'in the tile  [تبدأ الطريق من أوله؟] (Starting from the beginning?) '
        'on the page "تعلّم التداول" (Learn to trade) when AR language is selected')
    @pytest.mark.parametrize('cur_language', ['ar'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_272
    def test_272(self, worker_id, d, cur_language, cur_country, cur_role,
                 cur_login, cur_password):
        """
         Check: The page with “404 error” message is displayed
                after clicking the link [تعلّم التداول] (Learn to trade)
                in the tile  [تبدأ الطريق من أوله؟] (Starting from the beginning?)
                on the page "تعلّم التداول" (Learn to trade) when AR language is selected
         Language: AR.
         License: SCA.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "272",
            'The page with “404 error” message is displayed '
            'after clicking the link [تعلّم التداول] (Learn to trade) '
            'in the tile  [تبدأ الطريق من أوله؟] (Starting from the beginning?) '
            'on the page "تعلّم التداول" (Learn to trade) when AR language is selected',
            False,
            False
        )

        # Arrange
        page_conditions = NewConditions(d)
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL_NEW_AR_AE, "", cur_language,
                                             cur_country, cur_role, cur_login, cur_password)

        test_el = LearnToTradePage(d, link, bid)
        test_el.open_learn_to_trade_page(d, cur_language, cur_country, link)

        # Act
        test_el.click_the_learn_to_trade_link272()

        # Assert
        if not test_el.should_be_visible_block_trading_for_beginners():
            Common.pytest_fail('Bug # 55!272 The the block "Trading for beginners" is NOT into viewport')
        Common.save_current_screenshot(d, "AT_55!272 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW)

    @allure.step(
        'Start retest manual TC_55!273 | The page with “404 error” message is displayed '
        'after clicking the link [تعلّم التداول] (Learn to trade) '
        'in the tile [ترغب في تحسين استراتيجياتك؟] (Looking to sharpen your strategies?) '
        'on the page "تعلّم التداول" (Learn to trade) when AR language is selected')
    @pytest.mark.parametrize('cur_language', ['ar'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_273
    def test_273(self, worker_id, d, cur_language, cur_country, cur_role,
                 cur_login, cur_password):
        """
         Check: The page with “404 error” message is displayed
                after clicking the link [تعلّم التداول] (Learn to trade)
                in the tile [ترغب في تحسين استراتيجياتك؟] (Looking to sharpen your strategies?)
                on the page "تعلّم التداول" (Learn to trade) when AR language is selected
         Language: AR.
         License: SCA.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "273",
            'The page with “404 error” message is displayed '
            'after clicking the link [تعلّم التداول] (Learn to trade) '
            'in the tile [ترغب في تحسين استراتيجياتك؟] (Looking to sharpen your strategies?) '
            'on the page "تعلّم التداول" (Learn to trade) when AR language is selected',
            False,
            False
        )

        # Arrange
        page_conditions = NewConditions(d)
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_AR_AE, "",
            cur_language, cur_country, cur_role, cur_login, cur_password
        )

        test_el = LearnToTradePage(d, link, bid)
        test_el.open_learn_to_trade_page(d, cur_language, cur_country, link)

        # Act
        test_el.click_the_learn_to_trade_link273()

        # Assert
        if not test_el.should_be_visible_block_trading_for_beginners():
            Common.pytest_fail('Bug # 55!273 The the block "Experienced traders" is NOT into viewport')
        Common.save_current_screenshot(d, "AT_55!273 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW)

    @allure.step('Start retest manual TC_55!288 The page "Trading products" is opened '
                 'after clicking the link [Our mobile Apps] '
                 'in the tile "Industry-leading features for an industry-leading platform" '
                 'on the page "Why Capital.com?" when any language (except EN) is selected')
    @pytest.mark.parametrize('cur_language_qty_rnd_from_14', ['ru', 'zh'])
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'ua', 'au'], 1))
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_288
    def test_288(self, worker_id, d, cur_language_qty_rnd_from_14, cur_country, cur_role, cur_login, cur_password):
        """
         Check: The page "Trading products" is opened after clicking the link [Our mobile Apps]
                in the tile "Industry-leading features for an industry-leading platform"
                on the page "Why Capital.com?" when any language (except EN) is selected
         Language: All, except EN.
         License: ASIC, CYSEC, SCB.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_qty_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "288",
            'The page "Trading products" is opened after clicking the link [Our mobile Apps] '
            'in the tile "Industry-leading features for an industry-leading platform" on the page "Why Capital.com?" '
            'when any language (except EN) is selected'
        )

        # Arrange
        Common.check_language_in_list_and_skip_if_present(cur_language_qty_rnd_from_14, [''])

        page_conditions = Conditions(d)
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL, "", cur_language_qty_rnd_from_14,
                                             cur_country, cur_role, cur_login, cur_password)

        # refresh page to prevent "stale element exception" on 1st test if its in NoAuth role
        d.refresh()

        page_header_menu = MenuSection(d, link)
        test_el = Bug288(d, link, bid)

        page_header_menu.move_focus_to_products_and_services_menu(d, cur_language_qty_rnd_from_14, cur_country)
        test_el.click_why_capital_menu_item()

        # Act
        test_el.click_our_mobile_apps_link()

        # Assert
        if not test_el.should_be_mobile_apps_page(cur_language_qty_rnd_from_14):
            Common.pytest_fail("Bug # 55!288 The Mobile Apps page is NOT opened")
        Common.save_current_screenshot(d, "AT_55!288 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step(
        'Start retest manual TC_55!292 There are no search results on the Search page '
        'when any language except EN is selected')
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'ua', 'au'], 1))
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_292
    def test_292(self, worker_id, d, cur_language_qty_rnd_from_14, cur_country, cur_role,
                 cur_login, cur_password, random_search_string):
        """
         Check: There are no search results on the Search page when any language except EN is selected.
         Language: All, except EN.
         License: ASIC, CYSEC, SCB.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_qty_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "292",
            'There are no search results on the Search page when any language except EN is selected',
            False,
            False
        )

        # Arrange
        Common.check_language_in_list_and_skip_if_present(cur_language_qty_rnd_from_14, [''])

        page_conditions = Conditions(d)
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL, "", cur_language_qty_rnd_from_14,
                                             cur_country, cur_role, cur_login, cur_password)

        # refresh page to prevent "stale element exception" on 1st test if its in NoAuth role
        d.refresh()

        search_field = SearchField(d, link, bid)
        search_field.element_click()

        # Act
        search_field.perform_search(random_search_string)

        # Assert
        if not search_field.should_be_any_search_result():
            Common.pytest_fail('Bug # 55!292 There are NO search items presented')
        Common.save_current_screenshot(d, "AT_55!292 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step(
        'Start retest manual TC_55!299 | The modal window "Log in to your Facebook account" is not opened '
        'after clicking the button [Facebook] in the Sign up / Log in form on any page '
        'when EN/AR language and SCA license is selected')
    @pytest.mark.parametrize('cur_language', ['ar', ''])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ['NoReg'])  # 'NoReg', 'NoAuth'
    @pytest.mark.bug_299
    def test_299(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: The modal window "Log in to your Facebook account" is not opened
                after clicking the button [Facebook] in the Signup / Log in form
                on any page when EN/AR language and SCA license is selected
         Language: AR, EN.
         License: SCA.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "299",
            'The modal window "Log in to your Facebook account" is not opened '
            'after clicking the button [Facebook] in the Sign up / Log in form on any page '
            'when EN/AR language and SCA license is selected',
            False,
            False
        )
        # Arrange
        page_conditions = NewConditions(d)
        link = page_conditions.preconditions(d, CapitalComPageSrc.URL_NEW_EN_AE, "", cur_language,
                                             cur_country, cur_role, cur_login, cur_password)

        test_el = CheckLoginFacebookModal(d, link, bid)
        signup_login = SignupLogin(d, link, bid)

        if cur_role == "NoReg":
            test_el.click_signup_button()
        if cur_role == "NoAuth":
            test_el.click_login_button()

        # Act
        test_el.click_fb_btn()

        # Assert
        if not test_el.should_be_fb_modal():
            Common.pytest_fail('Bug # 55!299 in progress')
        Common.save_current_screenshot(d, "AT_55!299 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        if cur_role == "NoReg":
            signup_login.close_new_signup_form()
        if cur_role == "NoAuth":
            signup_login.close_new_login_form()
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW_EN_AE)

    @allure.step(
        'Start retest manual TC_55!305 | Error message is displayed after clicking the link "أكثر" (More) '
        'in the tile "العملات المشفرة" (Cryptocurrencies) on the page "تجريبي" (Demo) '
        'when AR language and SCA license is selected')
    @pytest.mark.parametrize('cur_language', ['ar'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_305
    def test_305(self, worker_id, d, cur_language, cur_country, cur_role,
                 cur_login, cur_password):
        """
         Check: Error message is displayed after clicking the link "أكثر" (More)
         in the tile "العملات المشفرة" (Cryptocurrencies) on the page "تجريبي" (Demo)
         when AR language and SCA license is selected
         Language: AR.
         License: SCA.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "305",
            'Error message is displayed after clicking the link "أكثر" (More) '
            'in the tile "العملات المشفرة" (Cryptocurrencies) on the page "تجريبي" (Demo) '
            'when AR language and SCA license is selected',
            False,
            False
        )

        # Arrange
        page_conditions = NewConditions(d)
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_EN_AE, "",
            cur_language, cur_country, cur_role, cur_login, cur_password
        )

        test_el = Bug305(d, link, bid)
        test_el.open_demo_account_page(d, cur_language, cur_country, link)

        # Act
        test_el.click_more_button()

        # Assert
        if not test_el.should_be_cryptocurrency_trading_page():
            Common.pytest_fail('Bug # 55!305 The Cryptocurrency Trading page is NOT opened')
        Common.save_current_screenshot(d, "AT_55!305 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW_EN_AE)

    @allure.step(
        'Start retest manual TC_55!307 Error message “DNS_PROBE_FINISHED_NXDOMAIN” is displayed '
        'after clicking any of 12 links in the text on the page “Stock Market Trading Hours” '
        'when EN language is selected')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_307
    def test_307(self, worker_id, d, cur_language, cur_country, cur_role,
                 cur_login, cur_password):
        """
         Check: Error message “DNS_PROBE_FINISHED_NXDOMAIN” is displayed
         after clicking any of 12 links in the text on the page “Stock Market Trading Hours”
         when EN language is selected
         Language: EN.
         License: SCA.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "307",
            'Error message “DNS_PROBE_FINISHED_NXDOMAIN” is displayed '
            'after clicking any of 12 links in the text on the page “Stock Market Trading Hours” '
            'when EN language is selected',
            False,
            False
        )
        # Arrange
        page_conditions = NewConditions(d)
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_EN_AE, "",
            cur_language, cur_country, cur_role, cur_login, cur_password
        )

        test_el = Bug307(d, link, bid)
        test_el.open_shares_trading_page(d, cur_language, cur_country, link)
        test_el.open_stock_market_trading_hours_page()

        # Act
        test_el.click_any_trading_instrument_link()

        # Assert
        if not test_el.should_be_corresponding_page():
            Common.pytest_fail('Bug # 55!307 The corresponding page is NOT opened')
        Common.save_current_screenshot(d, "AT_55!307 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW_EN_AE)

    @allure.step(
        'Start retest manual TC_55!327 Part of the button [تداول عقود الفروقات عبر الويب] (Trade CFDs on the web) '
        'in the block "المنصة الإلكترونية عبر الويب" (Web platform) '
        'on the page "تداول العقود مقابل الفروقات" (CFD trading) is not clickable')
    @pytest.mark.parametrize('cur_language', ['ar'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ['NoReg'])   # 'Auth', 'NoAuth', 'NoReg'
    @pytest.mark.bug_327
    def test_327(self, worker_id, d, cur_language, cur_country, cur_role,
                 cur_login, cur_password):
        """
         Check: Part of the button [تداول عقود الفروقات عبر الويب] (Trade CFDs on the web)
         in the block "المنصة الإلكترونية عبر الويب" (Web platform)
         on the page "تداول العقود مقابل الفروقات" (CFD trading) is not clickable
         Language: AR.
         License: SCA.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "327",
            'Part of the button [تداول عقود الفروقات عبر الويب] (Trade CFDs on the web) '
            'in the block "المنصة الإلكترونية عبر الويب" (Web platform) '
            'on the page "تداول العقود مقابل الفروقات" (CFD trading) is not clickable',
            False,
            False
        )
        pytest.skip('In progress')
        # Arrange
        page_conditions = NewConditions(d)
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_EN_AE, "",
            cur_language, cur_country, cur_role, cur_login, cur_password
        )

        test_el = Bug327(d, link, bid)
        test_el.open_cfd_trading_page(d, cur_language, cur_country, link)

        # Act
        test_el.hover_over_trade_cfds_button()

        # Assert
        # if not test_el.:
        #     Common.pytest_fail('Bug # 55!327 ')
        # Common.save_current_screenshot(d, "AT_55!327 Pass")
        Common.pytest_fail('Bug # 55!327 ')

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW_EN_AE)

    @allure.step(
        'Start retest manual TC_55!330 | “Support” chat window is not opened after click on the “Support” button '
        'and this button disappears after the second clicking on it on any page '
        'after changing the language of the site (e.g. from EN to AR) (SCA license).')
    @pytest.mark.parametrize('cur_language', ['ar', ''])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_330
    def test_330(self, worker_id, d, cur_language, cur_country, cur_role,
                 cur_login, cur_password):
        """
         Check: “Support” chat window is not opened after click on the “Support” button
         and this button disappears after the second clicking on it on any page
         after changing the language of the site (e.g. from EN to AR) (SCA license).
         Language: AR, EN.
         License: SCA.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "330",
            '“Support” chat window is not opened after click on the “Support” button '
            'and this button disappears after the second clicking on it on any page '
            'after changing the language of the site (e.g. from EN to AR) (SCA license).',
            False,
            False
        )
        # Arrange
        page_conditions = NewConditions(d)
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_EN_AE, "",
            cur_language, cur_country, cur_role, cur_login, cur_password
        )

        test_el = Bug330(d, link, bid)
        test_el.open_support_window()
        test_el.should_be_support_window()
        test_el.close_support_window()
        test_el.change_language(cur_language)

        # Act
        test_el.open_support_window()

        # Assert
        if not test_el.should_be_support_window():
            Common.pytest_fail('Bug # 55!330 The Support Chat window is NOT opened')
        Common.save_current_screenshot(d, "AT_55!330 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW_EN_AE)

    @allure.step(
        'Start retest manual TC_55!332a | Error message is displayed after clicking the link "Stochastic Oscillator" '
        'of the block “How to trade using RSI and other indicators” '
        'on the page “RSI trading strategy: An educational guide”')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', random.sample(['au', 'de', 'ua'], 1))
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_332a
    def test_332a(self, worker_id, d, cur_language, cur_country, cur_role,
                  cur_login, cur_password):
        """
         Check: Error message is displayed after clicking the link "Stochastic Oscillator"
         of the block “How to trade using RSI and other indicators”
         on the page “RSI trading strategy: An educational guide”
         Language: EN.
         License: ASIC, CYSEC, SCB.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "332a",
            'Error message is displayed after clicking the link "Stochastic Oscillator" '
            'of the block “How to trade using RSI and other indicators” '
            'on the page “RSI trading strategy: An educational guide”',
            False,
            False
        )

        # Arrange
        page_conditions = Conditions(d)
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "",
            cur_language, cur_country, cur_role, cur_login, cur_password
        )

        page_header_menu = MenuSection(d, link)
        test_el = Bug332(d, link, bid)

        page_header_menu.menu_education_move_focus(d, cur_language, cur_country)
        page_header_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)
        test_el.click_rsi_trading_strategy_link()

        # Act
        test_el.click_stochastic_oscillator_link()

        # Assert
        if not test_el.should_be_stochastic_oscillator_strategy_page():
            Common.pytest_fail('Bug # 55!332a The "Stochastic oscillator strategy" page is NOT opened')
        Common.save_current_screenshot(d, "AT_55!332a Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step(
        'Start retest manual TC_55!332b | Error message is displayed after clicking the link "support and resistance" '
        'of the block “How to trade using RSI and other indicators” '
        'on the page “RSI trading strategy: An educational guide”')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', random.sample(['au', 'de', 'ua'], 1))
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_332b
    def test_332b(self, worker_id, d, cur_language, cur_country, cur_role,
                  cur_login, cur_password):
        """
         Check: Error message is displayed after clicking the link "support and resistance"
         of the block “How to trade using RSI and other indicators”
         on the page “RSI trading strategy: An educational guide”
         Language: EN.
         License: ASIC, CYSEC, SCB.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "332b",
            'Error message is displayed after clicking the link "support and resistance" '
            'of the block “How to trade using RSI and other indicators” '
            'on the page “RSI trading strategy: An educational guide”',
            False,
            False
        )

        # Arrange
        page_conditions = Conditions(d)
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "",
            cur_language, cur_country, cur_role, cur_login, cur_password
        )

        page_header_menu = MenuSection(d, link)
        test_el = Bug332(d, link, bid)

        page_header_menu.menu_education_move_focus(d, cur_language, cur_country)
        page_header_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)
        test_el.click_rsi_trading_strategy_link()

        # Act
        test_el.click_support_and_resistance_link()

        # Assert
        if not test_el.should_be_support_and_resistance_page():
            Common.pytest_fail('Bug # 55!332b The "What is support and resistance?" page is NOT opened')
        Common.save_current_screenshot(d, "AT_55!332b Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step(
        'Start retest manual TC_55!335 | Error message is displayed '
        'after clicking the link “تعلّم المزيد حول كيفيّة التداول على الأسهم“ (Learn more about shares trading) '
        'in the tile “التداول على الأسهم” (Shares trading) '
        'on the page “ما هو مفهوم التداول على النفط” (What is oil trading) when AR language is selected')
    @pytest.mark.parametrize('cur_language', ['ar'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_335
    def test_335(self, worker_id, d, cur_language, cur_country, cur_role,
                 cur_login, cur_password):
        """
         Check: Error message is displayed
         after clicking the link “تعلّم المزيد حول كيفيّة التداول على الأسهم“ (Learn more about shares trading)
         in the tile “التداول على الأسهم” (Shares trading)
         on the page “ما هو مفهوم التداول على النفط” (What is oil trading) when AR language is selected
         Language: AR.
         License: SCA.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "335",
            'Error message is displayed '
            'after clicking the link “تعلّم المزيد حول كيفيّة التداول على الأسهم“ (Learn more about shares trading) '
            'in the tile “التداول على الأسهم” (Shares trading) '
            'on the page “ما هو مفهوم التداول على النفط” (What is oil trading) when AR language is selected',
            False,
            False
        )

        # Arrange
        page_conditions = NewConditions(d)
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_EN_AE, "",
            cur_language, cur_country, cur_role, cur_login, cur_password
        )

        test_el = Bug335(d, link, bid)
        test_el.open_market_guides_page(d, cur_language, cur_country, link)
        test_el.click_oil_trading_guide_button()

        # Act
        test_el.click_learn_more_about_shares_trading_button()

        # Assert
        if not test_el.should_be_what_is_shares_trading_page():
            Common.pytest_fail('Bug # 55!335 The "What is shares trading" page is NOT opened')
        Common.save_current_screenshot(d, "AT_55!335 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW_EN_AE)

    @allure.step(
        'Start retest manual TC_55!359a | Error message is displayed after clicking the link “NASDAQ stock exchange” '
        'in the block “GOOGL Company profile” on the page “Trade Alphabet Inc - A - GOOGL CFD”')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_359a
    def test_359a(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: Error message is displayed after clicking the link “NASDAQ stock exchange”
         in the block “GOOGL Company profile” on the page “Trade Alphabet Inc - A - GOOGL CFD”
         Language: EN.
         License: FCA, FCA.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "359a",
            'Error message is displayed after clicking the link “NASDAQ stock exchange” '
            'in the block “GOOGL Company profile” on the page “Trade Alphabet Inc - A - GOOGL CFD”',
            False,
            False
        )

        # Arrange
        page_conditions = NewConditions(d)
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "",
            cur_language, cur_country, cur_role, cur_login, cur_password
        )

        test_el = Bug359(d, link, bid)
        test_el.open_shares_page(d, cur_language, cur_country, link)
        test_el.open_trade_alphabet_page_new()

        # Act
        test_el.click_nasdaq_link()

        # Assert
        if not test_el.should_not_be_error_page():
            Common.pytest_fail('Bug # 55!359a The ERROR page is opened')
        Common.save_current_screenshot(d, "AT_55!359a Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW)

    @allure.step(
        'Start retest manual TC_55!359b | Error message is displayed after clicking the link “NASDAQ stock exchange” '
        'in the block “GOOGL Company profile” on the page “Trade Alphabet Inc - A - GOOGL CFD”')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', random.sample(['au', 'de', 'ua'], 1))
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_359b
    def test_359b(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: Error message is displayed after clicking the link “NASDAQ stock exchange”
         in the block “GOOGL Company profile” on the page “Trade Alphabet Inc - A - GOOGL CFD”
         Language: EN.
         License: ASIC, CYSEC, SCB.
         Author: Sergey Aiidzhanov
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "359b",
            'Error message is displayed after clicking the link “NASDAQ stock exchange” '
            'in the block “GOOGL Company profile” on the page “Trade Alphabet Inc - A - GOOGL CFD”',
            False,
            False
        )

        # Arrange
        page_conditions = Conditions(d)
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "",
            cur_language, cur_country, cur_role, cur_login, cur_password
        )

        page_header_menu = MenuSection(d, link)
        test_el = Bug359(d, link, bid)

        page_header_menu.open_shares_market_menu(d, cur_language, cur_country, link)
        test_el.open_trade_alphabet_page_old()

        # Act
        test_el.click_nasdaq_link()

        # Assert
        if not test_el.should_not_be_alphabet_inc_page_old():
            Common.pytest_fail('Bug # 55!359b The "Trade Alphabet Inc - A - GOOGL CFD" page is still opened')
        Common.save_current_screenshot(d, "AT_55!359b Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)
