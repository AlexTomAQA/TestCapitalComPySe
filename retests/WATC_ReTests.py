"""
-*- coding: utf-8 -*-
@Time    : 18/12/2023
@Author  : Mike Taran
"""

from datetime import datetime
import os
import subprocess
import re
from tkinter import messagebox
from retests.GoogleSheets.googlesheets import GoogleSheet
from retests.retest_data.us_data import us_data

global test_id, retest_date, browser_name, path, num_test, lang, country, role, url


def pre_test(values):
    global test_id, retest_date, browser_name, path, num_test, lang, country, role, url

    # аргументы командной строки
    for row in values:
        test_id = row[0]
        retest_date = row[1]
        browser_name = row[6]
        path = us_data[row[7]]
        num_test = row[8]
        lang = '' if row[9] == 'en' else row[9]
        country = row[10]
        role = row[12]
        url = row[13]


def get_gs_data(num_row):
    # получение данных из Google Sheets
    gs = GoogleSheet()
    values = gs.getRangeValues(num_row)
    return values


def run_pytest():
    retest = True
    host = "\\".join(os.getcwd().split('\\')[:-1]) + '\\'
    command = (f"poetry run pytest"
               f" --retest={retest}"
               f" --browser_name={browser_name}"
               f" --lang={lang}"
               f" --country={country}"
               f" --role={role}"
               f" --tpi_link={url}"
               f" -m test_{num_test}"
               # f" --json-report --json-report-omit keywords streams"
               f" --no-summary -v"
               f" {host}{path}")

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout, stderr


def main():
    show_warning()

    num_row = 4
    gs = GoogleSheet()

    # старт ретеста
    start_retest_date = datetime.now().strftime("%d/%m/%Y")
    start_time = datetime.now().strftime("%H:%M:%S")
    gs_out = [["'=====> Bugs Report !!! Идет Retest <====="]]
    gs.putRangeValues('A1', gs_out)
    # gs.putRangeValues('AA2:AA3', [[start_retest_date], [start_time]])

    while True:
        # проверка данных ретеста
        values = get_gs_data(num_row)

        # pre-test
        pre_test(values)
        # if num_row != 4:
        #    if retest_date != old_date:
        if not retest_date:
            break
        # Запуск pytest с параметрами
        output, error = run_pytest()

        # проверка результатов тестирования
        gs_out = check_results(output, error)
        # заполнение Google Sheets

        gs.updateRangeValues(num_row, gs_out)
        # old_date = retest_date
        num_row += 1

    # стоп ретеста
    end_time = datetime.now()
    start_test_row = 'A1'
    gs_out = [['Bugs Report']]
    gs.putRangeValues(start_test_row, gs_out)


def check_results(output, error):
    # Проверка наличия ошибок при выполнении команды
    test_results = ""
    gs_out = [[]]
    if error:
        print(f"Ошибка: {error.decode('utf-8')}")
    else:
        test_results = output.decode('utf-8')
        print(f'\n{datetime.now()} {test_id}: {path}:{num_test} ({browser_name}-{lang}-{country}-{role})')

    # Проверка пройденных тестов
    passed_match = re.search(r"(\d+ passed)", test_results)
    if passed_match:
        passed = passed_match.group(1)
        print(f"Пройдено тестов: {passed}")
        gs_out = [['passed']]
    else:
        print("Пройденные тесты не найдены.")

    # Проверка не пройденных тестов
    failed_match = re.search(r"(\d+ failed)", test_results)
    if failed_match:
        failed = failed_match.group(1)
        print(f"Не пройдено тестов: {failed}")
        gs_out = [['failed']]
    else:
        print("Не пройденные тесты не найдены.")

    # Проверка пропущенных тестов
    skipped_match = re.search(r"(\d+ skipped)", test_results)
    if skipped_match:
        skipped = skipped_match.group(1)
        print(f"Пропущено тестов: {skipped}")
        gs_out = [['skipped']]
    else:
        print("Пропущенные тесты не найдены.")

    return gs_out


# Функция для вывода окна предупреждения
def show_warning():
    answer = messagebox.askyesno("Alert!!!", "В файле `conftest.py` должна быть выбрана только одна роль. "
                                             "Хотите продолжить?")
    if answer:
        print("Вы выбрали 'Да'")
    else:
        print("Вы выбрали 'Нет'")
        exit()


if __name__ == '__main__':
    main()
