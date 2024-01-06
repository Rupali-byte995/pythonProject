#HTTP status verification
def verify_http_status_code(response_data,expect_data):
    assert response_data.status_code==expect_data,"Expected status code is "+expect_data

def verify_json_key_for_not_null(key):
    assert key!=0,"Key is non empty"+key
    assert key>0,"key is greater than zero "
#Common Verification
#HTTP status code
#Headers
#Data Verification
#JSON Scehema
def verify_response_is_not_none(key):
    assert key is not None
def verify_response_time():
    pass
