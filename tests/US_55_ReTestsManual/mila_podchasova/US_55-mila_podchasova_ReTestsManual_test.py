"""
-*- coding: utf-8 -*-
@Time    : 2024/06/06 15:29
@Author  : podchasova11
"""
from datetime import datetime
import random

import pytest
import allure

from pages.BugsManual.bug_043 import ProfessionalMenuCheckFooter
from pages.BugsManual.bug_038 import WebTradingPlatformPage
from pages.BugsManual.bug_090 import CreateARiskFreeDemoAccountButton
from pages.BugsManual.bug_285 import ButtonMyAccount
from pages.BugsManual.bug_326 import Bug326
from pages.BugsManual.bug_350 import Bug350
from pages.Elements.AssertClass import AssertClass
from pages.Elements.PlatformOverviewButton import PlatformOverviewButton
from pages.Menu.menu import MenuSection
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55

from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.conditions_new import NewConditions


@pytest.mark.us_55
class TestManualDetectedBugs:
    page_conditions = None

    @allure.step("Start retest manual TC_55!00_038 The Trading platform overview page not open when"
                 " button [Platform overview] click on the 'Investmate app' page")
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'ua', 'au'], 1))
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_038
    def test_038(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: The Trading platform overview page does not open when
         the button [Platform overview] is pressed on the "Investmate app" page

         Author: podchasova11
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "038", "The Trading platform overview page not open when"
                   " button [Platform overview] click on the 'Investmate app' page"
        )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PlatformOverviewButton(d, link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, link)

        print(f'\n{datetime.now()}   3. Assert')

        page = WebTradingPlatformPage(d, link, bid)
        if not page.should_be_web_trading_platform_page(d, link):
            Common().pytest_fail(f"Bug#038. "
                                 "Expected result:The Desktop Trading page is opened "
                                 "\n"
                                 "Actual result: The Home page is opened ")
        Common().save_current_screenshot(d, "AT_55!038 Pass")

    @allure.step("Start retest manual TC_55!00_043 "
                 "The footer is missing on click menu item [Professional] of the menu section [Ways to trade]")
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_043
    def test_043(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        The footer is missing on click menu item [Professional] of the menu section [Ways to trade]
        1. Hover over the [Ways to trade] menu section
        2. Click the [Professional]menu item
        Author: podchasova11
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "043",
            "The footer is missing on click menu item [Professional] of the menu section [Ways to trade]"
        )
        # pytest.skip("Autotest under construction")

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        link = menu.open_ways_to_trade_professional_menu(d, cur_language, cur_country, link)

        menu = ProfessionalMenuCheckFooter(d, link, bid)
        menu.check_that_footer_displayed_on_professional_page(d, cur_language, cur_country, link)

    @allure.step("Start retest manual TC_55!00_090 "
                 "The trading platform page is not opened "
                 "in [demo mode] after clicking on the [Create a risk-free demo account] button "
                 "on the 'Demo account' page")
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'ua'], 1)) # на лицензии 'au' другой локатор кнопки => тест выдает ошибку
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.bug_090
    def test_090(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        The trading platform page is not opened in "Demo account" page
        after clicking on the [Create a risk-free demo account] button
        Language: All.
        License: All, except FCA, SCA.
        Country: All, except GB, AE.
        Author: podchasova11
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "090",
            "The trading platform page is not opened "
            "in [demo mode] after clicking on the [Create a risk-free demo account] button"
            "on the 'Demo account' page"
        )

        # pytest.skip("Autotest under construction")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        # Arrange
        menu = MenuSection(d, link)
        link = menu.sub_menu_demo_account_move_focus_click(d, cur_language, cur_country, link)
        # Act, Assert
        test_element = CreateARiskFreeDemoAccountButton(d, link, bid)
        test_element.full_test(d, cur_role, link)

    @allure.step("Start retest manual TC_55!00_285en Opened the Trading platform page "
                 "instead [My Account] menu after clicking the [My account] button")
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.bug_285en
    def test_285en(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Opened the Trading platform page
        instead [My Account] menu after clicking the [My account] button
        Language: EN
        License: SCA.
        Country: AE.
        Author: podchasova11
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "285en",
            "Opened the Trading platform page "
            "instead [My Account] menu after clicking the [My account] button"
        )

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_EN_AE, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # Arrange
        button = ButtonMyAccount(d, link, bid)
        button.arrange_(link)

        # Act
        button.element_click()

        # Assert
        match cur_role:
            case "Auth":
                button.assert_my_account_menu_opened_en(d)

    @allure.step("Start retest manual TC_55!00_285ar Opened the Trading platform page "
                 "instead [My Account] menu after clicking the [My account] button")
    @pytest.mark.parametrize('cur_language', ['ar'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.bug_285ar
    def test_285ar(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Opened the Trading platform page
        instead [My Account] menu after clicking the [My account] button
        Language: AR
        License: SCA.
        Country: AE.
        Author: podchasova11
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "285ar",
            "Opened the Trading platform page "
            "instead [My Account] menu after clicking the [My account] button"
        )

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW_AR_AE, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # Arrange
        button = ButtonMyAccount(d, link, bid)
        button.arrange_(link)

        # Act
        button.element_click()

        # Assert
        match cur_role:
            case "Auth":
                button.assert_my_account_menu_opened_ar(d)

    @allure.step(
        'Start retest manual TC_55!326 | The page "Oops, this help center no longer exists"'
        ' is opened after clicking the link [Help Center] of the page "Contact us"')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'ua', 'au'], 1))
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_326
    def test_326(self, worker_id, d, cur_language, cur_country, cur_role,
                  cur_login, cur_password):
        """
         Check: The page "Oops, this help center no longer exists"
         is opened after clicking the link [Help Center] of the page "Contact us"
         Language: All.
         License: ASIC, CYSEC.
         Role: NoReg | NoAuth | Auth
         Author: podchasova11
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "326",
            "The page 'Oops, this help center no longer exists' "
            "is opened after clicking the link [Help Center] of the page 'Contact us'",
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
        page_header_menu.move_focus_to_more_menu(d, cur_language, cur_country)
        page_header_menu.sub_menu_help_and_support_move_focus_click(d, cur_language)

        test_el = Bug326(d, link, bid)

        # Act
        test_el.click_help_center_link()

        # Assert
        test_el.should_be_help_center_page()

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step(
        'Start retest manual TC_55!350 | Error message is displayed when clicking the link [How-to guides] '
        'in block “Looking for more?” on the page [Trading courses]')
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'ua'], 1))
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_350
    def test_350(self, worker_id, d, cur_language, cur_country, cur_role,
                  cur_login, cur_password):
        """
         Check: Error message is displayed when clicking the link [How-to guides]
         in block “Looking for more?” on the page [Trading courses]
         Language: All.
         License: CYSEC, SCB.
         Role: NoReg | NoAuth | Auth
         Author: podchasova11
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "350",
            'Error message is displayed when clicking the link [How-to guides] '
            'in block “Looking for more?” on the page [Trading courses] ',
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
        page_header_menu.menu_education_move_focus(d, cur_language, cur_country)
        page_header_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)

        test_el = Bug350(d, link, bid)

        # Act
        test_el.click_how_to_guides_link()

        # Assert
        if not test_el.should_be_how_to_guides_page():
            Common.pytest_fail('Bug # 55!350 Error message is displayed after clicking the link [How-to guides]')
        Common.save_current_screenshot(d, "AT_55!350 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

