"""
-*- coding: utf-8 -*-
@Time    : 2023/05/23 19:00 GMT+3
@Author  : Suleyman Alirzaev
"""
import allure
import pytest

from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonBuyInContentBlock import BuyButtonContentBlock
from pages.Elements.ButtonGetStartedOnStickyBar import GetStartedOnStickyBar
from pages.Elements.ButtonOnHorizontalBanner import ButtonOnHorizontalBanner
from pages.Elements.ButtonOnVerticalBanner import ButtonOnVerticalBanner
from pages.Elements.ButtonSellInContentBlock import SellButtonContentBlock
from pages.Elements.ButtonStartTradingInContent import ContentStartTrading
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.common import Common
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v4

count = 1


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    file_name = "tests/US_11_Education/US_11-02-05_Cryptocurrency_trading/list_of_href.txt"
    list_item_link = Common().generate_cur_item_link_parameter(file_name)
    metafunc.parametrize("cur_item_link", list_item_link, scope="class")


def check_language(cur_language):
    if cur_language not in ['en', 'de', "es", "it", "pl", "ro", "ru", "zn"]:
        return
    pytest.skip(f"This test is not for {cur_language} language")


def check_country(cur_country):
    if cur_country in ["gb"]:
        pytest.skip(f"This test is not for {cur_country} country")


@pytest.mark.us_11_02_05
class TestCryptocurrencyTrading:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    @pytest.mark.test_01
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Start Trading] on Main banner
        Language: EN, DE, ES, IT, PL, RO, RU, ZN. License: All, except FCA (GB country)
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_01", "Testing button [Start Trading] on Main banner")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "it", "pl", "ro", "ru", "zh"])
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerStartTrading(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Try demo] on Main banner")
    @pytest.mark.test_02
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Try demo] on Main banner
        Language: EN, DE, ES, IT, PL, RO, RU, ZN. License: All, except FCA (GB country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_02", "Testing button [Try demo] on Main banner")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "it", "pl", "ro", "ru", "zh"])
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerTryDemo(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    @pytest.mark.test_03
    def test_03_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Trade] in Most traded block
        Language: EN, DE, ES, IT, PL, RO, RU, ZN. License: All, except FCA (GB country)
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_03", "Testing button [Trade] in Most traded block")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "it", "pl", "ro", "ru", "zh"])
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Sell] in content block")
    @pytest.mark.test_04
    def test_04_content_block_button_sell(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Sell] in content block
        Language:EN, DE, ES, IT, PL, RO, RU. License: All,except FCA (GB country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_04", "Testing button [Sell] in content block")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "it", "pl", "ro", "ru"])
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = SellButtonContentBlock(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Buy] in content block")
    @pytest.mark.test_05
    def test_05_content_block_button_buy(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Buy] in content block
        Language:EN, DE, ES, IT, PL, RO, RU. License: All,except FCA (GB country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_05", "Testing button [Buy] in content block")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "it", "pl", "ro", "ru"])
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BuyButtonContentBlock(d, cur_item_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Get started] on Sticky bar")
    @pytest.mark.test_06
    def test_06_sticky_bar_button_get_started(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Get started] on Sticky bar
        Language: EN, DE, ES, IT, PL, RO, RU. License: All,except FCA (GB country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_06", "Testing button [Get started] on Sticky bar")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "it", "pl", "ro", "ru"])
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = GetStartedOnStickyBar(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test of button [Start trading] in content block")
    @pytest.mark.test_07
    def test_07_start_trading_in_article_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [Start trading] in content block
        Language: EN, DE, ES, IT, ZN. License: All,except FCA (GB country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_07", "Testing button [Start trading] in content block")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "it", "zn"])
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ContentStartTrading(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)

    @allure.step("Start test button on the block [Vertical banner]")
    @pytest.mark.test_08
    def test_08_block_vertical_banner_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button on the block [Vertical banner]
        Language: DE, ES, IT, PL, RO, RU, ZH. License: All,except FCA (GB country)
        For "Authorized user" role:
            The Trading platform (TP) or Demo trading platform (TPD) are opened depending on the banner:
            TP if banner from the Live mode banners list / TPD if banner from the Demo mode banners list
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_08", "Testing button on the block [Vertical banner]")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["de", "es", "it", "pl", "ro", "ru", "zh"])
        Common().check_language_in_list_and_skip_if_not_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # банеры должны открываться в Demo mode for US_00
        banner00_ver_tpd = []
        # банеры должны открываться в Live mode for US_00
        banner00_ver_tp = []
        # баннеры открываются в Demo mode for US_01
        banner01_ver_tpd = ['168', '253', '380', '393']
        # баннеры открываются в Live mode for US_01
        banner01_ver_tp = ['198', '293', '381', '391', '426']

        test_element = ButtonOnVerticalBanner(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link,
                                        banner00_ver_tpd, banner00_ver_tp, banner01_ver_tpd, banner01_ver_tp)

    @allure.step("Start test button on the block [Horizontal banner]")
    @pytest.mark.test_09
    def test_09_block_horizontal_banner_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button on the block [Horizontal banner]
        Language: DE, ES, IT, PL, RO, RU, ZH. License: All,except FCA (GB country)
        For "Authorized user" role:
            The Trading platform (TP) or Demo trading platform (TPD) are opened depending on the banner:
            TP if banner from the Live mode banners list / TPD if banner from the Demo mode banners list
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_09", "Testing button on the block [Horizontal banner]")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["de", "es", "it", "pl", "ro", "ru", "zh"])
        Common().check_language_in_list_and_skip_if_not_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # банеры должны открываться в Demo mode for US_00
        banner00_hor_tpd = []
        # банеры должны открываться в Live mode for US_00
        banner00_hor_tp = []
        # баннеры открываются в Demo mode for US_01
        banner01_hor_tpd = ['199']
        # баннеры открываются в Live mode for US_01
        banner01_hor_tp = ['169', '254', '294', '379', '390', '429', '430']

        test_element = ButtonOnHorizontalBanner(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link,
                                        banner00_hor_tpd, banner00_hor_tp, banner01_hor_tpd, banner01_hor_tp)

    @allure.step("Start test of button [Create your account] in block [Steps trading]")
    @pytest.mark.test_10
    def test_10_block_steps_trading_button_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: EN, DE, ES, IT, PL, RO, RU, ZN. License: All,except FCA (GB country)
        """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.05", "Education > Menu item [Cryptocurrency trading]",
            ".01_10", "Testing button [Create your account] in block [Steps trading]")

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "de", "es", "it", "pl", "ro", "ru", "zn"])
        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, cur_item_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_item_link)
