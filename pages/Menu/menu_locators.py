from selenium.webdriver.common.by import By


class MenuLanguageAndCountry:
    MENU_LANGUAGE_AND_COUNTRY = (By.CSS_SELECTOR, "header.cc-header .js-licLangSw")
    # MENU_LANGUAGE_AND_COUNTRY = (By.CSS_SELECTOR, "header.cc-header .licLangSw__btn")
    DROP_DOWN_LIST_COUNTRY = (By.CSS_SELECTOR, "header .fieldDropdown")
    COUNTRIES_SEARCH_INPUT = (By.CSS_SELECTOR, "header .js-countriesSearchInput")
    COUNTRIES_LIST = (By.CSS_SELECTOR, "header .js-countriesList a")


class MenuWhyCapitalCom:
    SUB_MENU_EN_GB_WHY_CAPITAL_COM = (By.CSS_SELECTOR, '[data-type="nav_id687"]')
    SUB_MENU_EN_ESSENTIALS_OF_TRADING = (By.CSS_SELECTOR, '[data-type="nav_id706"]')


class MenuUS11Education:
    SUB_MENU_AR_LEARN_TO_TRADE = \
        (By.CSS_SELECTOR, ".cc-header .cc-nav__item > a[href='https://capital.com/ar/learn-to-trade']")
    SUB_MENU_CN_LEARN_TO_TRADE = \
        (By.CSS_SELECTOR, ".cc-header .cc-nav__item > a[href='https://capital.com/cn/learn-to-trade']")
    SUB_MENU_DE_LEARN_TO_TRADE = \
        (By.CSS_SELECTOR, ".cc-header .cc-nav__item > a[href='https://capital.com/de/learn-to-trade']")
    SUB_MENU_EL_LEARN_TO_TRADE = \
        (By.CSS_SELECTOR, ".cc-header .cc-nav__item > a[href='https://capital.com/el/learn-to-trade']")
    SUB_MENU_EN_LEARN_TO_TRADE = \
        (By.CSS_SELECTOR, ".cc-header .cc-nav__item > a[href='https://capital.com/learn-to-trade']")
    SUB_MENU_ES_LEARN_TO_TRADE = \
        (By.CSS_SELECTOR, ".cc-header .cc-nav__item > a[href='https://capital.com/es/learn-to-trade']")
    SUB_MENU_ET_LEARN_TO_TRADE = \
        (By.CSS_SELECTOR, ".cc-header .cc-nav__item > a[href='https://capital.com/et/learn-to-trade']")
    SUB_MENU_FR_LEARN_TO_TRADE = \
        (By.CSS_SELECTOR, ".cc-header .cc-nav__item > a[href='https://capital.com/fr/learn-to-trade']")
    SUB_MENU_HU_LEARN_TO_TRADE = \
        (By.CSS_SELECTOR, ".cc-header .cc-nav__item > a[href='https://capital.com/hu/learn-to-trade']")
    SUB_MENU_IT_LEARN_TO_TRADE = \
        (By.CSS_SELECTOR, ".cc-header .cc-nav__item > a[href='https://capital.com/it/learn-to-trade']")
    SUB_MENU_NL_LEARN_TO_TRADE = \
        (By.CSS_SELECTOR, ".cc-header .cc-nav__item > a[href='https://capital.com/nl/learn-to-trade']")
    SUB_MENU_PL_LEARN_TO_TRADE = \
        (By.CSS_SELECTOR, ".cc-header .cc-nav__item > a[href='https://capital.com/pl/learn-to-trade']")
    SUB_MENU_RO_LEARN_TO_TRADE = \
        (By.CSS_SELECTOR, ".cc-header .cc-nav__item > a[href='https://capital.com/ro/learn-to-trade']")
    SUB_MENU_RU_LEARN_TO_TRADE = \
        (By.CSS_SELECTOR, ".cc-header .cc-nav__item > a[href='https://capital.com/ru/learn-to-trade']")
    SUB_MENU_ZH_LEARN_TO_TRADE = \
        (By.CSS_SELECTOR, ".cc-header .cc-nav__item > a[href='https://capital.com/zh/learn-to-trade']")

    # SUB_MENU_EN_GB_LEARN_TO_TRADE = (By.CSS_SELECTOR, "#header a[href='/en-gb/learn']")
    SUB_MENU_EN_GB_LEARN_TO_TRADE = (By.CSS_SELECTOR, '[data-type="nav_id698"]')


class MenuUS11Glossary:
    SUB_MENU_AR_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/ar/financial-dictionary']")
    SUB_MENU_ID_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/id/financial-dictionary']")
    SUB_MENU_BG_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/bg/finansov-rechnik']")
    SUB_MENU_CN_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/cn/financial-dictionary']")
    SUB_MENU_CS_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/cs/financni-slovnik']")
    SUB_MENU_DA_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/da/finansiel-ordbog']")
    SUB_MENU_DE_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/de/finanzglossar']")
    SUB_MENU_EL_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/el/xromatooikonomiko-leksiko']")
    SUB_MENU_EN_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/financial-dictionary']")
    SUB_MENU_ES_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/es/diccionario-financiero']")
    SUB_MENU_ET_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/et/finantssonastik']")
    SUB_MENU_FI_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/fi/rahoitusalan-sanasto']")
    SUB_MENU_FR_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/fr/dictionnaire-financier']")
    SUB_MENU_HR_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/hr/financijski-rjecnik']")
    SUB_MENU_HU_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/hu/penzugyi-szotar']")
    SUB_MENU_IT_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/it/dizionario-finanziario']")
    SUB_MENU_LT_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/lt/finansinis-zodynas']")
    SUB_MENU_LV_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/lv/finansu-vardnica']")
    SUB_MENU_NL_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/nl/financieel-woordenboek']")
    SUB_MENU_PL_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/pl/slownik-finansowy']")
    SUB_MENU_PT_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/pt/dicionario-financeiro']")
    SUB_MENU_RO_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/ro/dictionar-financiar']")
    SUB_MENU_RU_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/ru/finansovyy-slovar']")
    SUB_MENU_SK_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/sk/financny-slovnik']")
    SUB_MENU_SL_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/sl/financni-slovar']")
    SUB_MENU_SV_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/sv/finansiell-ordbok']")
    SUB_MENU_TH_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/th/financial-dictionary']")
    SUB_MENU_VI_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/vi/financial-dictionary']")
    SUB_MENU_ZH_GLOSSARY = (By.CSS_SELECTOR,
                            "div.cc-nav__item a[href='https://capital.com/zh/financial-dictionary']")


