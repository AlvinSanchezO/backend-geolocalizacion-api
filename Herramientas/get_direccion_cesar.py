from geopy.geocoders import Nominatim


def get_direccion_cesarcore(lat: str, lon: str):
    geolocator = Nominatim(user_agent="cesar")
    location = geolocator.reverse(f"{lat}, {lon}")
    return location.address

