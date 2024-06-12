import requests

def fetch_restaurant_details(key, extracted_data):
    BASE_URL = 'https://api.content.tripadvisor.com/api/v1/location'

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

    return extracted_data