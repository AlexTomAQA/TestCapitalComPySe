"""
-*- coding: utf-8 -*-
@Date    : 18/10/2024
@Author  : Alexey Kurochkin
"""
from datetime import datetime
import random

import pytest
import allure

from pages.BugsManual.bug_429 import Bug429
from pages.BugsManual.bug_444 import Bug444
from pages.BugsManual.bug_467 import Bug467
from pages.BugsManual.bug_504 import Bug504
from pages.BugsManual.bug_587 import Bug587
from pages.common import Common
from pages.conditions_v2 import apply_preconditions_to_link
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55

from src.src import CapitalComPageSrc


@pytest.mark.us_55
class TestManualDetectedBugs:
    page_conditions = None

    @allure.step(
        'Start retest manual TC_55!467 | Web pages with URLs of the FCA license '
        'are opened in menu item [Risk-management guide] when click on the link [broker]')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['ae', 'au'])
    @pytest.mark.parametrize('cur_role', random.sample(['Auth', 'NoAuth', 'NoReg'], 1, counts=[1, 1, 10]))
    @pytest.mark.bug_467
    def test_467(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         # Check: Web pages with URLs of the FCA license are opened
         in menu item [Risk-management guide] when click on the link [broker]
         Language: EN
         License: ASIC, SCA, CYSEC
         Author: Aleksei Kurochkin
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "467",
            "Web pages with URLs of the FCA license are opened "
            "in menu item [Risk-management guide] when click on the link [broker]",
            False,
            False
        )

        # Arrange
        link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        test_el = Bug467(d, link, bid)
        test_el.open_risk_management_page(d, cur_language, cur_country, link)

        # Act
        test_el.click_link_broker()

        # Assert
        if not test_el.should_be_au_or_ae_page():
            Common.pytest_fail('Bug # 55!467 The page is opened in FCA licence')
        Common.save_current_screenshot(d, "AT_55!467 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW)

    @allure.step(
        'Start retest manual TC_55!504 | Link [Privacy Policy] is not active in Sing up form '
        'when selected SCA (AR language)')
    @pytest.mark.parametrize('cur_language', ['ar'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ['NoAuth', 'NoReg'])
    @pytest.mark.bug_504
    def test_504(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         # Check: Link [Privacy Policy] is not active in Sing up form when selected SCA (AR language)
         Language: AR
         License: SCA
         Author: Aleksei Kurochkin
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "504",
            "Link [Privacy Policy] is not active in Sing up form when selected SCA (AR language)",
            False,
            False
        )

        # Arrange
        link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        test_el = Bug504(d, link, bid)

        # Act
        test_el.click_sign_up()

        # Assert
        if not test_el.should_be_link_to_privacy_policy():
            Common.pytest_fail('Bug # 55!504 The link [Privacy Policy] is not active in Sing up form '
                               'when selected SCA (AR language)')
        Common.save_current_screenshot(d, "AT_55!504 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW)

    @allure.step(
        'Start retest manual TC_55!444 | Placeholder "Country search" is displayed in EN language '
        'in the search field of dropdown "البلد" (Country) in the modal window '
        '"الإعدادات الإقليمية" (Regional settings) when AR language and SCA license are selected')
    @pytest.mark.parametrize('cur_language', ['ar'])
    @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', ['NoAuth', 'NoReg'])
    @pytest.mark.bug_444
    def test_444(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: Scroll down to the footer >
                Click button "البلد" (Country) / "اللغة" (Language) >
                Click the arrow button of the dropdown "البلد" (Country) in pop up window
         Language: AR
         License: SCA
         Author: Aleksei Kurochkin
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "444",
            'Placeholder "Country search" is displayed in EN language '
            'in the search field of dropdown "البلد" (Country) in the modal window '
            '"الإعدادات الإقليمية" (Regional settings) when AR language and SCA license are selected',
            False,
            False
        )

        # Arrange
        link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        test_el = Bug444(d, link, bid)
        test_el.open_country_and_language_selection_pop_up_window()

        # Act
        test_el.click_dropdown_menu_country()

        # Assert
        if test_el.is_placeholder_in_english_language():
            Common.pytest_fail('Bug # 55!444 The placeholder is "Country search" -> EN instead of AR')
        Common.save_current_screenshot(d, "AT_55!444 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW)

    #
    # BUGS BELOW ARE SKIPPED (IN PROGRESS)
    #

    @pytest.mark.skip("in progress")
    @allure.step(
        'Start retest manual TC_55!429 | ???')  # todo
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['au'])
    @pytest.mark.parametrize('cur_role', random.sample(['Auth', 'NoAuth', 'NoReg'], 1))
    @pytest.mark.bug_429
    def test_429(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         # Check: ???? todo

         Language: EN
         License: ASIC
         Author: Aleksei Kurochkin
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "429",
            "???",  # todo
            False,
            False
        )

        # Arrange
        link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        test_el = Bug429(d, link, bid)
        test_el.open_commodities_page(d, cur_language, cur_country, link)
        test_el.open_silver_commodity()

        # Act
        test_el.open_the_article()

        # Assert
        if test_el.is_paragraph_with_bold_text_present():
            Common.pytest_fail('Bug # 55!429 ....')  # todo
        Common.save_current_screenshot(d, "AT_55!429 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW)

    @pytest.mark.skip("in progress")
    @allure.step(
        'Start retest manual TC_55!587 | ???')  # todo
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['au'])
    @pytest.mark.parametrize('cur_role', random.sample(['Auth', 'NoAuth', 'NoReg'], 1))
    @pytest.mark.bug_587
    def test_587(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         # Check: ???? todo

         Language: EN
         License: ASIC
         Author: Aleksei Kurochkin
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "587",
            "???",  # todo
            False,
            False
        )

        # Arrange
        link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        test_el = Bug587(d, link, bid)
        test_el.open_page_market_guides(d, cur_language, cur_country, link)
        test_el.click_shares_trading_guide()
        test_el.click_learn_more_about_ipos()

        # Act
        test_el.click_liquidity()

        # Assert
        if test_el.is_404_present_on_page():
            Common.pytest_fail('Bug # 55!587 ....')  # todo
        Common.save_current_screenshot(d, "AT_55!587 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW)
