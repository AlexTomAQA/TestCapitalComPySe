from datetime import datetime
import random

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AppliedFilters(BasePage):
    @allure.step(f"{datetime.now()}, Start full_test of display of applied filters")
    def full_test(self):
        region_checkbox_list = self.driver.find_elements(*By.CSS_SELECTOR, '#flt_reg > li > label.checkbox > span')
        sectors_checkbox_list = self.driver.find_elements(*By.CSS_SELECTOR, '#flt_sec > li > label.checkbox > span')

        region_random_list = random.sample(region_checkbox_list, 3)

        for element in region_random_list:
            element.click()
        #        region_text_list = [element.text for element in region_random_list]

        sectors_random_list = random.sample(sectors_checkbox_list, 2)
        for element in sectors_random_list:
            element.click()
        #        sector_text_list = [element.text for element in sectors_random_list]

        #        filters_list = region_text_list + sector_text_list

        selected_filters_list = self.driver.find_elements(*By.CSS_SELECTOR, '#flt_labels > span >span.text-ellipsis')
        selected_filters_text_list = [filters.text for filters in selected_filters_list]
        print(selected_filters_text_list)

        self.driver.refresh()

        filters_list_after_refresh = self.driver.find_elements(*By.CSS_SELECTOR, '#flt_labels > span >span.text-ellipsis')
        filters_text_list_after_refresh = [element.text for element in filters_list_after_refresh]
        print(filters_text_list_after_refresh)