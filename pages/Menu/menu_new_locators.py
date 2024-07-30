from selenium.webdriver.common.by import By


class MenuTrading:
    # Trading
    MENU_SCA_TRADING = (
        By.CSS_SELECTOR, '.menuGroup_linkfirstLevel__d5JGC > [data-type="nav_id798"]')

    ## Trading platforms
    SUB_MENU_SCA_WEB_PLATFORM = (By.CSS_SELECTOR, '[data-type="nav_id818"]')

    MENU_SCA_MARKETS = (By.CSS_SELECTOR, 'span > a[data-type="nav_id824"]')
    SUB_MENU_SCA_CRYPTOCURRENCIES = (By.CSS_SELECTOR, 'div.grid_grid__2D3md > a[data-type="nav_id895"')
