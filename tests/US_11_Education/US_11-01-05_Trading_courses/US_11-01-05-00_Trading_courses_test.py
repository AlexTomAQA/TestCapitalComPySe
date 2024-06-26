from datetime import datetime

import allure
import pytest

from pages.common import Common
from pages.Menu.menu import MenuSection
from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.Elements.OurCoursesBlockCreateAccountButton import ButtonCreateAccountBlockOurCourses
from pages.Elements.testing_elements_locators import CoursesPage
from pages.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions import Conditions
from src.src import CapitalComPageSrc

count = 1


@pytest.fixture()
def cur_time():
    """Fixture"""
    return str(datetime.now())


@pytest.mark.us_11_01_05
class TestTradingCourses:
    page_conditions = None

    @allure.step(f"{datetime.now()}   Start test_11.01.05_01 button [Create account] in the block 'Our courses'.")
    @pytest.mark.test_01
    def test_01_create_account_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Block 'Our courses' -> button [Create account]
        Language: All. License: All. Role: All
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.05", "Education > Menu Item [Trading courses]",
            ".00_01", "Testing button [Create account] in block [Our courses]")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "el", "es", "fr", "it", "hu", "pl", "cn", "nl", "ro", "ru", "zh"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language, cur_country)
        link = page_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)

        test_element = ButtonCreateAccountBlockOurCourses(d, link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, link)

    @allure.step(f"{datetime.now()}   Start test_11.01.05_04 button [1. Create your account] in block 'Steps trading'.")
    @pytest.mark.test_04
    def test_04_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Steps trading -> button [1. Create your account]
        Language: All. License: All.
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.05", "Education > Menu Item [Trading courses]",
            ".00_04", "Testing button [1. Create your account] in block [Steps trading]")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "el", "es", "fr", "it", "hu", "pl", "cn", "nl", "ro", "ru", "zh"])

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language, cur_country)
        link = page_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, link)

    @allure.step(f"{datetime.now()}   Start pretest")
    def test_99_trading_courses_item_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        global count
        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.01.05", "Education > Menu Item [Trading courses]",
            ".00_99", "Pretest for US_11.01.05.01")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "el", "es", "fr", "it", "hu", "pl", "cn", "nl", "ro", "ru", "zh"])

        if count == 0:
            pytest.skip("The list of Trading courses links is already created")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language, cur_country)
        page_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        file_name = "tests/US_11_Education/US_11-01-05_Trading_courses/list_of_href.txt"
        list_items = d.find_elements(*CoursesPage.COURSES_PAGES_LIST)

        Common().creating_file_of_hrefs("Trading courses", list_items, file_name, 0)

        count -= 1
