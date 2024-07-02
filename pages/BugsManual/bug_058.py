"""
-*- coding: utf-8 -*-
@Time    : 2024/06/27 20:00
@Author  : Artem Dashkov
"""
from datetime import datetime
import allure

from pages.common import Common
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ContentBlockLocators
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

BUTTON_NAME = '[Bullish]'
BLOCK_NAME = '"What is your sentiment?"'
BUTTON_LOCATOR = (By.CSS_SELECTOR, '.sentiment__btn.js_vote_bullBear[data-type="bullBearWidget-vote-bull"]')
BLOCK_LOCATOR = (By.CSS_SELECTOR, '.sentiment[data-type="bullBearWidget"]')
ARTICLES_LOCATOR = (By.XPATH, "//a [@class='main-article-item__thumb']")
ARTICLE_TITLE_LOCATOR = (By.CSS_SELECTOR, ".sentiment__step.js-vote-step0 h2")
YOU_VOTED_BULLISH_LOCATOR = (By.XPATH, '//p[@class="js-vote-bull"]')
STATUS_OF_SENTIMENT_LOCATOR = (By.CSS_SELECTOR, '[class*="sentiment__step js-vote-step0"]')


class WhatIsYourSentimentWidget(BasePage):
    global BUTTON_NAME
    global BLOCK_NAME
    global BUTTON_LOCATOR
    global BLOCK_LOCATOR
    global ARTICLES_LOCATOR
    global ARTICLE_TITLE_LOCATOR

    def __init__(self, browser, link, bid):
        self.list_of_rest_numbers_articles = None
        self.first_article_with_widget = None
        self.trading_instrument_name = None
        self.what_is_your_sentiment_widget = []

        super().__init__(browser, link, bid)

    def arrange(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        # Check presenting articles
        print(f"{datetime.now()}   IS articles present on this page? =>")
        if len(self.driver.find_elements(*ARTICLES_LOCATOR)) == 0:
            msg = f"Articles are NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => Articles present on this page!\n")

        quantity_articles = len(self.driver.find_elements(*ARTICLES_LOCATOR))
        list_of_numbers_articles = list(range(0, quantity_articles))  # for example [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.list_of_rest_numbers_articles = list_of_numbers_articles.copy()

        # Selected random (first in line) article with block "What is your sentiment..."
        for number_article in list_of_numbers_articles:
            print(f'{datetime.now()}   => Number_article: {number_article}')
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                self.driver.find_elements(*ARTICLES_LOCATOR)[number_article]
            )
            print(f'{datetime.now()}   => Scrolled on the article: {number_article}')

            self.driver.find_elements(*ARTICLES_LOCATOR)[number_article].click()
            print(f'{datetime.now()}   => Clicked on title of article')
            print(f'{datetime.now()} Current page is: {self.driver.current_url}\n')

            # Check presenting widget "What is your sentiment..."
            print(f"{datetime.now()}   Widget present on this page? =>")
            if len(self.driver.find_elements(*BLOCK_LOCATOR)) == 0:
                print(f"{datetime.now()}   => Widget not present on this page.\n")
                self.list_of_rest_numbers_articles.remove(number_article)
                self.driver.back()
                # self.wait_for_change_url(cur_item_link, timeout=30)
                continue
            print(f"{datetime.now()}   => Widget present on this page!")
            self.list_of_rest_numbers_articles.remove(number_article)

            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                self.driver.find_elements(*BLOCK_LOCATOR)[0]
            )
            print(f'{datetime.now()}   => Scrolled on the Widget.\n')

            break

        # Check presenting and visible article's title
        print(f"{datetime.now()}   Article's title present on this page? =>")
        if len(self.driver.find_elements(*ARTICLE_TITLE_LOCATOR)) == 0:
            print(f"{datetime.now()}   => Article's title not present on this page.\n")
            # self.wait_for_change_url(cur_item_link, timeout=30)
            Common.pytest_fail()
        print(f"{datetime.now()}   => Article's title present on this page!\n")

        # Get name of trading instrument
        article_title = self.driver.find_elements(*ARTICLE_TITLE_LOCATOR)[0].text
        print(f"article_title: {article_title}")
        self.trading_instrument_name = article_title.split()[-1].replace("?", "") # for example AUD/USD
        print(f"{datetime.now()}   Name of trading instrument is: {self.trading_instrument_name}.")

        # Check presenting and visible [Bullish] button
        self.element_is_present_and_visible_v2(BUTTON_LOCATOR, "[Bullish] button")

        # [Bullish] button click
        self.driver.find_element(*BUTTON_LOCATOR).click()
        print(f"{datetime.now()}   [Bullish] button clicked.")

    def act(self, d):
        print(f"\n{datetime.now()}   2. Act")

        # Selected random (second) article with block "What is your sentiment..."
        for number_second_article in self.list_of_rest_numbers_articles:
            self.driver.find_elements(*ARTICLES_LOCATOR)[number_second_article].click()

            # Check presenting widget "What is your sentiment..."
            print(f"{datetime.now()}   Widget present on this page? =>")
            if len(self.driver.find_elements(*BLOCK_LOCATOR)) == 0:
                print(f"{datetime.now()}   => Widget not present on this page.")
                self.driver.back()
                continue
            print(f"{datetime.now()}   => Widget present on this page!\n")

            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                self.driver.find_elements(*BLOCK_LOCATOR)[0]
            )
            # Get name of trading instrument
            second_article_title = self.driver.find_element(*ARTICLE_TITLE_LOCATOR).text
            second_trading_instrument_name = second_article_title.split()[-1].replace("?", "")  # for example AUD/USD
            print(f"{datetime.now()}   Name of trading instrument is: {second_trading_instrument_name}.")

            # Check name of trading instrument first and second articles
            print(f"{datetime.now()}   Are Names of trading instrument the same? =>")
            if second_trading_instrument_name == self.trading_instrument_name:
                print(f"{datetime.now()}   => Names of trading instrument are the same.")
                self.driver.back()
                continue
            print(f"{datetime.now()}   => Names of trading instrument are not the same!\n")
            break

    def assert_(self, d):
        # Get [Bullish] button status
        status_of_widget = self.driver.find_element(*STATUS_OF_SENTIMENT_LOCATOR).get_attribute("class")
        if "hidden" in status_of_widget:
            Common.pytest_fail(f"For other trading instrument [Bullish] button not available. "
                               f"Test of voted function in 'What is your sentiment...' block doesn't work correctly")
        print("Test of voted function in 'What is your sentiment...' block work correctly")
