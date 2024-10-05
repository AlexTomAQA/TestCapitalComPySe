"""
-*- coding: utf-8 -*-
@Time    : 2024/07/22 16:40 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

WHY_CAPITAL_MENU_ITEM_LOC = ("css selector", ".cc-nav__link.js-analyticsClick[href='https://capital.com/why-capital-com']")
INVESTMATE_LINK_LOC = ("css selector", "main > section:nth-child(7) p:nth-child(4) > a")
BREADCRUMB_LOC = ("css selector", ".cc-breadcrumbs span")
TITLE_LOC = ("css selector", "head > title")


class Bug315(BasePage):
    def click_why_capital_menu_item(self):
        print(f'\n{datetime.now()}   Click the Why Capital.com? menu item =>')
        el = Wait(self.driver, 5).until(EC.element_to_be_clickable(WHY_CAPITAL_MENU_ITEM_LOC))
        el.click()
        print(f'{datetime.now()}   => Done, the corresponding page is opened')
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')

    def click_investmate_link(self):
        print(f'\n{datetime.now()}   Click the Investmate link =>')
        link = Wait(self.driver, 5).until(EC.element_to_be_clickable(INVESTMATE_LINK_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            link
        )
        link.click()
        print(f'{datetime.now()}   => Done, the corresponding page is opened')
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')

    def should_be_investmate_page(self, cur_language):
        print(f'\n{datetime.now()}   Check if the Investmate page is opened =>')

        bc_name = ''
        title_name = ''

        match cur_language:
            case 'en':
                bc_name = ' Investmate app'
                title_name = 'Financial Trading Learning App | Capital.com'

        if bc_name in self.driver.find_element(*BREADCRUMB_LOC).text:
            if title_name in self.driver.find_element(*TITLE_LOC).text:
                print(f'{datetime.now()}   => The Mobile Apps page is opened')
                return True
        print(f'{datetime.now()}   => Wrong page')
        return False
