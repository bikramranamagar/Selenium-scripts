import requests
import json


api = "https://reqres.in/api/users"

authorization_token = "token ....any _token"

def post_request():
    url = api + "/users/"
    headers = {"Authorization": authorization_token}
    data = [{
        "name":"john", "job":"QA tester","email":"jonn@email.com"},
            {"name": "Alice", "job": "Developer", "email": "alice@email.com"},
        {"name": "Bob", "job": "Designer", "email": "bob@email.com"}
    ]
    response = requests.post(url,json=data, headers=headers)
    assert response.status_code==201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    user_id = json_data("id")
    print("The new  users posted  for the api are:",json_str)
    print("-----------------------------------")
    print("the id for new user is:",user_id)
    
    
    
# def get_request():
#     url = api
#     headers = {"Authorization": authorization_token}
#     response = requests.get(url, headers=headers)
#     assert response.status_code==200
#     json_data = response.json()
#     json_str = json.dumps(json_data, indent=4)
#     print("The returned users for the api are:",json_str)
#     print("-----------------------------------")


post_request()
# get_request()