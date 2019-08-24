import os
import json
import tweepy
from Classes.AuthTwitter import AuthTwitter
from Classes.StreamListener import StreamListener

# Load credentials from json file

path = os.path.abspath('creds.json')
with open(path, "r") as file:
    creds = json.load(file)

# Get access to api
api = AuthTwitter(creds).get_api_instance()

# Create Listener using Stream API
tweepy_listener = StreamListener()
tweepy_stream = tweepy.Stream(auth=api.auth, listener=tweepy_listener)
tweepy_stream.filter(track=['@VbotAnhq'])
