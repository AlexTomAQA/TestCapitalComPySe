"""
-*- coding: utf-8 -*-
@Time    : 2024/06/14 18:00
@Author  : Kasilà
"""

from datetime import datetime
import random

import allure
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.common import Common


class AppliedFilters(BasePage):

    def __init__(self, driver, link="", bid=""):
        self.selected_filters_text_list = []
        super().__init__(driver, link, bid)

    @allure.step(f"{datetime.now()}   Start test the display of the applied filters")
    def test_(self, d, cur_language, cur_country, cur_role, cur_item_link):

        self.arrange_v0(d, cur_item_link)

        for i in range(5):
            self.element_click(d)
            test_element = AssertFilters(d, cur_item_link)
            test_element.assert_filters(d, cur_item_link, self.selected_filters_text_list)
        if len(self.selected_filters_text_list) != 0:
            self.selected_filters_text_list = []

    def arrange_v0(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll to the labels")
        filters_labels = self.driver.find_element(By.CSS_SELECTOR, '#flt_labels')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            filters_labels
        )
        print(f"{datetime.now()}   Close the filters if selected")
        filter_labels_list = self.driver.find_elements(By.CSS_SELECTOR, 'span.cross-button')

        for attempt in range(3):
            try:
                if len(filter_labels_list) > 0:
                    for element in filter_labels_list:
                        element.click()
                break
            except StaleElementReferenceException:
                filter_labels_list = self.driver.find_elements(By.CSS_SELECTOR,
                                                               '#flt_labels > span > span.cross-button')

        print(f"{datetime.now()}   Select region filters")
        region_checkbox_list = self.driver.find_elements(By.CSS_SELECTOR, '#flt_reg > li > label.checkbox > span')
        region_random_list = random.sample(region_checkbox_list, 3)
        for element in region_random_list:
            ActionChains(d) \
                .move_to_element(element) \
                .click(element) \
                .perform()

        print(f"{datetime.now()}   Select sectors filters")
        sectors_checkbox_list = self.driver.find_elements(By.CSS_SELECTOR, '#flt_sec > li > label.checkbox > span')
        sectors_random_list = random.sample(sectors_checkbox_list, 2)
        for element in sectors_random_list:
            ActionChains(d) \
                .move_to_element(element) \
                .pause(0.5) \
                .click(element) \
                .perform()

        print(f"{datetime.now()}   Scroll to selected filters")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            filters_labels
        )
        selected_filters_locator = (By.CSS_SELECTOR, '#flt_labels > span >span.text-ellipsis')
        time_out = 10

        print(f"{datetime.now()}   Check the labels of the selected filters")

        while True:
            try:
                WebDriverWait(self.driver, time_out).until(
                    lambda b: len(self.driver.find_elements(*selected_filters_locator)) == 5
                )
                break
            except TimeoutException:
                return

        print(f"{datetime.now()}   Extract the text attribute from the labels of the selected filters")
        try:
            selected_filters_list = self.driver.find_elements(*selected_filters_locator)
            self.selected_filters_text_list = [filters.text for filters in selected_filters_list]
        except StaleElementReferenceException:
            selected_filters_list = self.driver.find_elements(*selected_filters_locator)
            self.selected_filters_text_list = [filters.text for filters in selected_filters_list]

    def arrange_v1(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v1")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll to the filter labels")
        filters_labels = self.driver.find_element(By.CSS_SELECTOR, '#flt_labels')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            filters_labels
        )
        print(f"{datetime.now()}   Close the filters if selected")
        filter_labels_list = self.driver.find_elements(By.CSS_SELECTOR, 'span.cross-button')
        for attempt in range(3):
            try:
                if len(filter_labels_list) > 0:
                    for element in filter_labels_list:
                        element.click()
                break
            except StaleElementReferenceException:
                filter_labels_list = self.driver.find_elements(By.CSS_SELECTOR,
                                                               '#flt_labels > span > span.cross-button')
        self.selected_filters_text_list = None

        print(f"{datetime.now()}   Select region filters")
        region_checkbox_list = self.driver.find_elements(By.CSS_SELECTOR, '#flt_reg > li > label.checkbox > span')
        region_random_list = random.sample(region_checkbox_list, 3)
        for element in region_random_list:
            element.click()
        region_text_list = [region.text for region in region_random_list]

        print(f"{datetime.now()}   Select sectors filters")
        sectors_checkbox_list = self.driver.find_elements(By.CSS_SELECTOR, '#flt_sec > li > label.checkbox > span')
        sectors_random_list = random.sample(sectors_checkbox_list, 2)
        for element in sectors_random_list:
            element.click()
        sectors_text_list = [sector.text for sector in sectors_random_list]

        self.selected_filters_text_list = region_text_list + sectors_text_list
        print(f"{datetime.now()}   All selected filters {self.selected_filters_text_list}")


    def element_click(self, d):
        print(f"\n{datetime.now()}   2. Act")

        print(f"{datetime.now()}   Select a random item sort")
        ActionChains(d) \
            .move_to_element(self.driver.find_element(By.CSS_SELECTOR, 'div.js-fieldDropdown-markets')) \
            .click(self.driver.find_element(By.CSS_SELECTOR, 'div.js-fieldDropdown-markets')) \
            .perform()

        dropdown_item_list = self.driver.find_elements(By.CSS_SELECTOR, 'ul > li.sort')
        dropdown_item = random.choice(dropdown_item_list)
        dropdown_text_item = dropdown_item.text

        ActionChains(d) \
            .move_to_element(dropdown_item) \
            .click(dropdown_item) \
            .perform()

        print(f"{datetime.now()}   Sort - {dropdown_text_item} - is selected")

class AssertFilters(BasePage):
    def __init__(self, driver, link="", bid=""):
        self.actual_filters_text_list = []
        super().__init__(driver, link, bid)

    @allure.step('Checking that applied filters "Region/Sectors" are displayed')
    def assert_filters(self, d, cur_link, selected_filters_text_list):
        print(f"\n{datetime.now()}   3. Assert_v0")

        filters_labels = self.driver.find_element(By.CSS_SELECTOR, '#flt_labels')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            filters_labels
        )

        actual_filters_locator = (By.CSS_SELECTOR, '#flt_labels > span > span.text-ellipsis')

        try:
            actual_filters_list = self.driver.find_elements(*actual_filters_locator)
            self.actual_filters_text_list = [element.text for element in actual_filters_list]
        except StaleElementReferenceException:
            actual_filters_list = self.driver.find_elements(*actual_filters_locator)
            self.actual_filters_text_list = [element.text for element in actual_filters_list]

        if set(self.actual_filters_text_list) != set(selected_filters_text_list) or not self.actual_filters_text_list:
            print(f"{datetime.now()}   Expected result: applied filters 'Region/Sectors' {selected_filters_text_list}"
                  f"\n"
                  f"Actual result: after selecting item 'Most traded' from the dropdown, are displayed {self.actual_filters_text_list}")
            Common.pytest_fail(f"Bug # 55!048 Expected result: Applied filters 'Region/Sectors': {selected_filters_text_list} "
                               f"\n"
                               f"are not displayed after selecting item 'Most traded' from the dropdown, "
                               f"\n"
                               f"only filters are displayed: {self.actual_filters_text_list}")
        else:
            print(f"{datetime.now()}   Applied filters {selected_filters_text_list} are displayed")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
