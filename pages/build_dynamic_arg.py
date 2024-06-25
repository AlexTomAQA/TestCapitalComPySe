"""
-*- coding: utf-8 -*-
@Time    : 2023/04/14 16:30
@Author  : Alexander Tomelo
"""
import platform

import pytest
import allure
# import sys
from datetime import datetime


count = 1


@allure.step(f"{datetime.now()}   Start Building dynamic arguments for allure report generation")
def build_dynamic_arg_new_v4(d, worker_id, cur_language, cur_country, cur_role,
                             us, desc_us, num_tc, desc_tc):
    """
    function for dynamic bild names pf epic, feature and story
    """
    global count

    # tc = f"TC_{us}_{num_tc}"
    print(d.get_window_size())
    # print(f"\n{datetime.now()}   browser = {d.name}")
    print(f"\n{datetime.now()}   worker_id = {worker_id}")
    # print(f"\n{datetime.now()}   Start {tc}")
    print(f"\n{datetime.now()}   0. Allure grouping v4")

    # language = cur_language
    if cur_language == "":
        cur_language = "en"

    # dynamic_epic = f"US_{us} | {desc_us}"
    # dynamic_feature = f"Language: {cur_language}"
    # dynamic_story = f"Country: {cur_country} / Role: {cur_role}"

    dynamic_epic = f"US_{us} | {desc_us}"
    dynamic_feature = f"Role: {cur_role}"
    dynamic_story = f"Country: {cur_country} / Language: {cur_language}"

    bug_id = f"Bid:{us}{num_tc}-{cur_language}.{cur_country}.{cur_role}"

    allure.dynamic.epic(dynamic_epic)
    allure.dynamic.feature(dynamic_feature)
    allure.dynamic.story(dynamic_story)
    allure.dynamic.title(
        f"TC_{us}{num_tc} | {desc_tc}. {bug_id}")

    del dynamic_story
    del dynamic_feature
    del dynamic_epic
    del cur_language

    return bug_id


def build_dynamic_arg_v4(d, worker_id, cur_language, cur_country, cur_role,
                         us, desc_us, num_tc, desc_tc, manual=False, new_layout=False):
    """
    function for dynamic bild names pf epic, feature and story
    Args:
        d - Web-driver
        worker_id - # потока при многопоточном тестировании
        cur_language - язык
        cur_country - страна/лицензия
        cur_role - роль
        us - номер US
        desc_us - описание US
        num_tc - номер ТК
        desc_tc - описание ТК
        manual - для ретестов мануальных тестировщиков
        new_layout - новый вариант layouts для FCA/En (пока использование не обязательное)
    """
    global count

    allure.step(f"{datetime.now()}   Start Building dynamic arguments for allure report generation")
    # tc = f"TC_{us}_{num_tc}"
    print(d.get_window_size())
    # print(f"\n{datetime.now()}   browser = {d.name}")
    print(f"\n{datetime.now()}   worker_id = {worker_id}")
    # print(f"\n{datetime.now()}   Start {tc}")
    print(f"\n{datetime.now()}   0. Allure grouping v4")
    # название OS и браузера
    platform_v = platform.platform()
    os_name = platform_v.split("-")[0][0] + platform_v.split("-")[1]

    cur_br = d.capabilities['browserName'].lower()
    browser_mapping = {'microsoftedge': 'E', 'chrome': 'C', 'firefox': 'F', 'safari': 'S'}
    browser_name = browser_mapping.get(cur_br, 'Unknown')
    if browser_name == 'Unknown':
        print(f"Unsupported browser: {browser_name}")
    #
    # language = cur_language
    if cur_language == "":
        cur_language = "en"
    # dynamic_epic = f"US_{us} | {desc_us}"
    # dynamic_feature = f"Language: {cur_language}"
    # dynamic_story = f"Country: {cur_country} / Role: {cur_role}"

    # dynamic_epic = f"US_{us} | {desc_us}"
    # dynamic_feature = f"Country: {cur_country}"
    # dynamic_story = f"Language: {cur_language} / Role: {cur_role}"

    dynamic_epic = f"US_{us} | {desc_us}"
    dynamic_feature = f"Role: {cur_role}"
    dynamic_story = f"Country: {cur_country} / Language: {cur_language}"

    if manual:
        bug_id = (f"Bid:{us}{num_tc}-{cur_language}.{cur_country}.{cur_role}-{os_name}.{browser_name}"
                  f"-M{"N" if new_layout else "O"}")
    else:
        bug_id = f"Bid:{us}{num_tc}-{cur_language}.{cur_country}.{cur_role}"

    allure.dynamic.epic(dynamic_epic)
    allure.dynamic.feature(dynamic_feature)
    allure.dynamic.story(dynamic_story)
    allure.dynamic.title(
        f"TC_{us}{num_tc} | {desc_tc}. {bug_id}")

    del dynamic_story
    del dynamic_feature
    del dynamic_epic
    del cur_language

    return bug_id


