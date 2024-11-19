from datetime import datetime

from pages.Menu.New.from_learn_menu_open_risk_managment_guide import MenuNew
from pages.base_page import BasePage

main_page_link = 'https://capital.com/'
LOCATOR_LINK_BROKER = ('xpath', "//a[text()='broker']")


class Bug467(BasePage):

    @staticmethod
    def open_risk_management_page(d, cur_language, cur_country, link):
        MenuNew(d, main_page_link).from_learn_menu_open_risk_management_guide(d, cur_language, cur_country, link)

    def click_link_broker(self):
        print(f'\n{datetime.now()}   Click link "broker" =>')
        self.driver.find_element(*LOCATOR_LINK_BROKER).click()

        print(f'{datetime.now()}   => Done, the corresponding page is opened')
        print(f'{datetime.now()}   Current URL: {self.driver.current_url}')

    def should_be_au_or_ae_page(self):
        right_urls = ["https://capital.com/en-au/why-capital",
                      "https://capital.com/en-ae/why-capital",
                      "https://capital.com/en-eu/why-capital"]
        if self.driver.current_url in right_urls:
            return True
        return False
