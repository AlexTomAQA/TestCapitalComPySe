from datetime import datetime

from pages.base_page import BasePage


class Locators:
    SIGNUP_BUTTON = ('css selector',
                     'div.wrap_wrap__S_v0r.panel_wrap__Y43T_ > div.accountBtns_btnsPlace___6pn2 div.accountBtns_btns___4MAA button.accountBtns_btn__vOcCs.accountBtns_btnPrimary__2wVcA')
    LINK_PRIVACY_POLICY = ('css selector',
                           'div.box_box__5Jmfa div.grid_grid__2D3md div.helpers_textCenter__cyckU p[data-testid="SIGN_UP_agreement"] a')


class Bug504(BasePage):

    def click_sign_up(self):
        print(f'\n{datetime.now()}   Click [Sign Up] button =>')
        self.driver.find_element(*Locators.SIGNUP_BUTTON).click()

    def should_be_link_to_privacy_policy(self):
        try:
            self.driver.find_element(*Locators.LINK_PRIVACY_POLICY)
            return True
        except:
            return False
