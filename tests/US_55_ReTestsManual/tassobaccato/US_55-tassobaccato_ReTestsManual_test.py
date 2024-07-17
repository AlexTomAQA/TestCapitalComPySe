"""
-*- coding: utf-8 -*-
@Time    : 2024/05/06 22:00
@Author  : Kasilà
"""
import pytest
import allure

from pages.BugsManual.bug_039 import AppliedFilters
from pages.BugsManual.bug_061 import Sidebar
from pages.Menu.menu import MenuSection
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55

from pages.Elements.MyAccountButton import MyAccountButton
from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.conditions_new import NewConditions


@pytest.mark.us_55
class TestManualDetectedBugs:
    page_conditions = None

    @allure.step("Start retest manual TC_55!005 of button [My account] in the Header")
    @pytest.mark.parametrize('cur_language', [''])
    @pytest.mark.parametrize('cur_country', ['gb'])
    @pytest.mark.parametrize('cur_role', ["Auth"])
    @pytest.mark.bug_005
    def test_005(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
         Check: Button [My account] in the Header
         Language: En. License: FCA.
         Author: Kasila
         """
        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "005",
            "The 'My Account' menu is not displayed when click on the [My Account] button in the Header"
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MyAccountButton(d, link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, link)

    @allure.step("Start retest manual AT_55!00_039 of filters application in the 'Live shares prices' widget")
    @pytest.mark.parametrize('cur_country', ['es', 'ua', 'au'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.bug_039
    def test_039(self, worker_id, d, cur_language_2_rnd_from_14, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Filters application in the 'Live shares prices' widget
        Language: All
        License: CYSEC, SCB, ASIC
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_2_rnd_from_14, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "039",
            "Applied filters 'Region/Sectors' are not displayed after selecting an item from the "
                   "'Most traded' dropdown in the 'Live shares prices'  widget on the 'Shares' page"
            )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_2_rnd_from_14, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_shares_market_menu(d, cur_language_2_rnd_from_14, cur_country, link)

        test_element = AppliedFilters(d, cur_item_link, bid)
        test_element.test_(d, cur_language_2_rnd_from_14, cur_country,cur_role, cur_item_link)

    @allure.step('Start retest manual AT_55!061 of the  presence of the "Crypto trading  guide" sidebar on '
                 '"Bitcoin Gold" and "Crypto vs stocks: What is the difference?" pages')
    @pytest.mark.parametrize('cur_country', ['es', 'ua', 'au'])
    @pytest.mark.parametrize('cur_role', ["NoReg", "Auth", "NoAuth"])
    @pytest.mark.parametrize('sidebar_item', ['Bitcoin Gold', 'Cryptocurrencies vs. Stocks: What is the Difference?'])
    @pytest.mark.bug_061
    def test_061(self, worker_id, d, cur_language_2_rnd_from_7, cur_country, cur_role, cur_login, cur_password,
                 sidebar_item):
        """
        Check: presence of the sidebar "Crypto Trading Guide" on the "Bitcoin Gold" and "Cryptocurrencies vs. Stocks:
        What's the Difference?" pages.
        Language: EN, DE, ZH, RU, ES,IT, PL
        License: CYSEC, SCB, ASIC
        Author: Kasila
        """

        bid = build_dynamic_arg_for_us_55(
            d, worker_id, cur_language_2_rnd_from_7, cur_country, cur_role,
            "55", "ReTests of Manual Detected Bugs",
            "061",
            'Sidebar " Crypto trading  guide" is absent on pages "Bitcoin Gold" and "Crypto vs '
                   'stocks: What’s the difference?"'
        )

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language_2_rnd_from_7, cur_country, cur_role, cur_login, cur_password)

        menu = MenuSection(d, link)
        cur_item_link = menu.open_education_cryptocurrency_trading_menu(d, cur_language_2_rnd_from_7, cur_country,
                                                                        link)

        test_element = Sidebar(d, cur_item_link, bid)
        match cur_language_2_rnd_from_7:
            case "" | "de" | "zh":
                test_element.sidebar_en_de_zh(d, cur_item_link, sidebar_item)
            case "ru" | "es" | "it" | "pl":
                test_element.sidebar_ru_es_it_pl(d, cur_item_link, sidebar_item)
        test_element.assert_(sidebar_item)
