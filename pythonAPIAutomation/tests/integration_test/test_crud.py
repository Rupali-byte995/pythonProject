from src.helpers.api_requests_wrapper import post_requests, put_requests, delete_requests
from src.constants.api_constants import URL, base_url, url_create_booking, url_create_token, url_patch_pu_delete_booking
from src.helpers.utils import common_headers_json, common_headers_for_put_delete_patch
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.coomon_verification import verify_response_is_not_none, verify_http_status_code
import pytest


class Test_crud_tc():
    @pytest.fixture()
    def create_token(self):
        response = post_requests(url=url_create_token(self), auth=None, headers=common_headers_json(),
                                 payload=payload_create_token(), in_json=False)
        verify_http_status_code(response, 200)
        token = response.json()['token']
        verify_response_is_not_none(token)
        print(token)
        return token

    @pytest.fixture()
    def create_booking(self):
        response = post_requests(url=url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload=payload_create_booking(), in_json=False)
        print(response)
        verify_response_is_not_none(response.json()['bookingid'])
        verify_http_status_code(response, 200)
        print(response.json()['bookingid'])
        bookingid = response.json()['bookingid']
        return bookingid

    def test_update_booking(self,create_token,create_booking):
            bookingid = create_booking
            put_url=url_create_booking()+"/"+bookingid
            response=put_requests(url=put_url,auth=None,headers=common_headers_for_put_delete_patch(),
                           payload=payload_create_booking(),in_json=False)
            print(response)
            print(create_token)


    def test_delete_booking(self,create_booking):
        bookingid=create_booking
        del_url = url_create_booking() + "/"+str(bookingid)
        response = delete_requests(url=del_url, auth=None, headers=common_headers_for_put_delete_patch(),
                                   in_json=False)
        print(response)
