import requests
import json


def request_photos():
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=oJYSGqNJii0OF3YJTblfIfmN4FgGXjPLGr0ZeMDW"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.text)["latest_photos"][:25]


def create_list(data):
    list = []
    for key in data:
        list.append(key["img_src"])
    return list


def build_web_page(list):
    url = ""
    f = open('imagenes.html', 'w')
    inicio = "<html><head></head><body><ul>"
    for foto in list:
        url += "<li><img src=" + foto + "></li>"
    fin = "</ul></body></head></html>"
    f.write(inicio + url + fin)
    f.close()


data = request_photos()
print(data)
list = create_list(data)
print(list)
build_web_page(list)
