"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import allure
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from pages.base_page import BasePage
from pages.Trading_platform.Topbar.topbar_locators import TopBarLocators


class TopBar(BasePage):

    @allure.step("Check if the Logo element is present on the page")
    def trading_platform_logo_is_present(self):
        """Check that the Capital.com Logo is present"""
        # Setup wait for later
        print(f"{datetime.now()}   Start check that the Trading platform page is loaded and LOGO is present on it =>")
        timeout = 15
        print(f"{datetime.now()}   Set timeout = {timeout}")
        wait = WebDriverWait(self.driver, timeout)

        # # Wait for the new tab to finish loading content
        # print(f"{datetime.now()}   Wait until load page with special title =>")
        # try:
        #     assert wait.until(EC.title_is("Trading Platform | Capital.com"), "Произошло исключение TimeoutException"), \
        #         'Page with title "Trading Platform | Capital.com" not loaded'
        #     print(f'{datetime.now()}   => Page with title "Trading Platform | Capital.com" is loaded')
        # except TimeoutException:
        #     pytest.fail(f'Page with "Trading Platform | Capital.com" title loaded over {timeout} seconds')
        #
        print(f"{datetime.now()}   Is present LOGO on this page? =>")
        if self.element_is_visible(TopBarLocators.LOGO, timeout):
            print(f"{datetime.now()}   => LOGO is visible on this page")
            return True
        else:
            print(f"{datetime.now()}   => LOGO not present on this page after more 30 seconds")
            return False
