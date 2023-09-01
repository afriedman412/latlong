
from geopy.geocoders import Nominatim
from time import sleep

gl = Nominatim(user_agent="my_geocoder")

def process_one_location(location_query):
    location = gl.geocode(location_query)
    return location

def process_locations(locations):
    processed_locations = []
    for n, location in enumerate(locations):
        processed_locations.append(process_one_location(location))
        if n and not n % 3:
            sleep(1)
    return processed_locations