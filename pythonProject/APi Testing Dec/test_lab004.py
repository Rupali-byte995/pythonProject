import pytest
import requests


# create post request
@pytest.mark.positive
def test_postivetc():


    url = "https://restful-booker.herokuapp.com/booking"
    header = {"Content-Type": "application/json"}
    json_payload = {
    "firstname" : "Pillu",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response = requests.post(url,headers=header,json=json_payload)
# Assertions to check status code is 200
    data=response.json()
    assert data['booking']['firstname']=="Pillu","Incorrect response"

def test_negativetc():
    url = "https://restful-booker.herokuapp.com/booking"
    header = {"Content-Type": "application/json"}
    json_payload ={}
    response = requests.post(url, header,json=json_payload)
#Assertions

    assert response.status_code==500
