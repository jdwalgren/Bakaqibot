import time
import tweepy
import json
import requests

# Twitter Dev Tokens
auth = tweepy.OAuthHandler("NbRCVzJt3XHOEemFMws6depjP", "IiXgK2JBMzBIjCNDW73hUX5EN771kq2zPpVJL3OJp1pv7SXTaj")
auth.set_access_token("1305642602759217152-SpoWsLhcr8Vfypq6QwAboDTF7PjCrh", "PJekrktdWfdVyZ2NkxLk9mw2YzKaBFjOeg0xN25xTtuiw")

# token 35e4a3b51d6f74ebb6ac6ea9a3fe9bdb0bb7b5f7
# Bakersfield = "https://api.waqi.info/feed/california/kern/bakersfield-california-avenue/?keyword=bakersfield&token=35e4a3b51d6f74ebb6ac6ea9a3fe9bdb0bb7b5f7"

request_result = requests.get("https://api.waqi.info/feed/california/kern/bakersfield-california-avenue/?keyword=bakersfield&token=35e4a3b51d6f74ebb6ac6ea9a3fe9bdb0bb7b5f7")
request_json = request_result.json()
airq = request_json["data"]["aqi"]

# Create API object
api = tweepy.API(auth)

#Time Stamp
localtime = time.asctime(time.gmtime())
update = "Hello, today is {}, and the air quality for Bakersfield is {}.".format(localtime, airq)

#sleep timer 
# time.sleep(14400)

# update = "Hello, today is", localtime , "and the air quality is", Bakersfield"

api.update_status(update)


