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
    MARKETS_MOST_TRADE_LINK_LIST = (By.CSS_SELECTOR, '[data-type="markets_list_deep"] a')
    MARKETS_MOST_TRADE_INSTRUMENT_CONTENT = (By.CSS_SELECTOR, '.js-ckeContent h3')
    MARKETS_MOST_TRADE_INSTRUMENT_404 = (By.CSS_SELECTOR, 'section.blockMd .gLg h1')
    MARKETS_MOST_TRADE_INSTRUMENT_KEY_STATS = (By.CSS_SELECTOR, '.helpers_frameLoader__7Uhll .heading_h2__kkLcC')

    # way_to_trade
    WAYSTOTRADE_PROFESSIONAL_ELIGIBLE_BTN = (By.CSS_SELECTOR, '[data-type="eligibility_block_btn1"]')
    WAYSTOTRADE_PROFESSIONAL_APPLY_BTN = (By.CSS_SELECTOR, '[data-type="background_banner_block_btn1_custom"]')
    WAYSTOTRADE_PROFESSIONAL_NO_CAPITAL_YET_APPLY_BTN = (By.CSS_SELECTOR, 'button[data-type="apply_now_block_btn1"]')
    WAYSTOTRADE_PROFESSIONAL_EXISTING_CLIENT_BTN = (By.CSS_SELECTOR, '[data-type="apply_now_block_link2"]')
    WAYSTOTRADE_PROFESSIONAL_MAIN_BANNER = (By.CSS_SELECTOR, '[data-type="background_banner_block"]')

    # trading platform
    TRADING_PLATFORM_SUPPORT_BTN = (By.CSS_SELECTOR, '[data-type="fullscreen_banner_block_btn1_custom"]')
