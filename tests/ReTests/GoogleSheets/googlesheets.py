"""
-*- coding: utf-8 -*-
@Time    : 18/12/2023
@Author  : Mike Taran
"""

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleSheet:
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    RANGE_NAME = "BugsReport!A4:P4"
    # If modifying these scopes, delete the file token.json.
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    # The ID and range of a spreadsheet.
    SPREADSHEET_ID = "1jG0hdjrUdjMFBYHXyBKRGbBwV0ICxfBPaBkgB98Nuuk"
    SHEET_NAME = 'BugsReport'
    SHEET_ID = '540090404'
    service = None

    def __init__(self):
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", self.SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print('flow')
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", self.SCOPES
                )
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        try:
            self.service = build("sheets", "v4", credentials=creds)
        except HttpError as err:
            print(err)

    # Этот будет принимать имя листа и идентификатор таблицы, затем находить и возвращать
    # идентификатор листа по его имени.
    def get_sheet_id(self, sheet_name, spreadsheet_id):
        sheet_metadata = self.service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
        sheets = sheet_metadata.get('sheets', '')
        for sheet in sheets:
            if sheet['properties']['title'] == sheet_name:
                return sheet['properties']['sheetId']
        return None  # Если лист не найден

    def getRangeValues(self, end_row=4):
        RANGE_NAME = f"{self.SHEET_NAME}!A4:P{end_row}"
        # Call the Sheets API
        sheet = self.service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=self.SPREADSHEET_ID, range=RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        return values

    def updateRangeValues(self, cell='V4', values=""):
        RANGE_NAME = f'{self.SHEET_NAME}!{cell}'
        data = [{
            'range': RANGE_NAME,
            'values': values
        }]
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }
        result = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.SPREADSHEET_ID,
                                                                  body=body).execute()
        return result

    def add_new_column_after_(self, index_of_col=21):
        print("Добавление нового столбца")
        if index_of_col is not None:
            request_body = {
                'requests': [{
                    'insertDimension': {
                        'range': {
                            'sheetId': self.SHEET_ID,
                            'dimension': 'COLUMNS',
                            'startIndex': index_of_col,
                            'endIndex': index_of_col + 1  # Вставляем сразу после столбца 'R'
                        }
                    }
                }]
            }
            self.service.spreadsheets().batchUpdate(spreadsheetId=self.SPREADSHEET_ID,
                                                    body=request_body).execute()

        else:
            print(f"Столбец {index_of_col} не найден в таблице.")
