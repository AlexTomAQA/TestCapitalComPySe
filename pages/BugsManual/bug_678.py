"""
-*- coding: utf-8 -*-
@Time    : 2025/02/05 16:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime

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

    def __init__(self, driver, link, bid):
        super().__init__(driver, link, bid)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)

    @allure.step(f"{datetime.now()}   Find article 'Bitcoin price predictions 2025–2050'")
    def find_article_bitcoin_price_predictions(self):
        # Check presenting, visibility link
        count = 0
        while count != 5:
            try:
                self.wait.until(EC.visibility_of_element_located(self.BITCOIN_PRICE_PREDICTIONS_ARTICLE))
            except TimeoutException:
                self.find_link_scroll_check_visibility_and_clickability(
                    f"Number page of pagination is: {count}",
                    self.CURRENT_PAGE_OF_PAGINATION)
                current_number_page_of_pagination = self.driver.find_element(*self.CURRENT_PAGE_OF_PAGINATION)
                count = current_number_page_of_pagination.text
                print(f"{datetime.now()}   Current number page of pagination is {count}")
                count += 1 # next number of page
                print(f"{datetime.now()}   Start click next number page of pagination is {count}")

                self.driver.find_element(By.XPATH,
                f"//a[contains(@class, 'pagination_pagination__lllu8')][contains(text(), '{count}')]").click()
                print(f"{datetime.now()}   End click next number page of pagination is {count}")

        print("Stop here!")


        self.find_link_scroll_check_visibility_and_clickability(
            "How to create an MT4 account",
            self.HOW_TO_CREATE_AN_MT4_ACCOUNT_LINK)
        # click link
        print(f"{datetime.now()}   Start click [How to create an MT4 account] link")
        self.driver.find_element(*self.HOW_TO_CREATE_AN_MT4_ACCOUNT_LINK).click()
        print(f"{datetime.now()}   End click [How to create an MT4 account] link\n")
        Common().save_current_screenshot(self.driver,
            "After click on [How to create an MT4 account] link")

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
                                             "After switch on second link")
        print(f"{datetime.now()}   Start to check language of the title on the opened page")

        title_on_the_opened_page = self.driver.find_element(*self.TITLE_HOW_TO_CREATE_A_METATRADER_PAGE)

        if "How to create" in title_on_the_opened_page.text:
            msg = (f"Instead Dutch language opened page "
                   f"has English language. "
                   f"Title on the opened page is '{title_on_the_opened_page.text}'")
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   Language on the opened page is not English, need to check Screenshot.\n")
