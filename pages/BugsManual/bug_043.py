"""
-*- coding: utf-8 -*-
@Time    : 2024/06/25 07:00
@Author  : podchasova11
"""
from datetime import datetime
import allure
import pytest

from pages.Menu.menu_locators import MenuUS55WaysToTrade
from pages.base_page import BasePage
from test_data.professional_page_data import page_title


class ProfessionalMenuCheckFooter(BasePage):

    @allure.step('Select Way_to_trade menu, Professional submenu, check that footer is displayed')
    def check_that_footer_displayed_on_professional_page(self, d, cur_language, cur_country, link):
        if not self.current_page_is(link):
            self.link = link
            self.open_page()

        self.check_that_footer_is_opened(d, cur_language, cur_country, link)

        print(f"\n{datetime.now()}   3. Cur URL = {d.current_url}")

    @allure.step(f"{datetime.now()}.   Check that Footer is opened on page [Professional]")
    def check_that_footer_is_opened(self, d, cur_language, cur_country, link):
        """
        Check that Footer is opened on the page [Professional]
        """

        self.should_be_page_title_v3(page_title["PAGE_TITLE"])

        footer = d.find_elements(*MenuUS55WaysToTrade.FOOTER_CAPITAL_LOGO)
        if len(footer) == 0:
            pytest.fail("Bug # 043. The footer is missing after clicked menu item [Professional] "
                        "of the menu section [Ways to trade]")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            footer[0]
        )

        print(f"{datetime.now()}   Is visible CAPITAL.COM logo from footer? =>")
        if self.element_is_visible(MenuUS55WaysToTrade.FOOTER_CAPITAL_LOGO):
            allure.attach(self.driver.get_screenshot_as_png(), "scr_qr", allure.attachment_type.PNG)
            print(f"{datetime.now()}   => CAPITAL.COM logo from footer is visible on the page")
        else:
            print(f"{datetime.now()}   => CAPITAL.COM logo from footer is not visible on the page")
            pytest.fail("Bug # 043. The footer is missing after click menu item [Professional] "
                        "of the menu section [Ways to trade]")



