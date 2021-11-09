import json
import requests
def get():
    response = requests.request("GET", "https://reqres.in/api/users")
    return json.loads(response.text)

def post():
    payload = json.dumps(
            {
                "first_name": "Ignacio",
                "last_name": "Prueba",
                "avatar": "https://reqres.in/img/faces/1-image.jpg"
            }
        )
    response = requests.request("POST", "https://reqres.in/api/users", data=payload)
    return json.loads(response.text)

user_data=get()
created_user= post()