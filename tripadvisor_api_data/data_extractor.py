def extract_data(original_data):
    extracted_data = []
    for location in original_data['data']:
        extracted_data.append({
            'location_id' : location['location_id'],
            'name' : location['name'],
            'address_string' : location['address_obj']['address_string']
        })
    return extracted_data