class MenuUS11ForexTrading:
    SUB_MENU_AR_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/ar/trade-forex']")
    SUB_MENU_BG_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/bg/trade-forex']")
    SUB_MENU_CN_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/cn/trade-forex']")
    SUB_MENU_CS_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/cs/trade-forex']")
    SUB_MENU_DA_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/da/trade-forex']")
    SUB_MENU_DE_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/de/waehrungshandel")
    SUB_MENU_EL_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/el/trade-forex']")
    SUB_MENU_EN_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/trade-forex']")
    SUB_MENU_ES_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/es/trade-forex']")
    SUB_MENU_ET_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/et/trade-forex']")
    SUB_MENU_FI_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/fi/trade-forex']")
    SUB_MENU_FR_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/fr/trade-forex']")
    SUB_MENU_HR_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/hr/trade-forex']")
    SUB_MENU_HU_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/hu/trade-forex']")
    SUB_MENU_ID_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/id/trade-forex']")
    SUB_MENU_IT_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/it/trading-su-forex']")
    SUB_MENU_LT_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/lt/trade-forex']")
    SUB_MENU_LV_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/lv/trade-forex']")
    SUB_MENU_NL_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/nl/trade-forex']")
    SUB_MENU_PL_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/pl/trade-forex']")
    SUB_MENU_PT_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/pt/trade-forex']")
    SUB_MENU_RO_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/ro/trade-forex']")
    SUB_MENU_RU_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/ru/torgovlya-forex-cfd']")
    SUB_MENU_SK_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/sk/trade-forex']")
    SUB_MENU_SL_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/sl/trade-forex']")
    SUB_MENU_SV_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/sv/trade-forex']")
    SUB_MENU_TH_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/th/trade-forex']")
    SUB_MENU_VI_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/vi/trade-forex']")
    SUB_MENU_ZH_FOREX_TRADING = (By.CSS_SELECTOR,
                                 ".cc-header .cc-nav__wrap a[href='https://capital.com/zh/trade-currency']")
    # SUB_MENU_ZH_FOREX_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/zh/trade-currency']")


class Menu1101:
    SUB_MENU_EN_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .cc-nav__wrap a[href='https://capital.com/basics-of-trading']")
    SUB_MENU_AR_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/ar/basics-of-trading']")
    SUB_MENU_BG_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/bg/basics-of-trading'] ")
    SUB_MENU_CS_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .cc-nav a[href='https://capital.com/cs/basics-of-trading']")

    SUB_MENU_DA_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/da/basics-of-trading']")
    SUB_MENU_DE_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid a[href='https://capital.com/de/basics-of-trading']")
    SUB_MENU_ET_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/et/basics-of-trading']")
    SUB_MENU_EL_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/el/basics-of-trading']")
    SUB_MENU_ES_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/es/basics-of-trading']")
    SUB_MENU_FR_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/fr/basics-of-trading']")
    SUB_MENU_HR_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/hr/basics-of-trading']")
    SUB_MENU_IT_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/it/basi-di-trading']")
    SUB_MENU_LV_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/lv/basics-of-trading']")
    SUB_MENU_LT_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/lt/basics-of-trading']")
    SUB_MENU_HU_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/hu/basics-of-trading']")
    SUB_MENU_NL_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/nl/basics-of-trading']")
    SUB_MENU_PL_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/pl/basics-of-trading']")
    SUB_MENU_PT_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/pt/basics-of-trading']")
    SUB_MENU_RO_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/ro/basics-of-trading']")
    SUB_MENU_RU_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/ru/basics-of-trading']")
    SUB_MENU_SK_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/sk/basics-of-trading']")
    SUB_MENU_SL_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/sl/basics-of-trading']")
    SUB_MENU_FI_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/fi/basics-of-trading']")
    SUB_MENU_SV_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/sv/basics-of-trading']")
    SUB_MENU_VI_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/vi/basics-of-trading']")
    SUB_MENU_ZH_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/zh/basics-of-trading']")
    SUB_MENU_CN_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,
                                          "div .grid > a[href='https://capital.com/cn/basics-of-trading']")
    # SUB_MENU_ID_ITEM_BASICS_OF_TRADING = (By.CSS_SELECTOR,"")--нет раздела


class MenuUS11LearningHub:
    SUB_MENU_EN_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/./learn-to-trade']")
    SUB_MENU_AR_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/ar/./learn-to-trade']")
    SUB_MENU_BG_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/bg/./learn-to-trade']")
    SUB_MENU_CS_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/cs/./learn-to-trade']")
    SUB_MENU_DA_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/da/./learn-to-trade']")
    SUB_MENU_DE_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/de/./learn-to-trade']")
    SUB_MENU_ET_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/et/./learn-to-trade']")
    SUB_MENU_EL_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/el/./learn-to-trade']")
    SUB_MENU_ES_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/es/./learn-to-trade']")
    SUB_MENU_FR_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/fr/./learn-to-trade']")
    SUB_MENU_HR_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/hr/./learn-to-trade']")
    SUB_MENU_IT_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/it/./learn-to-trade']")
    SUB_MENU_LV_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/lv/./learn-to-trade']")
    SUB_MENU_LT_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/lt/./learn-to-trade']")
    SUB_MENU_HU_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/hu/./learn-to-trade']")
    SUB_MENU_NL_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/nl/./learn-to-trade']")
    SUB_MENU_PL_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/pl/./learn-to-trade']")
    SUB_MENU_PT_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/pt/./learn-to-trade']")
    SUB_MENU_RO_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/ro/./learn-to-trade']")
    SUB_MENU_RU_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/ru/./learn-to-trade']")
    SUB_MENU_SK_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/sk/./learn-to-trade']")
    SUB_MENU_SL_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/sl/./learn-to-trade']")
    SUB_MENU_FI_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/fi/./learn-to-trade']")
    SUB_MENU_SV_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/sv/./learn-to-trade']")
    SUB_MENU_VI_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/vi/./learn-to-trade']")
    SUB_MENU_ZH_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/zh/./learn-to-trade']")
    SUB_MENU_TH_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/th/./learn-to-trade']")
    SUB_MENU_CN_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/cn/./learn-to-trade']")
    SUB_MENU_ID_ITEM_LEARNING_HUB = (By.CSS_SELECTOR,
                                     "div .grid > a[href='https://capital.com/id/./learn-to-trade']")


class MenuUS11TradingCourses:
    SUB_MENU_EN_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/online-finance-courses']")
    SUB_MENU_AR_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/ar/online-finance-courses']")
    SUB_MENU_DE_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/de/online-finance-courses']")
    SUB_MENU_EL_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/el/online-finance-courses']")
    SUB_MENU_ES_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/es/online-finance-courses']")
    SUB_MENU_FR_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/fr/online-finance-courses']")
    SUB_MENU_IT_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/it/corsi-online']")
    SUB_MENU_HU_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/hu/online-finance-courses']")
    SUB_MENU_NL_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/nl/online-finance-courses']")
    SUB_MENU_PL_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/pl/online-finance-courses']")
    SUB_MENU_RO_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/ro/online-finance-courses']")
    SUB_MENU_RU_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/ru/online-finance-courses']")
    SUB_MENU_ZH_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/zh/online-finance-courses']")
    SUB_MENU_CN_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/cn/online-finance-courses']")

    SUB_MENU_BG_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/bg/online-finance-courses']")
    SUB_MENU_CS_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/cs/online-finance-courses']")
    SUB_MENU_DA_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/da/online-finance-courses']")
    SUB_MENU_ET_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/et/online-finance-courses']")
    SUB_MENU_HR_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/hr/online-finance-courses']")
    SUB_MENU_LV_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/lv/online-finance-courses']")
    SUB_MENU_LT_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/lt/online-finance-courses']")
    SUB_MENU_PT_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/pt/online-finance-courses']")
    SUB_MENU_SK_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/sk/online-finance-courses']")
    SUB_MENU_SL_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/sl/online-finance-courses']")
    SUB_MENU_FI_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/fi/online-finance-courses']")
    SUB_MENU_SV_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/sv/online-finance-courses']")
    SUB_MENU_VI_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/vi/online-finance-courses']")
    SUB_MENU_ID_ITEM_TRADING_COURSES = (By.CSS_SELECTOR,
                                        "div .grid > a[href='https://capital.com/id/online-finance-courses']")


