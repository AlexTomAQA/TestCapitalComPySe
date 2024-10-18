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

from pages.BugsManual.bug_052 import CommoditiesPageOpenCheck
from pages.BugsManual.bug_076 import ProfessionalAccountPage
from pages.BugsManual.bug_085 import TradingGuidesPageDeTest
from pages.BugsManual.bug_158 import NewsAndAnalysisMenuSection
from pages.BugsManual.bug_272 import Bug272
from pages.BugsManual.bug_273 import Bug273
from pages.BugsManual.bug_288 import Bug288
from pages.BugsManual.bug_299 import CheckLoginFacebookModal
from pages.BugsManual.bug_305 import Bug305
from pages.BugsManual.bug_307 import Bug307
from pages.BugsManual.bug_330 import Bug330
from pages.BugsManual.bug_332 import Bug332
from pages.BugsManual.bug_335 import Bug335
from pages.BugsManual.bug_359 import Bug359
from pages.BugsManual.bug_364 import Bug364
from pages.BugsManual.bug_366 import Bug366
from pages.BugsManual.bug_372 import Bug372
from pages.BugsManual.bug_373 import Bug373
from pages.BugsManual.bug_378 import Bug378
from pages.BugsManual.bug_392 import Bug392
from pages.BugsManual.bug_416 import Bug416
from pages.Elements.HeaderSearchField import SearchField
from pages.Signup_login.signup_login import SignupLogin
from pages.Elements.HeaderLoginButton import HeaderButtonLogin
from pages.Elements.Alert import Alert
from pages.Menu.menu import MenuSection
from src.src import CapitalComPageSrc



