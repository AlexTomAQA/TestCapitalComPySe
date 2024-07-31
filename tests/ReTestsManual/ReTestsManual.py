import os
import time
from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.Elements.AssertClass import AssertClass
from pages.Signup_login.signup_login_locators import NewLoginFormLocators, NewSignupFormLocators
from pages.conditions import Conditions
from pages.ReTests.ReTest_table_fill import retest_table_fill

from pages.Menu.New.menu_new import MainMenu
from pages.menu_section.menu_section import MenuSections
from pages.conditions_new import NewConditions
# from pages.Elements.AssertClass import AssertClass

from pages.build_dynamic_arg import build_dynamic_arg_v4
# import io
from src.src import CapitalComPageSrc


def if_retest_passed(d, bid):
    allure.attach(
        d.get_screenshot_as_png(),
        name=f"Screenshot{datetime.now()}",
        attachment_type=AttachmentType.PNG,
    )
    retest_table_fill(d, bid, '00', "", True, True)


# @pytest.mark.FCABugs
class TestManualBugs:
    page_conditions = None

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step("Bug#01: Content of the Block ""USD/CHF"" is not loaded in the ""US Dollar / Swiss Franc"" page ")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_01
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_01(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country, cur_os):
        """
        Content of the Block ""USD/CHF"" is not loaded in the ""US Dollar / Swiss Franc"" page after clicking
        the ""USD/CHF"" trading instrument in the  ""Forex Markets"" Widget"
            1. Hover over the [Markets] menu section
            2. Click the [Forex] menu item
            3. Scroll down to the ""Forex Markets"" Widget
            4. Click USD/CHF trading instruments
            5. Scroll down to ""USD/CHF"" Block"
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_01", "Content of the Block ""USD/CHF"" is not loaded in the ""US Dollar / Swiss Franc"""
                   " page after clicking", True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_markets_forex_sub_menu(d, cur_language, cur_country, link)

        # определение количества страниц
        markets_page = MenuSections(d)
        # pagination = markets_page.elements_are_located(markets_page.MARKETS_LIST_PAGINATION)
        # qty_pages = int(pagination[-2].text)
        qty_pages = 1
        print("qty_pages=", qty_pages)

        # перебор страниц
        most_trade_instrument_list = []
        error_trade_instrument_list = []
        for i in range(qty_pages):
            print("page:", i + 1)
            most_traded_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LINK_LIST)
            for j in range(len(most_traded_list)):
                most_traded_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LINK_LIST)

                markets_page.go_to_element(most_traded_list[j])
                most_traded_instrument_name = most_traded_list[j].text
                try:
                    markets_page.element_is_clickable(most_traded_list[j]).click()
                except StaleElementReferenceException:
                    print("StaleElementReferenceException")
                    most_traded_list = markets_page.elements_are_located(
                        markets_page.MARKETS_MOST_TRADE_LINK_LIST)
                    markets_page.element_is_clickable(most_traded_list[j]).click()

                err_404 = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_INSTRUMENT_404, 1)
                if err_404:
                    error_trade_instrument_list.append(most_traded_instrument_name + ":404")
                    d.back()
                else:
                    content_list = markets_page.elements_are_located(
                        markets_page.MARKETS_MOST_TRADE_INSTRUMENT_CONTENT, 1)
                    if content_list:
                        d.back()
                    else:
                        most_trade_instrument_list.append(most_traded_instrument_name)
                        d.back()
            print("trade instrument: ", len(most_trade_instrument_list), most_trade_instrument_list)
            print("error_404: ", error_trade_instrument_list)

            pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
            if i != qty_pages - 1:
                pagination[-1].click()
            time.sleep(1)
        if len(most_trade_instrument_list) > 0:
            # проверка бага для ретеста
            print(f'\nBug: {bid}')
            retest_table_fill(d, bid, '01', "", True, True)
            #
            assert False, (f"Bug#01. Expected Result: Content of the Block is displayed. \n"
                           f"Actual Result: Content of the Block is not displayed. \n"
                           f"error_404: {error_trade_instrument_list}. \n"
                           f"trade instrument: {len(most_trade_instrument_list)} {most_trade_instrument_list}\n"
                           f"qty_pages: {qty_pages}")

        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#02:  "Sell"/"Buy" in the Widget "Trading instrument is not clickable')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_02
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_02(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Page of the corresponding trading instrument is opened  after clicking [numeric values] in the
        column "Sell"/"Buy" in the Widget "Trading instrument"
        1. Hover over the [Markets] menu section
        2. Click the [Forex] menu item
        3. Scroll down to the Widget "Trading instrument"
        4. Click the  button [numeric values] in column "Sell"/"Buy"
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_02", 'Sell"/"Buy" in the Widget "Trading instrument is not clickable', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_markets_forex_sub_menu(d, cur_language, cur_country, link)

        # определение количества страниц
        markets_page = MenuSections(d)
        # pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
        # qty_pages = int(pagination[-2].text)
        qty_pages = 1
        print("qty_pages=", qty_pages)

        # перебор страниц
        for i in range(qty_pages):
            print("page:", i + 1)
            most_traded_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LIST)
            most_traded_link_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LINK_LIST)
            # проверяем, что ссылки для полей sell/buy существуют
            if len(most_traded_list) == len(most_traded_link_list):
                retest_table_fill(d, bid, '02', "", True, True)
                assert False, (
                    "Bug#02. Expected Result: Sign up form is opened/ unregistered Login form is opened/ unauthorized "
                    "Transition to the trading platform / authorized.\n"
                    "Actual Result: Page of the corresponding trading instrument is opened ")

            pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
            if i != qty_pages - 1:
                pagination[-1].click()
            time.sleep(1)

        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#04:  Block "Key Stats" is not displayed to the right of the Block "Trading Condition"')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_04
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_04(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Block "Key Stats" is not displayed to the right of the Block "Trading Condition" after clicking any
        trading instrument in the Widget "Indices Markets""Buy"
        1. Hover over the [Markets] menu section
        2. Click the [Indices] menu item
        3. Scroll down to the Widget "Indices Markets"
        4. Click any trading instrument
        5. Scroll to Block "Trading Condition"
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_04", 'Block "Key Stats" is not displayed to the right of the Block "Trading Condition"',
            True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_markets_indices_sub_menu(d, cur_language, cur_country, link)

        # определение количества страниц
        markets_page = MenuSections(d)
        # pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
        # qty_pages = int(pagination[-2].text)
        qty_pages = 1
        print("qty_pages=", qty_pages)

        # перебор страниц
        for i in range(qty_pages):
            print("page:", i + 1)
            most_traded_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LINK_LIST)
            for j in range(len(most_traded_list)):
                most_traded_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LINK_LIST)

                markets_page.go_to_element(most_traded_list[j])
                try:
                    markets_page.element_is_clickable(most_traded_list[j]).click()
                except StaleElementReferenceException:
                    print("StaleElementReferenceException")
                    most_traded_list = markets_page.elements_are_located(
                        markets_page.MARKETS_MOST_TRADE_LINK_LIST)
                    markets_page.element_is_clickable(most_traded_list[j]).click()

                key_stat_list = markets_page.elements_are_present(*markets_page.MARKETS_MOST_TRADE_INSTRUMENT_KEY_STATS)
                if not len(key_stat_list) == 2:
                    retest_table_fill(d, bid, '04', "", True, True)
                    assert False, ('Bug#04. '
                                   'Expected result: Block "Key Stats" is displayed to the right of '
                                   'the Block "Trading Condition"'
                                   '\n'
                                   'Actual result: Block "Key Stats" is not displayed ')
                d.back()
            pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
            if i != qty_pages - 1:
                pagination[-1].click()
            time.sleep(1)

        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#05:  Page "Discover the benefits of going Pro with capital.com" '
                 'is opened')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_05
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_05(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Page "Discover the benefits of going Pro with capital.com"  is opened after clicking the [I am eligible] button
        1. Hover over the [Ways to trade] menu section
        2. Click the [Professional]menu item
        3. Click the [I am eligible] button
        4. Click the "Back" button
        5. Hover over the [Ways to trade] menu section
        6. Click the [Professional] menu item
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_05", 'Page "Discover the benefits of going Pro with capital.com" is opened',
            True, True)

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_waytotrade_professional_sub_menu(d, cur_language, cur_country, link)
        menu_section = MenuSections(d, link)
        menu_section.element_is_clickable(menu_section.WAYSTOTRADE_PROFESSIONAL_ELIGIBLE_BTN).click()
        d.back()
        menu.open_waytotrade_professional_sub_menu(d, cur_language, cur_country, link)
        apply_btn = menu_section.elements_are_located(menu_section.WAYSTOTRADE_PROFESSIONAL_APPLY_BTN, 1)

        if not len(apply_btn) == 0:
            retest_table_fill(d, bid, '05', "", True, True)
            assert False, ('Bug#05. '
                           'Expected result: "Professional" page is opened'
                           '\n'
                           'Actual result: Page "Discover the benefits of going Pro with capital.com" '
                           'is opened ')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoAuth", "NoReg"])
    @allure.step('Bug#06:  The Sign Up/Login form is not opened after clicking button [Apply] in '
                 'the block "Discover the benefits')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_06
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_06(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        The Sign Up/Login form is not opened after clicking button [Apply] in the block "Discover the benefits..."
        on the "Professional" page
        1. Hover over the [Ways to trade] menu section
        2. Click the [Professional]menu item
        3. Click the [I am eligible] button
        steps
        1. Click the [Professional] menu item
        2. Go to block "Discover the benefits..."
        3. Click the button [Apply]
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_06", 'The Sign Up/Login form is not opened after clicking button [Apply] '
                   'in the block "Discover the benefits', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        cur_item_link = menu.open_waytotrade_professional_sub_menu(d, cur_language, cur_country, link)
        menu_section = MenuSections(d, link)
        menu_section.element_is_present_and_visible(menu_section.WAYSTOTRADE_PROFESSIONAL_ELIGIBLE_BTN).click()
        menu_section.element_is_clickable(menu_section.WAYSTOTRADE_PROFESSIONAL_APPLY_BTN, 1).click()

        test_element = AssertClass(d, cur_item_link)
        try:
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                # case "Auth":
                #     test_element.assert_trading_platform_v4(d, cur_item_link)
        except AssertionError:
            retest_table_fill(d, bid, '06', "", True, True)
            print(f"\n{datetime.now()}   Bug#06")
            assert False, ('Bug#06. Expected result: The Sign Up/Login form is opened'
                           '\n'
                           'Actual result: The trading platform page is opened')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @allure.step('Bug#07:  The trading platform page is not opened after clicking button [Apply] in '
                 'the block "Discover the benefits')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_07
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_07(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        The trading platform page is not opened after clicking button [Apply] in the block "Discover the benefits..."
        on the "Professional" page
        1. Hover over the [Ways to trade] menu section
        2. Click the [Professional]menu item
        3. Click the [I am eligible] button
        steps
        1. Click the [Professional] menu item
        2. Go to block "Discover the benefits..."
        3. Click the button [Apply]
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_07", 'The trading platform page is not opened after clicking button [Apply] '
                   'in the block "Discover the benefits', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        cur_item_link = menu.open_waytotrade_professional_sub_menu(d, cur_language, cur_country, link)
        menu_section = MenuSections(d, link)
        menu_section.element_is_present_and_visible(menu_section.WAYSTOTRADE_PROFESSIONAL_ELIGIBLE_BTN).click()
        menu_section.element_is_clickable(menu_section.WAYSTOTRADE_PROFESSIONAL_APPLY_BTN, 1).click()

        test_element = AssertClass(d, cur_item_link)
        try:
            match cur_role:
                # case "NoReg":
                #     test_element.assert_signup(d, cur_language, cur_item_link)
                # case "NoAuth":
                #     test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(d, cur_item_link)
        except AssertionError:
            print(f"\n{datetime.now()}   Bug#07")
            retest_table_fill(d, bid, '07', "", True, True)
            assert False, ('Bug#07. Expected result: The trading platform page is opened'
                           '\n'
                           'Actual result: The trading platform page is not opened')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @allure.step('Bug#08:  Sidebar "My account" is not displayed when clicking on the [My account] button '
                 ' in the Header ')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_08
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_08(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Sidebar "My account" is not displayed when clicking on the [My account] button  in the Header
        1. Navigate to Capital.com
        2. Selected the FCA license
        3. Selected EN language

        1. Click Button [My account]
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_08", 'Sidebar "My account" is not displayed when clicking on the [My account] button  '
                   'in the Header', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)

        if menu.element_is_visible(menu.HEADER_LOGIN_BTN):
            assert False, 'Bug#08. Interruption of authorization'

        account_btn = menu.element_is_visible(menu.MENU_ACCOUNT)
        account_btn.click()
        account_btn_link = d.current_url
        if account_btn_link == "https://capital.com/trading/platform":
            retest_table_fill(d, bid, '08', "", True, True)
            assert False, \
                ('Bug#08. '
                 'Expected result: Sidebar "My account" is displayed'
                 '\n'
                 'Actual result: The trading platform page is opened')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#09:  Bread crumbs are not displayed in the "Professional" page')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_09
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_09(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Bread crumbs are not displayed in the "Professional" page
        1. Hover over the [Ways to trade] menu section
        2. Click the [Professional]menu item
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_09", 'Bread crumbs are not displayed in the "Professional" page', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_waytotrade_professional_sub_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)
        bred_crumbs = menu.elements_are_located(sub_menu.BREADCRUMBS)
        if not bred_crumbs:
            retest_table_fill(d, bid, '09', "", True, True)
            assert False, ('Bug#09. Expected Result: Bread crumbs are displayed'
                           '\n'
                           'Actual Result: Bread crumbs are  not displayed')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#10:  Link "Apply here" is not clickable in the "No Capital.com account yet?"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.test_10
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_10(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Link "Apply here" is not clickable in the "No Capital.com account yet?" in the block "Apply
        now" in the menu item "Professional"
        1. Hover over the menu section "Ways to trade"
        2. Click the menu item "Professional"
        3. Click the [I am eligible] button
        4. Scroll down to the block "Apply now"
        5. Click the link "Apply here" in the "No Capital.com account yet?"

        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_10", 'Link "Apply here" is not clickable in the "No Capital.com account yet?"', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_waytotrade_professional_sub_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)
        sub_menu.element_is_present_and_visible(sub_menu.WAYSTOTRADE_PROFESSIONAL_ELIGIBLE_BTN).click()
        link1 = d.current_url
        if len(sub_menu.elements_are_present(*sub_menu.WAYSTOTRADE_PROFESSIONAL_NO_CAPITAL_YET_APPLY_BTN)) == 0:
            pytest.skip("Bug#11: Web-element is not present")

        sub_menu.element_is_clickable(sub_menu.WAYSTOTRADE_PROFESSIONAL_NO_CAPITAL_YET_APPLY_BTN).click()
        link2 = d.current_url
        if link2 == link1:
            retest_table_fill(d, bid, '10', "", True, True)
            assert False, ('Bug#10. Expected Result: Link "Apply here" is clickable'
                           '\n'
                           'Actual Result: Link "Apply here" is not clickable')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoAuth"])
    @allure.step('Bug#11:  Transition to the trading platform after clicking the [Apply here] link in '
                 'the "Apply now" Block')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_11
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_11(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Transition to the trading platform after clicking the [Apply here] link in the "Apply now" Block
        1. Hover over the [Ways to trade] menu section
        2. Click the [Professional] menu item
        3. Click the [I am eligible] button
        4. Scroll down to "Apply now" Block
        5. Click the [Apply here] link next to the text "Existing client?"
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_11", 'Transition to the trading platform after clicking the [Apply here] link in '
                   'the "Apply now" Block', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_waytotrade_professional_sub_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)
        sub_menu.element_is_present_and_visible(sub_menu.WAYSTOTRADE_PROFESSIONAL_ELIGIBLE_BTN).click()

        if len(sub_menu.elements_are_present(*sub_menu.WAYSTOTRADE_PROFESSIONAL_EXISTING_CLIENT_BTN)) == 0:
            pytest.skip("Bug#11: Web-element is not present")

        sub_menu.element_is_clickable(sub_menu.WAYSTOTRADE_PROFESSIONAL_EXISTING_CLIENT_BTN).click()
        cur_item_link = d.current_url
        test_element = AssertClass(d, cur_item_link)
        try:
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(d, cur_item_link)
        except AssertionError:
            print(f"\n{datetime.now()}   Bug#11")
            retest_table_fill(d, bid, '11', "", True, True)
            assert False, ('Bug#11. Expected result: Login form is opened'
                           '\n'
                           'Actual result: Transition to the trading platform')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#12:  The button [Open an account] is not named according to block "We’re here to help"')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_12
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_12(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        The button [Open an account] is not named according to block "We’re here to help" on
        the "Trading platforms" page
        1. Click the "Trading platforms" menu section
        2. Scroll down to block "We’re here to help"
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_12", 'The button [Open an account] is not named according to block "We’re here to help"', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_trading_platform_menu(d, cur_language, cur_country, link)

        sub_menu = MenuSections(d, link)
        support_button = sub_menu.element_is_present_and_visible(sub_menu.TRADING_PLATFORM_SUPPORT_BTN).text
        print(f"\n{datetime.now()}   Bug#12. The button [Open an account] is not named according to block "
              f"'We’re here to help'")
        if support_button == "Open an account":
            retest_table_fill(d, bid, '12', "", True, True)
            assert support_button != "Open an account", (
                'Bug#12. Expected result: The button [Open an account] is named '
                'according to block "We’re here to help"'
                '\n'
                'Actual result: The button [Open an account] is not named '
                'according to block "We’re here to help"')

        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step(
        'Bug#13:  Transition not to the top of the page in the page "Discover the benefits of going Pro with '
        '"Capital.com" after clicking the [I am eligible] button')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_13
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_13(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Transition not to the top of the page in the page "Discover the benefits of going Pro with "Capital.com"
        after clicking the [I am eligible] button
        1. Hover over the [Ways to trade] menu section
        2. Click the [Professional] menu item
        3. Click the [I am eligible] button
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_13", 'Transition not to the top of the page in the page "Discover the benefits of '
                   'going Pro with "Capital.com" after clicking the [I am eligible] button', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_waytotrade_professional_sub_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)
        sub_menu.element_is_present_and_visible(sub_menu.WAYSTOTRADE_PROFESSIONAL_ELIGIBLE_BTN).click()

        scroll_y = d.execute_script("return window.scrollY;")
        if scroll_y != 0:
            retest_table_fill(d, bid, '13', "", True, True)
            assert False, ('Bug#13. Expected result: Transition to the top of the page'
                           '\n'
                           'Actual result: Transition not to the top of the page ')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#14:  Bread crumbs are not displayed in the "Margin-calls" page')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_14
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_14(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Bread crumbs are not displayed in the "Margin-calls" page
        1. Hover over the [Ways to trade] menu section
        2. Click the [Margin Calls] menu tittle
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_14", 'Bread crumbs are not displayed in the "Margin-calls" page', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu_list = menu.elements_are_located(menu.MENU_LIST)
        link_list = []
        for i in range(len(menu_list)):

            sub_menu_locator = (
                By.CSS_SELECTOR, f'.menuGroup_item__jQrol:nth-child({i + 1}) '
                                 f'.menuGroup_dropdown__75ey5 div a')

            sub_menu_list = menu.elements_are_located(sub_menu_locator)

            for j in range(len(sub_menu_list)):
                menu_list = menu.elements_are_located(menu.MENU_LIST)
                sub_menu_list = menu.elements_are_located(sub_menu_locator)
                time.sleep(1)
                menu.open_menu_sub_menu(d, cur_language, menu_list[i], sub_menu_list[j])
                link = d.current_url
                menu_section = MenuSections(d, link)
                bred_crumbs = menu.elements_are_located(menu_section.BREADCRUMBS, 1)
                if not bred_crumbs:
                    link_list.append(link)
                    print("No breadcrumbs:", link)
                time.sleep(1)
        if len(link_list) > 0:
            retest_table_fill(d, bid, '14', "", True, True)
            assert False, ('Bug#14. Expected Result: Bread crumbs are displayed'
                           '\n'
                           'Actual Result: Bread crumbs are  not displayed \n'
                           f'No breadcrumbs: {len(link_list)} {link_list}')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#15:  Scrollbar thumb blended into the dark background in the Scrollbar '
                 'in the Dropdown [Languages]')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_15
    @pytest.mark.skip(reason="Non-functional bug")
    def test_15(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Scrollbar thumb blended into the dark background in the Scrollbar in the Dropdown [Languages] in the Main page
        1. Hover over the  Dropdown[Country&Languages]
        2. Click the arrow Dropdown [Country]
        3. Choose any country
        4. Click the arrow Dropdown [Languages]
        """

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_15", 'Scrollbar thumb blended into the dark background in the Scrollbar '
                   'in the Dropdown [Languages]', True, True)
        #

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#16:  Format of the text content does not correspond to the Block size '
                 'in the Dropdown [Languages]')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_16
    @pytest.mark.skip(reason="Non-functional bug")
    def test_16(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Format of the text content does not correspond to the Block size  "Why to bet on spread betting with
        Capital.com? in the "Spread betting" page
        1. Hover over the [Ways to trade] menu section
        2. Click the [Spread betting] menu item
        3. Scroll down to  Block"Why spread bet with Capital.com?"
        """

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_16", 'Format of the text content does not correspond to the Block size '
                   'in the Dropdown [Languages]', True, True)
        #

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#17:  After the transition from the website capital.com into the trading platform and back is '
                 'displayed [Log in] and [Sign up] buttons instead of the [My account] buttons')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.test_17
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_17(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        After the transition from the website capital.com into the trading platform and back is displayed
        [Log in] and [Sign up] buttons instead of the [My account] buttons when clicking the [Capital.com]
        Logo on the trading platform
        1. Click the [Log in] button
        2. Enter valid value in the Email and password fields
        3. Click the Capital.com [Logo]
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_17", 'After the transition from the website capital.com into the trading platform and '
                   'back is displayed[Log in] and [Sign up] buttons instead of the [My account] buttons', True, True)
        #
        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        page_conditions.to_do_authorisation(d, link, cur_login, cur_password, cur_role)
        menu.element_is_clickable(menu.MENU_ACCOUNT).click()
        menu.element_is_present_and_visible(menu.TP_LOGO).click()
        new_tab = d.window_handles[1]
        d.switch_to.window(new_tab)

        if not menu.element_is_visible(menu.HEADER_ACCOUNT_BTN_OLD):
            retest_table_fill(d, bid, '17', "", True, True)
            assert False, ('Bug#17.'
                           'Expected result: [My account] button is displayed'
                           '\n'
                           'Actual result: [Log in] and [Sign up] buttons '
                           'are displayed')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @allure.step('Bug#18:  Sign up form is opened after re-clicking the [Try demo] button and "Back" button in'
                 ' the "Shares Trading" Block in the "Shares" page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.test_18
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_18(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Sign up form is opened after re-clicking the [Try demo] button and "Back" button in the "Shares Trading"
        Block in the "Shares" page
        1. Hover over the [Markets] menu section
        2. Click the [Shares] menu item
        3. Scroll down to Block "Shares Trading"
        4. Click the [Try demo] button
        5. Click the "Back" button
        6. Click the [Try demo] button
        7. Click the "Back" button
        8. Click the [Try demo] button
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_18", 'Sign up form is opened after re-clicking the [Try demo] button and "Back" button in '
                   'the "Shares Trading" Block in the "Shares" page', True, True)
        #
        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #

        menu = MainMenu(d, link)
        menu.open_markets_shares_sub_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)
        try:
            for i in range(5):
                sub_menu.element_is_present_and_visible(sub_menu.MARKETS_SHARES_BANNER_TRY_DEMO_BTN)
                sub_menu.element_is_clickable(sub_menu.MARKETS_SHARES_BANNER_TRY_DEMO_BTN).click()
                time.sleep(1)
                d.back()
        except TimeoutException:
            retest_table_fill(d, bid, '18', "", True, True)
            assert False, (
                'Bug#18. Expected result: Transition to the trading platform'
                '\n'
                'Actual result: Sign up form is opened')

        cur_url = d.current_url
        print(f"\n{datetime.now()}   Bug#11")
        if cur_url == "https://capital.com/trading/platform/":
            retest_table_fill(d, bid, '18', "", True, True)
            assert False, (
                'Bug#18. Expected result: Transition to the trading platform'
                '\n'
                'Actual result: Sign up form is opened')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step(
        'Bug#19:  On click the link [Learn more about us] is not scrolled to the corresponding '
        'block "Learn more about us"  in the page "Client Funds"')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_19
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_19(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        On click the link [Learn more about us] is not scrolled to the corresponding block "Learn more about us"
        in the page "Client Funds"
        1. Navigate to capital.com
        2. Select language EN
        3. Hover over menu section [Why Capital.com?] in the "Header menu"
        4. Click menu item [Client Funds]
        5. Scroll to the block "Content"
        6. Click link [Learn more about us]
                """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_19", 'On click the link [Learn more about us] is not scrolled to the corresponding '
                   'block "Learn more about us"  in the page "Client Funds"', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_way_capital_client_funds_sub_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)
        content_list = sub_menu.elements_are_located(sub_menu.WHY_CAPITAL_CLIENT_FUNDS_CONTENTS_LIST)
        content_list[5].click()
        scroll_y = d.execute_script("return window.scrollY;")
        if scroll_y < 100:
            retest_table_fill(d, bid, '19', "", True, True)
            assert scroll_y > 100, ('Bug#19. Expected result: The page "Client founds" block" is scrolled to '
                                    'the corresponding block "Learn more about us"'
                                    '\n'
                                    'Actual result: The page "Client founds" block" is not scrolled to'
                                    ' the corresponding block "Learn more about us"')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#20:  Displays interruptions between transitions to other menu sections in the Header after'
                 ' hovering over other menu section'
                 'in the Dropdown [Languages]')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_20
    @pytest.mark.skip(reason="Non-functional bug")
    def test_20(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Displays interruptions between transitions to other menu sections in the Header
        after hovering over other menu section
        1. Click the [Markets] menu section
        2. Hover over different menu sections
        """

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_20", 'Displays interruptions between transitions to other menu sections in the Header '
                   'after hovering over other menu section', True, True)
        #

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step(
        'Bug#21: In the Footer on click link [Cookie settings] is not open modal window')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_21
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_21(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        In the Footer on click link [Cookie settings] is not open modal window
        1. Navigate to capital.com
        2. Select language EN
        3. Scroll to the Footer
        4. Click link [Cookie settings]
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_21", 'In the Footer on click link [Cookie settings] is not open modal window ', True, True)
        #
        page_conditions = NewConditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #
        menu = MainMenu(d)
        menu.element_is_present_and_visible(menu.COOKIE_SETTING).click()
        try:
            menu.elements_are_visible(menu.COOKIES_FRAME)
        except TimeoutException:
            retest_table_fill(d, bid, '21', "", True, True)
            assert False, (
                'Bug#21. The modal window with cookie settings is opened '
                '\n'
                'Actual result: The modal window with cookie settings is not opened ')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step(
        'Bug#22: In the Header the button [Search] is missing')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_22
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_22(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        In the Header the button [Search] is missing
        1. Navigate to capital.com
        2. Select language EN
        3. Scroll to the Header
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_22", 'In the Header the button [Search] is missing ', True, True)
        #
        page_conditions = NewConditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #
        menu = MainMenu(d)
        menu.element_is_present(*menu.HEADER_SEARCH)

        if len(menu.elements_are_present(*menu.HEADER_SEARCH)) == 0:
            retest_table_fill(d, bid, '19', "", True, True)
            assert False, (
                'Bug#22. In the Header the button [Search] is existing  '
                '\n'
                'Actual result: In the Header the button [Search] is missing ')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#23:  [Play] element in the center of the video does not disappear after playing the video')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_23
    @pytest.mark.skip(reason="Non-functional bug")
    def test_23(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        [Play] element in the center of the video does not disappear after playing the video in the Block
         "What are indices?" in the "What is indices trading" page
        1. Hover over the [Markets] menu section
        2. Click the [Indices] menu item
        3. Scroll down to the Block "Why trade indices with Capital.com?"
        4. Click the [Learn more about how to trade indices] link
        5. Scroll down to Block "What are indices?"
        6. Click the play video
        """

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_23", '[Play] element in the center of the video does not disappear after playing the video', True, True)
        #

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @allure.step('Bug#24:  Authorized user is logged out after changing the license to FCA(EN language)')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.test_24
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_24(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Authorized user is logged out after changing the license to FCA(EN language)
        1. Click [Log In] button
        2. Enter email and password
        3. Return to the site
        4. Change license to FCA
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_24", 'Authorized user is logged out after changing the license to FCA(EN language)', True, True)
        #
        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #
        menu = MainMenu(d, link)
        try:
            menu.element_is_visible(menu.HEADER_LOGIN_BTN)
        except TimeoutException:
            retest_table_fill(d, bid, '24', "", True, True)
            assert False, (
                'Bug#24. Expected result: User is autothorized'
                '\n'
                'Actual result: User is logged out')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step(
        'Bug#25: In the Footer the arrow button [Up] is missing')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_25
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_25(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        In the Footer the arrow button [Up] is missing
        1. Navigate to capital.com
        2. Select language EN
        3. Scroll to the Footer
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_25", 'In the Footer the arrow button [Up] is missing', True, True)
        #
        page_conditions = NewConditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #

        menu = MainMenu(d)
        menu.element_is_present_and_visible(menu.COOKIE_SETTING)
        if len(menu.elements_are_present(*menu.SCROLL_TO_TOP)) == 0:
            retest_table_fill(d, bid, '25', "", True, True)
            assert menu.element_is_present(*menu.SCROLL_TO_TOP), (
                'Bug#25. In the Footer the arrow button [Up] is existing '
                '\n'
                'Actual result: In the Footer the arrow button [Up] is missing')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoAuth"])
    @allure.step('Bug#26:  The Facebook icon is not clickable in the Signup/Login form ')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.test_26
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_26(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        The Facebook icon is not clickable in the Signup/Login form after reopening the Login/Signup form and
        clicking the Facebook icon when selecting FCA license and EN language
        1. Click the Button [Log in] on the Header
        2. Click the Facebook icon
        3. Close the Facebook modal window
        4. Close the Login form
        5. Click the [Login] or [Signup] button
        6. Click the Facebook icon
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_26", 'The Facebook icon is not clickable in the Signup/Login form ', True, True)
        #
        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #
        menu = MainMenu(d, link)
        menu.element_is_clickable(menu.HEADER_LOGIN_BTN).click()
        menu.element_is_clickable(NewLoginFormLocators().FACEBOOK_BTN).click()
        menu.element_is_clickable(NewLoginFormLocators().BUTTON_CLOSE_ON_LOGIN_FORM).click()
        # number_of_tabs = len(d.window_handles)
        new_tab = d.window_handles[1]
        d.switch_to.window(new_tab)
        d.close()
        core_tab = d.window_handles[0]
        d.switch_to.window(core_tab)

        #
        menu.element_is_clickable(menu.HEADER_LOGIN_BTN).click()
        menu.element_is_clickable(NewLoginFormLocators().FACEBOOK_BTN).click()
        number_of_tabs = len(d.window_handles)
        if number_of_tabs < 2:
            retest_table_fill(d, bid, '26', "", True, True)
            assert number_of_tabs > 1, (
                'Bug#26. The  Facebook icon is clickable and opens a pop up with login via Facebook '
                '\n'
                'Actual result: The Facebook icon is not clickable')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step(
        'Bug#27: The modal window translated into the browser language, not in English, '
        'opens after clicking Link [Cookies Settings] in the footer and selecting FCA license')
    @allure.severity(allure.severity_level.TRIVIAL)
    @pytest.mark.test_27
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_27(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        The modal window translated into the browser language, not in English, opens after clicking
        Link [Cookies Settings] in the footer and selecting FCA license
        1. Scroll to the footer
        2. Click  Link [Cookies Settings]
        3. Pay attention to the language of the modal window that opens
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_27", 'The modal window translated into the browser language, not in English,'
                   ' opens after clicking Link [Cookies Settings] in the footer and selecting FCA license', True, True)
        #
        page_conditions = NewConditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #

        menu = MainMenu(d)
        menu.element_is_present_and_visible(menu.COOKIE_SETTING).click()
        title = menu.element_is_visible(menu.COOKIE_SETTING_TITLE).text

        if title != 'Privacy Preference Center':
            retest_table_fill(d, bid, '27', "", True, True)
            assert title == 'Privacy Preference Center', (
                'Bug#27. Тhe modal window translated into English'
                '\n'
                'Actual result: Тhe modal window translated into browser language')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step(
        'Bug#28:  Block name "Apply now" is missing in the menu item "Professional" '
        'in the menu section "Ways to trade"')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_28
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_28(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Block name "Apply now" is missing in the menu item "Professional" in the menu section "Ways to trade"
        1. Hover over the menu section "Ways to trade"
        2. Click menu item "Professional"
        3. Scroll down to the block "Apply now"
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_28", 'Block name "Apply now" is missing in the menu item "Professional" '
                   'in the menu section "Ways to trade"', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_waytotrade_professional_sub_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)
        sub_menu.element_is_present_and_visible(sub_menu.WAYSTOTRADE_PROFESSIONAL_ELIGIBLE_BTN).click()
        if len(sub_menu.elements_are_present(*sub_menu.WAYSTOTRADE_PROFESSIONAL_NO_CAPITAL_YET_APPLY_BTN)) == 0:
            pytest.skip("Bug#28: Web-element is not present")

        sub_menu.element_is_present_and_visible(sub_menu.WAYSTOTRADE_PROFESSIONAL_NO_CAPITAL_YET_APPLY_BTN)

        if len(sub_menu.elements_are_present(*sub_menu.WAYSTOTRADE_PROFESSIONAL_APPLY_NOW_TITLE)) == 0:
            retest_table_fill(d, bid, '28', "", True, True)
            assert False, \
                ('Bug#28. Expected result:  Block name "Apply now" is displayed '
                 '\n'
                 'Actual result: Block name "Apply now" is missing ')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step(
        'Bug#29: Button [Try now] is missing in the block " Why choose Capital.com? ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_29
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_29(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Button [Try now] is missing in the block " Why choose Capital.com? Our numbers speak for
        themselves" in menu item "Web platform"/"Mobile apps" in menu section "Trading platforms"
        when choosing Eng for FCA license
        1. Hover over the menu section "Trading platforms"
        2. Click menu item "Web platform"/"Mobile apps"
        3. Scroll page down to the block " Why choose Capital.com? Our numbers speak for themselves"
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_29", 'Button [Try now] is missing in the block " Why choose Capital.com?', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_trading_platform_web_platform_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)
        sub_menu.element_is_present_and_visible(sub_menu.TRADING_PLATFORM_WEB_PLATFORM_WHY_CAPITAL_BLOCK)

        if len(sub_menu.elements_are_present(*sub_menu.TRADING_PLATFORM_WEB_PLATFORM_WHY_CAPITAL_BTN)) == 0:
            retest_table_fill(d, bid, '29', "", True, True)
            assert sub_menu.element_is_present(*sub_menu.TRADING_PLATFORM_WEB_PLATFORM_WHY_CAPITAL_BTN), \
                ('Bug#29. Expected result:  Button [Try now] is displayed'
                 '\n'
                 'Actual result: Button [Try now] is missing')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step(
        'Bug#30: There is no link to the FCA license in the footer of the site '
        'in the of the registration number 793714')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_30
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_30(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        There is no link to the FCA license in the footer of the site in the of the registration number 793714
        1. Scroll down to the footer
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_30", 'Button [Try now] is missing in the block " Why choose Capital.com?', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.element_is_present_and_visible(menu.FOOTER_RISK_WARNING_BLOCK)
        link = menu.elements_are_present(*menu.FOOTER_RISK_WARNING_BLOCK_LINK)

        if len(link) < 2:
            retest_table_fill(d, bid, '30', "", True, True)
            assert len(link) > 1, \
                ('Bug#30. Expected result:  Link to the license is displayed'
                 '\n'
                 'Actual result: Link to the license is not displayed')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step(
        'Bug#31: Links [Learn to trade] in the blocks "Starting from the beginning?" and '
        '"Looking to sharpen your strategies?" in the menu item [Learn to trade] don`t scroll '
        'to the  corresponding block on the page')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_31
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_31(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Links [Learn to trade] in the blocks "Starting from the beginning?" and "Looking to sharpen your strategies?"
        in the menu item [Learn to trade] don`t scroll to the  corresponding block on the page
        1. Hover over and click the menu section [Learn to trade]
        2. Scroll page down to the block "Starting from the beginning?" or "Looking to sharpen your strategies?"
        3. Click Link [Learn to trade]

        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_31", 'Links [Learn to trade] in the blocks "Starting from the beginning?" and '
                   '"Looking to sharpen your strategies?" in the menu item [Learn to trade] don`t scroll to the '
                   ' corresponding block on the page', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_learn_to_trade_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)
        link_list = sub_menu.elements_are_located(sub_menu.LEARN_TO_TRADE_BLOCK_LINK_LIST)
        sub_menu.go_to_element(link_list[0])
        scroll_0 = d.execute_script("return window.scrollY;")
        link_list[0].click()
        time.sleep(1)
        scroll_1 = d.execute_script("return window.scrollY;")
        sub_menu.go_to_element(link_list[1])
        link_list[1].click()
        time.sleep(1)
        scroll_2 = d.execute_script("return window.scrollY;")

        if not scroll_0 < scroll_1 < scroll_2:
            retest_table_fill(d, bid, '31', "", True, True)
            assert False, \
                ('Bug#31. Expected result:  The page  scrolls to the block "Trading beginners" '
                 '(from  block "Starting from the beginning?") or to the block "Experienced traders" '
                 '(from block "Looking to sharpen your strategies?")'
                 '\n'
                 'Actual result: The page doesn`t scroll to the block "Trading beginners" '
                 '(from  block "Starting from the beginning?") or to the block "Experienced traders" '
                 '(from block "Looking to sharpen your strategies?")')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @allure.step(
        'Bug#33: 429 status code (Too many requests) is displayed on the main page after sending several '
        'identical requests')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_33
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_33(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        429 status code (Too many requests) is displayed on the main page after sending several identical requests
        1. Click the [Sign up] button
        2. Click the "Back" button
        3. Click the [Sign up] button
        4. Click the "Back" button
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_33", '429 status code (Too many requests) is displayed on the main page after sending '
                   'several identical requests', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        sub_menu = MenuSections(d, link)
        try:
            for i in range(5):
                sub_menu.element_is_present_and_visible(sub_menu.MAIN_PAGE_SIGNUP_BTN).click()
                print(i, "back")
                d.back()
        except TimeoutException:
            retest_table_fill(d, bid, '33', "", True, True)
            assert True, \
                ('Bug#33. Expected result:  Main page is opened'
                 '\n'
                 'Actual result: 429 status code (Too many requests)')

        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step(
        'Bug#34:  Filtered list of cookies is not displayed according to the checked and unchecked checkboxes ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_34
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_34(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Filtered list of cookies is displayed according to the checked and unchecked checkboxes in the Drop-down menu
        in the Modal window after clicking the[Clear Filters] and [Apply] buttons
        1. Click the [Filters] button
        2. Selected checkboxs on "Perfomances Cookie", "Functional Cookies" and "Targeting Cookies"
        3. Click the [Apply] button
        4. Click the [Filter] button
        5. Selected a checkbox on "Perfomances Cookie"
        6. Click the [Apply] button
        7. Click the [Filters] button
        8. Click the [Clear filters] button
        9. Click the [Apply] button
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_34", 'Filtered list of cookies is not displayed according to the checked and unchecked '
                   'checkboxes', True, True)
        #
        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #
        menu = MainMenu(d, link)
        menu.element_is_present_and_visible(menu.COOKIE_SETTING).click()
        menu.element_is_present_and_visible(menu.STRICTLY_NECESSARY_COOKIES).click()
        menu.element_is_present_and_visible(menu.COOKIES_DETAILS_1).click()
        filter_list0 = len(menu.elements_are_located(menu.COOKIES_lIST_1))

        menu.element_is_clickable(menu.COOKIE_FILTER).click()
        menu.element_is_clickable(menu.COOKIE_FILTER_CHBOX2).click()
        menu.element_is_clickable(menu.COOKIE_FILTER_CHBOX3).click()
        menu.element_is_clickable(menu.COOKIE_FILTER_CHBOX4).click()
        menu.element_is_clickable(menu.COOKIE_FILTER_APPLY).click()

        filter_list1 = len(menu.elements_are_located(menu.COOKIES_lIST_1))
        #
        menu.element_is_clickable(menu.COOKIE_FILTER).click()
        menu.element_is_clickable(menu.COOKIE_CLEAR_FILTER).click()
        menu.element_is_clickable(menu.COOKIE_FILTER_APPLY).click()
        filter_list2 = len(menu.elements_are_located(menu.COOKIES_lIST_1))
        print(filter_list0)
        print(filter_list1)
        print(filter_list2)

        if filter_list2 == filter_list1:
            retest_table_fill(d, bid, '34', "", True, True)
            assert False, (
                'Bug#34. Displayed a filtered list of cookies according to the selected checkboxes '
                '\n'
                'Actual result: Filtered list of cookies is displayed according to the checked '
                'and unchecked checkboxes')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step(
        'Bug#40:  The "All markets" widget is displayed, but the arrangement of trading instruments with '
        'the filter applied isnot performed after selecting any item from the dropdown menu "Most traded"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_40
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_40(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        The "All markets" widget is displayed, but the arrangement of trading instruments with the filter applied is
        not performed after selecting any item from the dropdown menu "Most traded" in the [Markets] menu section
        1. Navigate to Capital.com
        2. Click the menu section [Markets]
        3. Scroll down to the "All Markets " Widget
        4. Click  the Dropdown "Most traded"
        5. Click on any item from this dropdown menu
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_40", 'The "All markets" widget is displayed, but the arrangement of trading instruments '
                   'with the filter applied is not performed after selecting any item from '
                   'the dropdown menu "Most traded"', True, True)
        # d.get("https://capital.com/en-gb")

        with allure.step('step 1'):
            print(f"\n{datetime.now()}   1. Navigate to Capital.com")
        #
        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #
        with allure.step('step 2'):
            print(f"\n{datetime.now()}   2. Click the menu section [Markets]")
        menu = MainMenu(d, link)
        menu.open_markets_menu(d, cur_language, cur_country, link)
        with allure.step('step 3'):
            print(f"\n{datetime.now()}   3. Scroll down to the [All Markets] Widget")
        menu.element_is_present_and_visible(menu.SUB_MENU_MARKETS_SORT).click()
        n = len(menu.elements_are_located(menu.SUB_MENU_MARKETS_SORT_LIST))
        menu.element_is_present_and_visible(menu.SUB_MENU_MARKETS_SORT).click()
        t = ["0"] * n
        for i in range(n):
            with allure.step('step 4'):
                print(f"\n{datetime.now()}   4. Click  the Dropdown [Most traded]")
            menu.element_is_present_and_visible(menu.SUB_MENU_MARKETS_SORT).click()
            elem = menu.elements_are_located(menu.SUB_MENU_MARKETS_SORT_LIST)[i]
            menu.element_is_clickable(elem).click()
            with allure.step('step 5'):
                print(f"\n{datetime.now()}   5. Click on any item from this dropdown menu")
            time.sleep(1)
            t[i] = menu.elements_are_located(menu.SUB_MENU_MARKETS_LIST)[0].text
        print(t)
        # проверка, что все элементы равны
        rez = all(x == t[0] for x in t)

        if rez:
            retest_table_fill(d, bid, '40', "", True, True)
            assert False, (
                'Bug#40. The "All markets" widget is displayed, and the arrangement of trading instruments with '
                'the filter applied is performed'
                '\n'
                'Actual result: The "All markets" widget is displayed, but the arrangement of trading instruments with '
                'the filter applied is not  performed')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step(
        'Bug#4m:  "Line Chart" is not displayed corresponding to the selected "Time steps"  1m/5m')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_4m
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_4m(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        "Line Chart" is not displayed corresponding to the selected "Time steps"  1m/5m and selected any trading
        instrument in the "Our CFD Markets" Widget
        1. Tap the Burger menu
        2. Tap the [Ways to trade] arrow dropdown
        3. Tap the [CFD trading] menu item
        4. Scroll down to "Our CFD Markets" Widget
        5. Tap the "Time steps" (1m/5m)
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_4m", '"Line Chart" is not displayed corresponding to the selected "Time steps"  1m/5m', True, True)
        #
        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #
        menu = MainMenu(d, link)
        menu.open_waytotrade_cfd_trading_sub_menu(d, cur_language, cur_country, link)
        time.sleep(1)
        menu.element_is_present_and_visible(menu.SUB_MENU_WAYS_TO_TRADE_CFD_TRADING_CHART)
        menu.element_is_present_and_visible(menu.SUB_MENU_WAYS_TO_TRADE_CFD_TRADING_CHART_15M).click()
        chart_15m_image = 'cart_15m.png'
        chart_15m = menu.element_is_present_and_visible(menu.SUB_MENU_WAYS_TO_TRADE_CFD_TRADING_CHART)
        time.sleep(1)
        chart_15m.screenshot(chart_15m_image)
        size_chart15 = os.path.getsize(chart_15m_image)
        print("size_chart15m:", size_chart15)

        menu.element_is_present_and_visible(menu.SUB_MENU_WAYS_TO_TRADE_CFD_TRADING_CHART_1M).click()
        chart_1m_image = 'cart_1m.png'
        chart_1m = menu.element_is_present_and_visible(menu.SUB_MENU_WAYS_TO_TRADE_CFD_TRADING_CHART)
        time.sleep(1)
        chart_1m.screenshot(chart_1m_image)
        size_chart1 = os.path.getsize(chart_1m_image)
        print("size_chart1m", size_chart1)

        menu.element_is_present_and_visible(menu.SUB_MENU_WAYS_TO_TRADE_CFD_TRADING_CHART_5M).click()
        chart_5m_image = 'cart_5m.png'
        chart_5m = menu.element_is_present_and_visible(menu.SUB_MENU_WAYS_TO_TRADE_CFD_TRADING_CHART)
        time.sleep(1)
        chart_5m.screenshot(chart_5m_image)
        size_chart5 = os.path.getsize(chart_1m_image)
        print("size_chart5m", size_chart5)
        os.remove(chart_15m_image)
        os.remove(chart_5m_image)
        os.remove(chart_1m_image)

        if not (size_chart1 > 10000 or size_chart5 > 10000):
            retest_table_fill(d, bid, '4m', "", True, True)
            assert False, (
                'Bug#4m. "Line Chart" is displayed and refreshed corresponding to the  selected "Time steps"'
                '\n'
                'Actual result: "Line Chart" is not displayed corresponding to the  selected "Time steps"')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "NoAuth"])
    @allure.step(
        'Bug#42: Validation error is not cleared in the Form [Sign up] when click button [Close]')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_42
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_42(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Validation error is not cleared in the Form [Sign up] when click button [Close]
        1. Click button [Sign up]
        2. Enter invalid email or password on Input Field [Email address/Password]
        3. Click button [Continue]
        4. Click button [Close]
        5. Click button [Sign up]
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_42", 'Validation error is not cleared in the Form [Sign up] when click button [Close]', True, True)
        #
        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #
        menu = MainMenu(d, link)
        menu.element_is_clickable(menu.HEADER_SIGNUP_BTN).click()
        signup_form = NewSignupFormLocators()
        menu.element_is_present_and_visible(signup_form.SIGNUP_FRAME)
        email = menu.element_is_present_and_visible(signup_form.SIGNUP_INPUT_EMAIL)
        email.send_keys("test01@gmail.com")
        password = menu.element_is_present_and_visible(signup_form.SIGNUP_INPUT_PASSWORD)
        password.send_keys("Qwer123")
        menu.element_is_clickable(signup_form.SIGNUP_CONTINUE_BTN).click()
        assert menu.element_is_visible(signup_form.SIGNUP_FORM_ERROR), "Error message was Not displayed"
        menu.element_is_clickable(signup_form.SIGNUP_FORM_CLOSE_BUTTON).click()
        menu.element_is_clickable(menu.HEADER_SIGNUP_BTN).click()

        try:
            menu.element_is_visible(signup_form.SIGNUP_FORM_ERROR)
            retest_table_fill(d, bid, '42', "", True, True)
            assert False, (
                'Bug#42. Validation error is cleared'
                '\n'
                'Actual result: Validation error is not cleared')
        except TimeoutException:
            if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "NoAuth"])
    @allure.step(
        'Bug#44: Validation error is not cleared in the Form [Sign up] when click button [Close]')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.test_44
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_44(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Account registration was successful and the transition to the trading platform after clicking
        the [Continue] button in the Signup form
        1. Click the Signup form
        2. Enter the valid email in the Email address field
        3. Enter an invalid value in the password field
        4. Click the [Continue] button
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_44", 'Account registration was successful and the transition to the trading platform after '
                   'clicking the [Continue] button in the Signup form', True, True)
        #
        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #
        menu = MainMenu(d, link)
        menu.element_is_clickable(menu.HEADER_SIGNUP_BTN).click()
        signup_form = NewSignupFormLocators()
        menu.element_is_present_and_visible(signup_form.SIGNUP_FRAME)
        email = menu.element_is_present_and_visible(signup_form.SIGNUP_INPUT_EMAIL)
        email.send_keys("test001.miketar+1@gmail.com")
        password = menu.element_is_present_and_visible(signup_form.SIGNUP_INPUT_PASSWORD)
        password.send_keys("Qwer1234")
        menu.element_is_clickable(signup_form.SIGNUP_CONTINUE_BTN).click()

        try:
            menu.element_is_visible(signup_form.SIGNUP_FORM_ERROR)
        except TimeoutException:
            retest_table_fill(d, bid, '44', "", True, True)
            assert False, (
                'Bug#44. Validation error is cleared'
                '\n'
                'Actual result: Validation error is not cleared')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#45:  The  button [Try demo] is missing in the block "Discover trading excellence with '
                 'Capital.com" in menu item [Forex] in menu section [Markets]')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_45
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_45(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        The  button [Try demo] is missing in the block "Discover trading excellence with Capital.com" in menu item
        [Forex] in menu section [Markets]
        1. Click to Hover over [Markets] menu section
        2. Click to menu item [Forex]
        3. Scroll to the block "Discover trading excellence with Capital.com"
        4. Pay attention to the buttons at the bottom of the block
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_45", 'The  button [Try demo] is missing in the block "Discover trading excellence '
                   'with Capital.com" in menu item [Forex] in menu section [Markets]', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_markets_forex_sub_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)
        sub_menu.element_is_present_and_visible(sub_menu.MARKETS_DISCOVER_BLOCK_CREATE_ACCOUNT_BTN)

        #
        if len(sub_menu.elements_are_present(*sub_menu.MARKETS_DISCOVER_BLOCK_TRY_DEMO_BTN)) == 0:
            retest_table_fill(d, bid, '45', "", True, True)
            assert False, (
                "Bug#45. Expected Result: Button [Try demo] is displayed.\n"
                "Actual Result: Button [Try demo] is not displayed")
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#47:  The  button [Try demo] is missing in the block "Discover trading excellence with '
                 'Capital.com" in menu item [Forex] in menu section [Markets]')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_47
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_47(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        The  button [Try demo] is missing in the block "Discover trading excellence with Capital.com" in menu item
        [Forex] in menu section [Markets]
        1. Click to Hover over [Markets] menu section
        2. Click to menu item [Forex]
        3. Scroll to the block "Discover trading excellence with Capital.com"
        4. Pay attention to the buttons at the bottom of the block
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_47", 'The  button [Try demo] is missing in the block "Discover trading excellence '
                   'with Capital.com" in menu item [Forex] in menu section [Markets]', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        sub_menu = MenuSections(d, link)
        sub_menu.element_is_present_and_visible(sub_menu.MAIN_PAGE_LEARNED_BLOCK_SIGNUP_BTN)

        #
        if len(sub_menu.elements_are_present(*sub_menu.MAIN_PAGE_LEARNED_BLOCK_DEMO_BTN)) == 0:
            retest_table_fill(d, bid, '47', "", True, True)
            assert False, (
                "Bug#47. Expected Result: Button [Try demo] is displayed.\n"
                "Actual Result: Button [Try demo] is not displayed")
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ['NoReg'])
    @allure.step("Bug#48: 404 status code is displayed on the [USD/JPY-Rate] page and switching to an ASIC license")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_48
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_48(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        404 status code is displayed on the "USD/JPY-Rate" page and switching to an ASIC license after
        clicking the "USD/JPY" trading instrument in the "Forex Market" Widget in the "Forex" page
        (Floating bug, also open another tab in parallel with another licence(Try all three roles) )
            1. Hover over the [Markets] menu section
            2. Click the [Forex] menu item
            3. Scroll down to the "Forex Market" widget
            4. Click the "USD/JPY"  trading instrument
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_48", "404 status code is displayed on the [USD/JPY-Rate] page and switching "
                   "to an ASIC license", True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_markets_forex_sub_menu(d, cur_language, cur_country, link)

        # определение количества страниц
        markets_page = MenuSections(d)
        # pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
        # qty_pages = int(pagination[-2].text)
        qty_pages = 2
        print("qty_pages=", qty_pages)

        # перебор страниц
        error_trade_instrument_list = []
        for i in range(qty_pages):
            print("page:", i + 1)
            most_traded_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LINK_LIST)
            for j in range(len(most_traded_list)):
                most_traded_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LINK_LIST)

                markets_page.go_to_element(most_traded_list[j])
                most_traded_instrument_name = most_traded_list[j].text
                try:
                    markets_page.element_is_clickable(most_traded_list[j]).click()
                except StaleElementReferenceException:
                    print("StaleElementReferenceException")
                    most_traded_list = markets_page.elements_are_located(
                        markets_page.MARKETS_MOST_TRADE_LINK_LIST)
                    markets_page.element_is_clickable(most_traded_list[j]).click()

                err_404 = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_INSTRUMENT_404, 1)
                if err_404:
                    error_trade_instrument_list.append(most_traded_instrument_name + ":404")
                    print("error_404: ", error_trade_instrument_list)
                    retest_table_fill(d, bid, '48', "", True, True)
                    assert False, (
                        f"Bug#48. Expected Result: Page of the corresponding trading instrument"
                        f"{error_trade_instrument_list} is opened. \n"
                        f"Actual Result: 404 status code is displayed on the {error_trade_instrument_list} "
                        f"page and switching to an ASIC license . \n"
                        f"error_404: {error_trade_instrument_list}. \n"
                        f"qty_pages: {qty_pages}")
                else:
                    time.sleep(1)
                    d.back()

            pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
            if i != qty_pages - 1:
                pagination[-1].click()
            time.sleep(1)
            print("Non one 404 error")
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#49:  The  button [Create account ] is located instead button [Sign up] in the Block '
                 '"Indices trading" in the  menu item [Indices]  in menu section [Markets]')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_49
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_49(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        The  button [Create account ] is located instead button [Sign up] in the Block "Indices trading" in the  menu
        item [Indices]  in menu section [Markets]
        1. Hover over [Markets] menu section
        2. Click to menu item [Indices]
        3. Scroll to the block "Indices trading"
        4. Pay attention to the buttons at the block

        also reproduced in the menu item [Commodities] in menu section [Markets]
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_49", 'The  button [Create account ] is located instead button [Sign up] in the Block '
                   '"Indices trading" in the  menu item [Indices]  in menu section [Markets]', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_markets_indices_sub_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)

        btn_create = sub_menu.element_is_present_and_visible(sub_menu.MARKETS_MAIN_BANNER_CREATE_ACCOUNT)
        name_btn = btn_create.text
        #
        if not name_btn == "Sign up":
            retest_table_fill(d, bid, '49', "", True, True)
            assert False, (
                "Bug#49. Expected Result: The  button [Sign up] is displayed.\n"
                "Actual Result: The  button [Create account ] is displayed")
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoAuth"])
    @allure.step('Bug#55:  Sign Up form is opened instead Login form in the Block "Helping traders make better '
                 'decisions" on the main page after clicking button [Try demo ]')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_55
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_55(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Sign Up form is opened instead Login form in the Block "Helping traders make better decisions" on the
         main page after clicking button [Try demo ]
        1. Scroll to the Block "Helping traders make better decisions" on the main page
        2.  Click button [Try demo ]
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_55", 'Sign Up form is opened instead Login form in the Block "Helping traders make better'
                   ' decisions" on the main page after clicking button [Try demo ]', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        sub_menu = MenuSections(d, link)

        sub_menu.element_is_present_and_visible(sub_menu.MAIN_PAGE_TRY_DEMO).click()

        test_element = AssertClass(d, link)
        try:
            match cur_role:
                # case "NoReg":
                #     test_element.assert_signup(d, cur_language, link)
                case "NoAuth":
                    test_element.assert_login(d, cur_language, link)
                # case "Auth":
                #     test_element.assert_trading_platform_v4(d, cur_item_link)
        except AssertionError:
            print(f"\n{datetime.now()}   Bug#55")
            retest_table_fill(d, bid, '55', "", True, True)
            assert False, (
                "Bug#55. Expected Result: Login form is opened.\n"
                "Actual Result: Sign Up form is opened")
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step(
        'Bug#57: The icon is missing in the item "Smart risk management" of the block "Why trade on 1X with.." '
        'on the "1X" page')
    @allure.severity(allure.severity_level.TRIVIAL)
    @pytest.mark.test_57
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_57(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        The icon is missing in the item "Smart risk management" of the block "Why trade on 1X with.." on the "1X" page
        1. Hover over menu section [Ways to trade]
        2. Click menu item [1X]
        3. Scroll to the block "Why trade on 1X with Capital.com?"
        4. Go to item "Smart risk management"
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_57", 'The icon is missing in the item "Smart risk management" of the block "Why trade on '
                   '1X with.." on the "1X" page', True, True)
        #
        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #
        menu = MainMenu(d, link)
        menu.open_waytotrade_1X_sub_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)
        time.sleep(1)
        sub_menu.element_is_present_and_visible(sub_menu.WAYSTOTRADE_1X_WHY_BLOCK_4)
        list_img = menu.elements_are_present(*sub_menu.WAYSTOTRADE_1X_WHY_BLOCK_4_IMG)

        time.sleep(1)
        if not len(list_img) > 1:
            retest_table_fill(d, bid, '57', "", True, True)
            assert False, (
                'Bug#57. Expected Result: The icon is in the item'
                '\n'
                'Actual result: The icon is missing in the item')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step(
        'Bug#58: Anchor is not attached to the "What is margin trading?" title on the "What is a margin?" page')
    @allure.severity(allure.severity_level.TRIVIAL)
    @pytest.mark.test_58
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_58(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Anchor is not attached to the "What is margin trading?" title on the "What is a margin?" page
        1. Hover over menu section [Learn to trade]
        2. Click menu item [Trading Strategies]
        3. Go to the block "Our most-read.."
        4. Click link [Margin trading guide] in the Tile [Margin trading]
        5. Click link [What is margin trading?] in block "Contents"

        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_58", 'Anchor is not attached to the "What is margin trading?" title on '
                   'the "What is a margin?" page', True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_learn_to_trade_trading_strategies_sub_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)
        sub_menu.element_is_present_and_visible(sub_menu.LEARN_TO_TRADE_MARGIN_TRADING_GUIDE_LINK).click()
        sub_menu.element_is_present_and_visible(sub_menu.LEARN_TO_TRADE_MARGIN_TRADING_GUIDE_1).click()

        scroll_0 = d.execute_script("return window.scrollY;")

        if not scroll_0 > 60:
            retest_table_fill(d, bid, '58', "", True, True)
            assert False, \
                ('Bug#58. Smooth transition to title "What is margin trading?"'
                 '\n'
                 'Actual result: No transition occurred  to title "What is margin trading?"')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "NoAuth"])
    @allure.step(
        'Bug#59: User is registered when two required characters are not entered in '
        'the "password" field in the Signup form')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.test_59
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_59(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        User is registered when two required characters are not entered in the "password" field in the Signup
        form after clicking the [Continue] button
        1. Click the [Sign up] button
        2. Enter valid value in the "Email" field
        3. Enter value in the "password" field without at least one special character at last one apper case letter
        4. Click the [Continue] button
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_59", 'User is registered when two required characters are not entered in '
                   'the "password" field in the Signup form '
                   'clicking the [Continue] button in the Signup form', True, True)
        #
        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #
        menu = MainMenu(d, link)
        menu.element_is_clickable(menu.HEADER_SIGNUP_BTN).click()
        signup_form = NewSignupFormLocators()
        menu.element_is_present_and_visible(signup_form.SIGNUP_FRAME)
        email = menu.element_is_present_and_visible(signup_form.SIGNUP_INPUT_EMAIL)
        email.send_keys("test001.miketar+1@gmail.com")
        password = menu.element_is_present_and_visible(signup_form.SIGNUP_INPUT_PASSWORD)
        password.send_keys("qwer1234")
        menu.element_is_clickable(signup_form.SIGNUP_CONTINUE_BTN).click()

        try:
            menu.element_is_visible(signup_form.SIGNUP_FORM_ERROR)
        except TimeoutException:
            retest_table_fill(d, bid, '59', "", True, True)
            assert False, (
                'Bug#59. Validation message "Email or password is invalid" is displayed'
                '\n'
                'Actual result: User is registered and transition to the trading platform')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "NoAuth"])
    @allure.step(
        'Bug#60: Validation message "Email or password is invalid" is displayed ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_60
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_60(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        [Continue] button is active for sending POST request in the Sign up/Log in form
        after clicking the [Sign up / Log in] buttons
        1. Click the Signup/ Log in form
        2. Click the [Continue] button
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_60", 'Validation message "Email or password is invalid" is displayed', True, True)
        #
        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #
        menu = MainMenu(d, link)
        menu.element_is_clickable(menu.HEADER_SIGNUP_BTN).click()
        signup_form = NewSignupFormLocators()
        menu.element_is_present_and_visible(signup_form.SIGNUP_FRAME)
        menu.element_is_clickable(signup_form.SIGNUP_CONTINUE_BTN).click()

        try:
            menu.element_is_clickable(signup_form.SIGNUP_CONTINUE_BTN)
            retest_table_fill(d, bid, '60', "", True, True)
            assert False, (
                'Bug#60. [Continue] button is inactive until valid values are entered in the email and password '
                'fields and validated'
                '\n'
                'Actual result: [Continue] button is active for sending POST request')
        except TimeoutException:
            if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "NoAuth"])
    @allure.step(
        'Bug#61: There is no a  [Close] button for closing Validation message in the Signup/Login form'
        'the "password" field in the Signup form')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_61
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_61(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        There is no a  [Close] button for closing Validation message in the Signup/Login form after entering values
        in the "email" and "password" fields and clicking the [Continue] button
        1. Click the [Log in/Sign up] button
        2. Enter valid value in the "email" field
        3. Enter invalid value in the "password" field
        4. Click the [Continue] button
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_61", 'There is no a  [Close] button for closing Validation message in the Signup/Login form', True, True)
        #
        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #
        menu = MainMenu(d, link)
        menu.element_is_clickable(menu.HEADER_SIGNUP_BTN).click()
        signup_form = NewSignupFormLocators()
        menu.element_is_present_and_visible(signup_form.SIGNUP_FRAME)
        menu.element_is_clickable(signup_form.SIGNUP_CONTINUE_BTN).click()

        if not menu.element_is_visible(signup_form.SIGNUP_FORM_ERROR_CLOSE_BTN):
            retest_table_fill(d, bid, '61', "", True, True)
            assert False, (
                'Bug#61. There is no a  [Close] button for closing Validation message'
                '\n'
                'Actual result: There is no a  [Close] button for closing Validation message')
        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step("Bug#62: There is no transition to the corresponding page with a trading instrument when clicking on "
                 "any of the trading instruments in the dropdown in the [Search]")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_62
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_62(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        There is no transition to the corresponding page with a trading instrument when clicking on any of the trading
        instruments in the dropdown in the [Search] input field in the "Forex Markets" widget(this bug is reproduced
        in all markets: Shares, Indices, Commodities, Forex )( AJAX requests, checking synchronous operations)
        1. Hover over [Markets] menu section
        2. Click the [Forex] menu item
        3. Scroll down to the "Forex Markets" widget
        4. Click the [Search] input field
        5. Enter any value for example "eur"
        6. Click any item from dropdown list
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_62", "There is no transition to the corresponding page with a trading instrument when "
                   "clicking on any of the trading instruments in the dropdown in the [Search]", True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_markets_forex_sub_menu(d, cur_language, cur_country, link)

        markets_page = MenuSections(d)

        search = markets_page.element_is_present_and_visible(markets_page.MARKETS_MOST_TRADE_SEARCH)
        search.send_keys("eur")
        search_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_LINK_LIST)
        try:
            ActionChains(d) \
                .move_to_element(search_list[1]) \
                .pause(0.5) \
                .move_to_element(search_list[1]) \
                .pause(1) \
                .click() \
                .perform()
        except TimeoutException:
            print()

        retest_table_fill(d, bid, '62', "", True, True)
        try:
            markets_page.element_is_located(markets_page.MARKETS_MOST_TRADE_INSTRUMENT_PAGE)
        except TimeoutException:
            assert False, (
                f"Bug#62. Expected Result:  Page of the corresponding trading instrument is opened\n"
                f"Actual Result: Items in the Dropdown list are not clickable \n")

        if_retest_passed(d, bid)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#65: The footer is missing on click menu item [Professional] of the menu section [Ways to trade]"')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.test_65
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_65(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Page "The footer is missing on click menu item [Professional] of the menu section [Ways to trade]
        1. Hover over the [Ways to trade] menu section
        2. Click the [Professional]menu item
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "FCABugs", "Capital.com FCA",
            "_65", 'The footer is missing on click menu item [Professional] of the menu section [Ways to trade]',
            True, True)

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_waytotrade_professional_sub_menu(d, cur_language, cur_country, link)

        if not menu.element_is_visible(menu.FOOTER_RISK_WARNING_BLOCK):
            retest_table_fill(d, bid, '65', "", True, True)
            assert False, ('Bug#65. '
                           'Expected result: The footer is displayed '
                           '\n'
                           'Actual result: The footer is missing" '
                           'is opened ')
        if_retest_passed(d, bid)
