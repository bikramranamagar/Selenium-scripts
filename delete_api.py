import requests
import json

api = "https://reqres.in/api/user/2"

authorization_token = "token token _values"
headers = {"Authorization": authorization_token}

def delete_request():
    url = api
    response = requests.delete(url, headers=headers)
    assert response.status_code==204
    print("The delete users is:")
    print("-----------------------------------")


delete_request()
