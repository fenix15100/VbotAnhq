import os
import tweepy
import json


class MonitorListener(tweepy.StreamListener):

    def __init__(self, api=None,target_id='4711825403'):
        super().__init__()
        self.api = api
        self.target_id = target_id

    @staticmethod
    def from_creator(status,target_id):
        if status['user']['id_str'] == target_id:
            return True
        else:
            return False

    def on_data(self, status):
        data = json.loads(status)

        if MonitorListener.from_creator(data,self.target_id):
            print(data)
            path = os.path.abspath('Library/status_target.json')
            with open(path, "w") as file:
                print(data, file=file)
                print('\n',file=file)

    def on_error(self, status_code):
        # code to run each time an error is received
        if status_code == 420:
            return False
        else:
            return True
