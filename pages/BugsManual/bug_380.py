"""
-*- coding: utf-8 -*-
@Time    : 2024/10/02 19:30
@Author  : Kasilà
"""


import random
from datetime import datetime
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.captcha import Captcha
from pages.common import Common


class SocialNetwork(BasePage):
    @allure.step(f"{datetime.now()}   Start testing that the relevant pages of 'Social networks' are opened”")
    def social_networks(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        tabs = self.driver.window_handles
        while True:
            if len(tabs) > 1:
                self.driver.switch_to.window(tabs[0])
                self.driver.close()
                self.driver.switch_to.window(tabs[1])
                tabs = self.driver.window_handles
            else:
                break

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Scroll to the 'How can we help?' block")
        how_can_we_help_block = self.driver.find_element(By.CSS_SELECTOR, 'div.path_mainContent__TIwFt > div > div:nth-child(2) > div')
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            how_can_we_help_block
        )

        print(f"{datetime.now()}   Click on the 'More' link on a random tile")
        while True:
            more_btn_list = self.driver.find_elements(By.CSS_SELECTOR, 'div.tile_content__zquEw > a')
            random_btn_more = random.choice(more_btn_list)
            random_btn_more.click()
            current_url = self.driver.current_url
            if current_url != 'https://capital.com/en-ae/about-us':
                break
            else:
                self.driver.back()

        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])

        current_url = self.driver.current_url
        print(f"{datetime.now()}   Current URL is {current_url}")

        print(f"{datetime.now()}   Scroll down to the 'Social networks' block")
        try:
            social_block = self.driver.find_element(By.CSS_SELECTOR, 'footer > div')
            self.driver.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                social_block
            )
        except NoSuchElementException:
            Captcha(d).fail_test_if_captcha_present_v3()

    def element_click(self, d):
        print(f"{datetime.now()}   2. Act")

        print(f"{datetime.now()}   Click a random social network icon")
        social_icon_list = self.driver.find_elements(By.CSS_SELECTOR, 'a.lt-footer__social-link')
        random_social_icon = random.choice(social_icon_list)
        random_social_icon.click()
        print(f"{datetime.now()}   The {random_social_icon.text} icon is clicked")

        tabs = self.driver.window_handles
        if len(tabs) > 2:
            self.driver.switch_to.window(tabs[2])

    @allure.step(f"{datetime.now()}   Assert")
    def assert_page(self, d):
        print(f"{datetime.now()}   3.Assert")

        current_page = self.driver.current_url
        expected_pages = ('https://www.facebook.com/capitalcom/', 'https://x.com/capitalcom',
                          'https://www.youtube.com/channel/UCn65Ma-zHYgnr56LPAwWDTw',
                          'https://www.linkedin.com/company/capital.com',
                          'https://www.instagram.com/accounts/login/?next=%2Faccounts%2Flogout%2F')

        if current_page in expected_pages:
            print(f"{datetime.now()}   The ({current_page}) page is opened")
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
        else:
            Common.pytest_fail(f"Bug # 55!380"
                               f"\n"
                               f"Expected result: The relevant page of a random 'Social network' is opened"
                               f"\n"
                               f"Actual result: The ({current_page}) page is opened")
