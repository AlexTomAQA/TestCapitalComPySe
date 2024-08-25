"""
-*- coding: utf-8 -*-
@Time    : 2024/08/25 18:25 GMT+5
@Author  : Sergey Aiidzhanov
"""
from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

RSI_LINK_LOC = ('xpath', '//a[contains(text(), "RSI")]')
STOCHASTIC_LINK_LOC = ('xpath', '//a[contains(text(), "Stochastic Oscillator")]')
SUPPORT_LINK_LOC = ('xpath', '//a[contains(text(), "support and resistance")]')
BREADCRUMB_LOC = ('css selector', '.cc-breadcrumbs span')
TITLE_LOC = ('css selector', '.cc-banner h1')


class Bug332(BasePage):
    def click_rsi_trading_strategy_link(self):
        print(f'\n{datetime.now()}   Click the [RSI trading strategy: An educational guide] link =>')
        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(RSI_LINK_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()
        print(f'{datetime.now()}   => Done, the link is clicked')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

    def click_stochastic_oscillator_link(self):
        print(f'\n{datetime.now()}   Click the [Stochastic Oscillator] link =>')
        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(STOCHASTIC_LINK_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()
        print(f'{datetime.now()}   => Done, the link is clicked')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

    def click_support_and_resistance_link(self):
        print(f'\n{datetime.now()}   Click the [support and resistance] link =>')
        el = Wait(self.driver, 2).until(EC.element_to_be_clickable(SUPPORT_LINK_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            el
        )
        el.click()
        print(f'{datetime.now()}   => Done, the link is clicked')
        print(f'{datetime.now()}   => Current URL: {self.driver.current_url}')

    def should_be_stochastic_oscillator_strategy_page(self):
        print(f'\n{datetime.now()}   Check if the "Stochastic oscillator strategy" page is opened => ')

        try:
            self.driver.find_element(*BREADCRUMB_LOC)
        except NoSuchElementException:
            print(f'{datetime.now()}   => The page is not opened (Breadcrumb Element not found)')
            return False

        try:
            self.driver.find_element(*TITLE_LOC)
        except NoSuchElementException:
            print(f'{datetime.now()}   => The page is not opened (Title Element not found)')
            return False

        if 'Stochastic oscillator strategy' in self.driver.find_element(*BREADCRUMB_LOC).text:
            if 'Stochastic oscillator strategy' in self.driver.find_element(*TITLE_LOC).text:
                print(f'{datetime.now()}   => The "Stochastic oscillator strategy" page is opened')
                return True
        print(f'{datetime.now()}   => The wrong page is opened')
        return False

    def should_be_support_and_resistance_page(self):
        print(f'\n{datetime.now()}   Check if the "What is support and resistance?" page is opened => ')

        try:
            self.driver.find_element(*BREADCRUMB_LOC)
        except NoSuchElementException:
            print(f'{datetime.now()}   => The page is not opened (Breadcrumb Element not found)')
            return False

        try:
            self.driver.find_element(*TITLE_LOC)
        except NoSuchElementException:
            print(f'{datetime.now()}   => The page is not opened (Title Element not found)')
            return False

        if 'What is support and resistance?' in self.driver.find_element(*BREADCRUMB_LOC).text:
            if 'What is support and resistance?' in self.driver.find_element(*TITLE_LOC).text:
                print(f'{datetime.now()}   => The "What is support and resistance?" page is opened')
                return True
        print(f'{datetime.now()}   => The wrong page is opened')
        return False
