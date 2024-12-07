"""
@Author  : Aleksei Kurochkin
"""
from pages.base_page import BasePage
from pages.Menu.New.from_learn_menu_open_market_guides import MenuNewLearn


class Locators:
    LINK_SHARES_TRADING_GUIDE = ('xpath', "//b[contains(text(), 'Shares trading guide')]")
    LINK_LEARN_MORE_ABOUT_IPOS = ('xpath', "//a[contains(text(), 'Learn more about IPOs.')]")
    LINK_LIQUIDITY = ('xpath', "//a[contains(text(), 'liquidity')]")
    TEXT_404 = ('xpath', "//p[contains(text(), '404')]")


class Bug587(BasePage):

    @staticmethod
    def open_page_market_guides(d, cur_language, cur_country, link):
        MenuNewLearn(d).from_learn_menu_open_market_guides(d, cur_language, cur_country, link)

    def click_shares_trading_guide(self):
        self.driver.find_element(*Locators.LINK_SHARES_TRADING_GUIDE).click()

    def click_learn_more_about_ipos(self):
        self.driver.find_element(*Locators.LINK_LEARN_MORE_ABOUT_IPOS).click()

    def click_liquidity(self):
        self.driver.find_element(*Locators.LINK_LIQUIDITY).click()

    def is_404_present_on_page(self):
        if self.driver.find_element(*Locators.TEXT_404):
            return True
        return False