class MenuUS11CommoditiesTrading:
    SUB_MENU_AR_COMMODITIES_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/ar/trade-commodities']")

    # SUB_MENU_BG_COMMODITIES_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/bg/trade-commodities']")

    # SUB_MENU_CS_COMMODITIES_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/cs/trade-commodities']")

    SUB_MENU_CN_COMMODITIES_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/cn/trade-commodities']")

    # SUB_MENU_DA_COMMODITIES_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/da/trade-commodities']") # Нет такой страницы

    SUB_MENU_DE_COMMODITIES_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/de/rohstoffhandel']")

    # SUB_MENU_EL_COMMODITIES_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/el/trade-commodities']") # Нет такой страницы

    SUB_MENU_EN_COMMODITIES_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/trade-commodities']")

    SUB_MENU_ES_COMMODITIES_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/es/trade-commodities']")

    # SUB_MENU_ET_COMMODITIES_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/et/trade-commodities']")

    # SUB_MENU_FI_COMMODITIES_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/fi/trade-commodities']")

    SUB_MENU_FR_COMMODITIES_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/fr/trade-commodities']")

    # SUB_MENU_HR_COMMODITIES_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/hr/trade-commodities']")

    # SUB_MENU_HU_COMMODITIES_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/hu/trade-commodities']")

    SUB_MENU_IT_COMMODITIES_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/it/trading-materie-prime']")

    # SUB_MENU_ID_COMMODITIES_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/id/trade-commodities']")

    # SUB_MENU_LT_COMMODITIES_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/lt/trade-commodities']")

    # SUB_MENU_LV_COMMODITIES_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/lv/trade-commodities']")

    SUB_MENU_NL_COMMODITIES_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/nl/trade-commodities']")

    SUB_MENU_PL_COMMODITIES_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/pl/trade-commodities']")

    # SUB_MENU_PT_COMMODITIES_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/pt/trade-commodities']")

    SUB_MENU_RO_COMMODITIES_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/ro/trade-commodities']")

    SUB_MENU_RU_COMMODITIES_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/ru/torgovlya-syrievymi-tovarami-cfd']")

    # SUB_MENU_SK_COMMODITIES_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/sk/trade-commodities']")

    # SUB_MENU_SL_COMMODITIES_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/sl/trade-commodities']")

    # SUB_MENU_SV_COMMODITIES_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/sv/trade-commodities']")

    SUB_MENU_ZH_COMMODITIES_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/zh/trade-commodities']")

    SUB_MENU_VI_COMMODITIES_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/vi/trade-commodities']")

    # SUB_MENU_TH_COMMODITIES_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/th/trade-commodities']")


class MenuUS11MarketGuides:
    SUB_MENU_EN_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/trading-guides']")
    SUB_MENU_AR_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/ar/trading-guides']")
    SUB_MENU_BG_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/bg/trading-guides']")
    SUB_MENU_CS_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/cs/trading-guides']")
    SUB_MENU_DA_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/da/trading-guides']")
    SUB_MENU_DE_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/de/trading-guides']")
    SUB_MENU_ET_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/et/trading-guides']")
    SUB_MENU_EL_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/el/trading-guides']")
    SUB_MENU_ES_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/es/trading-guides']")
    SUB_MENU_FR_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/fr/trading-guides']")
    SUB_MENU_HR_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/hr/trading-guides']")
    SUB_MENU_IT_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/it/guide-di-trading']")
    SUB_MENU_LV_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/lv/trading-guides']")
    SUB_MENU_LT_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/lt/trading-guides']")
    SUB_MENU_HU_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/hu/trading-guides']")
    SUB_MENU_NL_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/nl/trading-guides']")
    SUB_MENU_PL_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/pl/trading-guides']")
    SUB_MENU_PT_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/pt/trading-guides']")
    SUB_MENU_RO_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/ro/trading-guides']")
    SUB_MENU_RU_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/ru/trading-guides']")
    SUB_MENU_SK_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/sk/trading-guides']")
    SUB_MENU_SL_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/sl/trading-guides']")
    SUB_MENU_FI_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/fi/trading-guides']")
    SUB_MENU_SV_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/sv/trading-guides']")
    SUB_MENU_VI_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/vi/trading-guides']")
    SUB_MENU_ZH_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/zh/trading-guides']")
    SUB_MENU_CN_ITEM_MARKET_GUIDES = (By.CSS_SELECTOR,
                                      "div .grid > a[href='https://capital.com/cn/trading-guides']")


class MenuUS11CryptocurrencyTrading:
    # SUB_MENU_AR_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/ar/trade-cryptocurrency']")

    # SUB_MENU_BG_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/bg/trade-cryptocurrency']")

    # SUB_MENU_CS_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/cs/trade-cryptocurrency']")

    SUB_MENU_CN_CRYPTOCURRENCY_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/cn/trade-cryptocurrency']")

    # SUB_MENU_DA_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/da/trade-cryptocurrency']")

    SUB_MENU_DE_CRYPTOCURRENCY_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/de/kryptowaehrung-handel']")

    # SUB_MENU_EL_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/el/trade-cryptocurrency']")

    SUB_MENU_EN_CRYPTOCURRENCY_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/trade-cryptocurrency']")

    SUB_MENU_ES_CRYPTOCURRENCY_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/es/trade-cryptocurrency']")

    # SUB_MENU_ET_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/et/trade-cryptocurrency']")

    # SUB_MENU_FI_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/fi/trade-cryptocurrency']")

    SUB_MENU_FR_CRYPTOCURRENCY_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/fr/trade-cryptocurrency']")

    # SUB_MENU_HR_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/hr/trade-cryptocurrency']")

    # SUB_MENU_HU_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/hu/trade-cryptocurrency']")

    SUB_MENU_IT_CRYPTOCURRENCY_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/it/trading-crypto']")

    # SUB_MENU_ID_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/id/panduan-perdagangan-mata-uang-kripto']")

    # SUB_MENU_LT_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/lt/trade-cryptocurrency']")

    # SUB_MENU_LV_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/lv/trade-cryptocurrency']") # Нет такой страницы

    # SUB_MENU_NL_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/nl/trade-cryptocurrency']") # Нет такой страницы

    SUB_MENU_PL_CRYPTOCURRENCY_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/pl/trade-cryptocurrency']")

    # SUB_MENU_PT_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/pt/trade-cryptocurrency']") # Нет такой страницы

    SUB_MENU_RO_CRYPTOCURRENCY_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/ro/cryptocurrency-trading']")

    SUB_MENU_RU_CRYPTOCURRENCY_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/ru/torgovlya-crypto-cfd']")

    # SUB_MENU_SK_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/sk/trade-cryptocurrency']") # Нет такой страницы

    # SUB_MENU_SL_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/sl/trade-cryptocurrency']") # Нет такой страницы

    # SUB_MENU_SV_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/sv/trade-cryptocurrency']") # Нет такой страницы

    # SUB_MENU_TH_CRYPTOCURRENCY_TRADING = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/th/trade-cryptocurrency']") # Нет такой страницы

    SUB_MENU_VI_CRYPTOCURRENCY_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/vi/trade-cryptocurrency']")

    SUB_MENU_ZH_CRYPTOCURRENCY_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/zh/trade-cryptocurrency']")


