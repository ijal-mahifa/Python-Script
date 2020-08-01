import requests
from source import url

first_url = url.main_urls()

response = requests.get(first_url)
json_data = response.json()
totalResources = json_data['pages']['totalResources']


def get_url():
    list_url = []

    for i in range(totalResources + 1):
        urls = '{}'.format(url.urls())
        anchor = i * 60
        if totalResources > anchor:
            list_url.append(urls+'&anchor={}'.format(anchor))
            # print(url.format(anchor))
    return list_url