def build_dynamic_arg_for_us_55(
        d, worker_id, cur_language, cur_country, cur_role,
        us, desc_us, num_tc, desc_tc, manual=False, new_layout=False):
    """
    function for dynamic bild names pf epic, feature and story
    Args:
        d - Web-driver
        worker_id - # потока при многопоточном тестировании
        cur_language - язык
        cur_country - страна/лицензия
        cur_role - роль
        us - номер US
        desc_us - описание US
        num_tc - номер ТК
        desc_tc - описание ТК
        manual - для ретестов мануальных тестировщиков
        new_layout - новый вариант layouts для FCA/En (пока использование не обязательное)
    """
    global count

    allure.step(f"{datetime.now()}   Start Building dynamic arguments for US_55")
    # tc = f"TC_{us}_{num_tc}"
    print(d.get_window_size())
    # print(f"\n{datetime.now()}   browser = {d.name}")
    print(f"\n{datetime.now()}   worker_id = {worker_id}")
    # print(f"\n{datetime.now()}   Start {tc}")
    print(f"\n{datetime.now()}   0. Allure grouping for US_55")
    # название OS и браузера
    platform_v = platform.platform()
    os_name = platform_v.split("-")[0][0] + platform_v.split("-")[1]

    cur_br = d.capabilities['browserName'].lower()
    browser_mapping = {'microsoftedge': 'E', 'chrome': 'C', 'firefox': 'F', 'safari': 'S'}
    browser_name = browser_mapping.get(cur_br, 'Unknown')
    if browser_name == 'Unknown':
        print(f"Unsupported browser: {browser_name}")
    #
    # language = cur_language
    if cur_language == "":
        cur_language = "en"

    dynamic_epic = f"TC_{us}!{num_tc} | {desc_tc}"
    # dynamic_epic = f"US_{us} | {desc_us}"

    dynamic_feature = f"Role: {cur_role}"
    # dynamic_feature = f"Language: {cur_language}"
    # dynamic_feature = f"Country: {cur_country}"
    # dynamic_feature = f"Test-case: {us}{num_tc}"

    dynamic_story = f"Country: {cur_country}"
    # dynamic_story = f"License: {cur_license} - Country: {cur_country}"
    # dynamic_story = f"Country: {cur_country} / Role: {cur_role}"
    # dynamic_story = f"Language: {cur_language} / Role: {cur_role}"
    # dynamic_story = f"Role: {cur_role}"
    if manual:
        bug_id = (f"Bid:{us}{num_tc}-{cur_language}.{cur_country}.{cur_role}-{os_name}.{browser_name}"
                  f"-M{"N" if new_layout else "O"}")
    else:
        bug_id = f"Bid:{us}!{num_tc}-{cur_language}.{cur_country}.{cur_role}"

    allure.dynamic.epic(dynamic_epic)
    allure.dynamic.feature(dynamic_feature)
    allure.dynamic.story(dynamic_story)
    allure.dynamic.title(f"TC_{us}!{num_tc} | Country: {cur_country}, Language: {cur_language}. Bid: {bug_id}")

    del dynamic_story
    del dynamic_feature
    del dynamic_epic
    del cur_language

    return bug_id


def build_dynamic_arg_v3(d, worker_id, cur_language, cur_country, cur_role,
                         us, desc_feature, num_tc, desc_story):
    """
    function for dynamic bild names pf epic, feature and story
    """
    global count

    # tc = f"TC_{us}_{num_tc}"
    print(d.get_window_size())
    # print(f"\n{datetime.now()}   browser = {d.name}")
    print(f"\n{datetime.now()}   worker_id = {worker_id}")
    # print(f"\n{datetime.now()}   Start {tc}")
    print(f"\n{datetime.now()}   0. Allure grouping v3")

    language = cur_language
    if cur_language == "":
        language = "en"
    dynamic_epic = f"Language: {language} / US_{us} | {desc_feature}"
    dynamic_feature = f"Country: {cur_country} / Role: {cur_role} / TS_{us} | {desc_feature}"
    dynamic_story = f"TC_{us}{num_tc} | {desc_story}"

    allure.dynamic.epic(dynamic_epic)
    allure.dynamic.feature(dynamic_feature)
    allure.dynamic.story(dynamic_story)
    allure.dynamic.title(f"TC_{us}{num_tc} with parameters: {language}, {cur_country}, {cur_role}")
    del dynamic_story
    del dynamic_feature
    del dynamic_epic
    del language
    # del tc


def build_dynamic_arg_v2(obj, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                         us, desc_feature, num_tc, desc_story):
    """
    function for dynamic bild names pf epic, feature and story
    """
    global count

    tc = f"TC_{us}_{num_tc}"
    print(d.get_window_size())
    print(f"\n{datetime.now()}   browser = {d.name}")
    print(f"\n{datetime.now()}   worker_id = {worker_id}")
    print(f"\n{datetime.now()}   Start {tc}")
    print(f"\n{datetime.now()}   {obj}.{obj.page_conditions}")
    print(f"\n{datetime.now()}   0. Arrange")

    language = cur_language
    if cur_language == "":
        language = "en"
    dynamic_epic = f"Language: {language} / US_{us} | {desc_feature}"
    dynamic_feature = f"Country: {cur_country} / Role: {cur_role} / TS_{us} | {desc_feature}"
    dynamic_story = f"TC_{us}_{num_tc} | {desc_story}"

    allure.dynamic.epic(dynamic_epic)
    allure.dynamic.feature(dynamic_feature)
    allure.dynamic.story(dynamic_story)
    allure.dynamic.title(f"TC_{us}_{num_tc} with parameters: {language}, {cur_country}, {cur_role}")
    del dynamic_story
    del dynamic_feature
    del dynamic_epic
    del language
    del tc

    if prob_run_tc != "":
        pytest.skip(f"{prob_run_tc}")
