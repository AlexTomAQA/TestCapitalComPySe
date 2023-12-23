"""
-*- coding: utf-8 -*-
@Time    : 18/12/2023
@Author  : Mike Taran
"""

from datetime import datetime
import os
import subprocess
import re

from tests.ReTests.GoogleSheets.googlesheets import GoogleSheet
from tests.ReTests.retest_data import us_data

global test_id, retest_date, browser_name, path, num_test, lang, country, role, url


def pretest(row):
    global test_id, retest_date, browser_name, path, num_test, lang, country, role, url

    # аргументы командной строки
    try:
        test_id = row[0]
        browser_name = row[2]
        path = us_data.us_data[row[3]]
        num_test = row[4]
        lang = '' if row[5] == 'en' else row[5]
        country = row[6]
        role = row[8]
        url = row[9]
        # num_bug = row[12]
    except KeyError:
        print("Не корректные входные данные из таблицы WATC_BugsReport")


def get_gs_data(end_row):
    # получение данных из Google Sheets
    gs = GoogleSheet()
    values = gs.getRangeValues(end_row)
    if not values:
        print('Не данных в таблице!')
        exit()
    return values


def run_pytest():
    retest = True
    # получение корня проекта
    host = "\\".join(os.getcwd().split('\\')[:-2]) + '\\'
    # формирование командной строки и запуск pytest, как subprocess
    command = (f"poetry run pytest"
               f" --retest={retest}"
               f" --browser_name={browser_name}"
               f" --lang={lang}"
               f" --country={country}"
               f" --role={role}"
               f" --tpi_link={url}"
               f" -m test{num_test}"
               # f" --json-report --json-report-omit keywords streams"
               f" --no-summary -v"
               f" {host}{path}")

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout, stderr


def check_results(output, error):
    # Проверка наличия ошибок при выполнении
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
        gs_out = ['passed']
    else:
        print("Пройденные тесты не найдены.")

    # Проверка не пройденных тестов
    failed_match = re.search(r"(\d+ failed)", test_results)
    if failed_match:
        failed = failed_match.group(1)
        print(f"Не пройдено тестов: {failed}")
        gs_out = ['failed']
    else:
        print("Не пройденные тесты не найдены.")

    # Проверка пропущенных тестов
    skipped_match = re.search(r"(\d+ skipped)", test_results)
    if skipped_match:
        skipped = skipped_match.group(1)
        print(f"Пропущено тестов: {skipped}")
        gs_out = ['skipped']
    else:
        print("Пропущенные тесты не найдены.")

    return gs_out


class TestReTests:

    def test_retests(self):
        end_row = 1000
        gs = GoogleSheet()
        # проверка и получение данных ретеста
        values = get_gs_data(end_row)

        # добавление нового столбца для результатов ретеста
        gs.add_new_column_after_()

        # старт ретеста
        start_retest_date = [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
        gs_out = ["'=====> Bugs Report !!! Идет Retest <====="]
        gs.updateRangeValues('B1', [gs_out])
        gs.updateRangeValues('V1', [start_retest_date])

        start_row = 4
        gs_out_full = list()
        for row in values:
            print(f"\n\nRow № = {start_row}")
            print(f"Row Value = {row}")
            # проверка на пустую строку
            if not row:
                break

            # pre-test
            print("1. Run pretest")
            pretest(row)

            # Запуск pytest с параметрами
            print("2. Run run_pytest with parameters from row")
            output, error = run_pytest()

            # проверка результатов тестирования
            print("3. Run check_results")
            gs_out = check_results(output, error)

            # заполнение Google Sheets по-строчно
            # ==================
            print("4. Fixing one row check results into Google Sheet Bugs Report")
            result = gs.updateRangeValues(f'V{start_row}', [gs_out])
            print('{0} cells updated.'.format(result.get('totalUpdatedCells')))
            # ==================

            # print("4. Fixing check results in memory")
            # gs_out_full.append(gs_out)

            start_row += 1

        # заполнение Google Sheets сразу весь столбец
        # ==================
        # print("\n5. Update results from memory into Google sheet Bugs Report")
        # result = gs.updateRangeValues('V4', gs_out_full)
        # print('\n{0} cells updated.'.format(result.get('totalUpdatedCells')))
        # ==================

        # окончание ретеста
        end_retest_date = [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
        gs_out = ['Bugs Report']
        gs.updateRangeValues('B1', [gs_out])
        gs.updateRangeValues('V2', [end_retest_date])
        # exit(0)


# if __name__ == '__main__':
#
#     end_row = 1000
#     gs = GoogleSheet()
#
#     # проверка и получение данных ретеста
#     values = get_gs_data(end_row)
#
#     # добавление нового столбца для результатов ретеста
#     gs.add_new_column_after_()
#
#     # старт ретеста
#     start_retest_date = [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
#     gs_out = ["'=====> Bugs Report !!! Идет Retest <====="]
#     gs.updateRangeValues('B1', [gs_out])
#     gs.updateRangeValues('V1', [start_retest_date])
#
#     start_row = 4
#     gs_out_full = list()
#     for row in values:
#         # проверка на пустую строку
#         if not row:
#             break
#
#         # pre-test
#         pre_test(row)
#
#         # Запуск pytest с параметрами
#         output, error = run_pytest()
#
#         # проверка результатов тестирования
#         gs_out = check_results(output, error)
#
#         # заполнение Google Sheets по-строчно
#         # ==================
#         # result = gs.updateRangeValues(f'V{start_row}', [gs_out])
#         # print('{0} cells updated.'.format(result.get('totalUpdatedCells')))
#         # ==================
#         gs_out_full.append(gs_out)
#         start_row += 1
#
#     # заполнение Google Sheets сразу весь столбец
#     # ==================
#     result = gs.updateRangeValues('V4', gs_out_full)
#     print('\n{0} cells updated.'.format(result.get('totalUpdatedCells')))
#     # ==================
#
#     # окончание ретеста
#     end_retest_date = [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
#     gs_out = ['Bugs Report']
#     gs.updateRangeValues('B1', [gs_out])
#     gs.updateRangeValues('V2', [end_retest_date])
#     exit(0)
