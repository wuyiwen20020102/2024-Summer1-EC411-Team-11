import json 
import os
from tripadvisor_nearby_search import  fetch_restaurant
from tripadvisor_loc_info import fetch_restaurant_details

def main():
    key = '3265045EBF3847FCB2DCB6213C1FE9EB'
    latitude = 42.3455
    longitude = -71.10767

    restaurants = fetch_restaurant(key, latitude, longitude)
    file_path = os.path.join('tripadvisor_api_data', 'extracted_data.json')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w') as file:
        json.dump(restaurants, file, indent=4)
    
    with open(file_path, 'r') as file:
        extracted_data = json.load(file)
    
    updated_data = fetch_restaurant_details(key, extracted_data)
    
    with open(file_path, 'w') as file:
        json.dump(updated_data, file, indent=4)

if __name__ == "__main__":
    main()