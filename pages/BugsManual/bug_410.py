"""
-*- coding: utf-8 -*-
@Time    : 2024/10/25 19:50
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from src.src import CapitalComPageSrc

LINK_NAME = '"Daniela Hathorn"'
BUG_NUMBER = '410'

PAGINATION_LOCATOR = (By.CSS_SELECTOR,
                      '.pagination_pagination__lllu8.pagination_active__1sAIU ~ .pagination_pagination__lllu8')
ARTICLES_LOCATOR = (By.XPATH,
                    '//div[@class="article_content__1GOa_"]//a [@class="js-analyticsClick link_link__caosC"]')
# TARGET_ARTICLE_LOCATOR = (By.XPATH, "//b[contains(text(), 'ECB Preview')]")
TARGET_ARTICLE_LOCATOR = (By.CSS_SELECTOR, '.article_content__1GOa_ > [data-type="latest_articles_block_page_id_541754"]')

LINK_LOCATOR = (By.CSS_SELECTOR, 'a[data-type="author_link"]')

MESSAGE_404_LOCATOR = (By.XPATH, "//p[@class='textCenter title404'][contains(text(), '404')]")

class BUG_410(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: find articles, choose and click article, find links")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find articles, choose and click article, find links")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Check presenting articles on the page
        if len(self.driver.find_elements(*ARTICLES_LOCATOR)) == 0:
            msg = f"The page 'Market analysis' don't have articles"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   The page 'Market analysis' have articles in DOM\n")

        # Look for target article
        count = 0
        while count < 3:
            # Check presenting pagination on the page
            print(f"{datetime.now()}   Start to check presenting pagination on the page\n")
            if len(self.driver.find_elements(*PAGINATION_LOCATOR)) == 0:
                msg = f"The page 'Market analysis' don't have pagination"
                print(f"{datetime.now()}   => {msg}")
                Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
            print(f"{datetime.now()}   The page 'Market analysis' have pagination in DOM\n")

            # Check presenting target article on the page
            print(f"{datetime.now()}   Start to check presenting target article on the page\n")
            if len(self.driver.find_elements(*TARGET_ARTICLE_LOCATOR)) == 0:
                msg = f"The current page don't have target article. Try find on the other page."
                print(f"{datetime.now()}   => {msg}")
                print(f"{datetime.now()}   Start to click on the next page link")
                self.driver.find_elements(*PAGINATION_LOCATOR)[0].click()
                print(f"{datetime.now()}   End to click on the next page link")
                count += 1
                continue
            print(f"{datetime.now()}   The current page have target article in DOM\n")
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                self.driver.find_elements(*TARGET_ARTICLE_LOCATOR)[0]
            )
            break

        # Check visibility article on the page
        print(f"{datetime.now()}   Start to check visibility target article'\n")
        if not self.element_is_visible(TARGET_ARTICLE_LOCATOR):
            msg = f"Target article don't visible"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Target article is visible \n")

        # Check clickability article on the page
        print(f"{datetime.now()}   Start to check clickability target article\n")
        if not self.element_is_clickable(TARGET_ARTICLE_LOCATOR):
            msg = f"Target article don't clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Target article clickable\n")
        link_article = self.driver.find_elements(*TARGET_ARTICLE_LOCATOR)[0].get_attribute("href")

        print(f'{datetime.now()}   Start to click on target article')
        self.driver.find_elements(*TARGET_ARTICLE_LOCATOR)[0].click()
        print(f'{datetime.now()}   End to click on target article')

        # Check target url
        print(f'Link article: {link_article}')
        self.wait_for_target_url(link_article, 5)
        print(f'{datetime.now()}   Current page is: {self.driver.current_url}')

        # stop here

        # Check presenting link on the page
        if len(self.driver.find_elements(*LINK_LOCATOR)) == 0:
            msg = (f"The page 'ECB Preview...' don't have link {LINK_NAME} in DOM")
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   The page 'ECB Preview...' have link {LINK_NAME} in DOM\n")

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
