import requests
import json

api = "https://reqres.in/api"

authorization_token = "token token _values"
headers = {"Authorization": authorization_token}
data={
    "name":"john",
    "job":"QA tester"
}

def put_request(user_id):
    url = api + "/users/(user_id)"
    response = requests.put(url,json=data, headers=headers)
    assert response.status_code==200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("The returned users for the api are:",json_str)
    print("-----------------------------------")


put_request(1)
