import json
import requests

request_result = requests.get("https://api.waqi.info/feed/california/kern/bakersfield-california-avenue/?keyword=bakersfield&token=35e4a3b51d6f74ebb6ac6ea9a3fe9bdb0bb7b5f7")
request_json = request_result.json()
airq = request_json["data"]["aqi"]

print(airq)