from selenium.webdriver.common.by import By


class TradingMenuNew:
    # Trading
    MENU_SCA_TRADING = (
        By.CSS_SELECTOR, '.menuGroup_linkfirstLevel__d5JGC > [data-type="nav_id798"]')

    # Trading platforms
    SUB_MENU_SCA_WEB_PLATFORM = (By.CSS_SELECTOR, '[data-type="nav_id818"]')


class MarketsMenuNew:
    pass


class PricingMenuNew:
    pass


class LearnMenuNew:
    MENU_NEW_LEARN = ()
    SUB_MENU_NEW_RISK = ()


class AboutUsMenuNew:
    pass
