import json
from urllib import request, response
import requests

base_url = "https://swapi.dev/api/"

planets = base_url + "planets"

url_get = requests.get(base_url)
url_get_planet = requests.get(planets)
#print(url_get.text)
about_planets = url_get_planet.text

jj_planets = url_get_planet.json()

for i in jj_planets["results"]:
    print(i["name"])
