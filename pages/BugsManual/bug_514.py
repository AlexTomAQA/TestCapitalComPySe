"""
-*- coding: utf-8 -*-
@Time    : 2024/11/27 19:30
@Author  : Kasilà
"""


from datetime import datetime
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class AnnouncedLink(BasePage):
    @allure.step(f"{datetime.now()}   Start testing that the page with 'Maple crypto-lending' content is opened”")
    def announced_link(self, d, cur_item_link, cur_link):
        print(f"{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Selected Article 'Solana price prediction: Can SOL rebound?'")
        p = 1
        while p <= 24:
            try:
                article = self.driver.find_element(By.CSS_SELECTOR,
                        'div.article_content__1GOa_ > a[href*="/solana-sol-price-prediction-is-it-a-solid-investment')
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center"});', article
                )
                if not self.element_is_clickable(article):
                    allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
                    Common.pytest_fail("Article 'Solana price prediction: Can SOL rebound?' is not clickable")
                self.driver.find_element(By.CSS_SELECTOR,
                'div.article_content__1GOa_ > a[href*="/solana-sol-price-prediction-is-it-a-solid-investment').click()
                break
            except NoSuchElementException:
                p += 1
                print(f"{datetime.now()}   Go to the page {p}")
                pagination = self.driver.find_element(By.LINK_TEXT, str(p))
                self.driver.execute_script(
                    'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                    pagination
                )
                pagination.click()

        print(f"{datetime.now()}   Scroll to the 'Table of Contents'")
        table_of_contents = self.driver.find_element(By.CLASS_NAME, 'tableOfContent_frame__1c2SI')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center"});',
            table_of_contents
        )

        print(f"{datetime.now()}   Selected the contents item [Could Solana become a Cardano side-chain?]")
        could_solana_item = self.driver.find_element(By.XPATH, '//span[contains(text(), "Could Solana become a Cardano side-chain?")]')
        could_solana_item.click()

    def element_click(self):
        print(f"{datetime.now()}   2. Act")

        print(f"{datetime.now()}   Click on the [announced] link in the text")
        announced_link = self.driver.find_element(By.CSS_SELECTOR, 'a[href*="/maple.finance/news/maple-2-0-new-smart-contracts"]')

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center"});',
            announced_link
        )
        announced_link.click()
        tabs = self.driver.window_handles
        if len(tabs) > 1:
            self.driver.switch_to.window(tabs[1])


    @allure.step(f"{datetime.now()}   Assert")
    def assert_(self):
        print(f"{datetime.now()}   3.Assert")

        tabs = self.driver.window_handles
        if len(tabs) > 1:
            self.driver.switch_to.window(tabs[0])
            self.driver.close()
            self.driver.switch_to.window(tabs[1])
            current_url = self.driver.current_url
            print(f"{datetime.now()}   current URL is '{current_url}")

        page_title = self.driver.title
        allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        print(f"{datetime.now()}   The page with title '{page_title}' is opened")

        if page_title == 'Not Found':
            Common.pytest_fail(f"# Bug 55!514 "
                               f"\n"
                               f"Expected result: The page with 'Maple crypto-lending' content is opened"
                               f"\n"
                               f"Actual result: The page with title '{page_title}' is opened")
        else:
            print(f"{datetime.now()}   The 'Maple crypto-lending' page is opened")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
