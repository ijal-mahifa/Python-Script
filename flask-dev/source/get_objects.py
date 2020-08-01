import requests


def get_objects(link):
    response = requests.get(link)
    json_data = response.json()
    objects = json_data['objects']

    return objects
