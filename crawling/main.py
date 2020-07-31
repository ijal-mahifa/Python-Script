import get_url
import get_objects
import get_json
import json
import os

urls = get_url.get_url()


def main(link):
    list_data = []
    for url in link:
        object = get_objects.get_objects(url)
        dict_data = get_json.get_json(object)
        list_data = list_data + dict_data

    return list_data


if __name__ == '__main__':
    list_json = main(urls)
    print("\nJumlah Barang : {} barang".format(len(list_json)))
    print("Path for API : {}\n".format(os.path.join(os.getcwd())))
    for data in list_json:
        print(json.dumps(data,indent=2))

