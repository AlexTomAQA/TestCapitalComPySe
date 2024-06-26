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
ARTICLES_LOCATOR = (By.XPATH, "//div [@class='main-article-item__title']")
ARTICLE_TITLE_LOCATOR = (By.CSS_SELECTOR, ".sentiment__step.js-vote-step0 h2")
YOU_VOTED_BULLISH_LOCATOR = (By.XPATH, '//p[@class="js-vote-bull"]')
STATUS_OF_SENTIMENT_LOCATOR = (By.XPATH, '//div [@class="sentiment__step js-vote-step0"]')


class WhatIsYourSentimentWidget(BasePage):
    global BUTTON_NAME
    global BLOCK_NAME
    global BUTTON_LOCATOR
    global BLOCK_LOCATOR
    global ARTICLES_LOCATOR
    global ARTICLE_TITLE_LOCATOR

    def __init__(self, browser, link, bid):
        self.button_create_demo_account = None
        self.what_is_your_sentiment_widget = []

        super().__init__(browser, link, bid)

    @allure.step(f"{datetime.now()}   Start Full test for {BUTTON_NAME} button in {BLOCK_NAME} block")
    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)
        self.element_click(d)

        test_element = AssertClass(d, cur_item_link, self.bid)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

    def arrange_(self, d, cur_item_link):
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

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*ARTICLES_LOCATOR)[0]
        )

        quantity_articles = len(self.driver.find_elements(*ARTICLES_LOCATOR))
        list_of_numbers_articles = list(range(1, quantity_articles+1)) # for example [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Selected random (first in line) article with block "What is your sentiment..."
        first_article_with_widget = 0
        for number_article in list_of_numbers_articles:
            self.driver.find_elements(*ARTICLES_LOCATOR)[number_article].click()
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
            first_article_with_widget = number_article
            break

        # Check presenting and visible article's title
        self.element_is_present_and_visible_v2(ARTICLE_TITLE_LOCATOR, "Article's title")

        # Get name of trading instrument
        article_title = self.driver.find_element(*ARTICLE_TITLE_LOCATOR).text
        trading_instrument_name = article_title.split()[-1].replace("?", "") # for example AUD/USD
        print(f"{datetime.now()}   Name of trading instrument is: {trading_instrument_name}.")

        # Check presenting and visible [Bullish] button
        self.element_is_present_and_visible_v2(BUTTON_LOCATOR, "[Bullish] button")

        # [Bullish] button click
        self.driver.find_element(*BUTTON_LOCATOR).click()
        print(f"{datetime.now()}   [Bullish] button clicked.")

        # Back on page with list of articles
        self.driver.back()

        # Selected random (second) article with block "What is your sentiment..."
        for number_second_article in list_of_numbers_articles[first_article_with_widget:]:
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
            article_title_second = self.driver.find_element(*ARTICLE_TITLE_LOCATOR).text
            trading_instrument_name_2 = article_title_second.split()[-1].replace("?", "")  # for example AUD/USD
            print(f"{datetime.now()}   Name of trading instrument is: {trading_instrument_name_2}.")

            # Check name of trading instrument first and second articles
            print(f"{datetime.now()}   Are Names of trading instrument the same? =>")
            if trading_instrument_name_2 == trading_instrument_name:
                print(f"{datetime.now()}   => Names of trading instrument are the same.")
                self.driver.back()
                continue
            print(f"{datetime.now()}   => Names of trading instrument are not the same!\n")

            # Get [Bullish] button status
            status_of_widget = self.driver.find_element(*STATUS_OF_SENTIMENT_LOCATOR).get_attribute("class")

            assert ""

            break


        """
        print(f"{datetime.now()}   IS {BLOCK_NAME} block visible on this page? =>")
        if not self.element_is_visible(BLOCK_LOCATOR, 5):
            msg = f"{BLOCK_NAME} block is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BLOCK_NAME} block is visible on this page!\n")

        # Check presenting and visible button
        print(f"{datetime.now()}   IS {BUTTON_NAME} button present on this page? =>")
        self.button_create_demo_account = self.driver.find_elements(*BUTTON_LOCATOR)
        if len(self.button_create_demo_account) == 0:
            msg = f"{BUTTON_NAME} button is NOT present on this page"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} button present on this page!\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*BUTTON_LOCATOR)[0]
        )

        print(f"{datetime.now()}   IS {BUTTON_NAME} button visible on this page? =>")
        if not self.element_is_visible(BUTTON_LOCATOR, 5):
            msg = f"{BUTTON_NAME} button is NOT visible on this page!"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} button is visible on this page!\n")

        print(f"{datetime.now()}   {BUTTON_NAME} button scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.button_create_demo_account[0]
        )

    @allure.step(f"Click button {BUTTON_NAME} on {BLOCK_NAME} block")
    def element_click(self, d):
        print(f"\n{datetime.now()}   2. Act_v0")

        print(f"{datetime.now()}   {BUTTON_NAME} button is clickable? =>")
        time_out = 5
        self.button_create_demo_account = self.driver.find_elements(*BUTTON_LOCATOR)
        if not self.element_is_clickable(self.button_create_demo_account[0], time_out):
            msg = f"{BUTTON_NAME} button is not clickable after {time_out} sec. Stop AT>"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   => {BUTTON_NAME} button is clickable!\n")

        try:
            self.button_create_demo_account[0].click()
            print(f"{datetime.now()}   => {BUTTON_NAME} button clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => {BUTTON_NAME} button NOT CLICKED")

        del self.button_create_demo_account
        return True


        """
