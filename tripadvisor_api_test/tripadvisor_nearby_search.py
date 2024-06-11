import requests

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
    print(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")
    print(response.json())