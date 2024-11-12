"""
-*- coding: utf-8 -*-
@Time    : 2024/10/15 21:20 GMT+5
@Author  : Sergey Aiidzhanov
"""
from datetime import datetime

from pages.base_page import BasePage
from pages.Menu.New.from_about_us_menu_open_client_funds import MenuNew
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


WHATSAPP_LINK_LOC = ('xpath', '//a[text()="WhatsApp"]')
TITLE_LOC = ('xpath', '//h3[text()="Capital.com"]')
ACTION_BTN_LOC = ('css selector', '#action-button')


class Bug416(BasePage):

    @staticmethod
    def open_client_funds_page(d, cur_language, cur_country, link):
        MenuNew(d).from_about_us_menu_open_client_funds(d, cur_language, cur_country, link)

    def click_whatsapp_link(self):
        print(f'\n{datetime.now()}   Click WhatsApp link =>')

        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(WHATSAPP_LINK_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()

        print(f'{datetime.now()}   => Done, current URL: {self.driver.current_url}')

    def should_be_whatsapp_redirecting_page(self):
        print(f'\n{datetime.now()}   Check if the page with the link redirecting to the WhatsApp chat is opened =>')

        tabs = self.driver.window_handles
        print(f'\n{datetime.now()}   TABS QUANTITY: {len(tabs)}')
        if len(tabs) > 1:
            self.driver.switch_to.window(tabs[len(tabs) - 1])

        try:
            if Wait(self.driver, 2).until(EC.visibility_of_element_located(TITLE_LOC)):
                if Wait(self.driver, 2).until(EC.element_to_be_clickable(ACTION_BTN_LOC)):
                    print(f'{datetime.now()}   => The page is opened')
                    print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')
                    self.driver.close()
                    self.driver.switch_to.window(tabs[0])
                    print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')
                    return True
        except TimeoutException:
            print(f'{datetime.now()}   => The page is not opened')
            print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')
            self.driver.close()
            self.driver.switch_to.window(tabs[0])
            print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')
            return False
