"""
-*- coding: utf-8 -*-
@Time    : 2024/07/07 21:20 GMT+5
@Author  : Sergey Aiidzhanov
"""

import time
from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

NEWS_AND_ANALYSIS_MENU_SECTION_LOC = ("css selector", "a[data-type='nav_id10']")
BREADCRUMB_LOC = ("css selector", ".cc-breadcrumbs span")
TITLE_LOC = ("css selector", "h1.hero")


class NewsAndAnalysisMenuSection(BasePage):
    def click_element(self):
        print(f'\n{datetime.now()}   Click the News and Analysis menu section =>')
        btn = Wait(self.driver, 5).until(EC.element_to_be_clickable(NEWS_AND_ANALYSIS_MENU_SECTION_LOC))
        btn.click()
        print(f'{datetime.now()}   => Done, corresponding page is opened')
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')

    def should_be_news_and_analysis_page(self):
        time.sleep(1)
        print(f'\n{datetime.now()}   Check if the News and Analysis page is opened =>')
        if "教育" in self.driver.find_element(*BREADCRUMB_LOC).text:
            if "教育中心" in self.driver.find_element(*TITLE_LOC).text:
                print(f'{datetime.now()}   => Wrong page')
                return False
        print(f'{datetime.now()}   => The News and Analysis page is opened')
        return True
