"""
-*- coding: utf-8 -*-
@Time    : 2024/07/18 11:30 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

GO_TO_ALL_COMMODITIES_LINK_LOC = ("css selector", "a[data-type='wdg_go_to_market_deeplink']")


class CommoditiesPageOpenCheck(BasePage):
    def click_go_to_all_commodities_link(self):
        print(f'\n{datetime.now()}   Click the [Go to all commodities] link =>')
        link = Wait(self.driver, 2).until(EC.element_to_be_clickable(GO_TO_ALL_COMMODITIES_LINK_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            link
        )
        link.click()
        print(f'{datetime.now()}   The link is clicked, the corresponding page is opened')
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')

    def should_not_be_main_page(self):
        print(f"\n{datetime.now()}   Make sure that current URL is not main page's URL =>")
        if self.driver.current_url == "https://capital.com/":
            print(f"{datetime.now()}   => Current URL is EQUAL to main page's URL")
            return False
        print(f"{datetime.now()}   => Current URL is not equal to main page's URL")
        return True
