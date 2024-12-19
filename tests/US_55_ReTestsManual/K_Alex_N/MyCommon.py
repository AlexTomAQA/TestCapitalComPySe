from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class MyCommon:

    @staticmethod
    def search_and_open_an_article_in_market_analysis_page(driver, part_of_article_title):

        ARTICLE_LOCATOR = (By.XPATH, f"//div[@id='alc']//b[contains(text(), '{part_of_article_title}')]")
        LOCATOR_LINK_NEXT_PAGE = (By.XPATH, '//a[@aria-label="Go to the next page"]')
        LOCATOR_LAST_PAGE = (By.XPATH, '//a[@aria-label="Go to the next page"]/preceding::a[1]')
        CLOSE_BLUE_BLOCK = (By.CSS_SELECTOR, "div.main_banner__niieI button")

        # def is_clickable(locator):
        #     return WebDriverWait(driver, 1).until(EC.element_to_be_clickable(locator))

        def get_last_page() -> int:
            try:
                last_page_obj = driver.find_element(*LOCATOR_LAST_PAGE)
                last_page_number = int(last_page_obj.text)
                return last_page_number
            except:
                raise Exception("Last page number was not found")

        def is_article_present():
            try:
                driver.find_element(*ARTICLE_LOCATOR)
                return True
            except NoSuchElementException:
                return False

        def to_close_blue_block():
            try:
                driver.find_element(*CLOSE_BLUE_BLOCK).click()
            except:
                return

        def open_the_article():
            to_close_blue_block()
            driver.find_element(*ARTICLE_LOCATOR).click()

        def go_to_next_page():
            driver.find_element(*LOCATOR_LINK_NEXT_PAGE).click()

        last_page = get_last_page()

        for _ in range(1, last_page + 1):
            if is_article_present():
                open_the_article()
                return
            else:
                go_to_next_page()

        raise Exception(f"{last_page} pages were checked. Artile was not found.")
