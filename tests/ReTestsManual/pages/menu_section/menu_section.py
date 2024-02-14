import time

import allure
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from pages.base_page import BasePage


class MenuSections(BasePage):

    BREADCRUMBS = (By.CSS_SELECTOR, '[class*="breadcrumbs"]')

    # markets
    MARKETS_PAGINATION_LIST = (By.CSS_SELECTOR, '[data-type="markets_list_pagination"]')
    MARKETS_MOST_TRADE_LIST = (By.CSS_SELECTOR, '[data-type="markets_list_deep"]')
    MARKETS_MOST_TRADE_SEARCH = (By.CSS_SELECTOR, '#marketlist_search')
    MARKETS_MOST_TRADE_SEARCH_LIST = (By.CSS_SELECTOR, '.search_dropdown__GAZ2m div.result_item__rY8mQ')
    MARKETS_MOST_TRADE_LINK_LIST = (By.CSS_SELECTOR, '[data-type="markets_list_deep"] a')
    MARKETS_MOST_TRADE_INSTRUMENT_CONTENT = (By.CSS_SELECTOR, '.js-ckeContent h3')
    MARKETS_MOST_TRADE_INSTRUMENT_404 = (By.CSS_SELECTOR, 'section.blockMd .gLg h1')
    MARKETS_MOST_TRADE_INSTRUMENT_PAGE = (By.CSS_SELECTOR, '[data-type="market"]')
    MARKETS_MOST_TRADE_INSTRUMENT_KEY_STATS = (By.CSS_SELECTOR, '.helpers_frameLoader__7Uhll .heading_h2__kkLcC')
    MARKETS_SHARES_BANNER_TRY_DEMO_BTN = (By.CSS_SELECTOR, '[data-type="fullscreen_banner_block_btn2demo"]')
    MARKETS_SHARES_BANNER_SIGNUP_BTN = (By.CSS_SELECTOR, '[data-type="fullscreen_banner_block_btn1_signup"]')

    # way_to_trade
    WAYSTOTRADE_PROFESSIONAL_ELIGIBLE_BTN = (By.CSS_SELECTOR, '[data-type="eligibility_block_btn1"]')
    WAYSTOTRADE_PROFESSIONAL_APPLY_BTN = (By.CSS_SELECTOR, '[data-type="background_banner_block_btn1_custom"]')
    WAYSTOTRADE_PROFESSIONAL_NO_CAPITAL_YET_APPLY_BTN = (By.CSS_SELECTOR, 'button[data-type="apply_now_block_btn1"]')
    WAYSTOTRADE_PROFESSIONAL_EXISTING_CLIENT_BTN = (By.CSS_SELECTOR, '[data-type="apply_now_block_link2"]')
    WAYSTOTRADE_PROFESSIONAL_MAIN_BANNER = (By.CSS_SELECTOR, '[data-type="background_banner_block"]')
    WAYSTOTRADE_PROFESSIONAL_APPLY_NOW_TITLE = (By.CSS_SELECTOR, '.applyNow_applyNow__KQhnE h2')

    # trading platform
    TRADING_PLATFORM_SUPPORT_BTN = (By.CSS_SELECTOR, '[data-type="fullscreen_banner_block_btn1_custom"]')
    TRADING_PLATFORM_WEB_PLATFORM_WHY_CAPITAL_BLOCK = (By.CSS_SELECTOR, '.primary_box__jvUGh')
    TRADING_PLATFORM_WEB_PLATFORM_WHY_CAPITAL_BTN = (By.CSS_SELECTOR, '.primary_box__jvUGh a')

    # why capital.com?
    # client_funds
    WHY_CAPITAL_CLIENT_FUNDS_CONTENTS_LIST = (By.CSS_SELECTOR, '[data-type="content_nav_anchor"]')
