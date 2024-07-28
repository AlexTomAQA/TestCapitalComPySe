"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
from selenium.webdriver.common.by import By


class HeaderElementLocators:
	BUTTON_MY_ACCOUNT = (By.ID, "wg_userarea")
	MAIN_LOGO_CAPITAL_COM = (By.CSS_SELECTOR, ".cc-header .cc-header__logo")
	MAIN_LOGO_NEW_CAPITAL_COM = (By.CSS_SELECTOR, '#header [class*="logo_link__wVTFX helpers_hide"]')
	NEW_MAIN_LOGO_CAPITAL_COM = (By.CSS_SELECTOR, "header .helpers_hideXs__vzgPk.logo_link__wVTFX")
	MAIN_LOGO_CAPITAL_COM_SCA = (By.CSS_SELECTOR, ".logo_logo__x10mm.panel_logo__xwk_Y")
