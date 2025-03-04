"""
-*- coding: utf-8 -*-
@Time    : 2024/06/06 15:29
@Author  : podchasova11
"""
from datetime import datetime
import random

import pytest
import allure

from pages.BugsManual.bug_038 import WebTradingPlatformPage
from pages.BugsManual.bug_090 import CreateARiskFreeDemoAccountButton
from pages.BugsManual.bug_285 import ButtonMyAccount
from pages.BugsManual.bug_315 import Bug315
from pages.BugsManual.bug_326 import Bug326
from pages.BugsManual.bug_350 import Bug350
from pages.BugsManual.bug_363 import Bug363
from pages.BugsManual.bug_405 import Bug405
from pages.BugsManual.bug_408 import Bug408
from pages.BugsManual.bug_472 import Bug472
from pages.BugsManual.bug_594 import Bug594
from pages.Elements.PlatformOverviewButton import PlatformOverviewButton
from pages.Menu.New import from_markets_menu_open_market_analysis, from_markets_menu_open_cryptocurrencies, \
    from_about_us_menu_open_about_us, from_learn_menu_open_trading_strategies, from_trading_menu_open_mobile_apps
from pages.Menu.menu import MenuSection
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55

from pages.common import Common
from pages.conditions_v2 import apply_preconditions_to_link
from src.src import CapitalComPageSrc


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

        link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        # page_conditions = Conditions(d, "")
        # link = page_conditions.preconditions(
        #     d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PlatformOverviewButton(d, link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, link)

        print(f'\n{datetime.now()}   Assert')

        page = WebTradingPlatformPage(d, link, bid)
        if not page.should_be_web_trading_platform_page(d, link):
            Common().pytest_fail(f"Bug#038. "
                                 "Expected result:The Desktop Trading page is opened "
                                 "\n"
                                 "Actual result: The Home page is opened ")
        Common().save_current_screenshot(d, "AT_55!038 Pass")

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

        link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        # page_conditions = Conditions(d, "")
        # link = page_conditions.preconditions(
        #     d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
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

        link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        # page_conditions = NewConditions(d, "")
        # link = page_conditions.preconditions(
        #     d, CapitalComPageSrc.URL_NEW_EN_AE, "", cur_language, cur_country, cur_role, cur_login, cur_password)

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

        link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        # page_conditions = NewConditions(d, "")
        # link = page_conditions.preconditions(
        #     d, CapitalComPageSrc.URL_NEW_AR_AE, "", cur_language, cur_country, cur_role, cur_login, cur_password)

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
    @pytest.mark.parametrize('cur_country', ['de'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_326
    def test_326(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: The page "Oops, this help center no longer exists"
         is opened after clicking the link [Help Center] of the page "Contact us"
         Language: All.
         License: CYSEC.
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
        link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        # page_conditions = Conditions(d)
        # link = page_conditions.preconditions(
        #     d, CapitalComPageSrc.URL, "",
        #     cur_language, cur_country, cur_role, cur_login, cur_password
        # )

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
        'Start retest manual TC_55!350a | Error message "Oops, this help center no longer exists" '
        'is displayed when clicking the link [How-to guides] '
        'in block “Looking for more?” on the page [Trading courses]')
    @pytest.mark.parametrize('cur_language', ['de'])
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'au'], 1))
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_350a
    def test_350a(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: Error message is displayed when clicking the link [How-to guides]
         in block “Looking for more?” on the page [Trading courses]
         Language: All.
         License: CYSEC, ASIC.
         Role: NoReg | NoAuth | Auth
         Author: podchasova11
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "350a",
            'Error message "Oops, this help center no longer exists"'
            'is displayed when clicking the link [How-to guides] '
            'in block “Looking for more?” on the page [Trading courses] ',

            False,
            False
        )

        # Arrange
        link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        # page_conditions = Conditions(d)
        # link = page_conditions.preconditions(
        #     d, CapitalComPageSrc.URL, "",
        #     cur_language, cur_country, cur_role, cur_login, cur_password
        # )

        page_header_menu = MenuSection(d, link)
        page_header_menu.menu_education_move_focus(d, cur_language, cur_country)
        page_header_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)

        test_el = Bug350(d, link, bid)

        # Act
        test_el.click_how_to_guides_link()

        # Assert
        if not test_el.should_be_open_how_to_guides_page():
            Common.pytest_fail(f"#Bug # 55!350a "
                               f"\n"
                               f"Expected result: The Corresponding web page with resource  is opened"
                               f"\n"
                               f"Actual result: Error message 'Oops, this help center no longer exists' "
                               f"\n"
                               f"is displayed after clicking the link [How-to guides]")
        Common.save_current_screenshot(d, "AT_55!350a")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step(
        'Start retest manual TC_55!350b | Error message "The page you were looking for doesnt exist" '
        'is displayed when clicking the link [How-to guides] '
        'in block “Looking for more?” on the page [Trading courses]')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', (['ua']))
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_350b
    def test_350b(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: Error message "The page you were looking for doesnt exist"
         is displayed when clicking the link [How-to guides]
         in block “Looking for more?” on the page [Trading courses]
         Language: All.
         License: SCB.
         Role: NoReg | NoAuth | Auth
         Author: podchasova11
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "350b",
            'Error message "The page you were looking for doesnt exist"'
            'is displayed when clicking the link [How-to guides] '
            'in block “Looking for more?” on the page [Trading courses] ',
            False,
            False
        )

        # Arrange
        link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        # page_conditions = Conditions(d)
        # link = page_conditions.preconditions(
        #     d, CapitalComPageSrc.URL, "",
        #     cur_language, cur_country, cur_role, cur_login, cur_password
        # )

        page_header_menu = MenuSection(d, link)
        page_header_menu.menu_education_move_focus(d, cur_language, cur_country)
        page_header_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)

        test_el = Bug350(d, link, bid)

        # Act
        test_el.click_how_to_guides_link()

        # Assert
        if not test_el.should_be_open_how_to_guides_page_scb_license():
            Common.pytest_fail(f"#Bug # 55!350b "
                               f"\n"
                               f"Expected result: The Corresponding web page with resource  is opened"
                               f"\n"
                               f"Actual result: Error message 'The page you were looking for doesnt exist' "
                               f"\n"
                               f"is displayed after clicking the link [How-to guides]")

        Common.save_current_screenshot(d, "AT_55!350b")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step(
        'Start retest manual TC_55!366 | The Investmate page does not open after click link “Investmate”'
        ' in the block “Discover trading.” on the page “Why Capital.com?”')
    @pytest.mark.parametrize('cur_language', ['en'])
    @pytest.mark.parametrize('cur_country', random.sample(['de', 'ua'], 1))
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_315
    def test_315(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: The Investmate page does not open after click link “Investmate”'
        ' in the block “Discover trading.” on the page “Why Capital.com?”
         Language: ALL.
         License: CYSEC, SCB.
         Author: podchasova11
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "315",
            'The Investmate page does not open after click link “Investmate”'
            ' in the block “Discover trading.” on the page “Why Capital.com?”',
            False,
            False
        )
        # pytest.skip("315 In progress...")
        # Arrange
        Common.check_language_in_list_and_skip_if_present(cur_language, [''])

        link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role,
                                           cur_login, cur_password)

        page_header_menu = MenuSection(d, link)
        test_el = Bug315(d, link, bid)

        page_header_menu.move_focus_to_products_and_services_menu(d, cur_language, cur_country)
        test_el.click_why_capital_menu_item()

        # Act
        test_el.click_investmate_link()

        # Assert
        if not test_el.should_be_investmate_page(cur_language):
            Common.pytest_fail("Bug # 55!315 The Investment page is NOT opened")
        Common.save_current_screenshot(d, "AT_55!315 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL)

    @allure.step(
        "Start retest manual TC_55!363 | 'Honk Kong & Taiwan' not displayed up in search"
        " the dropdown [Regional settings]")
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_363
    def test_363_selected_country_not_displayed_up_in_search_the_dropdown(
            self, worker_id, d, cur_language_country_for_fca_and_sca, cur_role, cur_login, cur_password):
        """
        Check:  Click to the dropdown [Regional settings] > Click to the dropdown [Countries] >
                Click the [Search] input field > Enter value "Honk" > Check that country 'Honk Kong & Taiwan'
                displayed in search results

        Language: EN - FCA, SCA; AR - SCA
        License/Country: FCA, SCA
        Role: NoReg, NoAuth, Auth
        Author: podchasova11
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_country_for_fca_and_sca[0],
            cur_language_country_for_fca_and_sca[1], cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "363",
            "Click to the dropdown [Regional settings] > Click to the dropdown [Countries] > "
            "Click the [Search] input field > Enter value 'Honk' > Check that country 'Honk Kong & Taiwan'"
            "displayed in search results",
            False, True
        )
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language_country_for_fca_and_sca[0],
                                                    cur_language_country_for_fca_and_sca[1],
                                                    cur_role, cur_login, cur_password)

        test_element = Bug363(d, cur_item_link, bid)
        test_element.arrange(d, cur_item_link)

        # Act
        test_element.check_present_honk_kong_taiwan_locator(d)

        # Assert
        test_element.assert_(d, cur_language_country_for_fca_and_sca[0], cur_language_country_for_fca_and_sca[1])

    @allure.step("Start test of link 'Capital.com Research Team' on page 'BP share price forecast'")
    @pytest.mark.parametrize('cur_language', [""])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_405
    def test_405_link_research_team_open_on_404_error_message(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check:  Menu section [Markets] >
                Menu item [Market analysis] >
                Scroll down to the block “pagination” >
                Click the link "11"
                Click the link “BP share price forecast” >
                Сlick the link “Capital.com Research Team” >
        Language: EN
        License/Country: SCA
        Role: NoReg, NoAuth, Auth
        Author: podchasova11
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "405",
            "Menu section [Markets] > Menu item [Market analysis] >"
            "Scroll down to the block 'pagination' >"
            "Click the link '11' >"
            "Click the link 'BP share price forecast' >"
            "Сlick the header of the accordion 'How do you trade commodities?' >"
            "Сlick the link 'Capital.com Research Team' ",
            False, True
        )
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                                    cur_role, cur_login, cur_password)

        page_menu = from_markets_menu_open_market_analysis.MenuNew(d, cur_item_link)
        link = page_menu.from_markets_menu_open_market_analysis(
            d, cur_language, cur_country, cur_item_link)

        test_element = Bug405(d, link, bid)
        test_element.arrange(d, link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test of link '[ عقود الفروقات على الفضة ] (“silver CFDs”)'")
    @pytest.mark.parametrize('cur_language', ["ar"])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_408
    def test_408_link_research_silver_cfd_eng_lang(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check:  Menu section  [الأسواق ] (Learn) >
                Menu item [ استراتيجيات التداول ](Trading Strategies) >
                Scroll down to the block “Our most-read trading guides” >
                Click the link  [دليل التداول بالهامش ] (Margin trading guide) >
                Scroll down to the block “الأسئلة الشائعة” (FAQs) >
                Сlick the header of accordion “ما هو التداول بالهامش مع الشرح بمثال؟” (“What is the margin ...”) >
                Click the link [ عقود الفروقات على الفضة ] (“silver CFDs”)

        Language: AR
        License/Country: SCA
        Role: NoReg, NoAuth, Auth
        Author: podchasova11
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "408",
            "Menu section [Learn] > Menu item [Trading Strategies] >"
            "Scroll down to the block 'Our most-read trading guides' >"
            "Click the link  [دليل التداول بالهامش ] (Margin trading guide) >"
            "Scroll down to the block “الأسئلة الشائعة” (FAQs) >"
            "Сlick the header of the accordion “ما هو التداول بالهامش مع الشرح بمثال؟” (“What is the margin ...”) >"
            "Click the link [ عقود الفروقات على الفضة ] (“silver CFDs”) ",
            False, True
        )
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                                    cur_role, cur_login, cur_password)

        page_menu = from_learn_menu_open_trading_strategies.MenuNew(d, cur_item_link)
        link = page_menu.from_learn_menu_open_trading_strategies(
            d, cur_language, cur_country, cur_item_link)

        test_element = Bug408(d, link, bid)
        test_element.arrange(d, link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d)

    @allure.step(
        'Start retest manual TC_55!472 | Error message “Access denied Error 16"'
        'is displayed after clicking link '
        '[مكاتبنا الموزّعة على أربع قارات] ("Offices in four continents")'
        'in block [مكاتبنا العالمية] ("Our global offices")')
    @pytest.mark.parametrize('cur_language', ['ar'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ['Auth', 'NoAuth', 'NoReg'])
    @pytest.mark.bug_472
    def test_472(self, worker_id, d, cur_language, cur_country, cur_role,
                 cur_login, cur_password):
        """
         Check: Error message “Access denied Error 16"
         is displayed after clicking link
         [مكاتبنا الموزّعة على أربع قارات] ("Offices in four continents")
         in block [مكاتبنا العالمية] ("Our global offices")
         Language: AR.
         License: SCA.
         Author: podchasova11
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "472",
            'Error message “Access denied Error 16" '
            'is displayed after clicking link '
            '[مكاتبنا الموزّعة على أربع قارات] ("Offices in four continents")'
            'in block [مكاتبنا العالمية] ("Our global offices")',
            False,
            False
        )

        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = from_about_us_menu_open_about_us.MenuNew(d, cur_item_link)
        link = page_menu.from_about_us_menu_open_about_us(
            d, cur_language, cur_country, cur_item_link)

        test_element = Bug472(d, link, bid)
        test_element.arrange(d, link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d)

    @allure.step("Start test of link “CFD” in the block 'Capital.com mobile apps' on the page 'Mobile apps'")
    @pytest.mark.parametrize('cur_language', ['de'])
    @pytest.mark.parametrize('cur_country', ['de'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_594
    def test_594_link_research_silver_cfd_eng_lang(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check:  Menu section  [Trading] (Trading) >
                Menu item [Applications mobiles] (Mobile apps) >
                Click the link “CFD” in the block
                “Les applications mobiles de Capital.com” (Capital.com mobile apps) >

        Language: FR, IT
        License/Country: CYSEC
        Role: NoReg, NoAuth, Auth
        Author: podchasova11
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "594",
            "Menu section [Trading] > Menu item [Mobile apps] >"
            "Click the link [CFD] ",
            False, True
        )
        # Arrange
        cur_item_link = apply_preconditions_to_link(d, cur_language, cur_country,
                                                    cur_role, cur_login, cur_password)

        page_menu = from_trading_menu_open_mobile_apps.MenuNew(d, cur_item_link)
        link = page_menu.from_trading_menu_open_mobile_apps(
            d, cur_language, cur_country, cur_item_link)

        test_element = Bug594(d, link, bid)
        test_element.arrange(d, link)

        # Act
        test_element.act(d)

        # Assert
        test_element.assert_(d)