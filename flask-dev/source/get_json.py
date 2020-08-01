def get_json(json_ob):
    list_json = []
    for data in json_ob:
        for info in data['productInfo']:
            try:
                data_dict = {
                    'id': info['merchProduct']['id'],
                    'title': info['productContent']['title'],
                    'subtitle': info['productContent']['subtitle'],
                    'status': info['merchProduct']['status'],
                    'styleCode': info['merchProduct']['styleCode'],
                    'colorCode': info['merchProduct']['colorCode'],
                    'styleColor': info['merchProduct']['styleColor'],
                    'genders': info['merchProduct']['genders'],
                    'sportTags': info['merchProduct']['sportTags'],
                    'quantityLimit': info['merchProduct']['quantityLimit'],
                    'styleType': info['merchProduct']['styleType'],
                    'productType': info['merchProduct']['productType'],
                    'country': info['merchPrice']['country'],
                    'currency': info['merchPrice']['currency'],
                    'currentPrice': info['merchPrice']['currentPrice'],
                    'available': info['availability']['available'],
                    'imageUrls': info['imageUrls']['productImageUrl']
                }
                list_json.append(data_dict)
            except:
                continue

    return list_json
