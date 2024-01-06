import pytest
import requests
def test_sample1():
    assert 5==5
def test_sample2():
    assert 6==4
def test_sample3():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/1")
    assert response_body.status_code == 200  # if sc!200 then error else no error
    data = response_body.json()
    # Assertions to check keys
    assert 'firstname' in data, "First name is present"
    assert 'lastname' in data, 'Last name is present'

    # Assertions to check values(data)
    assert data['firstname'] == 'Sally', 'Correct infoinfo'
    assert data['bookingdates']['checkin'] == '2020-06-26', 'Correct infoinfo'
