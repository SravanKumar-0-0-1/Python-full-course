#API:(Application Programming Interface)
#An API (Application Programming Interface) is a set of rules and protocols that allow different software applications to communicate with each other.
#  It defines how requests and responses should be structured, enabling seamless integration between different services or systems.
#APIs are used to enable the integration of different software systems, allowing them to communicate with each other.

import requests
import json

base_url="https://pokeapi.co/api/v2/"
def get_details_info(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        return data
    else:
        print(f"failed to retrieve data{name}")
her_name="pikachu"
get_data=get_details_info(her_name.capitalize())
if get_data:
    print(f"Name:{get_data["name"]}")
    print(f"Name:{get_data["height"]}")

