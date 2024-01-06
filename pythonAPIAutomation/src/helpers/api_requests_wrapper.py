# To make the POST,PUT,PATCH,DELETE, GET
import json

import requests


# HTTP Methods-generic Functions
def get_requests(url, auth, in_json):
    response = requests.get(url=url, auth=auth)
    if in_json in True:
        return response.json()
    return response


# data=get_request("https://restfulbooker.com/booking/1",injson=False)
# data-> returns in json format else if in_json=false then it
def post_requests(url, auth, headers, payload, in_json):
    post_response = requests.post(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json == True:
        return post_response.json()
    return post_response

#patch request
def patch_requests(url, auth, headers, payload, in_json):
    patch_response = requests.patch(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json == True:
        return patch_response.json()
    return patch_response
#put request
def put_requests(url, auth, headers, payload, in_json):
    put_response = requests.put(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json == True:
        return put_response.json()
    return put_response
#Delete request
def delete_requests(url, auth, headers, in_json):
    delete_response = requests.delete(url=url, headers=headers, auth=auth)
    if in_json == True:
        return delete_response.json()
    return delete_response