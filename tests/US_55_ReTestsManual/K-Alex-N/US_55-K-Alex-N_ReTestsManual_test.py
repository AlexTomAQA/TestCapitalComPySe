"""
-*- coding: utf-8 -*-
@Date    : 18/10/2024
@Author  : Alexey Kurochkin
"""

import time
from datetime import datetime
import random

import pytest
import allure

from pages.common import Common
from pages.conditions_v2 import apply_preconditions_to_link
from pages.build_dynamic_arg import build_dynamic_arg_for_us_55


from pages.BugsManual.bug_272 import Bug272

from pages.Elements.HeaderSearchField import SearchField
from pages.Signup_login.signup_login import SignupLogin
from pages.Elements.HeaderLoginButton import HeaderButtonLogin
from pages.Elements.Alert import Alert
from pages.Menu.menu import MenuSection
from src.src import CapitalComPageSrc

@pytest.mark.us_55
class TestManualDetectedBugs:
    page_conditions = None

