import requests
import json

api = "https://reqres.in/api/users"

authorization_token = "token ....any _token"

def get_request():
    url = api 
    headers = {"Authorization": authorization_token}
    response = requests.get(url, headers=headers)
    assert response.status_code==200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("The returned users for the api are:",json_str)
    print("-----------------------------------")


get_request()
