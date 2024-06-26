from datetime import datetime
import random

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from pages.Elements.AssertClass import AssertClass
from pages.base_page import BasePage


class AppliedFilters(BasePage):

    def __init__(self, driver, link="", bid=""):
        self.selected_filters_text_list = None
        super().__init__(driver, link, bid)

    @allure.step(f"{datetime.now()}   Start full_test of display of applied filters")
    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):

        self.arrange_(d, cur_item_link)

        for i in range(5):
            self.element_click(d)
            self.open_page()
            test_element = AssertClass(d, cur_item_link)
            test_element.assert_filters(d, cur_item_link, self.selected_filters_text_list)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        filter_labels_list = self.driver.find_elements(By.CSS_SELECTOR, 'span.cross-button')
        if len(filter_labels_list) > 0:
            for element in filter_labels_list:
                element.click()

        region_checkbox_list = self.driver.find_elements(By.CSS_SELECTOR, '#flt_reg > li > label.checkbox > span')
        region_random_list = random.sample(region_checkbox_list, 3)
        for element in region_random_list:
            ActionChains(d) \
                .move_to_element(element) \
                .click(element) \
                .perform()

        sectors_checkbox_list = self.driver.find_elements(By.CSS_SELECTOR, '#flt_sec > li > label.checkbox > span')
        sectors_random_list = random.sample(sectors_checkbox_list, 2)
        for element in sectors_random_list:
            ActionChains(d) \
                .move_to_element(element) \
                .click(element) \
                .pause(0.3) \
                .perform()

        selected_filters_locator = (By.CSS_SELECTOR, '#flt_labels > span >span.text-ellipsis')
        time_out = 10
        Wait(self.driver, time_out).until(
            EC.presence_of_all_elements_located(selected_filters_locator)
        )

        selected_filters_list = self.driver.find_elements(*selected_filters_locator)
        self.selected_filters_text_list = [filters.text for filters in selected_filters_list]


    def element_click(self, d):
        print(f"\n{datetime.now()}   2. Act")

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
