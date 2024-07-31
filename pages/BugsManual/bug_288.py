"""
-*- coding: utf-8 -*-
@Time    : 2024/07/22 16:40 GMT+5
@Author  : Sergey Aiidzhanov
"""

from datetime import datetime

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

WHY_CAPITAL_MENU_ITEM_LOC = ("css selector", "a[data-type='nav_id115']")
OUR_MOB_APPS_LINK_LOC = ("css selector", "#sectionAccordionIndustry~.sectionAccordion__box--bgDark a")
BREADCRUMB_LOC = ("css selector", ".cc-breadcrumbs span")
TITLE_LOC = ("css selector", "h1.headTitle")    # title of Mobile Apps page
TITLE_ALT_LOC = ("css selector", "h1.hero")     # title of Trading Products page


class Bug288(BasePage):
    def click_why_capital_menu_item(self):
        print(f'\n{datetime.now()}   Click the Why Capital.com? menu item =>')
        el = Wait(self.driver, 5).until(EC.element_to_be_clickable(WHY_CAPITAL_MENU_ITEM_LOC))
        el.click()
        print(f'{datetime.now()}   => Done, the corresponding page is opened')
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')

    def click_our_mobile_apps_link(self):
        print(f'\n{datetime.now()}   Click the Our mobile Apps link =>')
        link = Wait(self.driver, 5).until(EC.element_to_be_clickable(OUR_MOB_APPS_LINK_LOC))
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            link
        )
        link.click()
        print(f'{datetime.now()}   => Done, the corresponding page is opened')
        print(f'\n{datetime.now()}   Current URL: {self.driver.current_url}')

    def should_be_mobile_apps_page(self, cur_language):
        print(f'\n{datetime.now()}   Check if the Mobile Apps page is opened =>')

        bc_name = ''
        title_name = ''

        match cur_language:
            case "ar":
                bc_name = 'تطبيقاتنا للهواتف المحمولة'
                title_name = 'تطبيقات جوّال Capital.com'
            case "de":
                bc_name = 'Unsere mobile App'
                title_name = 'Capital.com: Mobile Apps'
            case "el":
                bc_name = 'Τρόποι να διαπραγματευτείτε'     # breadcrumb and title of Trading Products page
                title_name = 'Τρόποι να διαπραγματευτείτε'   # Mobile Apps page does not exist
            case "es":
                bc_name = 'Nuestras aplicaciones móviles'
                title_name = 'Aplicaciones móviles de Capital.com'
            case "fr":
                bc_name = 'Nos applis mobiles'
                title_name = 'Applications mobiles de Capital.com'
            case "it":
                bc_name = 'Le nostre app mobili'
                title_name = 'App per dispositivi mobili di Capital.com'
            case "hu":
                bc_name = 'Mobilalkalmazásunk'
                title_name = 'Capital.com mobilalkalmazások'
            case "nl":
                bc_name = 'Onze mobiele apps'
                title_name = 'Capital.com mobiele apps'
            case "pl":
                bc_name = 'Nasze aplikacje mobilne'
                title_name = 'Aplikacje mobilne Capital.com'
            case "ro":
                bc_name = 'Aplicațiile noastre mobile'
                title_name = 'Aplicații mobile Capital.com'
            case "ru":
                bc_name = 'Наше мобильное приложение'
                title_name = 'Мобильные приложения Capital.com'
            case "zh":
                bc_name = '交易方式'       # breadcrumb and title of Trading Products page
                title_name = '交易方式'    # Mobile Apps page does not exist
            case "cn":
                bc_name = '我们的移动应用程序'
                title_name = 'Capital.com 移動應用程序'

            # TEST TEST

        if cur_language in ['el', 'zh']:
            if bc_name not in self.driver.find_element(*BREADCRUMB_LOC).text:
                if title_name not in self.driver.find_element(*TITLE_ALT_LOC).text:
                    print(f'{datetime.now()}   => The Mobile Apps page is opened')
                    return True
            print(f'{datetime.now()}   => Wrong page')
            return False

        if bc_name in self.driver.find_element(*BREADCRUMB_LOC).text:
            if title_name in self.driver.find_element(*TITLE_LOC).text:
                print(f'{datetime.now()}   => The Mobile Apps page is opened')
                return True
        print(f'{datetime.now()}   => Wrong page')
        return False
