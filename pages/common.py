"""
-*- coding: utf-8 -*-
@Time    : 2023/09/09 12:00
@Author  : Alexander Tomelo
"""
from datetime import datetime
from random import randint
import pytest
from conf import QTY_LINKS


class Common:

	def check_language_in_list_and_skip_if_present(self, cur_language, list_languages):
		if cur_language in list_languages:
			pytest.skip(f"This test is not for '{cur_language}' language")
		return

	def check_language_in_list_and_skip_if_not_present(self, cur_language, list_languages):
		if cur_language not in list_languages:
			pytest.skip(f"This test is not for '{cur_language}' language")
		return

	def check_country_in_list_and_skip_if_present(self, cur_country, list_countries):
		if cur_country in list_countries:
			pytest.skip(f"This test is not for '{cur_country}' country")
		return

	def check_country_in_list_and_skip_if_not_present(self, cur_country, list_countries):
		if cur_country not in list_countries:
			pytest.skip(f"This test is not for '{cur_country}' country")
		return

	def skip_test_for_language(self, cur_language) -> None:
		pytest.skip(f"This test-case is not for {cur_language} language")

	def skip_test_for_country(self, cur_country):
		pytest.skip(f"This test-case is not for {cur_country} country")

	def creating_file_of_hrefs(self, list_items, file_name):
		file = None
		list_url_out = list()
		count_in = len(list_items) - 1  # иссключаем первую (родительскую) страницу в списке
		count_out = 0
		url_prev = ""
		if count_in > 0:
			for i in range(QTY_LINKS):
				if i < count_in:
					while True:
						k = randint(1, count_in)
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
