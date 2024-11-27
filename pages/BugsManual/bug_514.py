"""
-*- coding: utf-8 -*-
@Time    : 2024/11/27 19:30
@Author  : Kasilà
"""


import random
from datetime import datetime
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from urllib import request, error


class AnnouncedLink(BasePage):
    @allure.step(f"{datetime.now()}   Start testing that the page with 'Maple crypto-lending' content is opened”")
    def announced_link(self, d, cur_item_link):
        print(f"{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Selected Article 'Solana price prediction: Can SOL rebound?'")
        p = 1
        while p <= 24:
            try:
                article = self.driver.find_element(By.CSS_SELECTOR, 'div.article_content__1GOa_ > a[href*="solana-sol-price-prediction-is-it-a-solid-investment"]')
                article.click()
                break
            except NoSuchElementException:
                p += 1
                print(f"{datetime.now()}   Go to the next page")
#                pagination = self.driver.find_element(By.LINK_TEXT, str(page))
                pagination = self.driver.find_element(By.CSS_SELECTOR, f'a[href*="page={p}"]')
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "start", inline: "center"});',
                    pagination
                )
                pagination.click()

        print(f"{datetime.now()}   Scroll to the 'Table of Contents'")
        table_of_contents = self.driver.find_element(By.CLASS_NAME, 'tableOfContent_frame__1c2SI')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "start", inline: "center"};',
            table_of_contents
        )

        print(f"{datetime.now()}   Selected the contents item [Could Solana become a Cardano side-chain?]")
        could_solana_item = self.driver.find_element(By.XPATH, '//span[contains(text(), "Could Solana become a Cardano side-chain?")]')
        could_solana_item.click()

    def element_click(self):
        print(f"{datetime.now()}   2. Act")

        print(f"{datetime.now()}   Click on the [announced] link in the text")
        announced_link = self.driver.find_element(By.LINK_TEXT, 'announced')
        announced_link.click()

    @allure.step(f"{datetime.now()}   Assert")
    def assert_(self):
        print(f"{datetime.now()}   3.Assert")

        current_url = self.driver.current_url()


        # Отправляем GET-запрос
        response = request.urlopen(current_url)
        # Получаем статус код
        status_code = response.getcode()

        if status_code != 200:
            print(f"{datetime.now()}   Status code is {status_code}")
            Common.pytest_fail(f"# Bug 55!514 "
                               f"\n"
                               f"Expected result: The page with 'Maple crypto-lending' content is opened, Status code is 200"
                               f"\n"
                               f"Actual result: The page with 'Maple crypto-lending' content is not opened, Status code is {status_code}")
