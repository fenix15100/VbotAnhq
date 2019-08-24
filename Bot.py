import json
import tweepy

# Load credentials from json file
with open("creds.json", "r") as file:
    creds = json.load(file)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(creds['CONSUMER_API_KEY'],creds['CONSUMER_API_KEY_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_TOKEN_SECRET'])

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Vayase señor cuesta, vayase!!")