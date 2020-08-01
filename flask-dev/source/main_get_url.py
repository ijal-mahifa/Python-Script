import requests
import url

first_url = "https://api.nike.com/product_feed/rollup_threads/v2?filter=marketplace%28ID%29&filter=language%28en-GB%29&filter=employeePrice%28true%29&anchor=60&consumerChannelId=d9a5bc42-4b9c-4976-858a-f159cf99c647&count=60"

response = requests.get(first_url)
json_data = response.json()
totalResources = json_data['pages']['totalResources']


def get_url():
    list_url = []

    for i in range(totalResources + 1):
        url = "https://api.nike.com/product_feed/rollup_threads/v2?filter=marketplace%28ID%29&filter=language%28en-GB%29&filter=employeePrice%28true%29&anchor={}&consumerChannelId=d9a5bc42-4b9c-4976-858a-f159cf99c647&count=60"
        anchor = i * 60
        if totalResources > anchor:
            list_url.append(url.format(anchor))
            # print(url.format(anchor))
    return list_url