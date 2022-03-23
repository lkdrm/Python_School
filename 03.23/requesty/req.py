import requests
import json
from pprint import pp, pprint

response = requests.get("https://swapi.dev/api/")
result = json.loads(response.text)
response_json = response.json()

#print(response.text)
#print(type(result))
#print(response.content)
pprint(response_json["planets"])

response_2 = requests.get("https://swapi.dev/api/planets/")
result_2 = response_2.json()
#pprint(result_2)
print(response_2.status_code)