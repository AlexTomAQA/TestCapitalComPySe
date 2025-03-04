"""
-*- coding: utf-8 -*-
@Time    : 2023/09/09 12:00
@Author  : Alexander Tomelo
"""
import sys
from datetime import datetime
from random import randint

import allure
import pytest
from selenium.webdriver import ActionChains
from src.src import CapitalComPageSrc

from conf import QTY_LINKS
from pages.Header.header_locators import HeaderElementLocators


class Common:
	flag_of_bug = False

	@staticmethod
	def save_current_screenshot(wd, name, type_of_file="PNG"):
		print(f"{datetime.now()}   Save current screenshot into {type_of_file} file")
		allure.attach(wd.get_screenshot_as_png(), name, allure.attachment_type.PNG)

	@staticmethod
	def skip_if_eng_lang_and_fca_license(cur_language, cur_country):
		if cur_country == "gb" and cur_language == "":
			pytest.skip("Current test case not available for the Eng language and FCA license")

	@staticmethod
	def check_language_in_list_and_skip_if_present(cur_language, list_languages):
		if cur_language in list_languages:
			pytest.skip(f"This test is not for '{cur_language}' language")
		return

	@staticmethod
	def check_language_in_list_and_skip_if_not_present(cur_language, list_languages):
		if cur_language not in list_languages:
			pytest.skip(f"This test is not for '{cur_language}' language")
		return

	@staticmethod
	def check_language_and_country_in_list_and_skip_if_not_present(
			cur_language, cur_country, *list_languages_country_args
	):
		flag_language_country = None
		for list_languages_country in list_languages_country_args:
			if cur_language in list_languages_country[0] and cur_country in list_languages_country[1]:
				flag_language_country = True
				break
			else:
				flag_language_country = False
		if not flag_language_country:
			pytest.skip(f"This test is not for couple '{cur_language}' language and '{cur_country}' country")

	@staticmethod
	def check_role_in_list_and_skip_if_present(cur_role, list_role):
		if cur_role not in list_role:
			pytest.skip(f"This test is not for '{cur_role}' role")
		return

	@staticmethod
	def check_country_in_list_and_skip_if_present(cur_country, list_countries):

		if cur_country in list_countries:
			pytest.skip(f"This test is not for '{cur_country}' country")
		return

	@staticmethod
	def check_market_in_list_and_skip_if_present(cur_market, list_markets):
		if cur_market in list_markets:
			pytest.skip(f"This test is not for '{cur_market}' market")
		return

	@staticmethod
	def check_country_in_list_and_skip_if_not_present(cur_country, list_countries):
		if cur_country not in list_countries:
			pytest.skip(f"This test is not for '{cur_country}' country")
		return

	@staticmethod
	def skip_test_for_language(cur_language) -> None:
		pytest.skip(f"This test-case is not for {cur_language} language")

	@staticmethod
	def skip_test_for_country(cur_country):
		pytest.skip(f"This test-case is not for {cur_country} country")

	@staticmethod
	@allure.step('Start Creating file of href method')
	def creating_file_of_hrefs(title_us, list_items, file_name, first_index=1):
		file = None
		list_url_out = list()

		print(f"{datetime.now()}")
		print(f"{datetime.now()}   {title_us} include {len(list_items) - first_index} child items for random select")

		count_in = len(list_items) - first_index  # исключаем первую (родительскую) страницу, если first_index = 1
		count_out = 0
		url_prev = ""
		if count_in > 0:
			for i in range(QTY_LINKS):
				if i < count_in:
					while True:
						k = randint(first_index, count_in - 1)
						item = list_items[k]
						url = item.get_property("href")
						print(f"{datetime.now()}   k = {k} - {url}")
						if url != url_prev and url not in list_url_out:
							break
					list_url_out.append(url)
					url_prev = url
					count_out += 1

		try:
			file = open(file_name, "w")
			print(f"{datetime.now()}   The file of hrefs contains the following URLs:")
			for i in range(len(list_url_out)):
				url = list_url_out[i]
				file.write(url + "\n")
				print(f"{datetime.now()}   {url}")
		finally:
			file.close()
			del file

		print(f"{datetime.now()}   Test data include {count_out} item(s)")
		if count_in != 0:
			print(f"{datetime.now()}   The test coverage = {count_out / count_in * 100} %")
		else:
			print(f"{datetime.now()}   The test coverage = 0 %")

	@staticmethod
	def generate_cur_item_link_parameter(file_name):

		list_item_link = list()
		try:
			# проверка аргументов командной строки
			retest = sys.argv[1].split('=')[1]
		except IndexError:
			retest = False

		if retest == 'True':
			if sys.argv[6].split('=')[0] == "--tpi_link":
				list_item_link.append(sys.argv[6].split('=')[1])
		else:

			try:
				file = open(file_name, "r")
			except FileNotFoundError:
				print(f"{datetime.now()}   There is no file with name {file_name}")
			else:
				for line in file:
					list_item_link.append(line[:-1])
					print(f"{datetime.now()}   {line[:-1]}")
				file.close()

		qty = len(list_item_link)
		if qty == 0:
			msg = "Отсутствуют тестовые данные: нет списка ссылок на страницы"
			print(f"{datetime.now()}   {msg}")
			pytest.exit(msg)
		else:
			print(f"{datetime.now()}   List of hrefs contains {qty} URLs")

		return list_item_link

	@staticmethod
	def browser_back_to_link_and_test_pass(driver, test_link, msg):
		do = True
		while do:
			driver.back()
			print(f"{datetime.now()}   => Driver.backed")
			if driver.current_url == test_link:
				do = False

		Common.flag_of_bug = False
		assert True, msg

	@staticmethod
	def browser_back_to_link_and_test_fail(driver, test_link, msg):
		Common().save_current_screenshot(driver, str(datetime.now()))

		do = True
		while do:
			driver.back()
			print(f"{datetime.now()}   => Driver.backed")
			if driver.current_url == test_link:
				do = False

		Common.flag_of_bug = True
		assert False, msg

	@staticmethod
	def browser_back_to_link(wd, test_link):
		count = 5
		do = True
		while do:
			wd.back()
			print(f"{datetime.now()}   => Driver.back")
			print(f"{datetime.now()}   Current page is: {wd.current_url}")
			count -= 1
			if wd.current_url == test_link or count == 0:
				do = False

	@staticmethod
	def assert_true_false(condition=False, msg=""):
		if condition:
			Common.flag_of_bug = False
			assert True, msg
		else:
			Common.flag_of_bug = True
			assert False, msg

	@staticmethod
	def move_pointer_to_capital_com_label(wd):
		elements = wd.find_elements(*HeaderElementLocators.MAIN_LOGO_CAPITAL_COM)
		if len(elements) == 0:
			elements = wd.find_elements(*HeaderElementLocators.NEW_MAIN_LOGO_CAPITAL_COM)
			if len(elements) == 0:
				elements = wd.find_elements(*HeaderElementLocators.MAIN_LOGO_CAPITAL_COM_SCA)
				if len(elements) == 0:
					msg = "Problem with capital.com logo"
					Common().pytest_fail(f"Bug # ???   {msg}")

		ActionChains(wd) \
			.move_to_element(elements[0]) \
			.perform()
		print(f"{datetime.now()}   => Focus moved to 'capital*com' logo")

	@staticmethod
	def pytest_fail(msg):
		Common.flag_of_bug = True
		pytest.fail(msg)

	@staticmethod
	def pytest_skip(msg):
		Common.flag_of_bug = False
		pytest.skip(msg)

	@staticmethod
	def check_language_and_country_and_define_host(cur_language, cur_country):
		host = None
		if cur_language == "" and cur_country == "gb":
			host = CapitalComPageSrc.URL_NEW
		elif cur_language == "" and cur_country == "au":
			host = CapitalComPageSrc.URL_NEW_EN_AU
		elif cur_language == "" and cur_country == "ae":
			host = CapitalComPageSrc.URL_NEW_EN_AE
		elif cur_language == "ar" and cur_country == "ae":
			host = CapitalComPageSrc.URL_NEW_AR_AE
		else:
			host = CapitalComPageSrc.URL
		return host

	@staticmethod
	def check_language_and_country_and_define_conditions(cur_language, cur_country, conditions, newConditions):
		if cur_language == "" and cur_country in ["gb", "au", "ae"]:
			return newConditions
		elif cur_language == "ar" and cur_country == "ae":
			return newConditions
		else:
			return conditions

	@staticmethod
	def click_link_and_print(wd, name_of_link, link_locator):
		"""
		Example:
			wd - 0bject of Selenium Webdriver
        	name_of_link = "Discover what you can trade"
            locator = (By.CSS_SELECTOR, '[data-type="tiles_w_img_link4_signup"]')
        """
		print(f"{datetime.now()}   Start to click on the link '{name_of_link}'")
		wd.find_element(*link_locator).click()
		print(f"{datetime.now()}   Link '{name_of_link}' is clicked\n")
