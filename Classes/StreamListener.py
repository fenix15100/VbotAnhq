import tweepy
import json


class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # code to run each time the stream receives a status
        print(status)

    def on_direct_message(self, status):
        # code to run each time the stream receives a direct message
        print(status)

    def on_data(self, status):

        data = json.loads(status)
        print(data['user'])

    def on_error(self, status_code):
        # code to run each time an error is received
        if status_code == 420:
            return False
        else:
            return True
