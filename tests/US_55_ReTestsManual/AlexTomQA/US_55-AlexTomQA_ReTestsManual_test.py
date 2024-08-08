"""
-*- coding: utf-8 -*-
@Time    : 2024/05/06 22:00
@Author  : Alexander Tomelo
"""
from datetime import datetime
import time

import pytest
import allure
from selenium.common.exceptions import ElementClickInterceptedException

from pages.base_page import BasePage
from pages.conditions import Conditions
from pages.common import Common
from pages.Menu.menu import MenuSection
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55
from pages.conditions_new import NewConditions
# from pages.Elements.StepTradingBlock import BlockStepTrading
# from pages.Elements.AssertClass import AssertClass
from src.src import CapitalComPageSrc
from pages.Elements.testing_elements_locators import ContentBlockLocators
from pages.Elements.GooglePlayButtonCFDTradinAppBlock import GooglePlayButtonOnCFDTradingAppBlock
# from pages.Elements.ContentsBlockLearnMoreAboutUsLink import ContentsBlockLearnMoreAboutUsLink

BUTTON_NAME = '[Learn more about us]'
BLOCK_NAME = '"Contents"'
TITLE_NAME = '"Learn more about us"'
BUTTON_LOCATOR = ContentBlockLocators.LEARN_MORE_ABOUT_US_LINK_CONTENTS_BLOCK
BLOCK_LOCATOR = ContentBlockLocators.CONTENTS_BLOCK
TITLE_LEARN_MORE_ABOUT_US_LOCATOR = ContentBlockLocators.TITLE_LEARN_MORE_ABOUT_US


