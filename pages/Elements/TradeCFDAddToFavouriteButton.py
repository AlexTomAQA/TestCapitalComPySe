from datetime import datetime
import pytest
import allure

from pages.Elements.AssertClass import AssertClass
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import TradeCFDLocators, TradingPlatformWatchlistTabs
from selenium.common.exceptions import ElementClickInterceptedException


class TradeCFDAddToFavoriteButton(BasePage):
    @allure.step(f"{datetime.now()}   Start test for TradeCFDAddToFavoriteButton of the trading instrument page")
    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)

        page_signup_login = SignupLogin(d, cur_item_link)
        page_signup_login.check_popup_signup_form()

        tab = TradingPlatformWatchlistTabs.FAVOURITES_TAB
        trade_instrument = self.element_click(cur_role)
        print(f"{datetime.now()}   Trade instrument from Full test is '{trade_instrument}'")
        test_element = AssertClass(d, cur_item_link, self.bid)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_with_selected_element(d, cur_item_link, tab, trade_instrument)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   BUTTON_ADD_TO_FAVOURITE is located on the page? =>")
        button_list = self.elements_are_located(TradeCFDLocators.ADD_TO_FAVORITE_BUTTON)

        if not button_list:
            print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE is not located on the page!")
            pytest.skip("ARRANGE: Checking element (BUTTON_ADD_TO_FAVOURITE) is not on this page")

        print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE is located on the page!")

    @allure.step("Click button [Add to favourite]")
    def element_click(self, cur_role):
        print(f"\n{datetime.now()}   2. Act_v0")
        button_list = self.driver.find_elements(*TradeCFDLocators.ADD_TO_FAVORITE_BUTTON)

        print(f"{datetime.now()}   BUTTON_ADD_TO_FAVOURITE is present? =>")
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE is not present on the page")
            del button_list
            return False
        print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE is present on the page")

        print(f"{datetime.now()}   BUTTON_ADD_TO_FAVOURITE scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )
        print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE scrolled")

        # Вытаскиваем линку из кнопки
        # button_link = button_list[0].get_attribute('href')
        # Берём ID итема, на который кликаем для сравнения с открытым ID на платформе
        # trade_instrument = button_link[button_link.find("spotlight") + 10:button_link.find("?")]
        trade_instrument = self.driver.find_element(*TradeCFDLocators.ITEM_NAME).text.split(' Spot')[0]

        print(f"{datetime.now()}   BUTTON_ADD_TO_FAVOURITE is clickable? =>")
        if not self.element_is_clickable(button_list[0], 5):
            print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE is not clickable more then 5 sec.")
            pytest.fail("BUTTON_ADD_TO_FAVOURITE is not clickable more then 5 sec.")
        try:
            print(f"{datetime.now()}   BUTTON_ADD_TO_FAVOURITE CLICK =>")
            button_list[0].click()
            # self.driver.execute_script("arguments[0].click();", button_list[0])
            print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE clicked!")

        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE NOT CLICKED")

            print(f"{datetime.now()}   'Sign up' form or page is auto opened")

            page_ = SignupLogin(self.driver)
            if page_.close_signup_form():
                pass
            elif page_.close_login_form():
                pass
            elif page_.close_signup_page():
                pass
            else:
                page_.close_login_page()

            # button_list[0].click()
            self.driver.execute_script("arguments[0].click();", button_list[0])
            del page_

        del button_list
        print(f'{datetime.now()}   Trade instrument from element click is {trade_instrument}')
        return trade_instrument

