"""
-*- coding: utf-8 -*-
@Time    : 2025/01/21 08:30
@Author  : Kasilà
"""


from datetime import datetime
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from selenium.common import NoSuchElementException


class PageError404(BasePage):
    @allure.step(f"{datetime.now()}   Start testing that the page 'Grondstoffen'(Commodities) is displayed")
    def page_error_404(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll down to the tile 'Wat is de handel in grondstoffen?'(What is commodity trading?)")
        tile = self.driver.find_element(By.CSS_SELECTOR, 'div.grid_up__CJBIw > div:nth-child(3)')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center"});', tile
        )

        print(f"{datetime.now()}   Click on the [Handelsgids voor grondstoffen](Commodity trading guide) link")
        commodity_trading_guide_link = self.driver.find_element(By.LINK_TEXT, 'Handelsgids voor grondstoffen')
        commodity_trading_guide_link.click()

    def element_click(self):
        print(f"{datetime.now()}   2. Act")
        print(f"{datetime.now()}   Click on the [grondstoffenmarkt](commodities market) link in the 'A complete guide "
              f"to commodities trading' block")

        commodities_market_link = self.driver.find_element(By.LINK_TEXT, 'grondstoffenmarkt')
        commodities_market_link.click()

    @allure.step(f"{datetime.now()}   Assert")
    def assert_(self):
        print(f"{datetime.now()}   3.Assert")


        expected_url = 'https://capital.com/nl-nl/markets/commodities'
        actual_url = self.driver.current_url

        try:
            error_404 = self.driver.find_element(By.CSS_SELECTOR, 'p.subTitle404')
            if error_404:
                Common.pytest_fail(f"#Bug # 55!660 "
                                   f"\n"
                                   f"Expected result: The page 'Grondstoffen'(Commodities) with '{expected_url}' URL is displayed"
                                   f"\n"
                                   f"Actual result: The page '404' with URL '{actual_url}' is displayed")
        except NoSuchElementException:
            if actual_url != expected_url:
                Common.pytest_fail(f"#Bug # 55!660 "
                                   f"\n"
                                   f"Expected result: The page 'Grondstoffen'(Commodities) with '{expected_url}' URL is displayed"
                                   f"\n"
                                   f"Actual result: The page with URL '{actual_url}' is displayed")
            else:
                print(f"{datetime.now()}   The page 'Grondstoffen'(Commodities) with '{expected_url}' URL is displayed")
                allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
