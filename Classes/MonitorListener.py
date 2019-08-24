import tweepy
import json


class MonitorListener(tweepy.StreamListener):

    def __init__(self, api):
        super().__init__()
        self.api = api

    @staticmethod
    def from_creator(status):
        try:
            if hasattr(status, 'retweeted_status'):
                return False
            elif status.in_reply_to_status_id != None:
                return False
            elif status.in_reply_to_screen_name != None:
                return False
            elif status.in_reply_to_user_id != None:
                return False
            else:
                return True
        except Exception as error:
            return False

    def on_data(self, status):
        data = json.loads(status)
        print(data)
        if MonitorListener.from_creator(data):
            print(data)

    def on_error(self, status_code):
        # code to run each time an error is received
        if status_code == 420:
            return False
        else:
            return True
