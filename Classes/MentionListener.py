import tweepy
import json


class MentionListener(tweepy.StreamListener):

    def __init__(self, api):
        super().__init__()
        self.api = api


    def on_data(self, status):
        data = json.loads(status)
        print(data)
        self.api.update_status('@' + data['user']['screen_name'] + '<Aqui iria el video>', data['id'])

    def on_error(self, status_code):
        # code to run each time an error is received
        if status_code == 420:
            return False
        else:
            return True