class MenuUS11CFDTradingGuide:
    # SUB_MENU_AR_CFD_TRADING_GUIDE = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/ar/what-is-cfd-trading']")

    SUB_MENU_BG_CFD_TRADING_GUIDE = (By.CSS_SELECTOR,
                                     "div .cc-nav__wrap a[href='https://capital.com/bg/kakvo-predstavlava-cfd']")

    # SUB_MENU_CN_CFD_TRADING_GUIDE = (By.CSS_SELECTOR,
    #                                  "div .cc-nav__wrap a[href='https://capital.com/cn/what-is-cfd-trading']")

    SUB_MENU_CS_CFD_TRADING_GUIDE = (By.CSS_SELECTOR,
                                     "div .cc-nav__wrap a[href='https://capital.com/cs/what-is-cfd-trading']")

    # SUB_MENU_DA_CFD_TRADING_GUIDE = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/da/what-is-cfd-trading']")

    SUB_MENU_DE_CFD_TRADING_GUIDE = (By.CSS_SELECTOR,
                                     "div .cc-nav__wrap a[href='https://capital.com/de/was-ist-cfd-handel']")

    # SUB_MENU_EL_CFD_TRADING_GUIDE = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/el/what-is-cfd-trading']")

    SUB_MENU_EN_CFD_TRADING_GUIDE = (By.CSS_SELECTOR,
                                     "div .cc-nav__wrap a[href='https://capital.com/what-is-cfd-trading']")

    SUB_MENU_ES_CFD_TRADING_GUIDE = (By.CSS_SELECTOR,
                                     "div .cc-nav__wrap a[href='https://capital.com/es/what-is-cfd-trading']")

    # SUB_MENU_ET_CFD_TRADING_GUIDE = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/et/what-is-cfd-trading']")

    # SUB_MENU_FI_CFD_TRADING_GUIDE = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/fi/what-is-cfd-trading']")

    SUB_MENU_FR_CFD_TRADING_GUIDE = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/fr/quest-ce-que-le-trading-de-cfd']")

    # SUB_MENU_HR_CFD_TRADING_GUIDE = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/hr/what-is-cfd-trading']")

    # SUB_MENU_HU_CFD_TRADING_GUIDE = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/hu/what-is-cfd-trading']")

    # SUB_MENU_ID_CFD_TRADING_GUIDE = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/id/panduan-perdagangan-mata-uang-kripto']")

    SUB_MENU_IT_CFD_TRADING_GUIDE = (By.CSS_SELECTOR,
                                     "div .cc-nav__wrap a[href='https://capital.com/it/cosa-sono-i-cfd']")

    # SUB_MENU_LT_CFD_TRADING_GUIDE = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/lt/what-is-cfd-trading']")

    # SUB_MENU_LV_CFD_TRADING_GUIDE = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/lv/what-is-cfd-trading']")

    SUB_MENU_NL_CFD_TRADING_GUIDE = (By.CSS_SELECTOR,
                                     "div .cc-nav__wrap a[href='https://capital.com/nl/wat-is-een-optiecontract']")

    SUB_MENU_PL_CFD_TRADING_GUIDE = (By.CSS_SELECTOR,
                                     "div .cc-nav__wrap a[href='https://capital.com/pl/what-is-cfd-trading']")

    # SUB_MENU_PT_CFD_TRADING_GUIDE = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/pt/what-is-cfd-trading']")

    SUB_MENU_RO_CFD_TRADING_GUIDE = (By.CSS_SELECTOR,
                                     "div .cc-nav__wrap a[href='https://capital.com/ro/what-is-cfd-trading']")

    SUB_MENU_RU_CFD_TRADING_GUIDE = (By.CSS_SELECTOR,
                                     "div .cc-nav__wrap a[href="
                                     "'https://capital.com/ru/cto-takoe-kontrakty-na-raznicu-cen']")

    # SUB_MENU_SK_CFD_TRADING_GUIDE = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/sk/what-is-cfd-trading']")

    # SUB_MENU_SL_CFD_TRADING_GUIDE = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/sl/what-is-cfd-trading']")

    SUB_MENU_SV_CFD_TRADING_GUIDE = (By.CSS_SELECTOR,
                                     "div .cc-nav__wrap a[href='https://capital.com/sv/var-ar-cfd-handel']")

    # SUB_MENU_TH_CFD_TRADING_GUIDE = \
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/th/what-is-cfd-trading']")

    SUB_MENU_VI_CFD_TRADING_GUIDE = (By.CSS_SELECTOR,
                                     "div .cc-nav__wrap a[href='https://capital.com/vi/what-is-cfd-trading']")

    SUB_MENU_ZH_CFD_TRADING_GUIDE = (By.CSS_SELECTOR,
                                     "div .cc-nav__wrap a[href='https://capital.com/zh/what-is-cfd-trading']")


class MenuUS11SpreadBettingGuide:
    SUB_MENU_EN_SPREAD_BETTING_GUIDE = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/what-is-spread-betting']")
    SUB_MENU_ES_SPREAD_BETTING_GUIDE = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/es/guia-de-apuestas-a-margen']")
    SUB_MENU_CN_SPREAD_BETTING_GUIDE = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/cn/what-is-spread-betting']")


