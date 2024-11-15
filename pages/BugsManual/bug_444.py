from datetime import datetime

from pages.base_page import BasePage

LOCATOR_COUNTRY_SELECTION_BUTTON = ('css selector', 'button.localization_btn__9zIyt.js-analyticsClick')
LOCATOR_COUNTRY_SELECTION_BUTTON_IN_POPUP_WINDOW = ('css selector',
                                                    'div.select_selected__8wH_E.select_gI__pn40f.js-analyticsClick i.flag_flag__oDQ9A')
LOCATOR_COUNTRY_SEARCH_FIELD = ('css selector', 'input#search-country')


class Bug444(BasePage):

    def open_country_and_language_selection_pop_up_window(self):
        print(f'\n{datetime.now()}   Click language selection button =>')
        self.driver.find_element(*LOCATOR_COUNTRY_SELECTION_BUTTON).click()

    def click_dropdown_menu_country(self):
        print(f'\n{datetime.now()}   Click dropdown menu country =>')
        self.driver.find_element(*LOCATOR_COUNTRY_SELECTION_BUTTON_IN_POPUP_WINDOW).click()

    def check_placeholder_in_search_field(self):
        print(f'\n{datetime.now()}   Click dropdown menu country =>')
        search_field = self.driver.find_element(*LOCATOR_COUNTRY_SEARCH_FIELD)
        print(search_field.title)
        print(search_field.tag_name)
        print(search_field.text)
        print(search_field.get_attribute("placeholder"))
        print(search_field.placeholder)

        # if search_field[placeholder] == 'Country search':
        #     print("OK!!!")
        # else:
        #     print("FFFFFFFFFFF")



    # def click_sign_up(self):
    #     print(f'\n{datetime.now()}   Click [Sign Up] button =>')
    #     self.driver.find_element(*LOCATOR_SIGNUP_BUTTON).click()
    #
    # def should_be_link_to_privacy_policy(self):
    #     try:
    #         self.driver.find_element(*LOCATOR_LINK_PRIVACY_POLICY)
    #         return True
    #     except:
    #         return False
