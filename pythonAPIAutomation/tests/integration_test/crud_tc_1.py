from src.constants.api_constants import URL,base_url,APIConstants
def test_urlprint():
    print("URL",URL)
    class_url=base_url()
    print(class_url)
    print(APIConstants.base_url())