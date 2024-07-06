"""
-*- coding: utf-8 -*-
@Time    : 2023/04/13 18:25
@Author  : Alexander Tomelo
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HeaderButtonLoginLocators:
    """ Locators for ..."""
    BUTTON_LOGIN = (By.CSS_SELECTOR, "div.cc-header__wrap > div#wphWrap a#wg_loginBtn")


class HeaderButtonTradeLocators:
    BUTTON_TRADE = (By.CSS_SELECTOR, ".cc-header__wrap > #wphWrap > .js_signup")


class VideoBannerLocators:
    VIDEO_BANNER = (By.CSS_SELECTOR, "div.side-video.side-video--vertical video")


class ButtonsUnderVideoBannerLocators:
    BUTTON_UNDER_VIDEO_BANNER_OLD = \
        (By.CSS_SELECTOR, "div.side-video.side-video--vertical > div > a.js_signup")
    BUTTON_TRY_FREE_DEMO_UNDER_VIDEO_BANNER = \
        (By.CSS_SELECTOR,
         "div.side-video.side-video--vertical > div > a[href='https://capital.com/trading/signup?go=demo']")
    BUTTON_CREATE_ACCOUNT_UNDER_VIDEO_BANNER = \
        (By.CSS_SELECTOR, "div.side-video.side-video--vertical > div > a")
    BUTTON_TRADE_NOW_UNDER_VIDEO_BANNER = \
        (By.CSS_SELECTOR, "div.side-video.side-video--vertical > div > a")


class VerHorBannerButtonLocators:
    VER_HOR_BANNER_BUTTON = (By.CSS_SELECTOR, ".grid  div.seo-banner a[href='/trading/signup']")

    # VER_BANNER_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "div.seo-banner > div > a[href='/trading/signup']")
    # HOR_BANNER_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "div.seo-banner > div > a[href='/trading/signup']")


class ButtonFreeDemoOnHorizontalBannerLocators:
    # old locator - BUTTON_FREE_DEMO_ON_HOR_BANNER = (By.CSS_SELECTOR, "div.js-bannerSection > .seo-banner--type1 a")
    BUTTON_FREE_DEMO_ON_HOR_BANNER = (By.CSS_SELECTOR, ".js-bannerSection div:not(.hidden).js-showBanner "
                                                       "[href='/trading/signup'][data-type*='b_hor']")


class ButtonOnHorizontalBannerLocators:
    BUTTON_ON_HOR_BANNER = (By.CSS_SELECTOR, ".js-showBanner:not(.hidden) .button-main[data-type*='b_hor']")


class ButtonOnVerticalBannerLocators:
    BUTTON_ON_VER_BANNER = (By.CSS_SELECTOR, ".js-showBanner:not(.hidden) .button-main[data-type*='b_vert']")


class BlockStepTradingLocators:
    BUT_CREATE_YOUR_ACCOUNT = (By.CSS_SELECTOR, "section.regSteps i.regSteps__item.js_signup")
    BUT_CREATE_YOUR_ACCOUNT_DE = (By.CSS_SELECTOR, "#cc_ab42 div.js_signup")
    BUT_CREATE_YOUR_ACCOUNT_EN = (By.CSS_SELECTOR, '[data-type="banner_with_steps"]')


class ButtonInBannerLocators:
    # BUTTON_IN_BANNER = (By.CSS_SELECTOR, ".grid .detail__aside .inBanner > a")
    BUTTON_IN_BANNER = (By.XPATH, "//div[not(contains(@class, 'hidden'))]/div/a[contains(@data-type, 'b_vert') "
                                  "and (@href='/trading/signup')]")
    BUTTON_IN_BANNER_DEMO = (By.CSS_SELECTOR, ".grid.detail__aside.inBanner > a[data - demomode = 'true']")


class ButtonTradeOnWidgetMostTradedLocators:
    MOST_TRADED = (By.CSS_SELECTOR, "div.mostTraded__market > a[href*='spotlight']")  # List
    MOST_TRADED_LIST = (By.CSS_SELECTOR, "div.mostTraded__market > a")
    MOST_TRADED_NAME_LIST = (By.CSS_SELECTOR, ".mostTraded__info > a")
    # MOST_TRADED_1 = (By.CSS_SELECTOR, "div:nth-child(1) > div.mostTraded__market > a")
    # MOST_TRADED_2 = (By.CSS_SELECTOR, "div:nth-child(2) > div.mostTraded__market > a")
    # MOST_TRADED_3 = (By.CSS_SELECTOR, "div:nth-child(3) > div.mostTraded__market > a")
    # MOST_TRADED_4 = (By.CSS_SELECTOR, "div:nth-child(4) > div.mostTraded__market > a")
    # MOST_TRADED_5 = (By.CSS_SELECTOR, "div:nth-child(5) > div.mostTraded__market > a")


class ButtonSellOnTableTradingInstrumentsLocators:
    TABLE_TRADING_INSTRUMENTS = (By.CSS_SELECTOR, "div.table-instruments table.table tbody")  # List
    TABLE_TRADING_INSTRUMENTS_LIST = (By.CSS_SELECTOR, "div.table-instruments a[data-side='sell']")  # Items
    TABLE_TRADING_INSTRUMENTS_NAME_LIST = (By.CSS_SELECTOR, "div.table-instruments p.table__info.stringEllipsed")


class BlockOurCoursesLocators:
    BUTTON_CREATE_ACCOUNT = (By.CSS_SELECTOR, "div [href='https://capital.com/trading/signup']")


class CoursesPage:
    COURSES_PAGES_LIST = (By.CSS_SELECTOR, "li.courseCard__row > a")


class SubPages:
    SUB_PAGES_LIST = (By.CSS_SELECTOR, "div.side-nav__wrap > div.side-nav > a")
    SUB_PAGES_MARKETS_FOREX_LIST = (By.CSS_SELECTOR, "tr.trlink.js-trlink > td > p > a")
    SUB_PAGES_MARKETS_TABLE_INSTRUMENTS_LIST = (By.CSS_SELECTOR, "div.table-instruments  td > p > a")


class BlockBuildYourSkills:
    BUTTON_CREATE_DEMO_ACCOUNT = \
        (By.CSS_SELECTOR,
         ".js-bannerSection .js-showBanner.whiteB [href='/trading/signup'][data-type*='b_ver']")


class BlockLearnFirstTradeCFD:
    BUTTON_TRY_DEMO = \
        (By.CSS_SELECTOR,
         ".js-bannerSection .js-showBanner.blueB [href='/trading/signup'][data-type*='b_ver']")


class ButtonsOnPageLocators:
    BUTTON_START_TRADING_IN_ARTICLE = (By.CSS_SELECTOR, "ul > li:nth-child(1) > a.js_signup")
    BUTTON_START_TRADING_IN_ARTICLE2 = (By.CSS_SELECTOR, ".hidden-xs.no-wrap.ready-starting__btn > a")
    BUTTON_START_TRADING_IN_ARTICLE3 = (By.CSS_SELECTOR, "[data-type='hp_choose_capital']")
    BUTTON_TRADING_SELL = (By.CSS_SELECTOR, "a.button-main.sell.ln-auto.js_signup")
    BUTTON_TRADING_BUY = (By.CSS_SELECTOR, "a.button-main.buy.ln-auto.js_signup")
    BUTTON_CREATE_ACCOUNT = (By.CSS_SELECTOR, "a[data-type='wdg_go_to_market_deeplink']")
    TRADING_INSTRUMENT = (By.CSS_SELECTOR, ".side-nav a.active")

    # Tables with Sell/Buy
    # Type of FI
    TYPE_FI_SHARES = (By.CSS_SELECTOR, "")
    TYPE_FI_COMMODITIES = (By.CSS_SELECTOR, "")
    TYPE_FI_FOREX = (By.CSS_SELECTOR, "")
    TYPE_FI_CRYPTOCURRENCY = (By.CSS_SELECTOR, "")
    TYPE_FI_INDICES = (By.CSS_SELECTOR, "")

    # Tabs of CFDs TABLE
    TABLE_CFDS = (By.CSS_SELECTOR, '.section.section__tabs')
    TAB_TRADING_ITEM_MOST_TRADED = (By.CSS_SELECTOR, '[data-id="mosttraded"]')
    TAB_TRADING_ITEM_TOP_RISERS = (By.CSS_SELECTOR, '[data-id="risers"]')
    TAB_TRADING_ITEM_TOP_FALLERS = (By.CSS_SELECTOR, '[data-id="fallers"]')
    TAB_TRADING_ITEM_MOST_VOLATILE = (By.CSS_SELECTOR, '[data-id="volatile"]')

    # Elements of 'Trade CFDs on Capital.com via TradingView' block
    TRADE_CFDS_ON_CAPITAL_BLOCK = (By.CSS_SELECTOR, '.tradingView[data-type="tradingview"]')
    EXPLORE_FEATURES_BUTTON = (By.CSS_SELECTOR, '.tradingView__btn[data-type="tradingview"]')

    # Elements of 'Trading instrument' widget
    TRADING_INSTRUMENT_WIDGET = (By.CSS_SELECTOR, '[data-wrap="homePage"]')

    MOST_TRADED_MARKET_TRADING_INSTRUMENT = (By.CSS_SELECTOR, '[data-type="wdg_market_tab_mosttraded"]')
    COMMODITIES_MARKET_TRADING_INSTRUMENT = (By.CSS_SELECTOR, '[data-type="wdg_market_tab_COM"]')
    INDICES_MARKET_TRADING_INSTRUMENT = (By.CSS_SELECTOR, '[data-type="wdg_market_tab_IND"]')
    CRYPTOCURRENCIES_MARKET_TRADING_INSTRUMENT = (By.CSS_SELECTOR, '[data-type="wdg_market_tab_CRYPTO"]')
    SHARES_MARKET_TRADING_INSTRUMENT = (By.CSS_SELECTOR, '[data-type="wdg_market_tab_SHARE"]')
    FOREX_MARKET_TRADING_INSTRUMENT = (By.CSS_SELECTOR, '[data-type="wdg_market_tab_FOREX"]')
    ETFS_MARKET_TRADING_INSTRUMENT = (By.CSS_SELECTOR, '[data-type="wdg_market_tab_etfs"]')

    MEATBALLS_MENU_BUTTON = (By.CSS_SELECTOR, '.cc-boxXs.tabsDrop__btn.js-tabsDrop__btn')

    TRADE_BUTTON_TRADING_INSTRUMENT = (By.CSS_SELECTOR, '.wMarkets__btn.js-wMarkets__tradeBtn.showLg')
    NAME_OF_TRADING_INSTRUMENT = (By.CSS_SELECTOR, '.wMarkets .wMarkets__item.js-wMarkets__item .wMarkets__link')

    # Elements of Our markets block
    OUR_MARKETS_BLOCK = (By.CSS_SELECTOR, '[data-type="wdg_markets"] .grid_grid__2D3md.grid_gComponent__Xx_xR')

    MOST_TRADED_MARKET = (By.CSS_SELECTOR, '[data-type="wdg_markets_tab_mosttraded"]')
    COMMODITIES_MARKET = (By.CSS_SELECTOR, '[data-type="wdg_markets_tab_COM"]')
    INDICES_MARKET = (By.CSS_SELECTOR, '[data-type="wdg_markets_tab_IND"]')
    SHARES_MARKET = (By.CSS_SELECTOR, '[data-type="wdg_markets_tab_SHARE"]')
    FOREX_MARKET = (By.CSS_SELECTOR, '[data-type="wdg_markets_tab_CURRENCY"]')
    ETFS_MARKET = (By.CSS_SELECTOR, '[data-type="wdg_markets_tab_etfs"]')

    BUTTON_OUR_MARKETS_BUY = (By.CSS_SELECTOR, "[data-type='wdg_markets_buy_btn']")
    BUTTON_OUR_MARKETS_SELL = (By.CSS_SELECTOR, "[data-type='wdg_markets_sell_btn']")
    INSTRUMENTS_OUR_MARKETS = (By.CSS_SELECTOR, "#splide01-list .splide__slide")

    BUTTON_ARROW_RIGHT = (By.CSS_SELECTOR, ".splide__arrow.splide__arrow--next")
    BUTTON_ARROW_LEFT = (By.CSS_SELECTOR, ".splide__arrow.splide__arrow--prev")

    # Elements of Widget 'Trading calculator'
    TRADING_CALCULATOR_WIDGET = (By.CSS_SELECTOR, '.tradingCalc.js-tradingCalc')
    BUTTON_START_TRADING_IN_TRADING_CALCULATOR = (By.CSS_SELECTOR, "[data-type='btn_calculator']")
    BUTTON_TRADE_NOW_IN_TRADING_CALCULATOR = (By.CSS_SELECTOR, "[data-type='btn_calculator_3']")

    # Elements of 'Trading experience' block
    TRADING_EXPERIENCE_BLOCK = (By.XPATH, "//div[@class='gapMd']")
    BUTTON_START_TRADING_IN_TRADING_EXPERIENCE = (By.CSS_SELECTOR, "[data-type='hp_choose_capital']")

    # Elements of 'Try trading for free' block
    TRY_TRADING_FOR_FREE_BLOCK = (By.CSS_SELECTOR, ".cc-boxXl.newToTrading")
    BUTTON_CREATE_DEMO_ACCOUNT_IN_TRADING_FOR_FREE = \
        (By.CSS_SELECTOR, "div [href='https://capital.com/trading/signup?go=demo']")

    # Item name
    SPAN_TRADING_ITEM_MOST_TRADED = (By.CSS_SELECTOR, ".table-tools.catTabs.tab-mosttraded > table > "
                                                      "tbody > tr > td.name > a > span.table-tools__title")
    SPAN_TRADING_ITEM_TOP_RISERS = (By.CSS_SELECTOR, ".table-tools.catTabs.tab-risers > table > "
                                                     "tbody > tr > td.name > a > span.table-tools__title")
    SPAN_TRADING_ITEM_TOP_FALLERS = (By.CSS_SELECTOR, ".table-tools.catTabs.tab-fallers > table > "
                                                      "tbody > tr > td.name > a > span.table-tools__title")
    SPAN_TRADING_ITEM_MOST_VOLATILE = (By.CSS_SELECTOR, ".table-tools.catTabs.tab-volatile > table > "
                                                        "tbody > tr > td.name > a > span.table-tools__title")
    # Buttons
    BUTTON_TRADING_SELL_MOST_TRADED = (By.CSS_SELECTOR, ".tab-mosttraded > table > tbody > tr > td:nth-child(3) > a")
    BUTTON_TRADING_BUY_MOST_TRADED = (By.CSS_SELECTOR, ".tab-mosttraded > table > tbody > tr > td:nth-child(5) > a")

    BUTTON_TRADING_SELL_TOP_RISERS = (By.CSS_SELECTOR, ".tab-risers > table > tbody > tr > td:nth-child(3) > a")
    BUTTON_TRADING_BUY_TOP_RISERS = (By.CSS_SELECTOR, ".tab-risers > table > tbody > tr > td:nth-child(5) > a")

    BUTTON_TRADING_SELL_TOP_FALLERS = (By.CSS_SELECTOR, ".tab-fallers > table > tbody > tr > td:nth-child(3) > a")
    BUTTON_TRADING_BUY_TOP_FALLERS = (By.CSS_SELECTOR, ".tab-fallers > table > tbody > tr > td:nth-child(5) > a")

    BUTTON_TRADING_SELL_MOST_VOLATILE = (By.CSS_SELECTOR, ".tab-volatile > table > tbody > tr > td:nth-child(3) > a")
    BUTTON_TRADING_BUY_MOST_VOLATILE = (By.CSS_SELECTOR, ".tab-volatile > table > tbody > tr > td:nth-child(5) > a")

    BUTTON_TRADING_SHOW_ALL_TAB_MOSTTRADED = (By.CSS_SELECTOR, ".tab-mosttraded > p > .btnShowMore > .js-showText")
    BUTTON_TRADING_SHOW_ALL_TAB_RISERS = (By.CSS_SELECTOR, ".tab-risers > p > .btnShowMore > .js-showText")
    BUTTON_TRADING_SHOW_ALL_TAB_FAILERS = (By.CSS_SELECTOR, ".tab-fallers > p > .btnShowMore > .js-showText")
    BUTTON_TRADING_SHOW_ALL_TAB_VOLATILE = (By.CSS_SELECTOR, ".tab-volatile > p > .btnShowMore > .js-showText")

    BUTTON_ON_STICKY_BAR = (By.CSS_SELECTOR, "div.encStickyBar > div > a")
    BUTTON_SIGNUP_LOGIN = (By.CSS_SELECTOR, "a[href='/trading/signup'][class*='__cp_b'][class*='ln-auto']")


class MainBannerLocators:
    BUTTON_START_TRADING = (By.CSS_SELECTOR, "a.cc-banner__btn.btn.btn--darkText.js_signup")
    BUTTON_TRY_DEMO = (By.CSS_SELECTOR, "a.cc-banner__btn.btn.btn--emptyblack.js_signup.hideXs")
    BUTTON_OPEN_AN_ACCOUNT = (By.CSS_SELECTOR, '[data-type*="background_banner_block_btn1"]')
    BUTTON_TRY_DEMO_ACCOUNT = (By.CSS_SELECTOR, '[data-type*="background_banner_block_btn2"]')
    BUTTON_TRY_DEMO_MAIN_PAGE = (By.CSS_SELECTOR, '[data-type*="homepage_hero_banner_btn1_demo"]')
    BUTTON_SIGN_UP_MAIN_PAGE = (By.CSS_SELECTOR, '[data-type*="homepage_hero_banner_btn2_signup"]')


class MainPageBannerLocators:
    MAIN_PAGE_BANNER_BLOCK = (By.CSS_SELECTOR, "main > .bannersHome")
    GET_INVOLVED_TAB_MAIN_PAGE_BANNER = (By.CSS_SELECTOR, '.bannersHome__nav > [data-slick-index = "0"]')
    TRADE_NOW_BUTTON_GET_INVOLVED_TAB = (
        By.XPATH, '//div[@class="bannersHome__buttons"] /a[@href="/trading/signup"]')
    TRY_FREE_DEMO_BUTTON_GET_INVOLVED_TAB = (
        By.XPATH, '//div[@class="bannersHome__buttons"] /a[@href="/trading/signup?go=demo"]')

    FIND_US_ON_TRADINGVIEW_TAB_MAIN_PAGE_BANNER = (By.CSS_SELECTOR, 'button[data-type="topbanner-tradingview_slider"]')
    EXPLORE_FEATURES_BUTTON_FIND_US_ON_TRADINGVIEW_TAB = (
        By.XPATH, '//div[@class="bannersHome__buttons"] /a[@href="https://www.tradingview.com/broker/Capitalcom/"]')

    MAIN_PAGE_BANNER_BLOCK_V2 = (By.CSS_SELECTOR, "main.grid.gLg")
    GET_INVOLVED_TAB_MAIN_PAGE_BANNER_V2 = (By.CSS_SELECTOR, 'button[aria-controls="splide01-slide02"]')
    INDUSTRY_LEADING_SUPPORT_TAB_MAIN_PAGE_BANNER_V2 = (
        By.CSS_SELECTOR, 'button[aria-controls="splide01-slide04"]')
    START_TRADING_BUTTON_INDUSTRY_LEADING_SUPPORT_TAB_V2 = (
        By.CSS_SELECTOR, '#splide01-slide04 [href="/trading/signup"]')
    PRACTICE_FOR_FREE_BUTTON_INDUSTRY_LEADING_SUPPORT_TAB_V2 = (
        By.CSS_SELECTOR, '#splide01-slide04 [href="/trading/signup?go=demo"]')
    TRADE_NOW_BUTTON_GET_INVOLVED_TAB_V2 = (By.CSS_SELECTOR, '#splide01-slide02 [href="/trading/signup"]')
    PRACTICE_FOR_FREE_BUTTON_GET_INVOLVED_TAB_V2 = (
        By.CSS_SELECTOR, '#splide01-slide02 [href="/trading/signup?go=demo"]')


class RightBannerLocators:
    BUTTON_TRY_DEMO_RIGHT_BANNER = (By.CSS_SELECTOR, "btn inBanner__btn rounded-lg ln-auto")


class BlockSignUpAndTradeSmartTodayLocators:
    BUTTON_DOWNLOAD_APP_STORE = (By.CSS_SELECTOR, "div.banner-capital__buttons a[data-type='banner_capital_ios']")
    BUTTON_GET_IT_ON_GOOGLE_PLAY = (By.CSS_SELECTOR, "div.banner-capital__buttons a[data-type='banner_capital_google']")
    BUTTON_EXPLORE_WEB_PLATFORM = (
        By.CSS_SELECTOR, "a.badge-platform.banner-capital__button-store")
    OLD_BUTTON_EXPLORE_WEB_PLATFORM = (
        By.CSS_SELECTOR, "div.banner-capital__buttons a[data-type='banner_capital_platform']")


class ContentBlockLocators:
    BUTTON_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "a[data-type='wdg_go_to_market_deeplink']")
    BUTTON_OPEN_AN_ACCOUNT_CONTENT_BLOCK = (By.CSS_SELECTOR, '[data-type="tiles_w_img_btn1_signup"]')
    BUTTON_TRY_DEMO_ACCOUNT_CONTENT_BLOCK = (By.CSS_SELECTOR, '[data-type="tiles_w_img_btn2_demo"]')
    BUTTON_CREATE_A_LIVE_ACCOUNT_UNLEVERAGED_TRADING_BLOCK = \
        (By.CSS_SELECTOR, 'div > p:nth-child(8) > a[data-type="plain_button"]')
    BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_UNLEVERAGED_TRADING_BLOCK = \
        (By.CSS_SELECTOR, 'div > p:nth-child(8) > [data-type="plain_button_demo"]')
    BUTTON_CREATE_A_LIVE_ACCOUNT_HOW_TO_GET_STARTED_WITH_TRADING_BLOCK = \
        (By.CSS_SELECTOR, 'div > p:nth-child(21) > a[data-type="plain_button"]')
    BUTTON_CREATE_A_RISK_FREE_DEMO_ACCOUNT_HOW_TO_GET_STARTED_WITH_TRADING_BLOCK = \
        (By.CSS_SELECTOR, 'div > p:nth-child(21) > a[data-type="plain_button_demo"]')

    # Elements of 'Why choose Capital.com?' block
    WHY_CHOOSE_BLOCK = (By.CSS_SELECTOR, ".js-bannerSection .js-showBanner")
    WHY_CHOOSE_BLOCK_IN_CONTENT = (By.CSS_SELECTOR, ".brick .cc-counter")
    WHY_CHOOSE_BLOCK_TRY_DEMO_BUTTON = (By.CSS_SELECTOR, '[data-type="tiles_w_img_btn1_demo"]')
    WHY_CHOOSE_BLOCK_SIGN_UP_BUTTON = (By.CSS_SELECTOR, '[data-type="tiles_w_img_btn2_signup"]')
    WHY_CHOOSE_BLOCK_TRY_NOW_BUTTON = (By.CSS_SELECTOR, '.js-bannerSection .js-showBanner .btn.js_signup')
    WHY_CHOOSE_BLOCK_IN_CONTENT_TRY_NOW_BUTTON = (
        By.CSS_SELECTOR, '.btn.cc-counter__btn')

    FOR_LEARNER_TRADERS_BLOCK_TRY_DEMO_BUTTON = (
        By.CSS_SELECTOR, '[data-type="learn_traders_block"] .l_btn_signup_demo')
    FOR_LEARNER_TRADERS_BLOCK_SIGN_UP_BUTTON = (
        By.CSS_SELECTOR, '[data-type="learn_traders_block_btn1_signup"]')

    # Elements of 'Explore our platform' block
    EXPLORE_OUR_PLATFORM_BLOCK = (By.CSS_SELECTOR, '.wrap section.cc-boxLg > .flex-wrap')
    EASY_TO_USE_LINK_EXPLORE_OUR_PLATFORM_BLOCK = (
        By.CSS_SELECTOR,
        '.hideXs [href="https://capital.com/trading/platform/"]')
    TRY_NOW_BUTTON_EXPLORE_OUR_PLATFORM_BLOCK = (
        By.CSS_SELECTOR,
        'div.js-analyticsVisible[data-type="btn_nearby_video"] a.hideXs:nth-child(2)')

    # Elements of "Trader's Dashboard" widget
    TRADERS_DASHBOARD_WIDGET = (By.CSS_SELECTOR, 'div[data-type="traders_dashboard"]')
    TRADE_BUTTON_TRADERS_DASHBOARD_WIDGET = (By.XPATH, '(//div[@class="tradersDashboard__main"]//button)')
    NAME_OF_TRADING_INSTRUMENT = (By.CSS_SELECTOR, ".tradersDashboard__item .tradersDashboard__name b")

    # Elements of 'Why Capital.com?' > 'Client funds' menu
    LEARN_MORE_ABOUT_US_LINK_CONTENTS_BLOCK = ('xpath', "//span[text()='Learn more about us ']")
    CONTENTS_BLOCK = ('css selector', '#tableOfContent')
    TITLE_LEARN_MORE_ABOUT_US = ('xpath', "//h2[text()='Learn more about us ']")


class QRCodeLocators:
    QR_CODE_INVESTMATE = (By.CSS_SELECTOR, "#qr_cfd_new > img")
    QR_CODE_EASY_LEARNING = (By.CSS_SELECTOR, "#qr_cfd_new2 > img")
    QR_CODE_CAPITAL = (By.CSS_SELECTOR, "#qr_cfd > img")

    QR_CODE_INVESTMATE_LINK = (By.CSS_SELECTOR, "#qr_cfd_new")
    QR_CODE_EASY_LEARNING_LINK = (By.CSS_SELECTOR, "#qr_cfd_new2")
    QR_CODE_CAPITAL_LINK = (By.CSS_SELECTOR, "#qr_cfd")


class CounterBanner:
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".cc-counter__btn")


class OurAppsBlock:
    OUR_APPS_BLOCK = (By.CSS_SELECTOR, ".promoApps > .promoApps__content")
    DOWNLOAD_ON_THE_APP_STORE_BUTTON_OUR_APPS_BLOCK = (By.CSS_SELECTOR, ".storeBtns  > [data-type='our_app_Ios']")
    GET_IT_ON_GOOGLE_PLAY_BUTTON_OUR_APPS_BLOCK = (By.CSS_SELECTOR, ".storeBtns  > [data-type='our_app_Googl']")


class TableTradingInstrumentsLocators:
    TABLE_TRADING_INSTRUMENTS = (By.CSS_SELECTOR, "div.row")  # таблица инструментов
    BUTTON_SELL_TRADING_INSTRUMENT = (By.CSS_SELECTOR, '.table--fixedInstr [data-side="sell"]')
    BUTTON_BUY_TRADING_INSTRUMENT = (By.CSS_SELECTOR, '.table--fixedInstr [data-side="buy"]')  # список инструментов
    ITEM_TRADING_INSTRUMENT = (By.CSS_SELECTOR, "p.stringEllipsed > b")  # названия инструментов
    ITEM_TRADING_INSTRUMENT_LINK = (By.CSS_SELECTOR, "p.table__info.stringEllipsed > a")  # ссылка
    ITEMS_TRADING_INSTRUMENT_LINK = (By.CSS_SELECTOR, '//p[@class="table__info stringEllipsed"]')  # ссылка XPATH
    LINE_TRADING_INSTRUMENT = (By.CSS_SELECTOR, "tr.trlink.js-trlink")
    MARKET_ICON = (By.CSS_SELECTOR, "i.marketIcon")


class FieldDropdownMarketsLocator:
    FIELD_DROPDOWN_MARKETS = (By.CSS_SELECTOR, '.fieldDropdown.js-fieldDropdown-markets')
    FIELD_DROPDOWN_LIST = (By.CSS_SELECTOR, '.js-fieldDropdown-markets.opened')
    FIELD_DROPDOWN_MOST_TRADED = (By.CSS_SELECTOR, 'input[placeholder="Most traded"]')
    FIELD_DROPDOWN_TOP_RISERS = (By.CSS_SELECTOR, 'input[placeholder="Top risers"]')
    FIELD_DROPDOWN_TOP_FALLERS = (By.CSS_SELECTOR, 'input[placeholder="Top fallers"]')
    FIELD_DROPDOWN_MOST_VOLATILE = (By.CSS_SELECTOR, 'input[placeholder="Most volatile"]')


class ItemSortDropdownLocators:
    ALL_ITEM_DROPDOWN_SORT = (By.CSS_SELECTOR, 'ul.fieldDropdown__list')
    ITEM_DROPDOWN_SORT_MOST_TRADED = (By.CSS_SELECTOR, 'li[data-sort="most"]')
    ITEM_DROPDOWN_SORT_TOP_RISERS = (By.CSS_SELECTOR, 'li[data-sort="risers"]')
    ITEM_DROPDOWN_SORT_TOP_FALLERS = (By.CSS_SELECTOR, 'li[data-sort="fallers"]')
    ITEM_DROPDOWN_SORT_MOST_VOLATILE = (By.CSS_SELECTOR, 'li[data-sort="volatile"]')


class TradeCFDLocators:
    ADD_TO_FAVORITE_BUTTON = (By.CSS_SELECTOR, "[data-type='add_fav']")
    LONG_POSITION = (By.CSS_SELECTOR, "tr:nth-child(2) > td:nth-child(1) > div")
    SHORT_POSITION = (By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(1) > div")
    GO_TO_PLATFORM_BUTTON = (By.CSS_SELECTOR, "[href='trading/platform']")
    BUY_BUTTON = (By.CSS_SELECTOR, "[data-type='market_buy']")
    SELL_BUTTON = (By.CSS_SELECTOR, "div.sharesName__price > a[data-type='market_sell']")
    ITEM_NAME = (By.CSS_SELECTOR, ".cc-breadcrumbs span")


class TradingInstrumentsBlockLocators:
    BUTTON_START_TRADING_NOW = (By.CSS_SELECTOR, ".banner .button-main.js_signup")


class PageTradingInstrumentMarketsLocators:
    BUTTON_VIEW_DETAILED_CHART = \
        (By.CSS_SELECTOR, "a[data-type='detailed_chart']")
    TOOLINFO_SHORT_POSITION_OVERNIGHT_FEE = \
        (By.CSS_SELECTOR, "tbody > tr:nth-child(3) > td:nth-child(1) > div.toolInfo")
    TOOLINFO_LONG_POSITION_OVERNIGHT_FEE = \
        (By.CSS_SELECTOR, "tbody > tr:nth-child(2) > td:nth-child(1) > div.toolInfo")
    TOOLTIP_SHORT_POSITION_FEE = \
        (By.CSS_SELECTOR, "tbody > tr:nth-child(3) > td:nth-child(1) > div >div.cc-tooltip")
    TOOLTIP_LONG_POSITION_FEE = \
        (By.CSS_SELECTOR, "tbody > tr:nth-child(2) > td:nth-child(1) > div >div.cc-tooltip")
    BUTTON_GO_TO_PLATFORM = \
        (By.CSS_SELECTOR, "tbody > tr:nth-child(3) > td:nth-child(1) > div > div > a[href='trading/platform']")
    BUTTON_GO_TO_PLATFORM_LG = \
        (By.CSS_SELECTOR, "tbody > tr:nth-child(2) > td:nth-child(1) > div > div > a[href='trading/platform']")
# new locators
    LONG_POSITION_OVERNIGHT_FEE = \
        (By.CSS_SELECTOR, ".brick > table.table > tbody > tr:nth-child(2)")
    LONG_POSITION_BUTTON_GO_TO_PLATFORM = \
        (By.CSS_SELECTOR, "tbody > tr:nth-child(2) > td:nth-child(1) > div > div > a[href='trading/platform']")
    SHORT_POSITION_OVERNIGHT_FEE = \
        (By.CSS_SELECTOR, ".brick > table.table > tbody > tr:nth-child(3)")
    SHORT_POSITION_BUTTON_GO_TO_PLATFORM = \
        (By.CSS_SELECTOR, "tbody > tr:nth-child(3) > td:nth-child(1) > div > div > a[href='trading/platform']")
    BUTTON_NOTIFICATION = \
        (By.CSS_SELECTOR, "a[data-type='market_alerts']")
    TAG_TRADE_INSTRUMENT = (By.CSS_SELECTOR, "div.cc-box h1")


class TradingPlatformWatchlistTabs:
    FAVOURITES_TAB = (By.CSS_SELECTOR, ".selected .iconex-favourites-outline")
    ITEM_TITLE = (By.CLASS_NAME, "market-title")


class MarketSortAllMarketsLocators:
    TABLE_TRADING_INSTRUMENTS = (By.CLASS_NAME, "tabs__panes")
    ALL_TABS = (By.CLASS_NAME, "tabs__nav")
    ALL_MARKETS_TAB = (By.CSS_SELECTOR, "[data-cat='ALL']")
    COMMODITIES_MARKET_TAB = (By.CSS_SELECTOR, "[data-cat='COM']")
    INDICES_MARKET_TAB = (By.CSS_SELECTOR, "[data-cat='IND']")
    CRYPTO_MARKET_TAB = (By.CSS_SELECTOR, "[data-cat='CRYPTO']")
    SHARES_MARKET_TAB = (By.CSS_SELECTOR, "[data-cat='SHARE']")
    FOREX_MARKET_TAB = (By.CSS_SELECTOR, "[data-cat='CURRENCY']")
    # BUTTON_SELL_TRADING_INSTRUMENT_ALL_MARKETS = (By.CSS_SELECTOR, '[data-type="wdg_markets_sell_btn"]')
    # BUTTON_BUY_TRADING_INSTRUMENT_ALL_MARKETS = (By.CSS_SELECTOR, 'a[data-type="wdg_markets_buy_btn"]')
    # BUTTON_BUY_TRADING_INSTRUMENT_ALL_MARKETS = (By.CSS_SELECTOR, '.table--fixedInstr [data-side="buy"]')
    # BUTTON_SELL_TRADING_INSTRUMENT_ALL_MARKETS = (By.CSS_SELECTOR, '.table--fixedInstr [data-side="sell"]')
    # BUTTON_BUY_TRADING_INSTRUMENT_ALL_MARKETS = (By.CSS_SELECTOR, 'td.buy.text-right')
    # BUTTON_SELL_TRADING_INSTRUMENT_ALL_MARKETS = (By.CSS_SELECTOR, 'td.sell.text-right')
    BUTTON_SELL_TRADING_INSTRUMENT_ALL_MARKETS = (By.CSS_SELECTOR, "tbody > tr > td.sell")


class GlobalEnvironmentalLocators:
    BUTTON_START_TRADING = (By.CSS_SELECTOR, "a[data-type='esg_start_trading']")
    BUTTON_TRY_DEMO = (By.CSS_SELECTOR, "a[data-demomode='true']")


class HowToStartTradingSignupLocators:
    SIGNUP_FRAME = (By.CSS_SELECTOR, 'div.banner__item #lp_form_126_6')
    SIGNUP_INPUT_EMAIL = (By.CSS_SELECTOR, '#lp_form_126_6-email > input')
    SIGNUP_INPUT_PASSWORD = (By.CSS_SELECTOR, "#lp_form_126_6-pass > input")
    BUTTON_SIGN_UP = (By.CSS_SELECTOR, "div.bannerForm button.btn.btn")
    SIGNUP_PRIVACY_POLICY = (By.CSS_SELECTOR, "div.bannerForm div.reg-desc a[target='_blank']")


class MyAccountButtonLocators(BasePage):
    BUTTON_MY_ACCOUNT = (By.CSS_SELECTOR, ".accountBtns_userBtn__kCJ5A.accountBtns_btnEmpty__TCWRE")
    HEADER_LOGIN_BTN2 = (By.CSS_SELECTOR, '[data-type="btn_header_login"]')


class WhyChooseLocators:
    BLOCK_WHY_CHOOSE = (By.CSS_SELECTOR, '.js-showBanner')
    BUTTON_TRY_NOW_BLOCK_WHY_CHOOSE = (By.CSS_SELECTOR, '.cc-counter__btn')


class ProductsAndServicesOurMobileApps:
    PRODUCTS_AND_SERVICES_BUTTON = (By.CSS_SELECTOR, '[data-type="nav_id2"]')
    OUR_MOBILE_APPS_BUTTON = (By.CSS_SELECTOR, '[data-type="nav_id465"]')
    GOOGLE_PLAY_BUTTON = (By.CSS_SELECTOR, 'a.onelink-mobile-url.badge-googleplay')
    GOOGLE_PLAY_LOGO = (By.CSS_SELECTOR, 'span.google_logo')


class MobileTradingAppBlockLocators:
    MOBILE_TRADING_APP_BLOCK_PLATFORM_OVERVIEW_BUTTON = (
        By.CSS_SELECTOR, 'div.platform-web-description__text p:nth-child(2) > a')
    MOBILE_TRADING_APP_BLOCK = (By.CSS_SELECTOR, 'div.platform-web-description__text')


class TradingCoursesMenuItem:
    EDUCATION_SECTION = (By.CSS_SELECTOR, '[data-type="nav_id96"]')
    TRADING_COURSES = (By.CSS_SELECTOR, '[data-type="nav_id11"]')
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, '[data-type="courses_hub"]')


class WebTradingPlatformPageLocators:
    BREADCRUMBS_DESKTOP_TRADING = (By.CSS_SELECTOR, '[div.cc-breadcrumbs-wrap > nav > p > span]')
    PAGE_DESKTOP_TRADING_TITLE = (By.XPATH, '//title[text()="The Capital.com web trading platform | Capital.com"]')
