#Common headers
def common_headers_json():
    headers={
        "Content-Type":"application/json"

    }
    return headers
def common_headers_xml():
    headers={
        "Content-Type":"application/xml"
    }
    return headers
 #Read data from excel,csv,json,yaml-keep the fynctions in future
def common_headers_for_put_delete_patch():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM=",
    }
    return headers