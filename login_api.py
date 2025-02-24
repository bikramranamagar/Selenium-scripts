import requests
import json

api = "https://reqres.in/api/login"

def post_request():
    url = api
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    
    response = requests.post(url, json=data)

    if response.status_code == 200:
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("The user logged in successfully:", json_str)
        print("-----------------------------------")

post_request()
