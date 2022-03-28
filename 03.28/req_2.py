from unittest import result
from urllib import request
import requests
import json

base_url = "https://the-dune-api.herokuapp.com/"

endpoint = "quotes/10"

url = base_url + endpoint

response = requests.get(url)

if response.status_code ==200:
    result = response.json()
    for quote in result:
        print(f'Quote n.{quote["id"]}')
        print("Quote text: ", end="")
        print(quote["quote"])
else:
    print("There was an error while getting data from an API!")

# python -i req.py


#Post request

#response = request.post("https://jsonplaceholder.typicode.com/todos", data = json.dumps(#{"ky":"valu"}))

response = request.post("https://jsonplaceholder.typicode.com/todos", json = {"ky":"valu"}) # this is a better version