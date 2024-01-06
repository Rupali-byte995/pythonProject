# API  requests
import requests


# make get,patch,put,delete and put request and verify http methods

def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/1")
    print(response_body.text)
    print(response_body.status_code)
    print(response_body.json())
    if (response_body.status_code == 200):
        print("get request sucessful")


if __name__ == "__main__":
    main()
