import platform
from datetime import datetime
from tests.ReTestsAuto.GoogleSheets.googlesheets import GoogleSheet


def check_gs_table(bid, bug_n, manual=False):
    spreadsheet_id = GoogleSheet.SPREADSHEET_ID2 if manual else GoogleSheet.SPREADSHEET_ID1
    gs = GoogleSheet(spreadsheet_id)
    gs.wait_while_bugs_report_busy()
    gs_out = ["Busy"]
    gs.update_range_values('B1', [gs_out])

    # старт проверки
    bug_present = False
    # для таблицы мануальных багов
    if manual:
        start_update_date = [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
        gs.update_range_values('V1', [start_update_date])

    values = gs.get_all_row_values()
    for index, row in enumerate(values):
        if row:
            if bid in row[0]:
                if bug_n in row[-6]:
                    if manual:      # для таблицы мануальных багов
                        if bug_n == '00':
                            gs.update_range_values(f'V{5 + index}', [['passed']])
                        else:
                            gs.update_range_values(f'V{5 + index}', [['failed']])
                    else:
                        pass
                else:
                    bug_num = [["'" + bug_n]]
                    gs.update_range_values(f'P{5 + index}', bug_num)
                    print(f"\n{datetime.now()}   Баг {bid} уже существует, "
                          f"но у него изменился тип с {row[-6]} на {bug_n}")
                    if manual:      # для таблицы мануальных багов
                        if bug_n == '00':
                            gs.update_range_values(f'V{5 + index}', [['passed']])
                        else:
                            gs.update_range_values(f'V{5 + index}', [['failed']])
                bug_present = True
                break
            # else:
            #     break

    gs_out = ["Bugs Report"]
    gs.update_range_values('B1', [gs_out])
    return bug_present


def new_row_data(d, bid, bug_num, link, manual=False):
    # bid = "Bid:11.01.01.00_01-de.ae.NoReg" or
    # bid = "Bid:11.01.01.01_02-ru.au.NoAuth" or
    # bid = "Bid:01.05.00_01-nl.au.NoReg" or
    # bid = "Bid:01.05.01_04-nl.cn.Auth"
    us = bid.split(':')[1].split('-')[0].split('_')[0]
    tc = '_' + bid.split(':')[1].split('-')[0].split('_')[1]
    lng = bid.split(':')[1].split('-')[1].split('.')[0]
    ctr = bid.split(':')[1].split('-')[1].split('.')[1]
    rol = bid.split(':')[1].split('-')[1].split('.')[2]
    if us.split('.')[-1] == '00':
        link = ""
    new_bug_data_1 = [[bid, 'Ubuntu 22.04', 'Chrome', us, tc, lng, ctr]]
    new_bug_data_2 = [[rol, link]]

    if manual:
        # название OS и браузера
        platform_v = platform.platform()
        os_name = platform_v.split("-")[0][0] + platform_v.split("-")[1]
        cur_br = d.capabilities['browserName'].lower()
        browser_mapping = {'microsoftedge': 'E', 'chrome': 'C', 'firefox': 'F', 'safari': 'S'}
        browser_name = browser_mapping.get(cur_br, 'Unknown')
        if browser_name == 'Unknown':
            print(f"Unsupported browser: {browser_name}")
        new_bug_data_1 = [[bid, os_name, browser_name, us, tc, lng, ctr]]

    return new_bug_data_1, new_bug_data_2


def add_new_row_with_format(manual=False):
    spreadsheet_id = GoogleSheet.SPREADSHEET_ID2 if manual else GoogleSheet.SPREADSHEET_ID1
    gs = GoogleSheet(spreadsheet_id)

    start_update_date = [datetime.now().strftime("%d/%m/%y")]
    # добавление новой 4-й строки
    gs.add_new_row_before_()
    # копирование данных из предыдущей строки
    gs.new_data_copy_past(5, 6, 4, 5,
                          0, 17, 0, 17)
    # gs.clear_values_new_row()
    gs.update_range_values('U5', [start_update_date])


def fill_gs_table(value_1, value_2, bug_num, manual=False, new_layout=False):
    spreadsheet_id = GoogleSheet.SPREADSHEET_ID2 if manual else GoogleSheet.SPREADSHEET_ID1
    gs = GoogleSheet(spreadsheet_id)
    gs.update_range_values('A5', value_1)
    gs.update_range_values('I5', value_2)
    gs.update_range_values('P5', [[bug_num]])
    if manual:  # для таблицы мануальных багов
        if bug_num == "'00":
            gs.update_range_values('V5', [['passed']])
        else:
            gs.update_range_values('V5', [['failed']])

        if new_layout:  # для таблицы мануальных багов
            gs.update_range_values('K5', [['N']])
        else:
            gs.update_range_values('K5', [['O']])

        finish_date = [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
        gs.update_range_values('V2', [finish_date])


def retest_table_fill(d="", bid="", bug_n="", link="", manual=False, new_layout=False):
    # ========= не удалять ======================
    # bid = "Bid:11.02.02.01_07-en.de.Auth"
    # bug_n = "05"
    # link = 'https://capital.com/pl/handlovac-amd'
    # ===========================================
    """
    Метод для заполнения таблицы багов для авто и мануал ретеста
    Args:
        d - веб-драйвер
        bid - bug-ID
        bug_n - номер бага
        link - trade instrument
        manual - для мануальных багов
        new_layout - для нового дизайна веб-страницы

    """

    print(f"\n{datetime.now()}   Проверка бага в таблице ретеста  =>")
    spreadsheet_id = GoogleSheet.SPREADSHEET_ID2 if manual else GoogleSheet.SPREADSHEET_ID1
    gs = GoogleSheet(spreadsheet_id)
    print(f'\n gs = GoogleSheet() - создаем объект gs # 1: {gs}')

    if bid != "":
        bug_num = "'" + bug_n

        # проверка таблицы багов на наличии в ней текущего
        bug_present = check_gs_table(bid, bug_n, manual)
        if not bug_present:
            # формирование данных для заполнения
            new_bug_data_1, new_bug_data_2 = new_row_data(d, bid, bug_num, link, manual)

            gs.wait_while_bugs_report_busy()
            gs_out = ["Busy"]
            gs.update_range_values('B1', [gs_out])

            # добавление новой строки с копипастом формул и форматов
            add_new_row_with_format(manual)
            # заполнение таблицы
            fill_gs_table(new_bug_data_1, new_bug_data_2, bug_num, manual, new_layout)

            gs_out = ['Bugs Report']
            gs.update_range_values('B1', [gs_out])

            print(f"\n{datetime.now()}   Баг {bid}-{bug_n} добавлен в таблицу 'Bugs Report Auto detect' (для ретестов)")
        else:
            print(f"\n{datetime.now()}   Баг {bid}-{bug_n} обнаружен ранее и уже находится в 'Bugs Report Auto "
                  f"detect'")
    else:
        print(f"\n{datetime.now()}  Для бага: Bid-{bug_n} необходимо использовать проверку на ретест!!!")


# # ========= не удалять ======================
# if __name__ == "__main__":
#     retest_table_fill()
