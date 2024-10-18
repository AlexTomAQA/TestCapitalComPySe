"""
-*- coding: utf-8 -*-
@Time    : 2024/10/15 21:00
@Author  : Artem Dashkov
"""
import allure
import random
from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from src.src import CapitalComPageSrc

TARGET_AUTHOR_NAME = 'daniela hathorn'
BUG_NUMBER = '407'

PAGINATION_LOCATOR = (By.CSS_SELECTOR,
                      '.pagination_pagination__lllu8.pagination_active__1sAIU ~ .pagination_pagination__lllu8')
ARTICLES_LOCATOR = (By.XPATH,
                    '//div[@class="article_content__1GOa_"]//a [@class="js-analyticsClick link_link__caosC"]')
# TARGET_ARTICLE_LOCATOR = (By.XPATH, "//b[contains(text(), 'ECB Preview')]")
TARGET_ARTICLE_LOCATOR = (By.CSS_SELECTOR, '.article_content__1GOa_ > [data-type="latest_articles_block_page_id_541765"]')

LINK_LOCATOR = (By.CSS_SELECTOR, 'a[data-type="author_link"]')
DANIELA_HATHORN_AUTHOR_LOCATOR = (By.XPATH,
                                  "//span[@data-type='authors_field'] //a[contains(text(), 'Daniela Hathorn')]")

MESSAGE_404_LOCATOR = (By.XPATH, "//p[@class='textCenter title404'][contains(text(), '404')]")

class BUG_407(BasePage):

    @allure.step(f"{datetime.now()}   1. Start Arrange: "
                 f"find target article,"
                 f"choose and click article,"
                 f"find and click link 'Daniela Hathorn', "
                 f"choose any random article")
    def arrange(self, d, link):
        print(f"\n{datetime.now()}   1. Start Arrange: find target article, choose and click article, "
              f"find and click link 'Daniela Hathorn'")
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        # Look for target article
        count = 1
        while count < 7:
            # Check presenting articles on the page
            quantity_of_articles = len(self.driver.find_elements(*ARTICLES_LOCATOR))
            if quantity_of_articles == 0:
                msg = f"The page 'Market analysis' don't have articles"
                print(f"{datetime.now()}   => {msg}")
                Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
            print(f"{datetime.now()}   The page 'Market analysis' have articles in DOM\n")

            for number_of_article in range(0, quantity_of_articles):

                # Scroll to the article
                print(f"\n{datetime.now()}   Scroll to the article number: {number_of_article + 1}")
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    self.driver.find_elements(*ARTICLES_LOCATOR)[number_of_article]
                )

                # Start to click on the article
                print(f"\n{datetime.now()}   Start to click on the article number: {number_of_article+1}")
                self.driver.find_elements(*ARTICLES_LOCATOR)[number_of_article].click()
                print(f"\n{datetime.now()}   Article number: {number_of_article+1} is clicked\n")

                # Check presenting author link on the article page
                if len(self.driver.find_elements(*LINK_LOCATOR)) == 0:
                    msg = f"The article number: {number_of_article+1} don't have link on author in DOM"
                    print(f"{datetime.now()}   => {msg}")
                    Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
                print(f"{datetime.now()}   The article number: {number_of_article+1} have link on author in DOM\n")

                # Scroll to the link author
                print(f"\n{datetime.now()}   Scroll to the link author")
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    self.driver.find_element(*LINK_LOCATOR)
                )

                # Check author of article is Daniela Hathorn
                author_of_current_article = (self.driver.find_element(*LINK_LOCATOR).get_property()).lower()
                if TARGET_AUTHOR_NAME in author_of_current_article:
                    msg = (f"Author of article number: {number_of_article + 1} is Daniela Hathorn, "
                           f"author is: {author_of_current_article}")
                    print(f"{datetime.now()}   => {msg}")
                    self.driver.execute_script(
                        'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                        self.driver.find_element(*LINK_LOCATOR)
                    )
                    # We find target article. Exit from loop while.
                    count = 10
                    break
                else:
                    msg = (f"Author of article number: {number_of_article + 1} is not Daniela Hathorn, "
                           f"author is: {author_of_current_article}")
                    print(f"{datetime.now()}   => {msg}")
                    print(
                        f"{datetime.now()}   => Come back on page with articles and try to check author of next article")
                    self.driver.back()
                    continue


            print(f"{datetime.now()}   On the current page aren't Daniela Hathorn articles. "
                  f"Need look for articles on the next page\n")

            # Check presenting pagination on the page
            print(f"{datetime.now()}   Start to check presenting pagination on the page")
            if len(self.driver.find_elements(*PAGINATION_LOCATOR)) == 0:
                msg = f"The page 'Market analysis' don't have pagination"
                print(f"{datetime.now()}   => {msg}")
                Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
            print(f"{datetime.now()}   The page 'Market analysis' have pagination in DOM\n")

            print(f"{datetime.now()}   Start to click on the next page link")
            self.driver.find_elements(*PAGINATION_LOCATOR)[0].click()
            print(f"{datetime.now()}   End to click on the next page link")
            count += 1
            print(f"{datetime.now()}   Number of current page is: {count}")
            continue

        # Check visibility Daniela Hathorn link on the page
        print(f"{datetime.now()}   Start to check visibility link {TARGET_AUTHOR_NAME}'\n")
        if not self.element_is_visible(LINK_LOCATOR):
            msg = f"Link {TARGET_AUTHOR_NAME} don't visible"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Link {TARGET_AUTHOR_NAME} visible \n")

        # Check clickability link on the page
        print(f"{datetime.now()}   Start to check clickability link {TARGET_AUTHOR_NAME}\n")
        if not self.element_is_clickable(LINK_LOCATOR):
            msg = f"Link {TARGET_AUTHOR_NAME} don't clickable"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"Bug # {BUG_NUMBER} {msg}")
        print(f"{datetime.now()}   Link {TARGET_AUTHOR_NAME} clickable\n")

        # Start click on the link Daniela Hathorn
        print(f"\n{datetime.now()}   Click on the link {TARGET_AUTHOR_NAME}")
        self.driver.find_element(*LINK_LOCATOR).click()
        print(f"\n{datetime.now()}   Link {TARGET_AUTHOR_NAME} is clicked\n")

    @allure.step(f"\n{datetime.now()}   2. Start Act.")
    def act(self, d):
        print(f"\n{datetime.now()}   2. Start Act. Choose any three random articles and check author")
        quantity_of_articles = len(self.driver.find_elements(*ARTICLES_LOCATOR))
        list_random_articles_for_check = random.sample()


        # STOP HERE

        self.driver.find_element(*LINK_LOCATOR).click()
        print(f"\n{datetime.now()}   Link {TARGET_AUTHOR_NAME} is clicked\n")

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
