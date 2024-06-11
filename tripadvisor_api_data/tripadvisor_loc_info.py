import requests
import json
import os

key = '3265045EBF3847FCB2DCB6213C1FE9EB'
BASE_URL = 'https://api.content.tripadvisor.com/api/v1/location'

file_path = os.path.join('tripadvisor_api_data', 'extracted_data.json')
with open(file_path , 'r') as file:
    extracted_data = json.load(file)

for id in extracted_data:
    location_id = id['location_id']
    url = f"{BASE_URL}/{location_id}/details?key={key}"
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        id['web_url'] = data.get('web_url', 'N/A')
        id['category'] = data.get('category', 'N/A')
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        print(response.json())

with open(file_path, 'w') as file:
    json.dump(extracted_data, file, indent=4)