class MenuUS11ETFTrading:
    SUB_MENU_AR_ETF_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/ar/trade-etfs']")

    # SUB_MENU_BG_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/bg/trade-etfs']")

    # SUB_MENU_CS_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/cs/trade-etfs']")

    SUB_MENU_CN_ETF_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/cn/trade-etfs']")

    # SUB_MENU_DA_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/da/trade-etfs']")

    SUB_MENU_DE_ETF_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/de/trade-etfs']")

    # SUB_MENU_EL_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/el/trade-etfs']")

    SUB_MENU_EN_ETF_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/trade-etfs']")

    SUB_MENU_ES_ETF_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/es/trade-etfs']")

    # SUB_MENU_ET_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/et/trade-etfs']")

    # SUB_MENU_FI_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/fi/trade-etfs']")

    # SUB_MENU_FR_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/fr/trade-etfs']")

    # SUB_MENU_HR_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/hr/trade-etfs']")

    # SUB_MENU_HU_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/hu/trade-etfs']")

    SUB_MENU_IT_ETF_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/it/trade-etfs']")

    # SUB_MENU_ID_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/id/panduan-perdagangan-mata-uang-kripto']")

    # SUB_MENU_LT_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/lt/trade-etfs']")

    # SUB_MENU_LV_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/lv/trade-etfs']")

    # SUB_MENU_NL_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/nl/trade-etfs']")

    # SUB_MENU_PL_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/pl/trade-etfs']") # В меню нет, но страница есть

    # SUB_MENU_PT_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/pt/trade-etfs']")

    # SUB_MENU_RO_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/ro/cryptocurrency-trading']")

    SUB_MENU_RU_ETF_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/ru/trade-etfs']")

    # SUB_MENU_SK_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/sk/trade-etfs']")

    # SUB_MENU_SL_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/sl/trade-etfs']")

    # SUB_MENU_SV_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/sv/trade-etfs']")

    # SUB_MENU_TH_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/th/trade-etfs']")

    SUB_MENU_VI_ETF_TRADING = \
        (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/vi/trade-etfs']")

    # SUB_MENU_ZH_ETF_TRADING =
    # (By.CSS_SELECTOR, "div .cc-nav__wrap a[href='https://capital.com/zh/trade-etfs']")


class MenuUS11TradingStrategiesGuide:
    SUB_MENU_EN_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/trading-strategies-guide']")
    SUB_MENU_AR_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,  # Нет такой страницы
                                            "div .grid > a[href='https://capital.com/ar/trading-strategies-guide']")
    # SUB_MENU_BG_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,  # Нет такой страницы
    #                                         "div .grid > a[href='https://capital.com/bg/trading-strategies-guide']")
    SUB_MENU_CS_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/cs/trading-strategies-guide']")
    SUB_MENU_DA_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/da/trading-strategies-guide']")
    SUB_MENU_DE_TRADING_STRATEGIES_GUIDE = \
        (By.CSS_SELECTOR, "div .grid > a[href='https://capital.com/de/trading-strategien-leitfaden']")
    SUB_MENU_ET_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/et/trading-strategies-guide']")
    SUB_MENU_EL_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/el/trading-strategies-guide']")
    SUB_MENU_ES_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,  # Нет такой страницы
                                            "div .cc-nav__wrap a[href='https://capital.com/es/guia-de-estrategias']")
    SUB_MENU_FR_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,  # Нет такой страницы
                                            "div .grid > a[href='https://capital.com/fr/trading-strategies-guide']")
    SUB_MENU_HR_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/hr/trading-strategies-guide']")
    SUB_MENU_IT_TRADING_STRATEGIES_GUIDE = \
        (By.CSS_SELECTOR, "div .grid > a[href='https://capital.com/it/strategie-di-trading']")
    SUB_MENU_LV_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/lv/trading-strategies-guide']")
    SUB_MENU_LT_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/lt/trading-strategies-guide']")
    SUB_MENU_HU_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/hu/trading-strategies-guide']")
    SUB_MENU_ID_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/id/trading-strategies-guide']")
    SUB_MENU_NL_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/nl/trading-strategies-guide']")
    SUB_MENU_PL_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/pl/trading-strategies-guide']")
    SUB_MENU_PT_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/pt/trading-strategies-guide']")
    SUB_MENU_RO_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/ro/trading-strategies-guide']")
    SUB_MENU_RU_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/ru/torgovye-strategii']")
    SUB_MENU_SK_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/sk/trading-strategies-guide']")
    SUB_MENU_SL_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/sl/trading-strategies-guide']")
    SUB_MENU_FI_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/fi/trading-strategies-guide']")
    SUB_MENU_SV_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/sv/trading-strategies-guide']")
    SUB_MENU_VI_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/vi/trading-strategies-guide']")
    SUB_MENU_ZH_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/zh/trading-strategies-guide']")
    SUB_MENU_TH_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/th/trading-strategies-guide']")
    SUB_MENU_CN_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR,
                                            "div .grid > a[href='https://capital.com/cn/trading-strategies-guide']")


class MenuUS11DayTrading:
    SUB_MENU_ALL_DAY_TRADING = (By.CSS_SELECTOR, ".cc-header a[href$='/day-trading']")


class MenuUS11IndicesTrading:
    SUB_MENU_ALL_INDICES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href$='/trade-indices']")
    SUB_MENU_AR_INDICES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href$='/ar/trade-indices")
    SUB_MENU_DE_INDICES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href$='/de/indizeshandel']")
    SUB_MENU_ES_INDICES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href$='/es/trade-indices")
    SUB_MENU_IT_INDICES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href$='/it/trading-su-indici']")
    SUB_MENU_CN_INDICES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href$='/cn/trade-indices")
    SUB_MENU_ZH_INDICES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href$='/zh/trade-indices']")
    SUB_MENU_RU_INDICES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href$='/ru/torgovlya-indeksami-cfd")


class MenuUS11WhatIsMargin:
    SUB_MENU_ALL_WHAT_IS_A_MARGIN = (By.CSS_SELECTOR, ".cc-header a[href$='/margin-trading']")


class MenuUS11InvestmateApp:
    SUB_MENU_ALL_INVESTMATE_APP = (By.CSS_SELECTOR, ".cc-header a[href$='/learn-trading-app'][class*='cc-nav__link']")
    SUB_MENU_DE_INVESTMATE_APP = (By.CSS_SELECTOR, ".cc-header a[href$='/trading-lernen-app'][class*='cc-nav__link']")
    SUB_MENU_ES_INVESTMATE_APP = (By.CSS_SELECTOR, ".cc-header a[href$='/investmate'][class*='cc-nav__link']")
    SUB_MENU_FR_INVESTMATE_APP = (By.CSS_SELECTOR, ".cc-header a[href$='/investmate'][class*='cc-nav__link']")
    SUB_MENU_IT_INVESTMATE_APP = (By.CSS_SELECTOR, ".cc-header a[href$='/investmate'][class*='cc-nav__link']")
    SUB_MENU_NL_INVESTMATE_APP = (By.CSS_SELECTOR, ".cc-header a[href$='/investmate'][class*='cc-nav__link']")
    SUB_MENU_PL_INVESTMATE_APP = (By.CSS_SELECTOR, '[data-type="nav_id78"]')
    SUB_MENU_CN_INVESTMATE_APP = (By.CSS_SELECTOR, '[data-type="nav_id78"]')


class MenuUS11TrendTrading:
    SUB_MENU_EN_ITEM_TREND_TRADING = (By.CSS_SELECTOR,
                                      "div .cc-nav__wrap a[href='https://capital.com/trend-trading']")

    # SUB_MENU_DE_ITEM_TREND_TRADING = (By.CSS_SELECTOR,
    #                                   "div .cc-nav__wrap a[href='https://capital.com/de/trendtrading']")
    # --страница на de есть на сайте, но раздела нет в меню


class MenuUS11TradingPsychologyGuide:
    SUB_MENU_EN_TRADING_PSYCHOLOGY_GUIDE = \
        (By.CSS_SELECTOR, ".cc-header .cc-nav__dropdown a[href$='/trading-psychology-guide']")
    SUB_MENU_AR_TRADING_PSYCHOLOGY_GUIDE = (By.CSS_SELECTOR, ".cc-header a[href$='/ar']")
    SUB_MENU_DE_TRADING_PSYCHOLOGY_GUIDE = (By.CSS_SELECTOR, ".cc-header a[href$='/de']")
    SUB_MENU_EL_TRADING_PSYCHOLOGY_GUIDE = (By.CSS_SELECTOR, ".cc-header a[href$='/el']")
    SUB_MENU_ES_TRADING_PSYCHOLOGY_GUIDE = (By.CSS_SELECTOR, ".cc-header a[href$='/es']")
    SUB_MENU_FR_TRADING_PSYCHOLOGY_GUIDE = (By.CSS_SELECTOR, ".cc-header a[href$='/fr']")
    SUB_MENU_IT_TRADING_PSYCHOLOGY_GUIDE = (By.CSS_SELECTOR, ".cc-header a[href$='/it']")
    SUB_MENU_HU_TRADING_PSYCHOLOGY_GUIDE = (By.CSS_SELECTOR, ".cc-header a[href$='/hu']")
    SUB_MENU_NL_TRADING_PSYCHOLOGY_GUIDE = (By.CSS_SELECTOR, ".cc-header a[href$='/nl']")
    SUB_MENU_PL_TRADING_PSYCHOLOGY_GUIDE = (By.CSS_SELECTOR, ".cc-header a[href$='/pl']")
    SUB_MENU_RO_TRADING_PSYCHOLOGY_GUIDE = (By.CSS_SELECTOR, ".cc-header a[href$='/ro']")
    SUB_MENU_RU_TRADING_PSYCHOLOGY_GUIDE = (By.CSS_SELECTOR, ".cc-header a[href$='/ru']")
    SUB_MENU_ZH_TRADING_PSYCHOLOGY_GUIDE = (By.CSS_SELECTOR, ".cc-header a[href$='/zh']")
    SUB_MENU_CN_TRADING_PSYCHOLOGY_GUIDE = (By.CSS_SELECTOR, ".cc-header a[href$='/cn']")