@pytest.mark.us_55
class TestManualDetected:
    page_conditions = None

    # @allure.step("Start test of _011")
    # @pytest.mark.parametrize('cur_language', [""])
    # @pytest.mark.parametrize('cur_country', ["de"])
    # @pytest.mark.parametrize('cur_role', ["NoReg"])
    # @pytest.mark.bug_011
    # def test_011(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
    #     """
    #     Check: Button [1. Create your account] in block [Steps trading]
    #     Language: All. License: All.
    #     Author  : Alexander Tomelo
    #     """
    #     bid = build_dynamic_arg_for_us_55(
    #         d, worker_id, cur_language, cur_country, cur_role,
    #         "55", "ReTests of Manual Detected Bugs",
    #         "011", "There are no digital values of the product \"ECFZ24\""
    #     )
    #     pytest.skip("Autotest under construction")
    #
        #
        # Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        # Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        # if cur_language not in ["", "de", "el", "es", "fr", "it", "hu", "nl", "pl", "ro", "ru", "zh"]:
        #     pytest.skip(f"This test-case is not for {cur_language} language")
        #
        # page_conditions = Conditions(d, "")
        # link = page_conditions.preconditions(
        #     d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
        #
        # page_menu = MenuSection(d, link)
        # page_menu.menu_education_move_focus(d, cur_language, cur_country)
        # link = page_menu.sub_menu_glossary_move_focus_click(d, cur_language)
        #
        # test_element = BlockStepTrading(d, link)
        # test_element.arrange_(d, link)
        #
        # test_element.element_click()
        #
        # test_element = AssertClass(d, link, bid)
        # match cur_role:
        #     case "NoReg" | "NoAuth":
        #         test_element.assert_signup(d, cur_language, link)
        #     case "Auth":
        #         test_element.assert_trading_platform_v4(d, link)
        #
        # del test_element
        # del page_menu

    @allure.step("Start test of _015")
    @pytest.mark.parametrize('cur_language', [""])
    @pytest.mark.parametrize('cur_country', ["au"])
    @pytest.mark.parametrize('cur_role', ["NoAuth"])
    @pytest.mark.bug_015a
    def test_015a(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        # Check: Button [1. Create your account] in block [Steps trading]
        # Language: All. License: All.
        Author: Alexander Tomelo
        """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "015a", "The page of the corresponding TI on the TP is not opened"
        )
        pytest.skip("Autotest under construction")

    @allure.step("Start test of button [Google Play] on the block 'CFD trading app'")
    @pytest.mark.parametrize('cur_country', ['de', 'au', 'ua'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_029
    def test_029_google_play_button_on_cfd_trading_app_block(
            self, worker_id, d, cur_language_qty_rnd_from_14, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Google Play] on the block CFD Trading app
        Language: All.
        License: Not FCA
        Author  : Ivan Kedrov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_qty_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "029",
            "Testing button [Google Play] on the block 'CFD trading app'",
            False, False
        )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_qty_rnd_from_14, cur_country, cur_role, cur_login,
            cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_our_mobile_apps_submenu_products_and_services_menu(
            d, cur_language_qty_rnd_from_14, cur_country, link)

        test_element = GooglePlayButtonOnCFDTradingAppBlock(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language_qty_rnd_from_14, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of link [Learn more about us] on the block 'Contents'")
    @pytest.mark.parametrize('cur_language', [""])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.test_024v2
    def test_031v2_learn_more_about_us_link_on_contents_block(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Link [Learn more about us] on block Contents?
        Language: En.
        License: FCA
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "031v2",
            "Testing link [Learn more about us] on the block 'Contents'",
            False, True
        )

        pytest.skip("Autotest under construction")

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_why_capital_com_client_funds_menu(
            d, cur_language, cur_country, link
        )

        # test_element = ContentsBlockLearnMoreAboutUsLink(d, cur_item_link, bid)
        # test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)
        lo = LocalObject(d, cur_item_link)
        lo.arrange_(d, cur_item_link)
        lo.element_click(d)

        # Check presenting Title
        print(f"\n{datetime.now()}   3. Assert")
        print(f"{datetime.now()}   IS {TITLE_NAME} title present on this page? =>")
        if len(d.find_elements(*TITLE_LEARN_MORE_ABOUT_US_LOCATOR)) == 0:
            msg = f"{TITLE_NAME} title is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {TITLE_NAME} title present on this page!\n")

        # Check visible Title
        print(f"{datetime.now()}   IS {TITLE_NAME} title visible on this page? =>")
        if not d.element_is_visible(TITLE_LEARN_MORE_ABOUT_US_LOCATOR, 5):
            msg = f"{TITLE_NAME} title is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {TITLE_NAME} title is visible on this page!\n")

        # Check visibility Title on area of window
        print(f"{datetime.now()}   IS {TITLE_NAME} title visible on area of window? =>")

        title = d.find_element(*TITLE_LEARN_MORE_ABOUT_US_LOCATOR)
        title_y = title.location['y']  # height coordinate of title
        time.sleep(1)
        current_y = d.execute_script("return window.scrollY;") # current height coordinate
        window_height = d.execute_script("return window.innerHeight;") # height inner window
        print('Height coordinate of title:', title_y)
        print('Current height coordinate:', current_y)
        print('Height inner window', window_height)

        if (title_y >= current_y) and (title_y <= (current_y + window_height)):
            print(f"{datetime.now()}   {TITLE_NAME} title IS visible on area of window. =>")
        else:
            msg = f"{TITLE_NAME} title is NOT visible on area of window!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        del title, title_y, current_y, window_height

    @allure.step("Start test of button [Create account] button in the Menu item [Trading Courses]")
    @pytest.mark.parametrize('cur_country', ['de', 'au', 'ua'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.bug_062
    def test_062_create_account_button_in_the_nemu_item_trading_courses(
            self, worker_id, d, cur_language_qty_rnd_from_14, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Create account] button in the Menu item [Trading Courses]
        Language: All.
        License: Not FCA
        Author  : Ivan Kedrov
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_qty_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "062",
            "Testing button [Create account] button in the Menu item [Trading Courses]",
            False, False
        )
        pytest.skip('Under construction')
        # page_conditions = Conditions(d, "")
        # link = page_conditions.preconditions(
        #     d, CapitalComPageSrc.URL, "", cur_language_3_rnd_from_12, cur_country, cur_role, cur_login,
        #     cur_password)
        #
        # menu = MenuSection(d, link)
        # menu.menu_education_move_focus(d, cur_language_3_rnd_from_12, cur_country)
        # cur_item_link = menu.sub_menu_trading_courses_move_focus_click(
        #     d, cur_language_3_rnd_from_12, cur_country, link)


class LocalObject(BasePage):

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not d.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        # Check presenting and visible in block
        print(f"{datetime.now()}   IS {BLOCK_NAME} block present on this page? =>")
        block_trading_experience = self.driver.find_elements(*BLOCK_LOCATOR)
        if len(block_trading_experience) == 0:
            msg = f"{BLOCK_NAME} block is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} block present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*BLOCK_LOCATOR)[0]
        )

        print(f"{datetime.now()}   IS {BLOCK_NAME} block visible on this page? =>")
        if not self.element_is_visible(BLOCK_LOCATOR, 5):
            msg = f"{BLOCK_NAME} block is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} block is visible on this page!\n")

        # Check presenting and visible link
        print(f"{datetime.now()}   IS {BUTTON_NAME} link present on this page? =>")
        self.button = self.driver.find_elements(*BUTTON_LOCATOR)
        if len(self.button) == 0:
            msg = f"{BUTTON_NAME} link is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} link present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*BUTTON_LOCATOR)[0]
        )

        print(f"{datetime.now()}   IS {BUTTON_NAME} link visible on this page? =>")
        if not self.element_is_visible(BUTTON_LOCATOR, 5):
            msg = f"{BUTTON_NAME} link is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} link is visible on this page!\n")

        print(f"{datetime.now()}   {BUTTON_NAME} link scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.button[0]
        )

    @allure.step(f"Click link {BUTTON_NAME} on {BLOCK_NAME} block")
    def element_click(self, d):
        print(f"\n{datetime.now()}   2. Act_v0")

        print(f"{datetime.now()}   {BUTTON_NAME} link is clickable? =>")
        time_out = 5
        self.button = self.driver.find_elements(*BUTTON_LOCATOR)
        if not self.element_is_clickable(self.button[0], time_out):
            msg = f"{BUTTON_NAME} link is not clickable after {time_out} sec. Stop AT>"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} link is clickable!\n")

        try:
            self.button[0].click()
            print(f"{datetime.now()}   => {BUTTON_NAME} link clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => {BUTTON_NAME} link NOT CLICKED\n")

        del self.button
        return True
