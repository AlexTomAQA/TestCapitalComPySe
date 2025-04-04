"""
-*- coding: utf-8 -*-
@Time    : 2025/03/13 20:00
@Author  : Artem Dashkov
"""
import allure
from datetime import datetime

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.common import Common
from selenium.webdriver.support.ui import WebDriverWait


class BUG_690(BasePage):
    OUR_TRADING_APP_BLOCK = (By.XPATH, "(//div[@data-type='tiles_w_img'])[2]")
    APP_LINK = (By.XPATH, "(//div[@data-type='tiles_w_img'])[2] //a[contains(text(), 'pp')]")

    SHARES_MARKETS_BLOCK = (By.CSS_SELECTOR, "[data-type='markets_list']")
    NOT_ACTIVE_PAGES_IN_PAGINATOR = (By.CSS_SELECTOR,
                    "[class='pagination_pagination__lllu8 js-analyticsClick link_link__caosC']")
    DROPDOWN_LIST_SORT = (By.CSS_SELECTOR, "[class='filters_cell__jnXY0']:nth-child(1)")
    TOP_FALLERS_TAB = (By.CSS_SELECTOR, "[title='fallers']")
    ARROW_GO_TO_THE_NEXT_PAGE = (By.CSS_SELECTOR, "[aria-label='Go to the next page']")

    def __init__(self, driver, link, bid):
        super().__init__(driver, link, bid)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)

    @allure.step(f"{datetime.now()}   Click last page in paginator")
    def click_last_page_in_paginator(self):

        # Check presenting, visibility block
        self.find_block_scroll_and_check_visibility(
            "Shares markets block", self.SHARES_MARKETS_BLOCK)

        # Check presenting link on the page
        if len(self.driver.find_elements(*self.NOT_ACTIVE_PAGES_IN_PAGINATOR)) == 0:
            msg = f"Page don't have link 'Pages in paginator' in DOM"
            print(f"{datetime.now()}   => {msg}")
            Common().pytest_fail(f"{msg}")
        print(f"{datetime.now()}   Page have link 'Pages in paginator' in DOM\n")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            self.driver.find_elements(*self.NOT_ACTIVE_PAGES_IN_PAGINATOR)[-1]
        )
        print(f"{datetime.now()}   Scrolled to link 'Pages in paginator'")

        # click link
        print(f"{datetime.now()}   Start click last page in paginator")
        self.driver.find_elements(*self.NOT_ACTIVE_PAGES_IN_PAGINATOR)[-1].click()
        print(f"{datetime.now()}   End click last page in paginator\n")
        Common().save_current_screenshot(self.driver,
                                         "After click on last page in paginator")

    @allure.step(f"{datetime.now()}   Click last page in paginator")
    def click_top_fallers_on_dropdown_list_sort(self):
        # Check presenting, visibility dropdown list 'Sort'
        self.find_block_scroll_and_check_visibility(
            "Dropdown list", self.DROPDOWN_LIST_SORT)

        drop_down_list_sort = self.driver.find_element(*self.DROPDOWN_LIST_SORT)
        top_fallers_tab = self.driver.find_element(*self.TOP_FALLERS_TAB)

        print(f"{datetime.now()}   Start click dropdown list 'Sort', move to 'Top Fallers' Tab and click")
        action = ActionChains(self.driver)
        action.click(drop_down_list_sort) \
            .pause(1) \
            .move_to_element(top_fallers_tab) \
            .click() \
            .perform()
        print(f"{datetime.now()}   End click dropdown list 'Sort', move to 'Top Fallers' Tab and click")
        Common().save_current_screenshot(self.driver,
                                         "After click on 'Top Fallers' Tab")

    @allure.step(f"{datetime.now()}   Is expected page open?")
    def is_right_arrow_on_the_page(self):
        print(f"{datetime.now()}   Start to check right arrow on the page.")
        if len(self.driver.find_elements(*self.ARROW_GO_TO_THE_NEXT_PAGE)) > 0:
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                self.driver.find_element(*self.ARROW_GO_TO_THE_NEXT_PAGE)
            )
            Common().save_current_screenshot(self.driver,
                                             "After navigate on the right arrow")
            msg = "There is a right arrow on the current page, but it shouldn't be there."
            print(f"{datetime.now()}   => {msg}\n")
            Common().pytest_fail(msg)
        print(f"{datetime.now()}   Current page don't have right arrow, but need to check screenshot.")