class MenuUS11PositionTrading:
    SUB_MENU_ALL_POSITION_TRADING = (By.CSS_SELECTOR, ".cc-header a[href$='/position-trading']")


class MenuUS11SwingTrading:
    SUB_MENU_ALL_SWING_TRADING = (By.CSS_SELECTOR, ".cc-header a[href$='/swing-trading']")


class MenuUS11ScalpTrading:
    SUB_MENU_ALL_SCALP_TRADING = (By.CSS_SELECTOR, ".cc-header a[href$='/scalping']")


class MenuUS11SharesTrading:
    # для кнопки Start Trading
    # SUB_MENU_EN_SHARES_TRADING = (By.CSS_SELECTOR, ".cc-banner a[href$='/trading/signup']")
    SUB_MENU_AR_SHARES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/ar/trade-stocks']")
    SUB_MENU_CN_SHARES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/cn/trade-stocks']")
    SUB_MENU_DE_SHARES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/de/aktienhandel")
    # SUB_MENU_EL_SHARES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/el']")
    SUB_MENU_EN_SHARES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/trade-stocks']")
    SUB_MENU_ES_SHARES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/es/trade-stocks']")
    SUB_MENU_FR_SHARES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/fr/trade-stocks']")
    # SUB_MENU_HU_SHARES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/hu']")
    SUB_MENU_IT_SHARES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/it/trading-su-azioni']")
    SUB_MENU_NL_SHARES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/nl/trade-stocks']")
    SUB_MENU_PL_SHARES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/pl/trade-stocks']")
    SUB_MENU_RO_SHARES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/ro/trade-stocks']")
    SUB_MENU_RU_SHARES_TRADING = (By.CSS_SELECTOR,
                                  ".cc-header a[href='https://capital.com/ru/torgovlya-aktsiyami-cfd']")
    SUB_MENU_ZH_SHARES_TRADING = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/zh/trade-stocks']")


class MenuUS11RiskManagement:
    SUB_MENU_EN_RISK_MANAGEMENT = (By.CSS_SELECTOR, '[data-type="nav_id720"]')


class MenuUS11TechnicalAnalysis:
    SUB_MENU_EN_TECHNICAL_ANALYSIS = (By.CSS_SELECTOR, '[data-type="nav_id705"]')


class MenuUS11HELP:
    SUB_MENU_EN_HELP = (By.CSS_SELECTOR, '[data-type="nav_id779"]')


class MenuUS11LearnToTrade:
    SUB_MENU_EN_LEARN_TO_TRADE = (By.CSS_SELECTOR, '[data-type="nav_id698"]')


class MenuUS11TradingStrategies:
    SUB_MENU_EN_TRADING_STRATEGIES = (By.CSS_SELECTOR, '[data-type="nav_id697"]')


class MenuUS11EssentialsOfTrading:
    SUB_MENU_EN_ESSENTIALS_OF_TRADING = (By.CSS_SELECTOR, '[data-type="nav_id754"]')


class MenuUS11MarketGuidesNew:
    SUB_MENU_MARKET_GUIDES_NEW = (By.CSS_SELECTOR, '[data-type="nav_id700"]')


class MenuUS11MarketAnalysis:
    SUB_MENU_MARKET_ANALYSIS_EN_GB = (By.CSS_SELECTOR, '[data-type="nav_id771"]')
    SUB_MENU_MARKET_ANALYSIS_EN_AE = (By.CSS_SELECTOR, '[data-type="nav_id869"]')

# ".menu_menu__3Lgen a[href="/en-gb/learn"]"


class MenuProductsAndServices:
    MENU_PRODUCTS_AND_SERVICES_EN_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/./trading-products']")
    MENU_PRODUCTS_AND_SERVICES_AR_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/ar/trading-products']")
    MENU_PRODUCTS_AND_SERVICES_DE_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/de/trading-products']")
    MENU_PRODUCTS_AND_SERVICES_EL_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/el/trading-products']")
    MENU_PRODUCTS_AND_SERVICES_ES_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/es/trading-products']")
    MENU_PRODUCTS_AND_SERVICES_FR_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/fr/trading-products']")
    MENU_PRODUCTS_AND_SERVICES_IT_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/it/trading-products']")
    MENU_PRODUCTS_AND_SERVICES_HU_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/hu/trading-products']")
    MENU_PRODUCTS_AND_SERVICES_NL_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/nl/trading-products']")
    MENU_PRODUCTS_AND_SERVICES_PL_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/pl/trading-products']")
    MENU_PRODUCTS_AND_SERVICES_RO_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/ro/trading-products']")
    MENU_PRODUCTS_AND_SERVICES_RU_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/ru/trading-products']")
    MENU_PRODUCTS_AND_SERVICES_ZH_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/zh/trading-products']")
    MENU_PRODUCTS_AND_SERVICES_CN_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/cn/trading-products']")


class MenuUS01Markets:
    MENU_EN_GB_MARKETS = (By.CSS_SELECTOR, "#header a[href='/en-gb/markets']")
    MENU_MARKETS_EN_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/derivative-financial-instruments']")
    MENU_MARKETS_AR_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/ar/alaswaq']")
    MENU_MARKETS_DE_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/de/alle-maerkte']")
    MENU_MARKETS_EL_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/el/paragoga-xrimatopistotika-mesa']")
    MENU_MARKETS_ES_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/es/instrumentos-financieros-derivados']")
    MENU_MARKETS_FR_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/fr/instruments-financiers-derives']")
    MENU_MARKETS_IT_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/it/derivati']")
    MENU_MARKETS_HU_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/hu/derivativ-penzugyi-eszkozok']")
    MENU_MARKETS_NL_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/nl/derivaat-financieel-instrument']")
    MENU_MARKETS_PL_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/pl/pochodne-instrumenty-finansowe']")
    MENU_MARKETS_RO_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/ro/instrumente-financiare-derivate']")
    MENU_MARKETS_RU_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/ru/proizvodnyye-finansovyye-instrumenty']")
    MENU_MARKETS_ZH_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/zh/derivative-financial-instruments']")
    MENU_MARKETS_CN_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/cn/derivative-financial-instruments']")


