from selenium.webdriver.common.by import By


class TradingMenuNew:
    # Trading
    MENU_SCA_TRADING = (
        By.CSS_SELECTOR, 'span > a[data-type="nav_id798"]')
    MENU_FCA_TRADING = (
        By.CSS_SELECTOR, 'span > a[data-type="nav_id686"]')


class MarketsMenuNew:
    MENU_FCA_MARKETS = (By.CSS_SELECTOR, 'span > a[data-type="nav_id689"]')
    MENU_SCA_MARKETS = (By.CSS_SELECTOR, 'span > a[data-type="nav_id824"]')


class PricingMenuNew:
    MENU_FCA_PRICING = (By.CSS_SELECTOR, 'span > a[data-type="nav_id737"]')
    MENU_SCA_PRICING = (By.CSS_SELECTOR, 'span > a[data-type="nav_id804"]')


class LearnMenuNew:
    MENU_FCA_LEARN = (By.CSS_SELECTOR, 'span > a[data-type="nav_id698"]')
    MENU_SCA_LEARN = (By.CSS_SELECTOR, 'span > a[data-type="nav_id831"]')


class AboutUsMenuNew:
    MENU_FCA_ABOUT_US = (By.CSS_SELECTOR, 'span > a[data-type="nav_id691"]')
    MENU_SCA_ABOUT_US = (By.CSS_SELECTOR, 'span > a[data-type="nav_id808"]')
