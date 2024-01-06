# Create token
import requests
import pytest


def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    header = {"Content-Type": "application/json"}
    json_payload = {"username": "admin",
                    "password": "password123"}
    response = requests.post(url=url, headers=header, json=json_payload)
    # extracting value of token
    data = response.json()
    token_value = data['token']
    print(token_value)
    return token_value


def create_booking():
    URL = "https://restful-booker.herokuapp.com/booking"
    header = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Jason",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=header, json=json_payload)
    data = response.json()
    bookingid = data['bookingid']
    return bookingid


def test_put_request():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    put_url = URL + str(booking_id)
    cookie_value = "token=" + create_token()
    header = {"Content-Ty0pe": "application/json", "Cookie": cookie_value}
    json_payload = {
        "firstname": "Pramod",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=put_url, headers=header, json=json_payload)
    # Assertions
    assert response.status_code == 200, "Invalid update"


# Deleting the   request
def test_delete_booking():
    URL = "https://restful-booker.herokuapp.com/booking/"
    bookingid = create_booking()

    put_url = URL + str(bookingid)
    cookie_value = "token=" + create_token()
    header = {"Content-Type": "application/json", "Cookie": cookie_value}
    response = requests.delete(url=put_url, headers=header)
    assert response.status_code == 201
