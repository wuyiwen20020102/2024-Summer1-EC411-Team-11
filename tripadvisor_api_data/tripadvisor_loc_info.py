import requests

key = '3265045EBF3847FCB2DCB6213C1FE9EB'

BASE_URL = 'https://api.content.tripadvisor.com/api/v1/location'

location_id = '258730'

url = f"{BASE_URL}/{location_id}/details?key={key}"

headers = {
    'X-TripAdvisor-API-Key': key,
    'Content-Type': 'application/json',
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")
    print(response.json())