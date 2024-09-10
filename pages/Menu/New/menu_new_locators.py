from selenium.webdriver.common.by import By


class TradingMenuNew:
    # Trading
    MENU_SCA_TRADING = (By.CSS_SELECTOR, 'span > a[data-type="nav_id798"]')
    MENU_FCA_TRADING = (By.CSS_SELECTOR, 'span > a[data-type="nav_id686"]')
    MENU_ASIC_TRADING = (By.CSS_SELECTOR, 'span > a[data-type="nav_id1292"]')


class MarketsMenuNew:
    MENU_FCA_MARKETS = (By.CSS_SELECTOR, 'span > a[data-type="nav_id689"]')
    MENU_SCA_MARKETS = (By.CSS_SELECTOR, 'span > a[data-type="nav_id824"]')
    MENU_ASIC_MARKETS = (By.CSS_SELECTOR, 'span > a[data-type="nav_id1256"]')


class PricingMenuNew:
    MENU_FCA_PRICING = (By.CSS_SELECTOR, 'span > a[data-type="nav_id737"]')
    MENU_SCA_PRICING = (By.CSS_SELECTOR, 'span > a[data-type="nav_id804"]')
    MENU_ASIC_PRICING = (By.CSS_SELECTOR, 'span > a[data-type="nav_id1287"]')


class LearnMenuNew:
    MENU_FCA_LEARN = (By.CSS_SELECTOR, 'span > a[data-type="nav_id698"]')
    MENU_SCA_LEARN = (By.CSS_SELECTOR, 'span > a[data-type="nav_id831"]')
    MENU_ASIC_LEARN = (By.CSS_SELECTOR, 'span > a[data-type="nav_id1174"]')


class AboutUsMenuNew:
    MENU_FCA_ABOUT_US = (By.CSS_SELECTOR, 'span > a[data-type="nav_id691"]')
    MENU_SCA_ABOUT_US = (By.CSS_SELECTOR, 'span > a[data-type="nav_id808"]')
    MENU_ASIC_ABOUT_US = (By.CSS_SELECTOR, 'span > a[data-type="nav_id1272"]')
