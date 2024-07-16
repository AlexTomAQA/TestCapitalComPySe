"""
-*- coding: utf-8 -*-
@Time    : 2024/07/10 20:30 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

DEMO_ACCOUNT_MENU_ITEM_LOC = ("css selector", "a[data-type='nav_id578']")
TRADING_GUIDES_LINK_LOC = ("xpath", "//strong/a[contains(@href, '/trading-guides')]")
BREADCRUMB_LOC = ("css selector", ".cc-breadcrumbs span")
TITLE_LOC = ("css selector", "h1.hero")


class TradingGuidesPageDeTest(BasePage):
    def click_demo_acc_menu_item(self):
        print(f'\n{datetime.now()}   Click the Demo Account menu item =>')
        btn = Wait(self.driver, 5).until(EC.element_to_be_clickable(DEMO_ACCOUNT_MENU_ITEM_LOC))
        btn.click()
        print(f'{datetime.now()}   => Done, the corresponding page is opened')
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')

    def click_trading_guides_link(self):
        print(f'\n{datetime.now()}   Click the Trading Guides link =>')
        link = Wait(self.driver, 5).until(EC.element_to_be_clickable(TRADING_GUIDES_LINK_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            link
        )
        link.click()
        print(f'{datetime.now()}   => Done, the corresponding page is opened')
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')

    def should_be_trading_guides_page(self):
        print(f'\n{datetime.now()}   Check if the Trading Guides page is opened =>')
        if "Trading-Leitfäden" in self.driver.find_element(*BREADCRUMB_LOC).text:
            if "Trading-Leitfäden" in self.driver.find_element(*TITLE_LOC).text:
                print(f'{datetime.now()}   => The Trading Guides page is opened')
                return True
        print(f'{datetime.now()}   => Wrong page')
        return False
