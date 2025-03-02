"""
-*- coding: utf-8 -*-
@Time    : 2025/02/05 16:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime

import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BUG_678(BasePage):
    count = int
    HOW_TO_CREATE_AN_MT4_ACCOUNT_LINK = (
        By.CSS_SELECTOR, "[data-id='connectaccounttomt4'] [data-type='tiles_w_img_link2_signup']")
    TITLE_HOW_TO_CREATE_A_METATRADER_PAGE = (By.CSS_SELECTOR, "h1.lt-page__title")

    BITCOIN_PRICE_PREDICTIONS_ARTICLE = (By.XPATH, "//b[contains(text(), '2030-2050')]")
    CURRENT_PAGE_OF_PAGINATION = (By.CSS_SELECTOR, "[aria-current='page']")
    NEXT_PAGE_OF_PAGINATION = (By.XPATH,
            f"//a[contains(@class, 'pagination_pagination__lllu8')][contains(text(), '{count}')]")
    GOLDMAN_SACHS_LINK = (By.XPATH, "//p/a[contains(text(), 'Goldman Sachs')]")
    PAGE_NOT_FOUND_TITLE = (By.XPATH, "//h1[contains(text(), 'Page Not Found')]")

    def __init__(self, driver, link, bid):
        super().__init__(driver, link, bid)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)

    @allure.step(f"{datetime.now()}   Find article and click 'Bitcoin price predictions 2025–2050'")
    def find_article_bitcoin_price_predictions(self):
        # Check presenting, visibility link
        count = 0
        while count != 5:
            try:
                bitcoin_price_predictions_article = self.wait.until(EC.visibility_of_element_located(self.BITCOIN_PRICE_PREDICTIONS_ARTICLE))
                print(f"{datetime.now()}   'Bitcoin price predictions article' was found.")
                print(f"{datetime.now()}   Start to navigate on article.")
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    self.driver.find_element(*self.BITCOIN_PRICE_PREDICTIONS_ARTICLE)
                )
                print(f"{datetime.now()}   End to navigate on article.")
                print(f"{datetime.now()}   Start to click article")
                bitcoin_price_predictions_article.click()
                print(f"{datetime.now()}   End to click article")
                break
            except TimeoutException:
                self.find_link_scroll_check_visibility_and_clickability(
                    f"Number page of pagination is: {count}",
                    self.CURRENT_PAGE_OF_PAGINATION)
                current_number_page_of_pagination = self.driver.find_element(*self.CURRENT_PAGE_OF_PAGINATION)
                count = int(current_number_page_of_pagination.text)
                print(f"{datetime.now()}   Current number page of pagination is {count}")
                count += 1 # next number of page

                if count == 5:
                    msg = "Pages from 1 to 4 don't have article 'Bitcoin price predictions 2025–2050'"
                    print(f"{datetime.now()}   => {msg}\n")
                    Common().pytest_fail(msg)

                print(f"{datetime.now()}   Start click next number page of pagination is {count}")

                self.driver.find_element(By.XPATH,
                f"//a[contains(@class, 'pagination_pagination__lllu8')][contains(text(), '{count}')]").click()
                print(f"{datetime.now()}   End click next number page of pagination is {count}")

    @allure.step(f"{datetime.now()}   Find and click link 'Goldman Sachs'")
    def find_and_click_link_goldman_sachs(self):
        self.find_link_scroll_check_visibility_and_clickability(
            "Goldman Sachs",
            self.GOLDMAN_SACHS_LINK)
        # click link
        print(f"{datetime.now()}   Start click [Goldman Sachs] link")
        self.driver.find_element(*self.GOLDMAN_SACHS_LINK).click()
        print(f"{datetime.now()}   End click [Goldman Sachs] link\n")
        Common().save_current_screenshot(self.driver,
            "After click on [Goldman Sachs] link")

    @allure.step(f"{datetime.now()}   Is expected page open?")
    def is_expected_page_open(self):
        print(f"{datetime.now()}   How are many opened window?")
        tabs = self.driver.window_handles
        print(f"{datetime.now()}   Opened window is: {len(tabs)}")
        if len(tabs) > 1:
            self.driver.switch_to.window(tabs[0])
            self.driver.close()
            self.driver.switch_to.window(tabs[-1])
            Common().save_current_screenshot(self.driver,
                                             "After switch on second tab")
        print(f"{datetime.now()}   Start to check title on the opened page")

        if self.driver.find_element(*self.PAGE_NOT_FOUND_TITLE):
            msg = f"Opened page has text 'Page Not Found'"
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   Opened page has not text 'Page Not Found', but need to check Screenshot.\n")
