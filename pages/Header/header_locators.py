"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
from selenium.webdriver.common.by import By


class HeaderElementLocators:
	BUTTON_MY_ACCOUNT = (By.ID, "wg_userarea")
	MAIN_LOGO_CAPITAL_COM = (By.CSS_SELECTOR, ".cc-header .cc-header__logo")
	NEW_MAIN_LOGO_CAPITAL_COM = (By.CSS_SELECTOR, "header .helpers_hideXs__vzgPk.logo_link__wVTFX")
