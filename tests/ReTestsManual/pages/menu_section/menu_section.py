import time

import allure
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from pages.base_page import BasePage


class MarketsSection(BasePage):

    MARKETS_PAGINATION_LIST = (By.CSS_SELECTOR, '[data-type="markets_list_pagination"]')
    MARKETS_MOST_TRADE_LIST = (By.CSS_SELECTOR, '[data-type="markets_list_deep"]')
    MARKETS_MOST_TRADE_LINK_LIST = (By.CSS_SELECTOR, '[data-type="markets_list_deep"] a')
    MARKETS_MOST_TRADE_INSTRUMENT_CONTENT = (By.CSS_SELECTOR, '.js-ckeContent h3')
    MARKETS_MOST_TRADE_INSTRUMENT_404 = (By.CSS_SELECTOR, 'section.blockMd .gLg h1')
    MARKETS_MOST_TRADE_INSTRUMENT_KEY_STATS = (By.CSS_SELECTOR, '.helpers_frameLoader__7Uhll .heading_h2__kkLcC')


class WaysToTradeSection(BasePage):
    # professional
    WAYSTOTRADE_PROFESSIONAL_ELIGIBLE_BTN = (By.CSS_SELECTOR, '[data-type="eligibility_block_btn1"]')
    WAYSTOTRADE_PROFESSIONAL_APPLY_BTN = (By.CSS_SELECTOR, '[data-type="background_banner_block_btn1_custom"]')

