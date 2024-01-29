from io import BytesIO
from PIL import Image
import requests


def show_map(code=None, delta=None, map='map'):
    map_params = {
        "ll": code,
        "spn": delta,
        "l": map,
        "pt": code,
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    Image.open(BytesIO(
        response.content)).show()
