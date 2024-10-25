"""
-*- coding: utf-8 -*-
@Time    : 2024/10/25 19:50
@Author  : Artem Dashkov
"""
import time

import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common

BUG_NUMBER = '410'
LINK_LEARN_MORE_LOCATOR = (By.XPATH,
                           "//div[@class='js-ckeContent content_content__2ZOcD'] //a[contains(text(), 'Learn more')]")
ACCORDION_HOW_DO_YOU_TRADE_LOCATOR = (By.XPATH, "(//summary[@data-type='faq_chevron'])[2]")
LINK_CFDS_LOCATOR = (By.XPATH, "//div[@data-type='faq'] //a[contains(@href, 'cfd-trading')]")
LINK_ETFS_LOCATOR = (By.XPATH, "//div[@data-type='faq'] //a[contains(@href, 'top-etfs')]")
LINK_MARKET_LOCATOR = ()

class BUG_410(BasePage):

    @allure.step(f"{datetime.now()}   Start Arrange: find and click link 'Learn more...', "
                 f"find and click header of the accordion 'How do you trade...', "
                 f"find link of markets 'CFDs' or 'ETFs'")
    def arrange(self, d, link, type_of_markets):
        print(f"\n{datetime.now()}   1.1. Start Arrange: find and click link 'Learn more...'")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting link 'Learn more about commodities trading' on the page 'Commodities'
        if len(self.driver.find_elements(*LINK_LEARN_MORE_LOCATOR)) == 0:
            msg = f"The page 'Commodities' don't have link 'Learn more about commodities trading' in DOM"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   The page 'Commodities' have link 'Learn more about commodities trading' in DOM\n")

        # Scroll to the link 'Learn more about commodities trading'
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*LINK_LEARN_MORE_LOCATOR)[0]
        )

        # Check visibility link 'Learn more about commodities trading' on the page 'Commodities'
        print(f"{datetime.now()}   Start to check visibility link 'Learn more about commodities trading'\n")
        if not self.element_is_visible(LINK_LEARN_MORE_LOCATOR):
            msg = f"Link 'Learn more about commodities trading' don't visible"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Link 'Learn more about commodities trading' is visible \n")

        # Check clickability link 'Learn more about commodities trading' on the page 'Commodities'
        print(f"{datetime.now()}   Start to check clickability link 'Learn more about commodities trading'\n")
        if not self.element_is_clickable(LINK_LEARN_MORE_LOCATOR):
            msg = f"Link 'Learn more about commodities trading' don't clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Link 'Learn more about commodities trading' is clickable\n")
        url_link_learn_more = self.driver.find_element(*LINK_LEARN_MORE_LOCATOR).get_attribute("href")

        print(f'{datetime.now()}   Start to click on link "Learn more about commodities trading"')
        self.driver.find_element(*LINK_LEARN_MORE_LOCATOR).click()
        print(f'{datetime.now()}   End to click on target link "Learn more about commodities trading"')

        # Check target url
        print(f"Link of 'Learn more about commodities trading' is: {url_link_learn_more}")
        self.wait_for_target_url(url_link_learn_more, 5)
        print(f'{datetime.now()}   Current page is: {self.driver.current_url}')

        print(f"\n{datetime.now()}   1.2. Start Arrange: find and click accordion 'How do you trade commodities?'")
        # Check presenting accordion 'How do you trade commodities?'
        if len(self.driver.find_elements(*ACCORDION_HOW_DO_YOU_TRADE_LOCATOR)) == 0:
            msg = f"The page 'What is commodity trading' don't have accordion 'How do you trade commodities?' in DOM"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   The page 'What is commodity trading' have accordion "
              f"'How do you trade commodities?' in DOM\n")

        # Scroll to the accordion 'How do you trade commodities?'
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*ACCORDION_HOW_DO_YOU_TRADE_LOCATOR)[0]
        )

        # Check visibility accordion 'How do you trade commodities?'
        print(f"{datetime.now()}   Start to check visibility accordion 'How do you trade commodities?'\n")
        if not self.element_is_visible(ACCORDION_HOW_DO_YOU_TRADE_LOCATOR):
            msg = f"Accordion 'How do you trade commodities?' don't visible"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Accordion 'How do you trade commodities?' is visible \n")

        # Check clickability accordion 'How do you trade commodities?'
        print(f"{datetime.now()}   Start to check clickability accordion 'How do you trade commodities?'\n")
        if not self.element_is_clickable(ACCORDION_HOW_DO_YOU_TRADE_LOCATOR):
            msg = f"Accordion 'How do you trade commodities?' don't clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Accordion 'How do you trade commodities?' is clickable\n")

        print(f"{datetime.now()}   Start to click on accordion 'How do you trade commodities?'")
        self.driver.find_element(*ACCORDION_HOW_DO_YOU_TRADE_LOCATOR).click()
        print(f"{datetime.now()}   End to click on accordion 'How do you trade commodities?'")
        time.sleep(1)

        print(f"\n{datetime.now()}   1.3. Start Arrange: find and click link 'CFDs' or 'exchange traded funds (ETFs)'")
        print(f"\n{datetime.now()}   Type of market is {type_of_markets}.")
        global LINK_MARKET_LOCATOR
        match type_of_markets:
            case 'CFDs':
                LINK_MARKET_LOCATOR = LINK_CFDS_LOCATOR
            case 'ETFs':
                LINK_MARKET_LOCATOR = LINK_ETFS_LOCATOR

        # Check presenting link 'CFDs' or 'ETFs'
        if len(self.driver.find_elements(*LINK_MARKET_LOCATOR)) == 0:
            msg = f"The page 'What is commodity trading' don't have link '{type_of_markets}' in DOM"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   The page 'What is commodity trading' have link '{type_of_markets}' in DOM\n")

        # Scroll to the link 'CFDs' or 'ETFs'
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*LINK_MARKET_LOCATOR)[0]
        )

        # Check visibility link 'CFDs' or 'ETFs'
        print(f"{datetime.now()}   Start to check visibility link '{type_of_markets}'\n")
        if not self.element_is_visible(LINK_MARKET_LOCATOR):
            msg = f"Link '{type_of_markets}' don't visible"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Link '{type_of_markets}' is visible \n")

        # Check clickability link 'CFDs' or 'ETFs'
        print(f"{datetime.now()}   Start to check clickability link '{type_of_markets}'\n")
        if not self.element_is_clickable(LINK_MARKET_LOCATOR):
            msg = f"Link '{type_of_markets}' don't clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Link '{type_of_markets}' is clickable\n")

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d, type_of_markets):

        print(f"\n{datetime.now()}   2. Start Act. Click on the link '{type_of_markets}'")
        self.driver.find_element(*LINK_MARKET_LOCATOR).click()
        print(f"\n{datetime.now()}   Link '{type_of_markets}' is clicked\n")

    @allure.step(f"{datetime.now()}   3. Start Assert. Check message '404 not found' on the opened page")
    def assert_(self, d):
        print(f"{datetime.now()}   3. Start Assert. Check message '404 not found' on the opened page")

        # Check presenting 'en-gb' in url on the opened page
        print(f"{datetime.now()}   IS 'en-gb' in url on the opened page?")
        if 'en-gb' in self.driver.current_url:
            msg = f"Opened page have FCA license insted of SCA, url is: {self.driver.current_url}"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        elif 'en-ae' in self.driver.current_url:
            if ('cfd-trading' or 'top-etfs') in self.driver.current_url:
                print(f"{datetime.now()}   Current page opened in necessary license but need check screenshot")
                Common.save_current_screenshot(d, f"Need to check content of opened page")
            else:
                msg = f"Need to check content of opened page, url is: {self.driver.current_url}"
                print(f"{datetime.now()}   => {msg}")
                Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        else:
            msg = f"Need to check content of opened page, url is: {self.driver.current_url}"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        return True