class MenuUS02NewsAndAnalysis:
    MENU_NEWS_AND_ANALYSIS_EN_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/./market-analysis']")
    MENU_NEWS_AND_ANALYSIS_AR_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/ar/news-ar-local']")
    MENU_NEWS_AND_ANALYSIS_DE_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/de/wirtschaftsnews']")
    MENU_NEWS_AND_ANALYSIS_EL_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/el/financial-news-articles-local']")
    MENU_NEWS_AND_ANALYSIS_ES_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/es/noticias-loc']")
    MENU_NEWS_AND_ANALYSIS_FR_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/fr/nouvelles-economiques-loc']")
    MENU_NEWS_AND_ANALYSIS_IT_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/it/notizie-analisi']")
    MENU_NEWS_AND_ANALYSIS_HU_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/hu/financial-news-articles-local']")
    MENU_NEWS_AND_ANALYSIS_NL_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/nl/economie-nieuws-loc']")
    MENU_NEWS_AND_ANALYSIS_PL_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/pl/nowosci-ekonomiczne-loc']")
    MENU_NEWS_AND_ANALYSIS_RO_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/ro/stiri-economice-loc']")
    MENU_NEWS_AND_ANALYSIS_RU_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/ru/financial-news-articles-local']")
    MENU_NEWS_AND_ANALYSIS_ZH_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/zh/jingji-xinwen-loc']")
    MENU_NEWS_AND_ANALYSIS_CN_BUTTON = (
        By.CSS_SELECTOR,
        ".cc-header .cc-nav__item > a[href='https://capital.com/cn/learn-how-to-trade']")


class MenuUS0201MarketAnalysis:
    SUB_MENU_EN_MARKET_ANALYSIS = (By.CSS_SELECTOR,
                           ".cc-nav__dropdown a[href='https://capital.com/./market-analysis']")


class MenuUS01Indices:
    SUB_MENU_EN_INDICES = (By.CSS_SELECTOR,
                           ".cc-nav__dropdown a[href$='major-world-indices']")
    SUB_MENU_AR_INDICES = (By.CSS_SELECTOR,
                           ".cc-nav__dropdown a[href$='/ar/alasear-almubashirat-lilmuashirat-alealamiat-alrayiysia']")
    SUB_MENU_DE_INDICES = (By.CSS_SELECTOR,
                           ".cc-nav__dropdown a[href$='/de/welt-indizes']")
    SUB_MENU_EL_INDICES = (By.CSS_SELECTOR,
                           ".cc-nav__dropdown a[href$='/el/kirioi-pagkosmioi-deiktes']")
    SUB_MENU_ES_INDICES = (By.CSS_SELECTOR,
                           ".cc-nav__dropdown a[href$='/es/principales-indices-mundiales']")
    SUB_MENU_FR_INDICES = (By.CSS_SELECTOR,
                           ".cc-nav__dropdown a[href$='/fr/indices-principaux']")
    SUB_MENU_IT_INDICES = (By.CSS_SELECTOR,
                           ".cc-nav__dropdown a[href$='/it/indici-in-tempo-reale']")
    SUB_MENU_HU_INDICES = (By.CSS_SELECTOR,
                           ".cc-nav__dropdown a[href$='/hu/fobb-globalis-indexek']")
    SUB_MENU_NL_INDICES = (By.CSS_SELECTOR,
                           ".cc-nav__dropdown a[href$='nl/grootste-indexen-wereldwijd']")
    SUB_MENU_PL_INDICES = (By.CSS_SELECTOR,
                           ".cc-nav__dropdown a[href$='pl/glownych-indeksow-swiatowych']")
    SUB_MENU_RO_INDICES = (By.CSS_SELECTOR,
                           ".cc-nav__dropdown a[href$='/ro/principalii-indicatori-mondiali-']")
    SUB_MENU_RU_INDICES = (By.CSS_SELECTOR,
                           ".cc-nav__dropdown a[href$='/ru/mirovyye-fondovyye-indeksy']")
    SUB_MENU_ZH_INDICES = (By.CSS_SELECTOR,
                           ".cc-nav__dropdown a[href$='/zh/major-world-indices']")
    SUB_MENU_CN_INDICES = (By.CSS_SELECTOR,
                           ".cc-nav__dropdown a[href$='/cn/major-world-indices']")

    
class MenuUS0103MarketsForex:
    SUB_MENU_EN_FOREX = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/live-currency-prices']")
    SUB_MENU_AR_FOREX = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/ar/asear-alfurks-alan']")
    SUB_MENU_DE_FOREX = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/de/waehrungskurse']")
    SUB_MENU_EL_FOREX = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/el/alla-ergaleia']")
    SUB_MENU_ES_FOREX = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/es/en-vivo-moneda-precios']")
    SUB_MENU_FR_FOREX = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/fr/autres-instruments']")
    SUB_MENU_IT_FOREX = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/it/forex-in-tempo-reale']")
    SUB_MENU_HU_FOREX = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/hu/elo-valutaarfolyamok']")
    SUB_MENU_NL_FOREX = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/nl/andere-instrumenten']")
    SUB_MENU_PL_FOREX = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/pl/aktualne-ceny-waluty']")
    SUB_MENU_RU_FOREX = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/ru/forex']")
    SUB_MENU_CN_FOREX = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/cn/live-currency-prices']")
    SUB_MENU_RO_FOREX = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/ro/alte-instrumente']")
    SUB_MENU_ZH_FOREX = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/zh/live-currency-prices']")

    
