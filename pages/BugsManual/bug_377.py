"""
-*- coding: utf-8 -*-
@Time    : 2024/09/24 08:40
@Author  : Artem Dashkov
"""
import random

import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from src.src import CapitalComPageSrc

BLOCK_NAME = '"Capital.com is an execution-only brokerage platform…"'
LINK_NAME = '"Capital.com"'
BUG_NUMBER = '377'

BLOCK_LOCATOR = (By.XPATH, '//div[@class="box_box__5Jmfa box_sm__FGk8i grey"][1]')
LINK_LOCATOR = (By.XPATH,
                "//div[@class='box_box__5Jmfa box_sm__FGk8i grey'] //a[contains(text(), 'Capital.com')]")
ARTICLES_LOCATOR = (By.XPATH,
                    '//div[@class="article_content__1GOa_"]//a [@class="js-analyticsClick link_link__caosC"]')

MESSAGE_404_LOCATOR = (By.XPATH, "//p[@class='textCenter title404'][contains(text(), '404')]")

class BUG_377(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find articles, choose and click article, find block and link")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find articles, choose and click article, find block and link")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting articles on the page
        if len(self.driver.find_elements(*ARTICLES_LOCATOR)) == 0:
            msg = f"The page 'Market analysis' don't have articles"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   The page 'Why Capital.com?' have link {LINK_NAME} in DOM\n")

        # Choose random number of article and click
        number_articles = len(self.driver.find_elements(*ARTICLES_LOCATOR))
        print(f'{datetime.now()}   Number of articles is: {number_articles}')
        random_number_article = random.randint(1, number_articles)
        print(f'{datetime.now()}   Random number of article for click is: {random_number_article}')
        link_article = self.driver.find_elements(*ARTICLES_LOCATOR)[random_number_article-1].get_attribute("href")
        print(f'{datetime.now()}   Link of article for click is: {link_article}')
        print(f'{datetime.now()}   Start to click on article')

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*ARTICLES_LOCATOR)[random_number_article-1]
        )

        self.driver.find_elements(*ARTICLES_LOCATOR)[random_number_article-1].click()
        print(f'{datetime.now()}   End to click on article')

        # Check target url
        self.wait_for_target_url(link_article, 5)
        print(f'{datetime.now()}   Current page is: {self.driver.current_url}')

        # Check presenting link on the page
        if len(self.driver.find_elements(*LINK_LOCATOR)) == 0:
            msg = (f"The page 'Why Capital.com?' don't have link {LINK_NAME} in DOM")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   The page 'Why Capital.com?' have link {LINK_NAME} in DOM\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_element(*LINK_LOCATOR)
        )

        # Check visibility link on the page
        print(f"{datetime.now()}   Start to check visibility link {LINK_NAME}'\n")
        if not self.element_is_visible(LINK_LOCATOR):
            msg = f"Link {LINK_NAME} don't visible"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Link {LINK_NAME} visible \n")

        # Check clickability link on the page
        print(f"{datetime.now()}   Start to check clickability link {LINK_NAME}\n")
        if not self.element_is_clickable(LINK_LOCATOR):
            msg = f"Link {LINK_NAME} don't clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Link {LINK_NAME} clickable\n")

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):

        print(f"\n{datetime.now()}   2. Start Act. Click on the link {LINK_NAME}")

        self.driver.find_element(*LINK_LOCATOR).click()
        print(f"\n{datetime.now()}   Link {LINK_NAME} is clicked\n")

    @allure.step(f"{datetime.now()}   3. Start Assert. Check message '404 not found' on the opened page")
    def assert_(self, d):
        print(f"{datetime.now()}   3. Start Assert. Check message '404 not found' on the opened page")

        # Check presenting message '404 not found' on the opened page
        print(f"{datetime.now()}   IS message '404 not found' on the opened page?")
        if len(self.driver.find_elements(*MESSAGE_404_LOCATOR)) != 0:
            print(f"{datetime.now()}   Opened page have message '404 not found' in the DOM")

            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                self.driver.find_element(*MESSAGE_404_LOCATOR)
            )

            # Check visibility message '404 not found' on the opened page
            print(f"{datetime.now()}   IS message '404 not found' on the opened page?")
            if self.element_is_visible(MESSAGE_404_LOCATOR):
                msg = (f"Message '404 not found' is visible on the opened page")
                print(f"{datetime.now()}   => {msg}")
                Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")

        print(f"{datetime.now()}   Opened page don't have message '404 not found', but need to check content of page.")
        Common.save_current_screenshot(d, f"Opened page don't have message '404 not found'")
        self.driver.get(CapitalComPageSrc.URL_NEW_EN_AU)
        return True
