import tweepy


class AuthTwitter(object):

    def __init__(self, creds):
        # Authenticate to Twitter
        self.auth = tweepy.OAuthHandler(creds['CONSUMER_API_KEY'], creds['CONSUMER_API_KEY_SECRET'])
        self.auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_TOKEN_SECRET'])

        # Create API object
        self.api = tweepy.API(self.auth)

    def get_api_instance(self):
        return self.api
