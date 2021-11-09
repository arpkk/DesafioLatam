import json
import requests


def get():
    response = requests.request("GET", "https://reqres.in/api/users")
    return json.loads(response.text)


def post():
    payload = json.dumps({
        "first_name": "Ignacio",
        "job": "Profesor"
    })
    response = requests.request("POST", "https://reqres.in/api/users", data=payload)
    return json.loads(response.text)


def put():
    payload = json.dumps({
        "first_name": "Morpheus",
        "residence": "zion"
    })
    response = requests.request("PUT", "https://reqres.in/api/users", data=payload)
    return json.loads(response.text)

def delete():
    payload = json.dumps({
        "first_name": "Pepe"
    })
    response = requests.request("DELETE", "https://reqres.in/api/users", data=payload)

user_data = get()
created_user = post()
updated_user = put()
delete_user = delete()

print(user_data)
print(created_user)
print(updated_user)
print(delete_user)