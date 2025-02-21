import requests
import json

api = "https://reqres.in/api/users"

# Replace 'your_actual_token' with your real API token
token = "your_actual_token"
headers = {"Authorization": f"Bearer {token}"}  # Correct header format

def get_requests():
    response = requests.get(api, headers=headers)  # Pass headers
    
    if response.status_code == 200:
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("The returned users for the API are:", json_str)
        print("................")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        print("Response:", response.text)  # Print error details for debugging

get_requests()
