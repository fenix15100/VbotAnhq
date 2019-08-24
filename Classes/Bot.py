import os
import json
import tweepy
from AuthTwitter import AuthTwitter
from MentionListener import MentionListener


def run_bot():
    # Load credentials from json file
    path = os.path.abspath('creds.json')
    with open(path, "r") as file:
        creds = json.load(file)

    # Get access to api
    api = AuthTwitter(creds).get_api_instance()

    # Create Listener using Stream API for detects interations with bot
    mention_listener = MentionListener(api)
    mention_stream = tweepy.Stream(auth=api.auth, listener=mention_listener)
    mention_stream.filter(track=['@VbotAnhq'])



