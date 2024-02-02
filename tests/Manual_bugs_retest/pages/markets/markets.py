import time

import allure
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from pages.base_page import BasePage


class MarketsSection(BasePage):
    MARKETS_LIST_PAGINATION = (By.CSS_SELECTOR, '[data-type="markets_list_pagination"]')

    # forex
    MARKETS_FOREX_MOST_TRADE_LIST = (By.CSS_SELECTOR, '[data-type="markets_list_deep"]')
    MARKETS_FOREX_MOST_TRADE_LINK_LIST = (By.CSS_SELECTOR, '[data-type="markets_list_deep"] a')
    MARKETS_FOREX_MOST_TRADE_INSTRUMENT_CONTENT = (By.CSS_SELECTOR, '.js-ckeContent h3')
    MARKETS_FOREX_MOST_TRADE_INSTRUMENT_404 = (By.CSS_SELECTOR, 'section.blockMd .gLg h1')
