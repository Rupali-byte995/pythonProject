from  src.helpers.api_requests_wrapper import post_requests
from src.constants.api_constants import URL,base_url,url_create_booking
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.coomon_verification import verify_response_is_not_none,verify_http_status_code
import pytest
class TestCreateBooking(object):
    @pytest.mark.positive_tc
    def test_create_booking_tc1(self):
        response=post_requests(url=url_create_booking(),auth=None,headers=common_headers_json(),payload=payload_create_booking(),in_json=False)
        print(response)
        verify_response_is_not_none(response.json()['bookingid'])
        verify_http_status_code(response,200)
        print(response.json()['bookingid'])
        print(response.json()["booking"]["firstname"])
    @pytest.mark.negative_tc
    def test_create_booking_tc2(self):
        response = post_requests(url=url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload={}, in_json=False)

        verify_http_status_code(response, 500)
