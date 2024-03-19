from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import TradeCFDLocators
from selenium.common.exceptions import ElementClickInterceptedException


# class TradeCFDAddToFavoriteButton(BasePage):
#
#     @allure.step(f'{datetime.now()}   Start Full test for "Add to favourite" button on "Trade CFD" page')
#     def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):
#
#         self.arrange_(d, cur_item_link, True)
#         self.element_click()
#
#         test_element = AssertClass(d, cur_item_link, self.bid)
#         match cur_role:
#             case "NoReg":
#                 test_element.assert_signup(d, cur_language, cur_item_link)
#             case "NoAuth":
#                 test_element.assert_login(d, cur_language, cur_item_link)
#             case "Auth":
#                 test_element.assert_trading_platform_v4(d, cur_item_link)
#
#     def arrange_(self, d, cur_item_link, always=False):
#         print(f"\n{datetime.now()}   1. Arrange_v0")
#
#         if not self.current_page_is(cur_item_link):
#             self.link = cur_item_link
#             self.open_page()
#
#         button_list = self.driver.find_elements(*TradeCFDLocators.ADD_TO_FAVORITE_BUTTON)
#         if len(button_list) == 0:
#             print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE is not present on the page!")
#             del button_list
#             msg = "Testing element 'BUTTON_ADD_TO_FAVOURITE on 'Trade CFD' page is not on the DOM"
#             if always:
#                 pytest.fail(f"Bug № ??? {msg}")
#             else:
#                 pytest.skip(msg)
#
#         print(f"{datetime.now()}   BUTTON_ADD_TO_FAVOURITE scroll =>")
#         self.driver.execute_script(
#             'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', button_list[0]
#         )
#
#         print(f"{datetime.now()}   BUTTON_ADD_TO_FAVOURITE is visible? =>")
#         if self.element_is_visible(TradeCFDLocators.ADD_TO_FAVORITE_BUTTON):
#             print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE is visible on the page!")
#         else:
#             print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE is not visible on the page!")
#             pytest.fail("Bug! Testing element 'BUTTON_ADD_TO_FAVOURITE on 'Trade CFD' page is present on this page,"
#                         "but not visible")
#
#     @allure.step("Click button [Add to favourite] on 'Trade CFD' page")
#     def element_click(self):
#         print(f"\n{datetime.now()}   2. Act_v0")
#         print(f"{datetime.now()}   Start Click button [Add to favourite] =>")
#
#         button_list = self.driver.find_elements(*TradeCFDLocators.ADD_TO_FAVORITE_BUTTON)
#         print(f"{datetime.now()}   BUTTON_ADD_TO_FAVOURITE is clickable? =>")
#         time_out = 3
#         if not self.element_is_clickable(button_list[0], time_out):
#             print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE is not clickable after {time_out} sec. Stop TC>")
#             pytest.fail(f"BUTTON_ADD_TO_FAVOURITE is not clickable after {time_out} sec.")
#
#         print(f"{datetime.now()}   BUTTON_ADD_TO_FAVOURITE click =>")
#         button_not_clicked = False
#         try:
#             button_list[0].click()
#             print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE clicked")
#         except ElementClickInterceptedException:
#             button_not_clicked = True
#
#         if button_not_clicked:
#             print(f"{datetime.now()}   => BUTTON_ADD_TO_FAVOURITE not clicked")
#             pytest.fail(f"Bug # ??? BUTTON_ADD_TO_FAVOURITE is not clicked")
#
#         del button_list
#         return True

from datetime import datetime
import pytest
import allure

from pages.Elements.AssertClass import AssertClass
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import TradeCFDLocators
from selenium.common.exceptions import ElementClickInterceptedException


class TradeCFDAddToFavoriteButton(BasePage):

    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)

        # Checking if [SignUP for is popped up on the page]
        page_signup_login = SignupLogin(d, cur_item_link)
        page_signup_login.check_popup_signup_form()

        trade_instrument = self.element_click(cur_role)

        test_element = AssertClass(d, cur_item_link, self.bid)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link, False, True, trade_instrument)

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
        button_link = button_list[0].get_attribute('href')
        # Берём ID итема, на который кликаем для сравнения с открытым ID на платформе
        trade_instrument = button_link[button_link.find("spotlight") + 10:button_link.find("?")]

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
            else:
                page_.close_signup_page()

            # button_list[0].click()
            self.driver.execute_script("arguments[0].click();", button_list[0])
            del page_

        del button_list
        return trade_instrument
