import requests
import json 
from data_extractor import extract_data

key = '3265045EBF3847FCB2DCB6213C1FE9EB'

BASE_URL = "https://api.content.tripadvisor.com/api/v1/location/"

latitude = 42.3455
longitude = -71.10767
category = 'restaurants'
language = 'en'

url = f"{BASE_URL}nearby_search?latLong={latitude}%2C{longitude}&key={key}&{category}&{language}"

headers = {
    "accept": "application/json"
    }

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    extracted_data = extract_data(data)
    with open('extracted_restaurant_data.json', 'w') as file:
        json.dump(extracted_data, file, indent=4)
else:
    print(f"Failed to retrieve data: {response.status_code}")
    print(response.json())