class MenuUS0104Commodities:
    SUB_MENU_EN_COMMODITIES_BUTTON = \
        (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/live-commodity-prices']")
    SUB_MENU_AR_COMMODITIES_BUTTON = \
        (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/ar/mukhatat-asear-alsilae']")
    SUB_MENU_DE_COMMODITIES_BUTTON = \
        (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/de/rohstoffpreise']")
    SUB_MENU_EL_COMMODITIES_BUTTON = \
        (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/el/zontanes-times-emporevmaton']")
    SUB_MENU_ES_COMMODITIES_BUTTON = \
        (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/es/en-vivo-mercancia-precios']")
    SUB_MENU_FR_COMMODITIES_BUTTON = \
        (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/fr/prix-des-matieres-premieres-en-direct']")
    SUB_MENU_IT_COMMODITIES_BUTTON = \
        (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/it/prezzi-delle-materie-prime-in-tempo-reale']")
    SUB_MENU_HU_COMMODITIES_BUTTON = \
        (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/hu/elo-arupiaci-arak']")
    SUB_MENU_NL_COMMODITIES_BUTTON = \
        (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/nl/live-grondstoffen-prijzen']")
    SUB_MENU_PL_COMMODITIES_BUTTON = \
        (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/pl/aktualne-cen-towarow']")
    SUB_MENU_RO_COMMODITIES_BUTTON = \
        (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/ro/live-marfuri-preturi']")
    SUB_MENU_RU_COMMODITIES_BUTTON = \
        (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/ru/tseny-na-syryo']")
    SUB_MENU_ZH_COMMODITIES_BUTTON = \
        (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/zh/live-commodity-prices']")
    SUB_MENU_CN_COMMODITIES_BUTTON = \
        (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/cn/live-commodity-prices']")

# class MenuUS01MarketsButton:
#     MENU_MARKETS_BUTTON = (By.CSS_SELECTOR, "[data-type='nav_id3']")
#     SUB_MENU_SHARES_BUTTON = (By.CSS_SELECTOR, "[data-type='nav_id9']")
#     SUB_MENU_FOREX_BUTTON = (By.CSS_SELECTOR, "[data-type='nav_id57']")
#     SUB_MENU_INDICES_BUTTON = (By.CSS_SELECTOR, "[data-type='nav_id8']")
#     SUB_MENU_COMMODITIES_BUTTON = (By.CSS_SELECTOR, "[data-type='nav_id4']")
#     SUB_MENU_CRYPTOCURRENCIES_BUTTON = (By.CSS_SELECTOR, "[data-type='nav_id65']")
#     SUB_MENU_ESG_BUTTON = (By.CSS_SELECTOR, "[data-type='nav_id461']")
#     SUB_MENU_EN_GB_MARKETS_BUTTON = (By.CSS_SELECTOR, "[data-type='nav_id689']")

# class MenuUS0102MarketsShares:
#     SUB_MENU_EN_SHARES = (By.CSS_SELECTOR,
#                            ".cc-nav__dropdown a[href$='major-world-indices']")


class MenuUS0102MarketsShares:
    # SUB_MENU_EN_SHARES = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/live-currency-prices']")
    SUB_MENU_EN_SHARES = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/live-share-prices']")
    SUB_MENU_AR_SHARES = (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/ar/asear-alashum-fi-alwaqt-alfielii']")
    SUB_MENU_DE_SHARES = (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/de/aktienkurse-realtime']")
    SUB_MENU_EL_SHARES = (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/el/zontanes-times-metoxon']")
    SUB_MENU_ES_SHARES = (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/es/en-vivo-acciones-precios']")
    SUB_MENU_FR_SHARES = (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/fr/prix-des-actions-en-direct']")
    SUB_MENU_IT_SHARES = (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/it/prezzi-delle-azioni-in-tempo-reale']")
    SUB_MENU_HU_SHARES = (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/hu/elo-reszvenyarak']")
    SUB_MENU_NL_SHARES = (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/nl/live-aandelen-koersen']")
    SUB_MENU_PL_SHARES = (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/pl/aktualne-ceny-akcji']")
    SUB_MENU_RO_SHARES = (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/ro/live-actiuni-preturi']")
    SUB_MENU_RU_SHARES = (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/ru/kotirovki-aktsiy']")
    SUB_MENU_ZH_SHARES = (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/zh/live-share-prices']")
    SUB_MENU_CN_SHARES = (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/cn/live-share-prices']")


class MenuUS0107MarketsESG:
    SUB_MENU_EN_ESG = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/esg-rating']")


class MenuUS0109MarketsCFDCalculator:
    SUB_MENU_EN_CFDCALCULATOR = (By.CSS_SELECTOR, ".cc-header a[href='https://capital.com/./cfd-calculator']")

    
class MenuUS0101AllMarkets:
    SUB_MENU_EN_ALLMARKETS_BUTTON = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/derivative-financial-instruments']")
    SUB_MENU_AR_ALLMARKETS_BUTTON = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/ar/alaswaq']")
    SUB_MENU_DE_ALLMARKETS_BUTTON = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/de/alle-maerkte']")
    SUB_MENU_EL_ALLMARKETS_BUTTON = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/el/paragoga-xrimatopistotika-mesa']")
    SUB_MENU_ES_ALLMARKETS_BUTTON = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/es/instrumentos-financieros-derivados']")
    SUB_MENU_FR_ALLMARKETS_BUTTON = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/fr/instruments-financiers-derives']")
    SUB_MENU_IT_ALLMARKETS_BUTTON = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/it/derivati']")
    SUB_MENU_HU_ALLMARKETS_BUTTON = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/hu/derivativ-penzugyi-eszkozok']")
    SUB_MENU_NL_ALLMARKETS_BUTTON = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/nl/derivaat-financieel-instrument']")
    SUB_MENU_PL_ALLMARKETS_BUTTON = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/pl/pochodne-instrumenty-finansowe']")
    SUB_MENU_RO_ALLMARKETS_BUTTON = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/ro/instrumente-financiare-derivate']")
    SUB_MENU_RU_ALLMARKETS_BUTTON = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/ru/proizvodnyye-finansovyye-instrumenty']")
    SUB_MENU_ZH_ALLMARKETS_BUTTON = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/zh/derivative-financial-instruments']")
    SUB_MENU_CN_ALLMARKETS_BUTTON = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/cn/derivative-financial-instruments']")


class MenuProductsAndServicesOurMobileApps:
    SUB_MENU_EN_OUR_MOBILE_APPS = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/mobile-apps']")
    SUB_MENU_AR_OUR_MOBILE_APPS = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/ar/mobile-apps']")
    SUB_MENU_DE_OUR_MOBILE_APPS = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/de/mobile-apps']")
    SUB_MENU_ES_OUR_MOBILE_APPS = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/es/mobile-apps']")
    SUB_MENU_FR_OUR_MOBILE_APPS = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/fr/mobile-apps']")
    SUB_MENU_IT_OUR_MOBILE_APPS = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/it/mobile-apps']")
    SUB_MENU_HU_OUR_MOBILE_APPS = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/hu/mobile-apps']")
    SUB_MENU_NL_OUR_MOBILE_APPS = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/nl/mobile-apps']")
    SUB_MENU_PL_OUR_MOBILE_APPS = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/pl/mobile-apps']")
    SUB_MENU_RO_OUR_MOBILE_APPS = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/ro/mobile-apps']")
    SUB_MENU_RU_OUR_MOBILE_APPS = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/ru/mobile-apps']")
    SUB_MENU_CN_OUR_MOBILE_APPS = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/cn/mobile-apps']")


class MenuUS0106MarketsCryptocurrencies:
    SUB_MENU_EN_CRYPTOCURRENCIES = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/live-cryptocurrency-prices']")
    SUB_MENU_AR_CRYPTOCURRENCIES = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/ar/alrasm-albayaniu-lileumlat-alraqamia']")
    SUB_MENU_DE_CRYPTOCURRENCIES = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/de/kryptowaehrung-preise']")
    SUB_MENU_EL_CRYPTOCURRENCIES = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/el/zwntana-kryptonomismata-times']")
    SUB_MENU_ES_CRYPTOCURRENCIES = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/es/live-cryptocurrency-prices']")
    SUB_MENU_FR_CRYPTOCURRENCIES = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/fr/live-monnaies-crypto-prix']")
    SUB_MENU_IT_CRYPTOCURRENCIES = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/it/prezzi-delle-criptovalute-in-tempo-reale']")
    SUB_MENU_HU_CRYPTOCURRENCIES = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/hu/live-cryptocurrency-prices']")
    SUB_MENU_NL_CRYPTOCURRENCIES = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/nl/live-cryptovaluta-prijzen']")
    SUB_MENU_PL_CRYPTOCURRENCIES = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/pl/na-zywo-kryptowaluta-ceny']")
    SUB_MENU_RO_CRYPTOCURRENCIES = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/ro/live-criptomoneda-preturile']")
    SUB_MENU_RU_CRYPTOCURRENCIES = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/ru/tseny-na-kriptovalyuty']")
    SUB_MENU_ZH_CRYPTOCURRENCIES = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/zh/live-cryptocurrency-prices']")
    SUB_MENU_CN_CRYPTOCURRENCIES = \
        (By.CSS_SELECTOR, ".cc-nav__dropdown a[href='https://capital.com/cn/live-cryptocurrency-prices']")


class MenuUS55WaysToTrade:

    # ways to trade
    MENU_WAYS_TO_TRADE = (By.CSS_SELECTOR, '[data-type="nav_id686"]')
    SUB_MENU_WAYS_TO_TRADE_PROFESSIONAL = (By.CSS_SELECTOR, '[data-type="nav_id752"]')

    # footer
    # FOOTER_RISK_WARNING_BLOCK = (By.CSS_SELECTOR, 'footer .dark')
    # FOOTER_RISK_WARNING_BLOCK_LINK = (By.CSS_SELECTOR, 'footer .dark a')
    FOOTER_CAPITAL_LOGO = (By.CSS_SELECTOR, 'footer > div > a[href="/en-gb"]')
