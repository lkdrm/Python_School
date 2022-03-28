from urllib import request
import requests
import json

base_url = "https://the-dune-api.herokuapp.com/"

endpoint = "quotes"

url = base_url + endpoint
response = requests.get(url)
response.status_code
response.reason
type(response)
response.content
response.text
response.json()
json.loads(response.text)

result = response.json()

result[0]["quote"]

result[0]["id"]

request = response.request
request

request.url
request.path_url
request.headers
response.headers
response.headers["Content-Type"]
# python -i req.py