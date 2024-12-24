"""
-*- coding: utf-8 -*-
@Time    : 2024/12/21 21:30
@Author  : Kasilà
"""


from datetime import datetime
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common


class CocaColaCOPage(BasePage):
    @allure.step(f"{datetime.now()}   Start testing page opened after clicking the “initial public offering (IPO)” link")
    def coca_cola_co(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        tabs = self.driver.window_handles
        if len(tabs) > 1:
            self.driver.switch_to.window(tabs[0])
            self.driver.close()
            self.driver.switch_to.window(tabs[1])

        print(f"{datetime.now()}   Scroll down to the tile 'What is shares trading?' in the block “Market trading guides”")
        what_is_shares_trading_tile = self.driver.find_element(By.XPATH, '//h3[contains(text(), "What is shares trading?")]')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center",});', what_is_shares_trading_tile
        )

        print(f"{datetime.now()}   Click on the link “Shares trading guide”")
        shares_trading_guide_link = self.driver.find_element(By.CSS_SELECTOR, 'a[data-type="tiles_w_img_link2_signup"]')
        shares_trading_guide_link.click()

        print(f"{datetime.now()}   Scroll down to the block “Popular shares to trade”")
        popular_shares_to_trade_block = self.driver.find_element(By.CSS_SELECTOR, 'h2[data-id="part_2"]')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center"});', popular_shares_to_trade_block
        )

        print(f"{datetime.now()}   Click on the link “Netflix”")
        netflix_link = self.driver.find_element(By.LINK_TEXT, 'Netflix')
        netflix_link.click()

        print(f"{datetime.now()}   Scroll down to the block “Visit our other complete guides”")
        visit_our_other_block = self.driver.find_element(By.XPATH, '//h2[contains(text(), "Visit our other complete")]')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center"});', visit_our_other_block
        )

        print(f"{datetime.now()}   Click on the link “Trade Coca-Cola shares”")
        trade_coca_cola_shares_link = self.driver.find_element(By.CSS_SELECTOR, 'a[data-type="tiles_w_img_link2_signup"]')
        trade_coca_cola_shares_link.click()

        print(f"{datetime.now()}   Scroll down to the block “Performance of the Coca-Cola stock in recent years”")
        performance_coca_cola_block = self.driver.find_element(By.CSS_SELECTOR, 'h2[data-id="part_3"]')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center"});', performance_coca_cola_block
        )

    def element_click(self, d):
        print(f"{datetime.now()}   2. Act")

        print(f"{datetime.now()}   Click on the link 'KO'")
        ko_link = self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(5) > div > p > a')
        ko_link.click()
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])

    @allure.step(f"{datetime.now()}   Assert")
    def assert_(self):
        print(f"{datetime.now()}   3.Assert")

        try:
            error_information = self.driver.find_element(By.CSS_SELECTOR, 'a#error-information-button')
            if error_information:
                tabs = self.driver.window_handles
                print(f"{datetime.now()}   Error message “This site can’t be reached” is displayed")
                Common.pytest_fail("Bug # 55!624"
                                   "\n"
                                   "Expected result: The “Coca-Cola Co” page is displayed"
                                   "\n"
                                   "Actual result: Error message “This site can’t be reached” is displayed")
        except NoSuchElementException:
            print(f"{datetime.now()}   The “Coca-Cola Co” page is displayed")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
