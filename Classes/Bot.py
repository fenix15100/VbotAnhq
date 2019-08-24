import os
import json
import tweepy
from AuthTwitter import AuthTwitter
from MentionListener import MentionListener
from MonitorListener import MonitorListener


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
    mention_stream.filter(track=['@VbotAnhq'] ,is_async=True)

    # Create Listener for catch al videos from @EscenasANHQV ID 4711825403
    target_id = '4711825403'
    monitor_listener = MonitorListener(api,target_id=target_id)
    monitor_stream = tweepy.Stream(auth=api.auth, listener=monitor_listener)
    monitor_stream.filter(follow=[target_id], is_async=True)

