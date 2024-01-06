from dotenv import load_dotenv
import os
def test_auth():
    load_dotenv('.env')
    user=os.getenv("user")
    pwd=os.getenv("PASSWORD")

    print(user)
    print(pwd)