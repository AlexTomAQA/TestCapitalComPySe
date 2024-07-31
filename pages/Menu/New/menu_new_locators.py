from selenium.webdriver.common.by import By


class TradingMenuNew:
    # Trading
    MENU_SCA_TRADING = (
        By.CSS_SELECTOR, '.menuGroup_linkfirstLevel__d5JGC > [data-type="nav_id798"]')
    MENU_FCA_TRADING = (
        By.CSS_SELECTOR, '.menuGroup_linkfirstLevel__d5JGC > [data-type="nav_id686"]')

    # Trading platforms
    SUB_MENU_SCA_WEB_PLATFORM = (By.CSS_SELECTOR, '[data-type="nav_id818"]')
    SUB_MENU_FCA_SPREAD_BETTING = (By.CSS_SELECTOR, '[data-type="nav_id735"]')


class MarketsMenuNew:
    MENU_SCA_MARKETS = (By.CSS_SELECTOR, 'span > a[data-type="nav_id824"]')
    SUB_MENU_SCA_CRYPTOCURRENCIES = (By.CSS_SELECTOR, 'div.grid_grid__2D3md > a[data-type="nav_id895"')


class PricingMenuNew:
    pass


class LearnMenuNew:
    MENU_NEW_LEARN = ()
    SUB_MENU_NEW_RISK = ()


class AboutUsMenuNew:
    pass
