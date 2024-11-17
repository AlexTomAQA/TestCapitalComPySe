"""
-*- coding: utf-8 -*-
@Time    : 2024/09/15 22:00
@Author  : Sergey Aiidzhanov
"""
from pages.conditions import Conditions
from pages.conditions_new import NewConditions
from src.src import CapitalComPageSrc


def conditions_switch(d, cur_language, cur_country, cur_role, cur_login, cur_password):

    if cur_country in ['ua']:
        cond = Conditions(d)
        return cond.preconditions(d, CapitalComPageSrc.URL, '', cur_language, cur_country, cur_role,
                                  cur_login, cur_password)

    if cur_country in ['ae', 'au', 'gb', 'de']:
        cond = NewConditions(d)
        return cond.preconditions(d, CapitalComPageSrc.URL_NEW, '', cur_language, cur_country, cur_role,
                                  cur_login, cur_password)
