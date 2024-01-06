# read the CSV/Excel file
# Create the function create token which can take values from the excel file
# verify the expected result
# Steps
# read the Excel file - for this u need to the library openpyxl

import pytest
import requests
import openpyxl
from src.constants.api_constants import url_create_token
from src.helpers.utils import common_headers_json


def read_credentials_from_excel(filepath):
    credentials = []
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})#list of dictionary
    return credentials


def make_request_auth(username, password):
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post(url=url_create_token(), headers=common_headers_json(), json=payload)

    return response

@pytest.mark.parametrize("user_cred", read_credentials_from_excel("test_dat_ddt.xlsx"))
def test_post_create_token(user_cred):
    # make_request_auth-> Run this function-> Row that we have in Excel

        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        response = make_request_auth(username, password)
        print(response)
        assert response.status_code==200