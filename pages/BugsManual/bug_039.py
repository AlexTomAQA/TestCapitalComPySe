"""
-*- coding: utf-8 -*-
@Time    : 2024/06/14 18:00
@Author  : Kasilà
"""

from datetime import datetime
import random

import allure
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.Elements.AssertClass import AssertClass
from pages.base_page import BasePage


class AppliedFilters(BasePage):

    def __init__(self, driver, link="", bid=""):
        self.selected_filters_text_list = None
        super().__init__(driver, link, bid)

    @allure.step(f"{datetime.now()}   Start full_test of display of applied filters")
    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):

        self.arrange_v1(d, cur_item_link)

        for i in range(5):
            self.element_click(d)
            self.open_page()
            test_element = AssertClass(d, cur_item_link)
            test_element.assert_filters(d, cur_item_link, self.selected_filters_text_list)

    def arrange_(self, d, cur_item_link):
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
        self.selected_filters_text_list = None

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
                .click(element) \
                .pause(0.3) \
                .perform()

        print(f"{datetime.now()}   Scroll to selected filters")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            filters_labels
        )
        selected_filters_locator = (By.CSS_SELECTOR, '#flt_labels > span >span.text-ellipsis')
        time_out = 5

        print(f"{datetime.now()}   Extract the text attribute of selected filters")
        selected_filters_list = self.elements_are_located(selected_filters_locator, time_out)
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

        print(f"{datetime.now()}   Select a random sort")
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