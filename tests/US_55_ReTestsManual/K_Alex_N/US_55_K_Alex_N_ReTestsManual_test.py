"""
-*- coding: utf-8 -*-
@Date    : 18/10/2024
@Author  : Alexey Kurochkin
"""
from datetime import datetime
import random

import pytest
import allure
from selenium.common import NoSuchElementException

from pages.BugsManual.bug_429 import Bug429
from pages.BugsManual.bug_444 import Bug444
from pages.BugsManual.bug_467 import Bug467
from pages.BugsManual.bug_504 import Bug504
from pages.BugsManual.bug_513 import Bug513
from pages.BugsManual.bug_516 import Bug516
from pages.BugsManual.bug_587 import Bug587
from pages.BugsManual.bug_603 import Bug603
from pages.BugsManual.bug_634 import Bug634
from pages.common import Common
from pages.conditions_v2 import apply_preconditions_to_link
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55

from src.src import CapitalComPageSrc


@pytest.mark.us_55
class TestManualDetectedBugs:
    page_conditions = None

    def search_and_open_an_article_in_market_analysis_page(self, part_of_article_title):

        article_locator = ('xpath', f"//div[@id='alc']//b[contains(text(), '{part_of_article_title}')]")
        locator_link_next_page = ('xpath', '//a[@aria-label="Go to the next page"]')
        locator_last_page = ('xpath', '//a[@aria-label="Go to the next page"]/preceding::a[1]')

        def is_article_present():
            try:
                self.driver.find_element(*article_locator)
                return True
            except NoSuchElementException:
                return False

        def get_last_page() -> int:
            try:
                last_page_obj = self.driver.find_element(*locator_last_page)
                last_page_number = int(last_page_obj.text)
                return last_page_number
            except:
                raise Exception("Last page number was not found")

        def open_the_article():
            self.driver.find_element(*article_locator).click()

        def go_to_next_page():
            self.driver.find_element(*locator_link_next_page).click()

        last_page = get_last_page()

        for _ in range(1, last_page):
            if is_article_present():
                open_the_article()
                return
            else:
                go_to_next_page()

        else:
            raise Exception(f"{last_page} pages were checked. Artile was not found.")

    @allure.step(
        'Start retest manual TC_55!467 | Web pages with URLs of the FCA license '
        'are opened in menu item [Risk-management guide] when click on the link [broker]')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['ae', 'au'])
    @pytest.mark.parametrize('cur_role', random.sample(['Auth', 'NoAuth', 'NoReg'], 1, counts=[1, 1, 10]))
    @pytest.mark.bug_467
    def test_467(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: Web pages with URLs of the FCA license are opened
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
         Check: Link [Privacy Policy] is not active in Sing up form when selected SCA (AR language)
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

    @allure.step(
        'Start retest manual TC_55!429 |  The text in the block “What is the outlook for silver prices?” is '
        'displayed in bold font on the page “Why is the silver price falling? Sinks further below the pivotal '
        '$20 mark” when ASIC license is selected')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['au'])
    @pytest.mark.parametrize('cur_role', random.sample(['Auth', 'NoAuth', 'NoReg'], 1))
    @pytest.mark.bug_429
    def test_429(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: Menu section [Markets] >
                Menu item (Commodities) >
                Scroll down to the block “Commodities markets” >
                Click the link “Silver” in the widget “Trading instrument” >
                Scroll down to the block “Latest commodities articles” >
                Click the article link “Why is the silver price falling? Sinks further below the pivotal $20 mark” >
                Scroll down to the block “What is the outlook for silver prices?”

         Language: EN
         License: ASIC
         Author: Aleksei Kurochkin
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "429",
            "Menu section [Markets] > Menu item (Commodities) > Scroll down to the block “Commodities "
            "markets” > Click the link “Silver” in the widget “Trading instrument” > Scroll down to the block "
            "“Latest commodities articles” > Click the article link “Why is the silver price falling? Sinks "
            "further below the pivotal $20 mark” > Scroll down to the block “What is the outlook for silver prices?”",
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
            Common.pytest_fail('Bug # 55!429 there is paragraph\s with bold text')
        Common.save_current_screenshot(d, "AT_55!429 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW)

    @allure.step(
        'Start retest manual TC_55!587 | The page with “404 error message” is displayed after clicking the '
        'link “liquidity” in the block “Why do companies go public?” on the page “What is an IPO” when EN language '
        'is selected (SCA / FCA / ASIC / CYSEC licenses)')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['au', 'gb', 'ae', 'de'])
    @pytest.mark.parametrize('cur_role', random.sample(['Auth', 'NoAuth', 'NoReg'], 1))
    @pytest.mark.bug_587
    def test_587(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: Hover over menu section [Learn] >
                Click the menu item [Market guides] of the menu title [For trading beginners] >
                Click the link “Shares trading guide” >
                Click the link “Learn more about IPOs.” >
                Click the link “liquidity”

         Language: EN
         License: SCA / FCA / ASIC / CYSEC
         Author: Aleksei Kurochkin
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "587",
            "Hover over menu section [Learn] > Click the menu item [Market guides] of the menu "
            "title [For trading beginners] > Click the link “Shares trading guide” > "
            "Click the link “Learn more about IPOs.” > Click the link “liquidity”",
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
            Common.pytest_fail('Bug # 55!587 page 404 is opened')
        Common.save_current_screenshot(d, "AT_55!587 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW)

    @allure.step(
        'Start retest manual TC_55!513 | The anchor "part 2" on the "Solana price prediction: Can SOL rebound?" '
        'page is absent when selected ASIC license')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['au'])
    @pytest.mark.parametrize('cur_role', random.sample(['Auth', 'NoAuth', 'NoReg'], 1))
    @pytest.mark.bug_513
    def test_513(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        test = self
        self.cur_language = cur_language
        self.cur_country = cur_country
        self.driver = d

        """
         Check: Hover over to [Markets] menu section >
                Click to [Market analysis] menu item>  
                Go through pages and find article "Solana price prediction: Can SOL rebound?" >
                Click to [Solana to US Dollar] anchor link in "Table of Contents" block

         Language: EN
         License: ASIC
         Author: Aleksei Kurochkin
         """

        self.bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "513",
            'Hover over to [Markets] menu section > Click to [Market analysis] menu item > '
            'Go through pages and find article "Solana price prediction: Can SOL rebound?" > '
            'Click to [Solana to US Dollar] anchor link in "Table of Contents" block',
            False,
            False
        )

        # Arrange
        self.link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        self.bug = Bug513(test)
        self.bug.open_market_analysis_page(test)
        self.search_and_open_an_article_in_market_analysis_page("Solana price prediction")

        # Act
        self.bug.is_link_to_part2_present_in_table_of_content()

        # Assert
        if not self.bug.is_part2_present_in_titles():
            Common.pytest_fail('Bug # 55!513 link to part2 in table of content do not work')
        Common.save_current_screenshot(d, "AT_55!513 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW)

    @allure.step(
        'Start retest manual TC_55!516 | The [collapse] link is leads to non-existent page in the '
        '"The graph (GRT) price prediction..." article after click to [collapse] link')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['au'])
    @pytest.mark.parametrize('cur_role', random.sample(['Auth', 'NoAuth', 'NoReg'], 1))
    @pytest.mark.bug_516
    def test_516(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        test = self
        self.cur_language = cur_language
        self.cur_country = cur_country
        self.driver = d

        """
         Check: Menu section [Markets] > 
                Menu item [Markets analysis] > 
                article "The graph (GRT) price prediction.." > 
                Click on the [collapse] link
         Language: EN
         License: ASIC
         Author: Aleksei Kurochkin
         """

        self.bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "516",
            'Menu section [Markets] > Menu item [Markets analysis] > '
            'article "The graph (GRT) price prediction.." > Click on the [collapse] link',
            False,
            False
        )

        # Arrange
        self.link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        self.bug = Bug516(test)
        self.bug.open_market_analysis_page(test)

        # Act
        self.search_and_open_an_article_in_market_analysis_page("The graph (GRT) price prediction")

        # Assert
        if not self.bug.is_possible_open_collapse_page():
            Common.pytest_fail('Bug # 55!516 not possible to open page "collapse"')
        Common.save_current_screenshot(d, "AT_55!516 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW)

    # @pytest.mark.skip()
    @allure.step(
        'Start retest manual TC_55!603 | ')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb', 'ae', 'au', 'de'])
    # @pytest.mark.parametrize('cur_language', ['ar'])
    # @pytest.mark.parametrize('cur_country', ['ae'])
    @pytest.mark.parametrize('cur_role', random.sample(['Auth', 'NoAuth', 'NoReg'], 1))
    @pytest.mark.bug_603
    def test_603(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        test = self
        self.cur_language = cur_language
        self.cur_country = cur_country
        self.driver = d

        """
         Check: 
         Language: EN
         License: SCA, FCA, CYSEC or ASIC
         Author: Aleksei Kurochkin
         """

        self.bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "603",
            '',
            False,
            False
        )

        # Arrange
        self.link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        self.bug = Bug603(test)
        self.bug.open_charges_and_fees_page(test)

        # Act
        self.bug.click_find_out_more_link()

        # Assert
        if self.bug.if_page_loader_present():
            Common.pytest_fail('Bug # 55!603 the page loader is present"')
        Common.save_current_screenshot(d, "AT_55!603 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW)

    @allure.step(
        'Start retest manual TC_55!634 | The loading spinner is displayed continuously on the page "Gold price '
        'predictions for the next..." after click on [Trade now]')
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb', 'ae', 'au', 'de'])
    @pytest.mark.parametrize('cur_role', random.sample(['NoAuth', 'NoReg'], 1))
    @pytest.mark.bug_634
    def test_634(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        test = self
        self.cur_language = cur_language
        self.cur_country = cur_country
        self.driver = d

        """
         Check: Menu section [Markets] > 
                Menu item [Markets analysis] > 
                Article "Gold price predictions for the next.." > 
                Click on the [Trade now] link > 
                Click on [Close] button
         Language: EN
         License: SCA, FCA, CYSEC or ASIC
         Author: Aleksei Kurochkin
         """

        self.bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "634",
            'The loading spinner is displayed continuously on the page "Gold price '
                    'predictions for the next..." after click on [Trade now]',
            False,
            False
        )

        # Arrange
        self.link = apply_preconditions_to_link(d, cur_language, cur_country, cur_role, cur_login, cur_password)
        self.bug = Bug634(test)
        self.bug.open_market_analysis_page(test)
        self.search_and_open_an_article_in_market_analysis_page("Gold price predictions for the next")
        self.bug.click_try_demo()

        # Act
        self.bug.close_pop_up_window()

        # Assert
        if self.bug.if_page_loader_present():
            Common.pytest_fail('Bug # 55!634 the page loader is present')
        Common.save_current_screenshot(d, "AT_55!634 Pass")

        # Postconditions
        print(f'\n{datetime.now()}   Applying postconditions...')
        Common.browser_back_to_link(d, CapitalComPageSrc.URL_NEW)
