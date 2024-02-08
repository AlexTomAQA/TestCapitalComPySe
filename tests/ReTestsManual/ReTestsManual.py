import time
from datetime import datetime

import allure
import pytest
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.Elements.AssertClass import AssertClass
from tests.ReTestsManual.pages.menu.menu import MainMenu
from tests.ReTestsManual.pages.menu_section.menu_section import MenuSections

# from pages.Elements.AssertClass import AssertClass

from tests.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from src.src import CapitalComPageSrc


# @pytest.mark.Bugs_26012024_CCW_WEB
class TestManualBugs:
    page_conditions = None

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth", "NoAuth", "NoReg"])
    @allure.step("Bug#01: Content of the Block ""USD/CHF"" is not loaded in the ""US Dollar / Swiss Franc"" page ")
    @pytest.mark.test_01
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_01(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Content of the Block ""USD/CHF"" is not loaded in the ""US Dollar / Swiss Franc"" page after clicking
        the ""USD/CHF"" trading instrument in the  ""Forex Markets"" Widget"
            1. Hover over the [Markets] menu section
            2. Click the [Forex] menu item
            3. Scroll down to the ""Forex Markets"" Widget
            4. Click USD/CHF trading instruments
            5. Scroll down to ""USD/CHF"" Block"
        """

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".01", "Content of the Block ""USD/CHF"" is not loaded in the ""US Dollar / Swiss Franc"""
                   " page after clicking")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

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
            assert False, (f"Bug#01. Expected Result: Content of the Block is displayed. \n"
                           f"Actual Result: Content of the Block is not displayed. \n"
                           f"error_404: {error_trade_instrument_list}. \n"
                           f"trade instrument: {len(most_trade_instrument_list)} {most_trade_instrument_list}\n"
                           f"qty_pages: {qty_pages}")

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ['NoReg'])
    @allure.step("Bug#48: 404 status code is displayed on the [USD/JPY-Rate] page and switching to an ASIC license")
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

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".48", "404 status code is displayed on the [USD/JPY-Rate] page and switching to an ASIC license")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_markets_forex_sub_menu(d, cur_language, cur_country, link)

        # определение количества страниц
        markets_page = MenuSections(d)
        pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
        qty_pages = int(pagination[-2].text)
        # qty_pages = 1
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
                    assert False, (
                        f"Bug#48. Expected Result: Page of the corresponding trading instrument"
                        f"{error_trade_instrument_list} is opened. \n"
                        f"Actual Result: 404 status code is displayed on the {error_trade_instrument_list} "
                        f"page and switching to an ASIC license . \n"
                        f"error_404: {error_trade_instrument_list}. \n"
                        f"qty_pages: {qty_pages}")
                else:
                    d.back()

            pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
            if i != qty_pages - 1:
                pagination[-1].click()
            time.sleep(1)
            print("Non one 404 error")

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth", "NoAuth", "NoReg"])
    @allure.step('Bug#02:  "Sell"/"Buy" in the Widget "Trading instrument is not clickable')
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

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".02", 'Sell"/"Buy" in the Widget "Trading instrument is not clickable')

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

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
                assert False, (
                    "Bug#02. Expected Result: Sign up form is opened/ unregistered Login form is opened/ unauthorized "
                    "Transition to the trading platform / authorized.\n"
                    "Actual Result: Page of the corresponding trading instrument is opened ")

            pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
            if i != qty_pages - 1:
                pagination[-1].click()
            time.sleep(1)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth", "NoAuth", "NoReg"])
    @allure.step('Bug#04:  Block "Key Stats" is not displayed to the right of the Block "Trading Condition"')
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

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".04", 'Block "Key Stats" is not displayed to the right of the Block "Trading Condition"')

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

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

                key_stat_list = markets_page.elements_are_located(markets_page.MARKETS_MOST_TRADE_INSTRUMENT_KEY_STATS,
                                                                  1)
                assert len(key_stat_list) == 2, ('Bug#04. '
                                                 'Expected result: Block "Key Stats" is displayed to the right of '
                                                 'the Block "Trading Condition"'
                                                 '\n'
                                                 'Actual result: Block "Key Stats" is not displayed ')
                d.back()
            pagination = markets_page.elements_are_located(markets_page.MARKETS_PAGINATION_LIST)
            if i != qty_pages - 1:
                pagination[-1].click()
            time.sleep(1)

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth", "NoAuth", "NoReg"])
    @allure.step('Bug#05:  Block "Key Stats" is not displayed to the right of the Block "Trading Condition"')
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

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".05", 'Block "Key Stats" is not displayed to the right of the Block "Trading Condition"')

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
        assert len(apply_btn) == 0, ('Bug#05. '
                                     'Expected result: "Professional" page is opened'
                                     '\n'
                                     'Actual result: Page "Discover the benefits of going Pro with capital.com" '
                                     'is opened ')

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoAuth", "NoReg"])
    @allure.step('Bug#06:  The trading platform page is opened after clicking button [Apply] in '
                 'the block "Discover the benefits')
    @pytest.mark.test_06
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_06(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        The trading platform page is opened after clicking button [Apply] in the block "Discover the benefits..."
        on the "Professional" page
        1. Hover over the [Ways to trade] menu section
        2. Click the [Professional]menu item
        3. Click the [I am eligible] button
        steps
        1. Click the [Professional] menu item
        2. Go to block "Discover the benefits..."
        3. Click the button [Apply]
        """

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".06", 'The trading platform page is opened after clicking button [Apply] '
                   'in the block "Discover the benefits')

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        cur_item_link = menu.open_waytotrade_professional_sub_menu(d, cur_language, cur_country, link)
        menu_section = MenuSections(d, link)
        menu_section.element_is_clickable(menu_section.WAYSTOTRADE_PROFESSIONAL_ELIGIBLE_BTN).click()
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
            print(f"\n{datetime.now()}   Bug#06")
            assert False, ('Bug#06. Expected result: The Sign Up/Login form is opened'
                           '\n'
                           'Actual result: The trading platform page is opened')

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @allure.step('Bug#07:  The trading platform page is not opened after clicking button [Apply] in '
                 'the block "Discover the benefits')
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

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".07", 'The trading platform page is not opened after clicking button [Apply] '
                   'in the block "Discover the benefits')

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        cur_item_link = menu.open_waytotrade_professional_sub_menu(d, cur_language, cur_country, link)
        menu_section = MenuSections(d, link)
        menu_section.element_is_clickable(menu_section.WAYSTOTRADE_PROFESSIONAL_ELIGIBLE_BTN).click()
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
            assert False, ('Bug#07. Expected result: The trading platform page is opened'
                           '\n'
                           'Actual result: The trading platform page is not opened')

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @allure.step('Bug#08:  Sidebar "My account" is not displayed when clicking on the [My account] button '
                 ' in the Header ')
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

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".08", 'Sidebar "My account" is not displayed when clicking on the [My account] button  '
                   'in the Header')

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)

        menu_login = menu.elements_are_present(*menu.MENU_LOGIN)
        if len(menu_login) > 0:
            assert False, 'Bug#08. Interruption of authorization'

        account_btn = menu.element_is_visible(menu.MENU_ACCOUNT)
        account_btn_link = account_btn.get_attribute("href")

        assert account_btn_link != "/trading/platform", ('Bug#08. '
                                                         'Expected result: Sidebar "My account" is displayed'
                                                         '\n'
                                                         'Actual result: The trading platform page is opened')

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth", "NoAuth", "NoReg"])
    @allure.step('Bug#09:  Bread crumbs are not displayed in the "Professional" page')
    @pytest.mark.test_09
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_09(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Bread crumbs are not displayed in the "Professional" page
        1. Hover over the [Ways to trade] menu section
        2. Click the [Professional]menu item
        """
        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".09", 'Bread crumbs are not displayed in the "Professional" page')

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_waytotrade_professional_sub_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)
        bred_crumbs = menu.elements_are_located(sub_menu.BREADCRUMBS)
        if not bred_crumbs:
            assert False, ('Bug#09. Expected Result: Bread crumbs are displayed'
                           '\n'
                           'Actual Result: Bread crumbs are  not displayed')

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth", "NoAuth", "NoReg"])
    @allure.step('Bug#10:  Link "Apply here" is not clickable in the "No Capital.com account yet?"')
    @pytest.mark.test_10
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_10(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Link "Apply here" is not clickable in the "No Capital.com account yet?" in the block "Apply
        now" in the menu item "Professional"
        """
        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".10", 'Link "Apply here" is not clickable in the "No Capital.com account yet?"')

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_waytotrade_professional_sub_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)
        sub_menu.element_is_clickable(sub_menu.WAYSTOTRADE_PROFESSIONAL_ELIGIBLE_BTN).click()
        link1 = d.current_url
        apply_here = sub_menu.element_is_clickable(sub_menu.WAYSTOTRADE_PROFESSIONAL_NO_CAPITAL_YET_APPLY_BTN)
        apply_here.click()
        link2 = d.current_url
        assert link2 != link1, ('Bug#10. Expected Result: Link "Apply here" is clickable'
                                '\n'
                                'Actual Result: Link "Apply here" is not clickable')

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoAuth"])
    @allure.step('Bug#11:  Transition to the trading platform after clicking the [Apply here] link in '
                 'the "Apply now" Block')
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
        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".11", 'Transition to the trading platform after clicking the [Apply here] link in '
                   'the "Apply now" Block')

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_waytotrade_professional_sub_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)
        sub_menu.element_is_clickable(sub_menu.WAYSTOTRADE_PROFESSIONAL_ELIGIBLE_BTN).click()

        apply_here = sub_menu.element_is_present_and_visible(sub_menu.WAYSTOTRADE_PROFESSIONAL_EXISTING_CLIENT_BTN)
        apply_here.click()
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
            assert False, ('Bug#11. Expected result: Login form is opened'
                           '\n'
                           'Actual result: Transition to the trading platform')

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth", "NoAuth", "NoReg"])
    @allure.step('Bug#12:  The button [Open an account] is not named according to block "We’re here to help"')
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
        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".12", 'The button [Open an account] is not named according to block "We’re here to help"')

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_trading_platform_menu(d, cur_language, cur_country, link)

        sub_menu = MenuSections(d, link)
        support_button = sub_menu.element_is_present_and_visible(sub_menu.TRADING_PLATFORM_SUPPORT_BTN).text
        print(f"\n{datetime.now()}   Bug#12. The button [Open an account] is not named according to block "
              f"'We’re here to help'")
        assert support_button != "Open an account", ('Bug#12. Expected result: The button [Open an account] is named '
                                                     'according to block "We’re here to help"'
                                                     '\n'
                                                     'Actual result: The button [Open an account] is not named '
                                                     'according to block "We’re here to help"')

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step(
        'Bug#13:  Transition not to the top of the page in the page "Discover the benefits of going Pro with '
        '"Capital.com" after clicking the [I am eligible] button')
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
        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".13", 'Transition not to the top of the page in the page "Discover the benefits of '
                   'going Pro with "Capital.com" after clicking the [I am eligible] button')

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MainMenu(d, link)
        menu.open_waytotrade_professional_sub_menu(d, cur_language, cur_country, link)
        sub_menu = MenuSections(d, link)
        sub_menu.element_is_clickable(sub_menu.WAYSTOTRADE_PROFESSIONAL_ELIGIBLE_BTN).click()

        scroll_y = d.execute_script("return window.scrollY;")
        assert scroll_y == 0, ('Bug#13. Expected result: Transition to the top of the page'
                               '\n'
                               'Actual result: Transition not to the top of the page ')

    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg"])
    @allure.step('Bug#14:  Bread crumbs are not displayed')
    @pytest.mark.test_14
    # @pytest.mark.skip(reason="Skipped for debugging")
    def test_14(
            self, worker_id, d, cur_login, cur_password, cur_role, cur_language, cur_country):
        """
        Bread crumbs are not displayed in the "Margin-calls" page
        1. Hover over the [Ways to trade] menu section
        2. Click the [Margin Calls] menu tittle
        """

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "Bugs_26012024_CCW_WEB", "Capital.com FCA",
            ".14", 'Bread crumbs are not displayed in the "Professional" page')
        #
        # page_conditions = Conditions(d, "")
        # link = page_conditions.preconditions(
        #     d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        d.get('https://capital.com/en-gb')
        link = d.current_url
        link_list = []

        menu = MainMenu(d, link)
        menu_list = menu.elements_are_located(menu.MENU_LIST)

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
                # time.sleep(1)

        assert False, ('Bug#14. Expected Result: Bread crumbs are displayed'
                       '\n'
                       'Actual Result: Bread crumbs are  not displayed \n'
                       f'No breadcrumbs: {len(link_list)} {link_list}')

