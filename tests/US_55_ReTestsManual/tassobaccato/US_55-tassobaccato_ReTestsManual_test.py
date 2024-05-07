"""
-*- coding: utf-8 -*-
@Time    : 2024/05/06 22:00
@Author  : ???
"""
import pytest
import allure
from tests.build_dynamic_arg import build_dynamic_arg_v4


@pytest.mark.us_55
class TestManualDetectedBugs:

    @allure.step("Start test of ???")
    @pytest.mark.test_010
    def test_010(self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        # """
        # Check: Button [1. Create your account] in block [Steps trading]
        # Language: All. License: All.
        # """
        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "55", "ReTest Manual Detected Bugs]",
            ".005", "??? Description Bug")
        pytest.skip("Autotest under construction")
