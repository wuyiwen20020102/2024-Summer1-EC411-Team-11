import requests
from data_extractor import extract_data
from cal_new_coord import calculate_new_coords

def fetch_restaurant(key, latitude, longitude,):

    BASE_URL = "https://api.content.tripadvisor.com/api/v1/location/"
    radius = 5
    radiusUnit = 'km'
    category = 'restaurants'
    language = 'en'

    coords = calculate_new_coords(latitude, longitude, radius)

    headers = {
        "accept": "application/json"
        }

    restaurants = []
    location_ids = set()

    for coord in coords:
        lat, lon = coord
        url = f"{BASE_URL}nearby_search?latLong={lat}%2C{lon}&key={key}&category={category}&radius={radius}&radiusUnit={radiusUnit}&language={language}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            new_restaurants = extract_data(data)
            for restaurant in new_restaurants:
                if restaurant['location_id'] not in location_ids:
                    location_ids.add(restaurant['location_id'])
                    restaurants.append(restaurant)
                    if len(restaurants) >= 50:
                        break
        else:
            print(f"Failed to retrieve data for coord ({lat},{lon}): {response.status_code}")
            print(response.json())

        if len(restaurants) >= 50:
            break

    return restaurants[:50]
