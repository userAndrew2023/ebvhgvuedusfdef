import requests


def get_geocode(address):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": address,
        "format": "json"
    }

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        pass

    json_response = response.json()
    print(json_response)
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    return ",".join((toponym_longitude, toponym_lattitude))


def get_span(address):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": address,
        "format": "json"
    }

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        pass

    json_response = response.json()
    print(json_response)
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coordinates = toponym["boundedBy"]["Envelope"]
    lower = toponym_coordinates['lowerCorner'].split()
    upper = toponym_coordinates['upperCorner'].split()
    dx = abs(float(lower[0]) - float(upper[0])) / 2
    dy = abs(float(lower[1]) - float(upper[1])) / 2

    return f"{dx},{dy}"

