from math import radians, cos, sin, asin, sqrt

def calculate_new_coords(lat, lon, radius, num_points=8):
    coords = []
    coords.append((lat, lon))
    for i in range(num_points-1):
        angle = 2 * 3.14159 * i / num_points
        delta_lat = radius * cos(angle) / 110.574 
        delta_lon = radius * sin(angle) / (111.320 * cos(radians(lat)))
        new_lat = lat + delta_lat
        new_lon = lon + delta_lon
        coords.append((new_lat, new_lon))
    return coords