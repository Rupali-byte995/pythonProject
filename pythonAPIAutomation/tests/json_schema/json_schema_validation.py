import json
import os

from src.helpers.api_requests_wrapper import post_requests
from src.constants.api_constants import URL, base_url, url_create_booking
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.coomon_verification import verify_response_is_not_none, verify_http_status_code
import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError


class TestCreateBooking_jsonschema(object):
    def load_schema(self,schema_file):
        with open(schema_file,'r') as file:
            return json.load(file)

    @pytest.mark.positive_tc
    def test_create_booking_json_schema(self):
        response = post_requests(url=url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload=payload_create_booking(), in_json=False)
        print(response)
        verify_response_is_not_none(response.json()['bookingid'])
        verify_http_status_code(response, 200)
        print(response.json()['bookingid'])
        print(response.json()["booking"]["firstname"])
        response_json = response.json()
        file=os.getcwd()+"/schema.json"
        schema=self.load_schema(file)

        try:
             validate(instance=response_json, schema=schema)
        except ValidationError as e:
                    print("Error",e.message)
