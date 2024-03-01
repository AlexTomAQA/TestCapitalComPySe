"""
-*- coding: utf-8 -*-
@Time    : 2023/04/13 18:25
@Author  : Alexander Tomelo
"""
from selenium.webdriver.common.by import By


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


class BlockOurCoursesLocators:
    BUTTON_CREATE_ACCOUNT = (By.CSS_SELECTOR, "div [href='https://capital.com/trading/signup']")


class CoursesPage:
    COURSES_PAGES_LIST = (By.CSS_SELECTOR, "li.courseCard__row > a")


class SubPages:
    SUB_PAGES_LIST = (By.CSS_SELECTOR, "div.side-nav__wrap > div.side-nav > a")


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

    # Tabs
    TABLE_CFDS = (By.CSS_SELECTOR, '.section.section__tabs')
    TAB_TRADING_ITEM_MOST_TRADED = (By.CSS_SELECTOR, '[data-id="mosttraded"]')
    TAB_TRADING_ITEM_TOP_RISERS = (By.CSS_SELECTOR, '[data-id="risers"]')
    TAB_TRADING_ITEM_TOP_FALLERS = (By.CSS_SELECTOR, '[data-id="fallers"]')
    TAB_TRADING_ITEM_MOST_VOLATILE = (By.CSS_SELECTOR, '[data-id="volatile"]')
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
    BUTTON_TRY_DEMO_BLOCK_WHY_CHOOSE = (By.CSS_SELECTOR, '[data-type="tiles_w_img_btn1_demo"]')
    BUTTON_SIGN_UP_BLOCK_WHY_CHOOSE = (By.CSS_SELECTOR, '[data-type="tiles_w_img_btn2_signup"]')


class QRCodeLocators:
    QR_CODE_INVESTMATE = (By.CSS_SELECTOR, "#qr_cfd_new > img")
    QR_CODE_EASY_LEARNING = (By.CSS_SELECTOR, "#qr_cfd_new2 > img")
    QR_CODE_CAPITAL = (By.CSS_SELECTOR, "#qr_cfd > img")

    QR_CODE_INVESTMATE_LINK = (By.CSS_SELECTOR, "#qr_cfd_new")
    QR_CODE_EASY_LEARNING_LINK = (By.CSS_SELECTOR, "#qr_cfd_new2")
    QR_CODE_CAPITAL_LINK = (By.CSS_SELECTOR, "#qr_cfd")


class CounterBanner:
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".cc-counter__btn")


class FieldDropdownMarketsLocator:
    FIELD_DROPDOWN_MARKETS = (By.CSS_SELECTOR, 'div.js-fieldDropdown-markets')


class ItemSortDropdownLocators:
    ITEM_DROPDOWN_SORT_MOST_TRADED = (By.CSS_SELECTOR, 'li[data-sort="most"]')
    ITEM_DROPDOWN_SORT_TOP_RISERS = (By.CSS_SELECTOR, 'li[data-sort="risers"]')
    ITEM_DROPDOWN_SORT_TOP_FALLERS = (By.CSS_SELECTOR, 'li[data-sort="fallers"]')
    ITEM_DROPDOWN_SORT_MOST_VOLATILE = (By.CSS_SELECTOR, 'li[data-sort="volatile"]')


class TradeCFDLocators:
    ADD_TO_FAVORITE_BUTTON = (By.CSS_SELECTOR, "[data-type='add_fav']")
    LONG_POSITION = (By.CSS_SELECTOR, "tr:nth-child(2) > td:nth-child(1) > div")
    SHORT_POSITION = (By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(1) > div")
    GO_TO_PLATFORM_BUTTON = (By.CSS_SELECTOR, "[href='trading/platform']")
